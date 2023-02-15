def CompoundInterest(P, r, n, t):
    Amount = P * (pow((1 + (r/n)), n*t))
    print("Initial Investment Was "+ str(P))
    print("In " + str(t) + " Years, You Will Have $" + str(Amount) + " USD")
    print("You Earned " + (str(Amount - P)) + " Dollars")

#P = The Initial Investment
#r = The Interest Rate
#t = The Amount Of Time

print('---------------------------------')
print("Calculate Compound Interest Rate")
print('---------------------------------')

def CompoundIntPrompts():
    principle = float((input('Enter Initial Investment: ')))
    rate = float(input('Enter Interest Rate Percentage: % '))/100
    n_Input = input('Enter Coumpounding Period (1=daily, 2=monthly, 3=yearly): ')
    frequency = 1
    if float(n_Input) == 3:
        frequency = 1
    elif float(n_Input) == 2:
        frequency = 12
    elif float(n_Input) == 1:
        frequency = 365
    
    time = float(input('Enter The Amount Of Time You Would Like To Invest: '))

    CompoundInterest(principle, rate, frequency, time)

CompoundIntPrompts()



    
