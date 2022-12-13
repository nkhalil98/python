def fib(n):
    if n == 1 or n==0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
def fib_efficient(n, memo={0:1, 1:1}):
    if n in memo:
        return memo[n]
    else:
        result = fib_efficient(n-1, memo) + fib_efficient(n-2, memo)
        memo[n] = result
        return memo[n]