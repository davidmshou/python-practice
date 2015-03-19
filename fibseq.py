def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        series = [0,1]
        print(range(n)[-1])
        for i in range(n-1):
            series.append(series[i] + series[i+1])

        return series[-1]
        
print(fib(7))
