def linear_sqrt(x, epsilon, increment):
    assert x >= 0
    assert epsilon > 0
    guess = 0
    while abs(guess * guess - x) >= epsilon and guess * guess <= x:
        guess += increment
    if abs(guess * guess - x) >= epsilon:
        print(f"Failed to calculate square root of {x}.")
        print(f"Last guess was {guess}.")
        return -1
    return guess


def bisect_sqrt(x, epsilon):
    assert x >= 0
    assert epsilon > 0
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


def newton_raphson(x, epsilon):
    assert x >= 0
    assert epsilon > 0
    guess = x / 2
    while abs(guess * guess - x) >= epsilon:
        guess -= (guess**2 - x) / (2 * guess)
    return guess
