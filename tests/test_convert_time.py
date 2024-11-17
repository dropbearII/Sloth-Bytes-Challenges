import convert_time as ct


def test_12_am():
    assert ct.convert_time("12:00 am") == "0:00"


def test_6_20_pm():
    assert ct.convert_time("6:20 pm") == "18:20"


def test_21_00():
    assert ct.convert_time("21:00") == "9:00 pm"


def test_5_05():
    assert ct.convert_time("5:05") == "5:05 am"


def test_is_12_h_format_true():
    assert ct.is_12_hour_time_format("6:20 pm") is True
    assert ct.is_24_hour_time_format("6:20 pm") is False


def test_is_24_h_format_true():
    assert ct.is_12_hour_time_format("18:20") is False
    assert ct.is_24_hour_time_format("18:20") is True
