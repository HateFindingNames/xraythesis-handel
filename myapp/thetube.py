import pigpio
from time import sleep

class Tube:
    def __init__(self, spi_bus: int = 0):

        self.spi_bus = spi_bus

        self.pi = pigpio.pi()
        self.filrdypin = 24
        self.pi.set_pull_up_down(self.filrdypin, pigpio.PUD_DOWN)
        self.pi.set_mode(self.filrdypin, pigpio.INPUT) # GPIO 24

        self.enpin = 25
        self.pi.set_pull_up_down(self.enpin, pigpio.PUD_DOWN)
        self.pi.set_mode(self.enpin, pigpio.OUTPUT) # GPIO 25
        self.pi.write(self.enpin, 0)

        self.dac = self.pi.spi_open(1, 20000000, 1) # device 0 at 20MHz using mode 1 (clk-polarity 0, clock-phase 1)

        # ADC SPI-Com config: T=1 (LSB first on MOSI) (3-wire mode) nnnn=0001 (write 1 bytes then read) W=1 (3-wire) mm=11 (POL1, PHA1)
        # --> 0x4403
        self.adc = self.pi.spi_open(0, 100000, 0) # device 1 at 100kHz using mode 0 (clk-polarity 0, clock-phase 0)
        self.adc_read = 0x1Bfff # Single ended, ODD, channel 1

        self.setHV(0)
        self.setI(0)
        self.disable()

        # pwrdown = self.composeBytesDac(0, 0, pwr = False)
        # self.pi.spi_write(self.dac, pwrdown)

    def toggle(self):
        self.enabled = not self.enabled
        self.pi.write(self.enpin, self.enabled)

    def enable(self):
        self.enabled = True
        self.pi.write(self.enpin, True)
        # self.pi.spi_write(self.dac, self.Ival)
        # sleep(.01)
        # self.pi.spi_write(self.dac, self.HVval)

    def disable(self):
        self.enabled = False
        self.pi.write(self.enpin, False)

    def composeBytesDac(self,
                        data: int,
                        channel: bool,
                        fast: bool = False,
                        pwr: bool = True) -> list:
        """
        Register-Select Truth Table:
        R1  R2  REGISTER
        -------------------
        0   0   Write data to DAC B and BUFFER
        0   1   Write data to BUFFER
        1   0   Write data to DAC A and update DAC B with BUFFER content
        1   1   Reserved
        -------------------
        """
        channel = not channel

        if int(data) > 4095:
            print("Data too large. Must be 0 < data <= 4095!")
            pass

        if pwr == False:
            payload = 0x2000
            payload = payload.to_bytes(2, "big")
            return [payload[0], payload[1]]
        else:
            payload = 0x4000 # fast mode default            
            if not fast:
                payload = 0x0000

        payload = payload | (channel << 15)
        payload = payload | data
        payload = payload.to_bytes(2, "big")
        return payload

    def read(self,
             channel: bool) -> bytearray:
        """Reads analog signals on the MCP3202s CH0 or CH1."""

        # preparations
        adc_bytes = self.adc_read | (channel << 14)
        adc_bytes = adc_bytes.to_bytes(3, "big") # 0b00000001 11011111 11111111

        # ready to write/read
        _, b = self.pi.spi_xfer(self.adc, adc_bytes)
        raw = (b[-2] << 8) | b[-1] # remove most significant byte
        raw = raw & ~(0xf000) # set bits 12-15 zero
        if channel == False:
            res = (raw*0.018)
        else:
            res = (raw*0.302)
        return [raw, res]

    def setHV(self, hv: float) -> None:
        """Set HV Output in kV."""
        self.hv = hv
        if 4 <= hv <= 70:
            val = abs(int(hv/0.017))
            self.HVval = self.composeBytesDac(val, 0)
            print(f"HV set to {hv}kV -> {val}. Ok.")
        elif 0 <= hv < 4:
            self.hv = 0
            print(f"HV set to 0. Ok.")
            self.HVval = self.composeBytesDac(0, 0)
        else:
            self.hv = 0
            print("HV must be in range 4-70kV!")
            self.HVval = self.composeBytesDac(0, 0)

        self.pi.spi_write(self.dac, self.HVval)
    
    def setI(self, i: float) -> None:
        """Set Filament Current Output in uA. Output gets capped at 12 Watt."""
        try:
            imax = 12e3/self.hv
            if imax > 1000:
                imax = 1000
        except ZeroDivisionError:
            imax = 1000
        if 0 <= i <= 1000:
            if i > imax:
                i = imax
                print(f"Did cap filament current at 12W/{self.hv:.3f}V = {(12e3/self.hv):.3f}uA.")
            val = abs(int(i/0.291))
            self.Ival = self.composeBytesDac(val, 1)
            print(f"Filament current set to {i}uA -> {val}. Ok.")
        elif i < 0 or i > 1000:
            self.Ival = self.composeBytesDac(0, 1)
            print(f"Filament current must be in range 0-{(12/self.hv):.3f}uA but {i} given -> Did set to 0.")

        self.pi.spi_write(self.dac, self.Ival)

    def setPercent(self, percent: float, channel: bool) -> None:
        """Set Output in percent on specified channel."""
        if 0 <= percent <= 100:
            val = int(4095 * percent / 100)
            val = self.composeBytesDac(val, channel)
        else:
            val = self.composeBytesDac(0, channel)
            print("Percentage must be in range 0-100!")

        self.pi.spi_write(self.dac, val)

    def setVal(self, val, channel: bool):
        """Set Output as 0 <= integer <= 4095 on specified channel."""
        if 0 <= val <= 4095:
            val = self.composeBytesDac(val, channel)
        else:
            val = self.composeBytesDac(0, channel)
            print("Value must be in range 0-4095!")

        self.pi.spi_write(self.dac, val)

    def isRdy(self):
        if self.pi.read(self.filrdypin):
            print(f"Filament ready.")
        else:
            print(f"Filament not ready yet.")

    def close(self):
        self.pi.spi_close(self.dac)
        self.pi.spi_close(self.adc)