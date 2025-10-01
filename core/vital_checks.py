from core.base_vital_check import VitalCheck


class TemperatureCheck(VitalCheck):
    TEMP_RANGES = {"child": (97, 100), "adult": (95, 102)}

    def _get_temp_range(self):
        return self.TEMP_RANGES["child"] if self.age < 12 else self.TEMP_RANGES["adult"]

    def is_ok(self) -> bool:
        low_temp, high_temp = self._get_temp_range()
        return low_temp <= self.value <= high_temp

    def error_message(self) -> str:
        return f"Temperature critical! => {self.value}°F"


class PulseRateCheck(VitalCheck):
    PULSE_RANGES = {"child": (70, 120), "adult": (60, 100)}

    def _get_pulse_range(self):
        return (
            self.PULSE_RANGES["child"] if self.age < 12 else self.PULSE_RANGES["adult"]
        )

    def is_ok(self) -> bool:
        low_pulse, high_pulse = self._get_pulse_range()
        return low_pulse <= self.value <= high_pulse

    def error_message(self) -> str:
        return f"Pulse Rate out of range! => {self.value}bpm"


class Spo2Check(VitalCheck):
    # SPO2 rate is generally consistent across ages
    OXYGEN_RANGES = {"default": (90, 100)}

    def _get_oxygen_range(self):
        return self.OXYGEN_RANGES["default"]

    def is_ok(self) -> bool:
        low_oxygen, high_oxygen = self._get_oxygen_range()
        return low_oxygen <= self.value <= high_oxygen

    def error_message(self) -> str:
        return f"Oxygen Saturation out of range! => {self.value}%"


class BloodPressureCheck(VitalCheck):
    # Systolic and Diastolic as a tuple
    BP_RANGES = {
        "child": ((90, 110), (55, 75)),
        "adult": ((90, 120), (60, 80)),
    }

    def __init__(self, systolic: int, diastolic: int, age: int):
        super().__init__((systolic, diastolic), age)

    def _get_bp_range(self):
        return self.BP_RANGES["child"] if self.age < 12 else self.BP_RANGES["adult"]

    def is_ok(self) -> bool:
        (sys_low, sys_high), (dia_low, dia_high) = self._get_bp_range()
        systolic, diastolic = self.value
        return sys_low <= systolic <= sys_high and dia_low <= diastolic <= dia_high

    def error_message(self) -> str:
        systolic, diastolic = self.value
        return f"Blood Pressure out of range! => {systolic}/{diastolic}mmHg"
