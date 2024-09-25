"""
You are given the length of a video in minutes. The format is mm:ss (ex: "02:54").

Create a function that takes the video length and return it in seconds.

Notes

    The video length is given as a string.

    If the number of seconds is 60 or over, return -1 (see example #3).

    You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).

Examples

minutesToSeconds("01:00") = 60

minutesToSeconds("13:56") = 836

minutesToSeconds("10:60") = -1

minutesToSeconds("121:49") = 7309
"""

import re


def minutes_to_seconds(time: str) -> int:
    time_format = '[0-9]+:[0-5][0-9]'  # format of time 'mm:ss'
    if re.fullmatch(time_format, time):
        time_list: list[int] = list(map(int, time.split(':')))
        return time_list[0]*60+time_list[1]
    else:  # no match
        return -1


if __name__ == '__main__':
    print(minutes_to_seconds("01:00"))
    print(minutes_to_seconds("13:56"))
    print(minutes_to_seconds("10:60"))
    print(minutes_to_seconds("121:49"))
    print(minutes_to_seconds("11:23:00"))
