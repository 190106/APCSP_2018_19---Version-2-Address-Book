from __future__ import print_function
system = input(""""Which number system would you like to convert your decminal number into?
2. Binary
3. Base 3
4. Base 4
5. Base 5
6. Base 6
(Fun fact: base 2, 8, 16 are the most commonly used number systems for computers!!""")

if system == 2 :
    while True:
        def binary(x):
            strbin=''
            if int(x)>1:
        # if number is bigger than one then the program will then run this portion
                binary(int(x)//2)
        # This part calls the function binary() and the argument is x divided by 2 rounded down to an integer
        # ie. if the user was to input "3" it would divide 3 by 2 to get 1.5 but round down to 1
            print (int(x)%2, end="")





        print ("\n")
        # Gets the remainder of the division function and places all the numbers outputed into one line
        num=raw_input('enter a number or type n to exit')
        if str(num) == "n":
            break
        # Asks for user input for a decimal/denary value to calculate the binary value
        binary(num)
        # Calls on the function

        #Example number "10"
        # 1. 10 % 2

        # 2. 5 % 2

        # 3. Round down to 2 from 2.5 ---- 2 % 2

        # 4. 1 % 2

        # 5. Placement values of remainders are printed backwards from last digit to first
        # ie. in the binary of 1010 it would first place the zero on the right and then move left from that digit

elif system == 3 :
    while True:
        def binary(x):
            strbin=''
            if int(x)>1:
                binary(int(x)//3)
            print (int(x)%3, end="")
        print ("\n")
        num=raw_input('enter a number or type n to exit')
        if str(num) == "n":
            break
        binary(num)

if system == 4 :
    while True:
        def binary(x):
            strbin=''
            if int(x)>1:
                binary(int(x)//4)
            print (int(x)%4, end="")
        print ("\n")
        num=raw_input('enter a number or type n to exit')
        if str(num) == "n":
            break
        binary(num)


if system == 5 :
    while True:
        def binary(x):
            strbin=''
            if int(x)>1:
                binary(int(x)//5)
            print (int(x)%5, end="")
        print ("\n")
        num=raw_input('enter a number or type n to exit')
        if str(num) == "n":
            break
        binary(num)

if system == 6 :
    while True:
        def binary(x):
            strbin=''
            if int(x)>1:
                binary(int(x)//6)
            print (int(x)%6, end="")
        print ("\n")
        num=raw_input('enter a number or type n to exit')
        if str(num) == "n":
            break
        binary(num)
