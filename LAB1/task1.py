n, k = int(input()), int(input())


def fib1(n: int, k: int, num1=1, num2=1, count=1) -> None:
    if count > k:
        return
    elif count >= n:
        print(num1)

    fib1(n, k, num2, num1 + num2, count + 1)


fib1(n, k)
