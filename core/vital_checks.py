from core.base_vital_check import VitalCheck


class TemperatureCheck(VitalCheck):
    RANGES = {"child": (97, 100), "adult": (95, 102)}

    def _get_range(self):
        return self.RANGES["child"] if self.age < 12 else self.RANGES["adult"]

    def is_ok(self) -> bool:
        low, high = self._get_range()
        return low <= self.value <= high

    def error_message(self) -> str:
        return f"Temperature critical! => {self.value}°F"


class PulseRateCheck(VitalCheck):
    RANGES = {"child": (70, 120), "adult": (60, 100)}

    def _get_range(self):
        return self.RANGES["child"] if self.age < 12 else self.RANGES["adult"]

    def is_ok(self) -> bool:
        low, high = self._get_range()
        return low <= self.value <= high

    def error_message(self) -> str:
        return f"Pulse Rate out of range! => {self.value}bpm"


class Spo2Check(VitalCheck):
    # SPO2 rate is generally consistent across ages
    RANGES = {"default": (90, 100)}

    def _get_range(self):
        return self.RANGES["default"]

    def is_ok(self) -> bool:
        low, high = self._get_range()
        return low <= self.value <= high

    def error_message(self) -> str:
        return f"Oxygen Saturation out of range! => {self.value}%"


class BloodPressureCheck(VitalCheck):
    # Systolic and Diastolic as a tuple
    RANGES = {
        "child": ((90, 110), (55, 75)),
        "adult": ((90, 120), (60, 80)),
    }

    def __init__(self, systolic: int, diastolic: int, age: int):
        super().__init__((systolic, diastolic), age)

    def _get_range(self):
        return self.RANGES["child"] if self.age < 12 else self.RANGES["adult"]

    def is_ok(self) -> bool:
        (sys_low, sys_high), (dia_low, dia_high) = self._get_range()
        systolic, diastolic = self.value
        return (
            sys_low <= systolic <= sys_high
            and dia_low <= diastolic <= dia_high
        )

    def error_message(self) -> str:
        systolic, diastolic = self.value
        return f"Blood Pressure out of range! => {systolic}/{diastolic}mmHg"
