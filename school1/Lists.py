mylist = ['judah','castillo','angel']

repeat = 0 

while repeat == 0:
    user = input('input number: ')


    if user in mylist:
        print('user varified')
    else:
        print('it isnt in the list')