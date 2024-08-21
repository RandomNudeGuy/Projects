
def distance(num1, num2, num3):

    if ((abs(num2 - num1) == 1 or abs(num3 - num1) == 1) and (abs(num2 - num1) >= 2 and 
    abs(num2 - num3) >= 2) or (abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2)): #Checking without the vars
        print(True)
    else:
        print(False)

distance(4, 5, 3)
    #     if num2 - num1 and num3 >= 2:
    #         if num3 - num1 and num2 >= 2:
    #             print(True)
    #         else:
    #             print(False)
    #     else:
    #         print(False)
    # else:
    #     print(False) #! line 20 - 28 is previous attempt with ifs to check. didnt work

# def firstrole(num1, num2, num3):
#     firstrole_out = num2 or num3 - num1 == abs(1)
    #?first = abs(num3 - num1)# ALL 4 VARS ARE TO CALCULATE VVVVV
    #?first_2 = abs(num2 - num1)#
    #?second = abs(num2 - num1 and num2 - num3)#
    #?third = abs(num3 - num1 and num3 - num2)#

   #? print(first, second, third) #test to see results
