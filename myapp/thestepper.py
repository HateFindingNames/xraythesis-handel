import time
from gpiozero import OutputDevice

class MyStepper:
    """Custom stepper driver control class. Takes pins STEP, DIR, EN and MODE0 - MODE2
    as well as the motors nominal steps/rev and the desired ustepping mode as input."""

    def __init__(self, steppin, dirpin, mdpins, enpin=None, steps_per_rev=200, ustep=0):
        self.steppin = steppin
        self.dirpin = dirpin
        self.mdpins = mdpins
        if enpin:
            self.enpin = enpin
            self.en = OutputDevice(self.enpin, initial_value=0)

        self.step = OutputDevice(self.steppin, initial_value=0)
        self.dir = OutputDevice(self.dirpin, initial_value=0)
        self.md = []
        for mdpin in self.mdpins:
            self.md.append(OutputDevice(mdpin))

        self.rpm = 10
        self.position_in_steps = 0
        self.position_in_deg = 0
        self.position_in_rad = 0
        
        self.fstep = 250 # stepping freq in kHz
        self.tpulse_h = 1.9e-6
        self.tpulse_l = 1.9e-6

        self.ustepping = [
                [0,0,0], # full
                [0,0,1], # half
                [0,1,0], # 1/4
                [0,1,1], # ...
                [1,0,0],
                [1,0,1],
                [1,1,0],
                [1,1,1]
                ]
        self.steps_per_rev = steps_per_rev
        self.setMicroStepping(ustep)

        self.setSpeed()
        
    def setMotorEnable(self, enable=None):
        """Enables the driver."""

        if enable == True:
            self.en.value = 1
            print(f"Motor enabled.")
        else:
            self.en.value = 0
            print(f"Motor disabled.")

    def stepPulse(self):
        self.step.on()
        time.sleep(self.tpulse_h)
        self.step.off()
        time.sleep(self.tpulse_l)

    def cwMotion(self, steps, rpm=None):
        """Move Motor clockwise and takes desired steps and rpm as input."""

        if self.en.value:
            if rpm and rpm != self.rpm:
                self.rpm = rpm
                self.setSpeed()
            
            if steps < 0:
                self.dir.off()
                steps = steps * -1
                self.direction_to_move = "CC"
            else:
                self.dir.on()
                self.direction_to_move = "CW"

            self.steps_left = steps
            print(f"About to move {steps} steps {self.direction_to_move} at {self.rpm}.")
            while self.steps_left > 0:
                self.stepPulse()
                self.steps_left -= 1
                self.position_in_steps -= 1
                time.sleep(self.step_delay)
            print(f"Done moving {steps} steps {self.direction_to_move} at {self.rpm}.")
        else:
            print(f"Motor not enabled.")

    def ccMotion(self, steps, rpm=None):
        """Move Motor counter-clockwise and takes desired steps and rpm as input."""

        if self.en.value:
            if rpm:
                self.rpm = rpm
            
            if steps < 0:
                self.dir.on()
                steps = steps * -1
                self.direction_to_move = "CW"
            else:
                self.dir.off()
                self.direction_to_move = "CC"

            self.steps_left = steps
            self.setSpeed()
            print(f"About to move {steps} steps {self.direction_to_move} at {self.rpm}.")
            while self.steps_left > 0:
                self.stepPulse()
                self.steps_left -= 1
                self.position_in_steps -= 1
                time.sleep(self.step_delay)
            print(f"Done moving {steps} steps {self.direction_to_move} at {self.rpm}.")
        else:
            print(f"Motor not enabled.")

    def setSpeed(self):
        self.step_delay = 60 / (self.esteps_per_rev * self.rpm)     # Step delay in seconds
        print(f"Step Delay: {self.step_delay}")

    def setMicroStepping(self, u):
        """Sets uStepping mode."""

        if u == 0:
            mode = self.ustepping[0]
        elif u % 1 != 0:
            print(f"Microstepping mode has to be an integer!")
            pass
        elif u > len(self.ustepping):
            print(f"There are only {len(self.ustepping)} Microstepping modes!")
            pass
        else:
            mode = self.ustepping[2**u]
        
        print(f"Setting uStep mode to {mode}.")

        for i, state in enumerate(mode):
            self.md[i].value = state
        
        self.esteps_per_rev = self.steps_per_rev * 2**u
        fullstring = f"full"
        otherstring = f"1/{2**u}"
        print(f"Microstepping mode set to {fullstring if u == 0 else otherstring} step mode.")
    
    def getMicrostepping(self):
        """Gets the currently set uStepping mode."""

        for i, mode in enumerate(self.md):
            print(f"MD{i} is set {mode.value}.")