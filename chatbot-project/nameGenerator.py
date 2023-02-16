my_list = []
nameNumber = 0
def pickName(fromNames):
    () #choose names
    

while True:
    nameNumber += 1
    names = input("Enter name " + nameNumber + ": ")
    if "no more" in names:
        pickName(my_list)
    my_list.append(names)
