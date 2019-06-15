try:
    import machine
    isRunningOffChip = False
except:
    from machine_stub import machine
    isRunningOffChip = True

class BoothInUseLedIndicator:

    greenLed = None
    redLed = None

    def __init__(self, redLedPin, greenLedPin):
        self.greenLed = machine.Pin(greenLedPin, machine.Pin.OUT)
        self.redLed = machine.Pin(redLedPin, machine.Pin.OUT)

    def setOccupied(self, isInUse=True):
        if(isInUse):
            self.greenLed.off()
            self.redLed.on()
        else:
            self.redLed.off()
            self.greenLed.on()
    
    def setAvailable(self):
        self.setOccupied(False)
