def power(base: int | float, powerOf: int) -> int | float:
    if powerOf == 1:
        return base
    return base * power(base, powerOf - 1)

if __name__ == '__main__':
    print(power(3, 4))
