def print_last_digit(number):
    result = ((number % 10) if number > 0 else ((number * -1) % 10))
    print(result, end="")
    return (result)
