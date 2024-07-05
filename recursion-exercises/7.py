def sumSeries(n: int) -> int:
    # base
    if n <= 0:
        return 0

    return n + sumSeries(n - 2)

if __name__ == '__main__':
    print(sumSeries(6))
    print(sumSeries(10))
