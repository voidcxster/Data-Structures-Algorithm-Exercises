def gcd(a: int, b: int) -> int:
    largestInt: int = a if a > b else b
    for i in range(2, largestInt + 1):
        # check if both are divisible by i
        if a % i == 0 and b % i == 0:
            return i * gcd(a // i, b // i)

    return 1

if __name__ == '__main__':
    # print(gcd(60, 12))
    # print(gcd(14, 12))
    # print(gcd(60, 45))
    # print(gcd(15, 100))
    while True:
        a: int = int(input("Enter first int: "))
        b: int = int(input("Enter second int: "))
        print(gcd(a, b))
