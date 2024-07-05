def sumGeometricSeries(n: int, r: float | int, a: float | int) -> float | int:
    term: int | float = a * r
    if n == 1:
        return term

    return term + sumGeometricSeries(n - 1, r, term)

if __name__ == '__main__':
    print(sumGeometricSeries(4, 10, 100))
