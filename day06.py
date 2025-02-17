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

num = int(input())
print(fibonacci_recursion(num))


