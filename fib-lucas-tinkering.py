def fibonacci(n):
    """
    Return the nth value in the Fibonacci Series.

    Arg:
        n(int): Index whose value will print.
    Return:
        The value in the Fibonacci Series that corresponds to the value of n.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        series = [0, 1]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]


def lucas(n):
    """
    Return the nth number in the Lucas Series.

    Arg:
        n(int): Index within the Lucas series.
    Return:
        The value in the Lucas Series that corresponds to the value of n.
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        series = [2, 1]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]


def sum_series(n, x=0, y=1):
    """
    Return nth value from either Fibonacci Series or Lucas Series depending \
    on arguments. If only given (n), will return Fibonacci series. If given \
    (n, 2, 1) will return Lucas series. If given n with any other 2 numbers, \
    it will create it's own series and return the nth value.

    Args:
        n(int): Determines which value of the series to print.
        x(int): Optional argument defaulted to 0, and will combine with y \
        to create series of integers.
        y(int): Optional argument defaulted to 1, and will combine with x \
        to create a series of integers.
    Return:
        The nth value in either the Fibonacci series, the Lucas series, \
        or another series based on the values given for x and y.
    """

    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        series = [x, y]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]

print(sum_series(0, 5, 7))
