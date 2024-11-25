"""
Weekly Challenge 2024-11-19

Valid JavaScript Comments

In JavaScript, there are two types of comments:
    Single-line comments start with //
    Multi-line or inline comments start with /* and end with */

The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add,
there can be no single-line comments in between multi-line comments in between the /* and */.

Create a function that returns True if comments are properly formatted, and False otherwise.

Examples

comments_correct("//////")
output = True
# 3 single-line comments: ["//", "//", "//"]

comments_correct("/**//**////**/")
output = True
# 3 multi-line comments + 1 single-line comment:
# ["/*", "*/", "/*", "*/", "//", "/*", "*/"]

comments_correct("///*/**/")
output = False
# The first /* is missing a */

comments_correct("/////")
output = False
# The 5th / is single, not a double //
"""

import re


def java_comments_correct(comment: str) -> bool:
    pattern = re.compile('/{2}|/\\*\\*/')
    matches = re.finditer(pattern, comment)
    index: int = 0
    for element in matches:
        if element.start() != index:  # match skipped an index
            return False
        index = element.end()
    if index == len(comment):  # last index does not match string length
        return True
    else:
        return False


if __name__ == '__main__':
    print(java_comments_correct("//////"))
    print(java_comments_correct("/**//**////**/"))
    print(java_comments_correct("///*/**/"))
    print(java_comments_correct("/////"))
