mylist = ['judah','castillo','angel']

repeat = 0 

while repeat == 0:
    user = input('input number: ')


    if user in mylist:
        print('user varified')
    else:
        print('it isnt in the list')

    print(mylist)
    print("Select A Name")
    selected = input(">> ")
    if selected == mylist[0]:
        print('you selected ' + mylist[0])
    if selected == mylist[1]:
        print('you selected ' + mylist[1])
    if selected == mylist[2]:
        print('you selected ' + mylist[2])