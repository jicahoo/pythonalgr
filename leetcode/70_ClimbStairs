def fibonacci_v1(n, fn):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif fn[n - 1] != 0:
        return fn[n - 1]
    else:
        temp_fib = fibonacci_v1(n - 1, fn) + fibonacci_v1(n - 2, fn)
        fn[n - 1] = temp_fib
        return temp_fib


def fibonacci_v2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci_v2(n - 1) + fibonacci_v2(n - 2)


if __name__ == '__main__':
    # DP
    n = 40
    fn = [0] * n
    print fibonacci_v1(n, fn)
    print fibonacci_v2(n)
