import time
import sys
a = float(input('Enter 1 To List Multiples Of 5: ='))
m = float(input('Enter Max Of Multiples: ='))
i = 0
n = 0
s = 0
while a == 1:
    while n < m:
        n += 1
        i += 5
        time.sleep(0.001)
        print(i)
        s = (s + i)
    else:
        c = float(input('Enter 1 To Add Up All The Multiples: ='))
        if c == 1:
            print('The Sum Of All Multiples Is: ' + str(s))
            print('\n')
            sys.exit()
