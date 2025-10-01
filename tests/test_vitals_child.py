from core.vital_checks import (
    BloodPressureCheck,
    PulseRateCheck,
    Spo2Check,
    TemperatureCheck,
)


def test_all_vitals_ok_child():
    checks = [
        TemperatureCheck(value=98.6, age=10),
        PulseRateCheck(value=90, age=10),
        Spo2Check(value=95, age=10),
        BloodPressureCheck(systolic=100, diastolic=65, age=10),
    ]
    results = [c.validate() for c in checks]
    assert all(r is None for r in results)


def test_temperature_out_of_range_child():
    check = TemperatureCheck(value=104, age=10)
    result = check.validate()
    assert result == "Temperature critical! => 104°F"


def test_pulse_out_of_range_child():
    check = PulseRateCheck(value=150, age=10)
    result = check.validate()
    assert result == "Pulse Rate out of range! => 150bpm"


def test_spo2_out_of_range_child():
    check = Spo2Check(value=85, age=10)
    result = check.validate()
    assert result == "Oxygen Saturation out of range! => 85%"


def test_blood_pressure_out_of_range_child():
    check = BloodPressureCheck(systolic=130, diastolic=90, age=10)
    result = check.validate()
    assert result == "Blood Pressure out of range! => 130/90mmHg"


def test_mixed_vitals_child():
    checks = [
        TemperatureCheck(value=98.6, age=10),  # ok
        PulseRateCheck(value=150, age=10),  # out of range
        Spo2Check(value=85, age=10),  # out of range
        BloodPressureCheck(systolic=95, diastolic=60, age=10),  # ok
    ]
    results = [c.validate() for c in checks]
    assert results == [
        None,
        "Pulse Rate out of range! => 150bpm",
        "Oxygen Saturation out of range! => 85%",
        None,
    ]


def test_all_vitals_out_of_range_child():
    checks = [
        TemperatureCheck(value=104, age=10),
        PulseRateCheck(value=40, age=10),
        Spo2Check(value=85, age=10),
        BloodPressureCheck(systolic=130, diastolic=90, age=10),
    ]
    results = [c.validate() for c in checks]
    assert results == [
        "Temperature critical! => 104°F",
        "Pulse Rate out of range! => 40bpm",
        "Oxygen Saturation out of range! => 85%",
        "Blood Pressure out of range! => 130/90mmHg",
    ]
