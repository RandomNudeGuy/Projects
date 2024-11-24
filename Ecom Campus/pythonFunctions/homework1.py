# (1) Write a function that receives two parameters of type int.
# If the first parameter is bigger than the second parameter -> the function should
# returns the first parameter
# else -> the function should return the second parameter

# def big_number(first_num, second_num):
#     if first_num > second_num:
#         return
#     else:
#         return second_num
# ----------------------------------------------
# (2) Write a function that receives 2 parameters of type int.
# If the first parameter is equal to the second parameter -> the function should add 1 to
# the first parameter and return it.
#
# def check_num(first_num:int, second_num:int):
#     if first_num == second_num:
#         first_num += 1
#         return  first_num
#     else:
#         return
#-----------------------------------------------
# (3) Write a function that receives four parameters of type int.
# The function has to return the smaller value between all of them.
# If one of the parameters is between 1 to 5, then return -1.

# def small_value(first_num:int, second_num:int, third_num:int, four_num:int):
#     if 1 <= first_num <= 5 or 1 <= second_num <= 5 or 1 <= third_num <= 5 or 1 <= four_num <= 5:
#         return -1
#     else:
#         if first_num < second_num and first_num < third_num and first_num < four_num:
#             return first_num
#         elif second_num < first_num and second_num < third_num and second_num < four_num:
#             return second_num
#         elif third_num < second_num and third_num < first_num and third_num < four_num:
#             return third_num
#         elif four_num < second_num and four_num < third_num and four_num < first_num:
#             return four_num
#
#
# print(small_value(10,11,7,11))
# ----------------------------------------------------------
# (4) Write a function that receives one parameter of type int.
# If the number is even then return the string : “even”, otherwise “not even”.

# def even_not_even(num:int):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return ("not even")
#
# print(even_not_even())
# ----------------------------------------------------------
# (5) White a function that receives 4 parameters of type int.
# If all the four numbers are equal, the function returns the string “all equals”.
# If 2 of the four numbers are equals, the function returns the string “only 2 numbers
# are equals”.
# If none of the two cases happened, the function returns the string “all numbers not
# equals”.

def equall(num1:int, num2:int, num3:int, num4:int):
    
