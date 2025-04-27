def sqrt(n):
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number")

    guess = 0

    while guess * guess < n:
        guess += 1

    if guess * guess == n:
        return guess
    else:
        return -1


def linear_sqrt(x, epsilon=0.01):
    _validate_input(x, epsilon)

    guess = 0
    increment = epsilon**2

    while abs(guess * guess - x) >= epsilon and guess * guess <= x:
        guess += increment

    if abs(guess * guess - x) >= epsilon:
        return -1

    return guess


def bisect_sqrt(x, epsilon=0.01):
    _validate_input(x, epsilon)

    if x <= 1:
        low = 0
        high = 1
    else:
        low = 1
        high = x

    guess = (low + high) / 2

    while abs(guess * guess - x) >= epsilon:
        if guess * guess > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    return guess


def newton_raphson(x, epsilon=0.01):
    _validate_input(x, epsilon)

    guess = x / 2
    while abs(guess * guess - x) >= epsilon:
        guess -= (guess**2 - x) / (2 * guess)  # also: guess = (guess + x / guess) / 2
    return guess


def _validate_input(x, epsilon):
    assert x >= 0, "x must be non-negative"
    assert epsilon > 0, "epsilon must be positive"
    assert epsilon < 1, "epsilon must be less than 1"
