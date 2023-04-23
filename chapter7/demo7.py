def func(number):
    if number == 1:
        return 1
    else:
        return func(number - 1) * number


print(func(10))





























