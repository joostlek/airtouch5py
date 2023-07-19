from enum import Enum
from airtouch5py.packets.datapacket import Data


class SetPowerSetting(Enum):
    CHANGE_ON_OFF_STATUS = 0b0001  # Does this mean toggle?
    SET_TO_OFF = 0b0010
    SET_TO_ON = 0b0011
    SET_TO_AWAY = 0b0100
    SET_TO_SLEEP = 0b0101
    # Other: Keep power setting


class SetAcMode(Enum):
    SET_TO_AUTO = 0b0000
    SET_TO_HEAT = 0b0001
    SET_TO_DRY = 0b0010
    SET_TO_FAN = 0b0011
    SET_TO_COOL = 0b0100
    # Other: keep mode setting


class SetAcFanSpeed(Enum):
    SET_TO_AUTO = 0b0000
    SET_TO_QUIET = 0b0001  # "Quite" in the docs
    SET_TO_LOW = 0b0010
    SET_TO_MEDIUM = 0b0011
    SET_TO_HIGH = 0b0100
    SET_TO_POWERFUL = 0b0101
    SET_TO_TURBO = 0b0110
    SET_TO_INTELLIGENT_AUTO = 0b1000
    # Other: keep fan speed setting


class SetpointControl(Enum):
    CHANGE_SETPOINT = 0x40
    KEEP_SETPOINT_VALUE = 0x00
    # Other: Invalidate data (????)


class AcControl:
    power_setting: SetPowerSetting
    ac_number: int
    ac_mode: SetAcMode
    ac_fan_speed: SetAcFanSpeed
    setpoint_control: SetpointControl
    setpoint: float


class AcControlData(Data):
    """
    AC control messages are to control all ACs. Each message to AirTouch is to control one or more specific ACs.
    AirTouch will respond a message with sub type 0x23. (AC status message)
    """

    ac_control: list[AcControl]
