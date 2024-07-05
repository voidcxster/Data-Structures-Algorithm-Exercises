def sumDigits(n: int | str) -> int:
    # cast arg into str
    nStr: str = ''
    if type(n) is int:
        nStr = str(n)
    elif type(n) is str:
        nStr = n

    # base case
    if len(nStr) == 1:
        return int(n)

    return int(nStr[0]) + sumDigits(nStr[1:])

if __name__ == '__main__':
    print(sumDigits(345))
