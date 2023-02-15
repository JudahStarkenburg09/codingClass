def answer(number):

    if number == 0:
        return 1

    else:
        return number * answer(number-1)

number = int(input("Enter A Number Tp Recieve The Factorial: "))

print(answer(number))