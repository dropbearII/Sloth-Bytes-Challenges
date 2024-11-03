"""
Weekly Challenge 2024-10-29

Numbers to English

Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that
integer written in English.

Examples

numToEng(0)
output = "zero"

numToEng(18)
output = "eighteen"

numToEng(126)
output = "one hundred twenty six"

numToEng(909)
output = "nine hundred nine"

Notes

    There are no hyphens used (e.g. "thirty five" not "thirty-five").

    The word "and" is not used (e.g. "one hundred one" not "one hundred and one").
"""


def num_to_eng(num: int) -> [str]:
    if num < 0 or num > 999:
        return "Number has to be in range [0,999]"

    num_str = str(num)
    zero_to_nineteen: list[str] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                                   'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                                   'seventeen', 'eighteen', 'nineteen']
    tens_twenty_to_ninety: list[str] = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty',
                                        'ninety']
    eng_list: list[str] = []

    if num < 20:
        eng_list.append(zero_to_nineteen[num])
    if num >= 20:
        if num_str[-1] != '0':
            eng_list.append(zero_to_nineteen[int(num_str[-1])])
        if num_str[-2] != '0':
            eng_list.append(tens_twenty_to_ninety[int(num_str[-2])])
    if num > 99:
        eng_list.append('hundred')
        eng_list.append(zero_to_nineteen[int(num_str[-3])])

    result = ' '.join(reversed(eng_list))
    return result


if __name__ == '__main__':
    print(num_to_eng(0))
    print(num_to_eng(18))
    print(num_to_eng(30))
    print(num_to_eng(126))
    print(num_to_eng(909))
