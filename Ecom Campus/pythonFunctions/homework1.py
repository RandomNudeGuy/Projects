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

# def equall(num1:int, num2:int, num3:int, num4:int):
#     if num1 == num2 and num1 == num3 and num1 == num4:
#         return "all equal"
#     elif (num1 == num2 and num1 != num3 and num1 != num4) or \
#          (num1 == num3 and num1 != num2 and num1 != num4) or \
#          (num1 == num4 and num1 != num2 and num1 != num3) or \
#          (num2 == num3 and num2 != num1 and num2 != num4) or \
#          (num2 == num4 and num2 != num1 and num2 != num3) or \
#          (num3 == num4 and num3 != num1 and num3 != num2):
#         return  "only 2 numbers are equals"
#     else:
#         return "all nums not equall"
#

# ------------------------------------------------------------
#(6) Write a function that receives a parameter of type int.
# The number has to be between 1 to 7 and each number represents each day of the
# week.
# The function has to return the specific day that represents the number. If the number
# is not between 1 to 7, the function has to return the string “Error”.
# Ex: if the number is 2, the function returns “Monday”,
# if the number is 3, the function returns “Tuesday”.....

# def days_of_the_week(day:int):
#     if day == 1:
#         return "Sunday"
#     elif day == 2:
#         return "Monday"
#     elif day == 3:
#         return "Thuesday"
#     elif day == 4:
#         return "Wednesday"
#     elif day == 5:
#         return "Thursday"
#     elif day == 6:
#         return "Friday"
#     elif day == 7:
#         return "Saturday"
#     else:
#         return "Error"
#
# print(days_of_the_week(68))
# ---------------------------------------------------------------
# (7) Write a function that receives a number between 1 to 12.
# Each number represents each month of the year.
# The function has to return the number of the days in the month. If the number given
# is not between 1 to 12, then the functions -1.
# January, March, May, July, August, October, December -> 31 days in a month.
# February -> 28 days in a month.
# April, June, September, November -> 30 days in a month.
# Ex:
# if the number is 1, it means that the user wants to know how many days there are in
# January month.
# if the number is 2, it means that the user wants to know how many days there is in
# February month.
# If the input is 7, the output must be 31.
# If the input is 2, the output must be 28.

# def days_in_the_month(month:int):
#     if month == 1:
#         return 31
#     elif month == 2:
#         return 28
#     elif month == 3:
#         return 31
#     elif month == 4:
#         return 30
#     elif month == 5:
#         return 31
#     elif month == 6:
#         return 30
#     elif month == 7:
#         return 31
#     elif month == 8:
#         return 31
#     elif month == 9:
#         return 30
#     elif month == 10:
#         return 31
#     elif month == 11:
#         return 30
#     elif month == 12:
#         return 31
#     else:
#         return "Error"
#
# print(days_in_the_month(6))

# ----------------------------------------------------------------------
# (8) Write a function that uses global variables. (i made a function that changes a global var from false to true)
# false_bool = False
#
# def change_bool(bool:bool):
#     global false_bool
#     false_bool = True
#     return false_bool
#
# print(change_bool(false_bool))
# -------------------------------------------------------------------------
#(9) Write a function that uses local variables.(i made a function that calculates the root of argument, stores it in a local var, and returns the var)
# def local_root(num:int):
#     result = num ** 0.5
#     return  result
#
# print(local_root(9))