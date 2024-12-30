n, k = int(input()), int(input())


def fib3(n, k, min_index=0, max_index=0, min_val=1, max_val=1, sum=0, num1=1, num2=1, count=1):
    if count > k:
        print('Sum: {}\nMax: {}, Index: {}\nMin: {}, Index: {}\n'.format(sum, max_val, max_index, min_val, min_index))
        return
    a = num1 if num1 % 2 else -(count ** 2)
    fib3(n, k, count if a < min_val and count >= n else min_index, count if a > max_val and count >= n else max_index,
         a if a < min_val and count >= n else min_val, a if a > max_val and count >= n else max_val,
         sum + a if count >= n else sum, num2, num1 + num2, count + 1)


fib3(n, k)
