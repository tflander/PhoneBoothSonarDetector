import pytest
from boothInUseLedIndicator import BoothInUseLedIndicator

from mock import Mock, patch

try:
    import machine
    isRunningOffChip = False
except:
    from machine_stub import machine
    isRunningOffChip = True

@pytest.fixture
def boothInUseLedIndicator(monkeypatch, mockGreenLedPin, mockRedLedPin):
    with patch.object(BoothInUseLedIndicator, "__init__", lambda slf, redPin, greenPin: None):
        boothInUseLedIndicator = BoothInUseLedIndicator(None, None)
        boothInUseLedIndicator.greenLed = mockGreenLedPin
        boothInUseLedIndicator.redLed = mockRedLedPin
        return boothInUseLedIndicator
    
@pytest.fixture
def mockGreenLedPin():
    return Mock(spec=machine.Pin)

@pytest.fixture
def mockRedLedPin():
    return Mock(spec=machine.Pin)

class TestPinTransitions(object):

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        boothInUseLedIndicator.setOccupied()
        mockGreenLedPin.off.assert_called()
        mockRedLedPin.on.assert_called()


    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        boothInUseLedIndicator.setAvailable()
        mockGreenLedPin.on.assert_called()
        mockRedLedPin.off.assert_called()
