def sumHarmonicSeries(n: int) -> float:
    #base
    if n == 1:
        return 1

    return (1/n) + sumHarmonicSeries(n - 1)

if __name__ == '__main__':
    print(sumHarmonicSeries(7))
    print(sumHarmonicSeries(4))
