n, k = int(input()), int(input())


def fib4(n: int, k: int, num1=1, num2=1, count=1) -> None:
    if count > k:
        return
    elif count >= n:
        if not (num1 % 3):
            print(num1)
    fib4(n, k, num2, num1 + num2, count + 1)


fib4(n, k)
