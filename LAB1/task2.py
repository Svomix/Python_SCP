n, k = int(input()), int(input())


def fib2(n, k, num1=1, num2=1, count=1):
    if count > k:
        return
    elif count >= n:
        print(num1 if num1 % 2 else -(count ** 2))
    fib2(n, k, num2, num1 + num2, count + 1)


fib2(n, k)
