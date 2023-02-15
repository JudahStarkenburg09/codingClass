n = float(input('Enter A Number 1-12 For Multiplication Table: '))
t = 1
o = float(input('Enter How Large The Multiplication Table Should Be: '))
while t<=o:
    result = n*t
    print(str(n) + ' x ' + str(t) + ' = ' + str(result))
    t += 1