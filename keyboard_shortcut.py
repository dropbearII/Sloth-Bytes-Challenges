"""
Weekly Challenge 2024-11-06

Ctrl + C, Ctrl + V

Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V", return the sentence after those keyboard shortcuts have been applied!

    "Ctrl + C" will copy all text behind it.

     "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.

    A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.

Examples

#Example 1
keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon") output = "the egg and the egg and the spoon"

#Example 2
keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V")
output=  "WARNING WARNING"

#Example 3
keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V")
output = "The The Town The The Town"

Notes

    Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).

    Pasting should add a space between words.

"""
import re


def keyboard_shortcut(phrase: str) -> str:
    memory: dict[str, str] = {
        'copied': '',
        'last shortcut': '',
    }
    ctrl_C = 'Ctrl \\+ C'
    ctrl_V = 'Ctrl \\+ V'

    copy_start = 0
    p = phrase
    output = ''
    while re.search(ctrl_V, p) is not None:
        # identify shortcuts in string
        copy = re.search(ctrl_C, p)
        paste = re.search(ctrl_V, p)
        # print(copy.start(), copy.end(), copy.span(), paste.start(), paste.end(), paste.span())
        # print(type(copy.start()))
        if copy.end() + 1 == paste.start():
            clipboard = p[0:copy.start()]
            # print(clipboard)
            # output = 2*clipboard
            # output.strip()
            # print(output)
            modified = clipboard + p[:copy.start()] + p[paste.end() + 1:]
            output = modified
            # print(p[copy.end():])
            # input[copy.start():copy.end()] = ''
            # input.replace('Ctrl + C', '', 1)  # delete Ctrl+C from string
            # print(input)
        else:
            modified = p[:paste.start()] + p[paste.end() + 1:]
            # print('else: ' + modified)
        # clean up useles Ctrl + C
        # print('test')
        p = modified

    # re.sub('\s{2,}', '', output)
    output = output.strip()

    return output


if __name__ == '__main__':
    keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon")
