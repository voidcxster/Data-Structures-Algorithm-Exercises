import string

# had to get a bit of a hint w this one
def numToString(num: int, base: int = 10) -> str:
    digits: list[str] = list(string.digits + string.ascii_uppercase)

    if base > 36:
        raise Exception(
            "Not enough numbers and letters to convert to bases above 36. Try lowering the number."
        )
    elif base <= 0:
        raise Exception(
            "Cannot take negative bases. Try raising the number."
        )

    if num < base:
        return digits[num]

    return numToString(num // base, base) + digits[num % base]

if __name__ == '__main__':
    print(numToString(2835, 16))
    print(numToString(100, 8))
"""
how would i convert 100 into base 8?
100 - 64 = 36
1__
36 - 32 = 4
144

96
12
"""
