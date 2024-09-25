"""
minutesToSeconds("01:00") = 60

minutesToSeconds("13:56") = 836

minutesToSeconds("10:60") = -1

minuteToSeconds("121:49") = 7309

print(minutes_to_seconds("01:00"))
    print(minutes_to_seconds("13:56"))
    print(minutes_to_seconds("10:60"))
    print(minutes_to_seconds("121:49"))
    print(minutes_to_seconds("11:23:00"))

"""
import VideoLengthSeconds as v


def test_empty_string():
    assert v.minutes_to_seconds('') == -1


def test_correct_minutes_to_seconds():
    assert v.minutes_to_seconds('01:00') == 60
    assert v.minutes_to_seconds('1:00') == 60


def test_seconds_in_correct_range():
    assert v.minutes_to_seconds("10:60") == -1


def test_no_hours_given():
    assert v.minutes_to_seconds("11:23:00") == -1


def test_correct_conversion():
    assert v.minutes_to_seconds("13:56") == 836
    assert v.minutes_to_seconds("121:49") == 7309


def test_too_many_seconds():
    assert v.minutes_to_seconds("1:000") == -1
