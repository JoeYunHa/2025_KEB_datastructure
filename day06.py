fibonacci = [0,1]

def fibonacci_recursion(n) -> int:
    if n <=1:
        return fibonacci[n]
    else:
        if len(fibonacci) > n:
            return fibonacci[n]
        else:
            fibonacci.append(fibonacci_recursion(n-2) + fibonacci_recursion(n-1))
            return fibonacci[n]

memo = dict()
def fibonacci_memo(n) -> int:
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1)
        return memo[n]



num = int(input())
print(fibonacci_recursion(num))
print(fibonacci_memo(num))

