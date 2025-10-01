from core.vital_checks import (
    BloodPressureCheck,
    PulseRateCheck,
    Spo2Check,
    TemperatureCheck,
)


def test_all_vitals_ok_adult():
    checks = [
        TemperatureCheck(value=98, age=30),
        PulseRateCheck(value=75, age=30),
        Spo2Check(value=95, age=30),
        BloodPressureCheck(systolic=115, diastolic=75, age=30),
    ]
    results = [c.validate() for c in checks]
    assert all(re is None for re in results)


def test_temperature_out_of_range_adult():
    check = TemperatureCheck(value=104, age=30)
    result = check.validate()
    assert result == "Temperature critical! => 104°F"


def test_pulse_out_of_range_adult():
    check = PulseRateCheck(value=120, age=30)
    result = check.validate()
    assert result == "Pulse Rate out of range! => 120bpm"


def test_spo2_out_of_range_adult():
    check = Spo2Check(value=85, age=30)
    result = check.validate()
    assert result == "Oxygen Saturation out of range! => 85%"


def test_bp_out_of_range_adult():
    check = BloodPressureCheck(systolic=150, diastolic=95, age=30)
    result = check.validate()
    assert result == "Blood Pressure out of range! => 150/95mmHg"


def test_mixed_out_of_range_adult():
    checks = [
        TemperatureCheck(value=99, age=30),  # OK
        PulseRateCheck(value=120, age=30),  # Out of range
        Spo2Check(value=85, age=30),  # Out of range
        BloodPressureCheck(systolic=115, diastolic=75, age=30),  # OK
    ]
    results = [c.validate() for c in checks]
    assert results == [
        None,
        "Pulse Rate out of range! => 120bpm",
        "Oxygen Saturation out of range! => 85%",
        None,
    ]


def test_all_vitals_out_of_range_adult():
    checks = [
        TemperatureCheck(value=105, age=30),
        PulseRateCheck(value=130, age=30),
        Spo2Check(value=85, age=30),
        BloodPressureCheck(systolic=150, diastolic=95, age=30),
    ]
    results = [c.validate() for c in checks]
    assert results == [
        "Temperature critical! => 105°F",
        "Pulse Rate out of range! => 130bpm",
        "Oxygen Saturation out of range! => 85%",
        "Blood Pressure out of range! => 150/95mmHg",
    ]
