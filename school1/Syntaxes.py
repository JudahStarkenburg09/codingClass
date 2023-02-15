x = 0
while x < 5:
    x = x+1
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print("New Client:")
    name = input("Enter Your Name: ")
    birth = input("Enter Your Birthdate (X/X/X): ")
    reason = input("Enter The Reason You Are Here: ")
    appointment = input("Enter Todays Date: ")
    print('-------------------------')
    print("Info On Client:")
    print(name + ", " + "BirthDate: " + birth + ", Date Of Appointment: " + appointment + ", " + "Is Here For *" + reason + "*")