# python3

# 221RDB139 Kirils Aleksejevs 8. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i + 1))

        if next_char in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
            
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    if "F" in text:
        step = 0
        while step<6:
            with open (f"test/{step}") as fails:
                text = fails.read()
                mismatch  = find_mismatch
                print(mismatch)
                step += 1

if __name__ == "__main__":
    main()
