"""
Weekly Challenge 2024-11-12

12 vs 24 Hours

Create a function that converts 12-hour time to 24-hour time or vice versa. Return the output as a string.
Examples

convertTime("12:00 am")
output = "0:00"

convertTime("6:20 pm")
output = "18:20"

convertTime("21:00")
output = "9:00 pm"

convertTime("5:05")
output ="5:05 am"

Notes

    A 12-hour time input will be denoted with an am or pm suffix.

    A 24-hour input time contains no suffix.
"""
import re


def convert_time(time: str) -> str:
    converted = ''
    split: list[str]
    if is_12_hour_time_format(time):
        split = re.split('[:\\s]+', time)
        print(split)
        if split[2] == ('pm' or 'PM'):
            converted = str(int(split[0]) + 12) + ':' + split[1]
        else:
            if split[0] == '12':
                split[0] = '0'
            converted = split[0] + ':' + split[1]
            print(converted)
    if is_24_hour_time_format(time):
        split = re.split(':', time)
        if int(split[0]) > 12:
            split[0] = str(int(split[0]) - 12)
            split.append('pm')
        else:
            split.append('am')
        converted = split[0] + ':' + split[1] + ' ' + split[2]
    return converted


def is_12_hour_time_format(time: str) -> bool:
    return bool(re.match('^(0?[0-9]|1[0-2]):[0-5][0-9]\\s(am|pm|AM|PM)$', time))


def is_24_hour_time_format(time: str) -> bool:
    return bool(re.match('^((0?|1)[0-9]|2[0-3]):[0-5][0-9]$', time))


if __name__ == '__main__':
    print(convert_time("12:00 am"))
    print(is_12_hour_time_format("12:00 am"))
