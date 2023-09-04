import time
import pigpio

class Tube:
    def __init__(self,
                # datapin: int,
                # clkpin: int,
                # cspin: int,
                chip: str = "TLV5618A",
                spi_bus: int = 0,
                spi_device: int = 0):
        # self.datapin = datapin
        # self.clkin = clkpin
        # self.cspin = cspin

        self.spi_bus = spi_bus
        self.spi_device = spi_device

        self.pi = pigpio.pi()

        if chip == "TLV5618A":
            self.spi = self.pi.spi_open(self.spi_device, 20000000, 1) # device 0 at 20MHz using mode 1 (clk-polarity 0, clock-phase 1)
            self.R1_msk = 0x8000
            self.SPD_msk = 0x4000 # 1: fast mode; 0: slow mode
            self.PWR_msk = 0x2000 # 1: power down; 0: normal operation
            self.R0_msk = 0x1000

    def composeBytes(self,
                        data: int,
                        channel: str = "B",
                        speed="fast",
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
        if int(data) > 4095:
            print("Data too large. Must be 0 < data <= 4095!")
            pass

        if pwr == False:
            payload = 0x2000
            payload = payload.to_bytes(2, "big")
            return [payload[0], payload[1]]
        else:
            payload = 0x4000 # fast mode default            
            if speed == "slow":
                payload = 0x0000
            
        if channel != "B":
            self.set_bit(payload, self.R1_msk, 1)

        payload = payload | data
        payload = payload.to_bytes(2, "big")
        return [payload[0], payload[1]]
    
    def set_bit(self, bytes, bit_mask, bit) -> bytes:
        data = bytes[0] << 8
        data = data | bytes[1]
        if bit == 1:
            return data | bit_mask
        if bit == 0:
            return data & ~bit_mask

    def setVolt(self, volt: float) -> None:
        volt = int(4095 * volt / 5)
        volt = self.composeBytes(volt)
        self.pi.spi_write(self.spi_device, volt)
    
    def setPercent(self, percent: float) -> None:
        if percent <= 100:
            val = int(4095 * percent / 100)
        elif percent > 100:
            val = 4095
        elif percent < 0:
            val = 0
        val = self.composeBytes(val)
        self.pi.spi_write(self.spi_device, val)
    
    def setVal(self, val):
        val = self.composeBytes(val)
        self.pi.spi_write(self.spi_device, val)

    def close(self):
        self.pi.spi_close(self.spi)