# Exercise 1:
# 1. Create an array consisting of strings, each representing a day of the week,
# and display it.
# 2. Sort the array in default order and print it.
# 3. Sort the array in reverse order and print it
# 4. Create a function that receives the array and the way how to sort it as
# parameter and execute the sorting according to the parameter and print the
# array.
#
# Days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #
#
# def Sort_Array(Days, Sorting):
#     if Sorting == "default":
#         return Days
#     elif Sorting == "reverse":
#         Days.reverse()
#         return Days
#
# print(Days)
#
# Days.reverse()
# print(Days)
#
# print(Sort_Array(Days, "default"))
# ----------------------------------------
# Exercise 2:
# 1. Create a function that receives an integer array and a number as parameters
# (the number will serve as the array's index).
# 2. Display the array's value corresponding to the index number passed. For
# instance, if the number passed is 2, the value in the array at index 2 should be
# printed.
# 3. If the number provided is not within the range of the array's index, display the
# message "Sorry, no value in the array for index number: {number}"
#
# array_int = [1, 2, 3, 4, 5, 6, 7]
#
# def index_display(array, index):
#     if len(array) <= index:
#         return f"Sorry, no value in the array for index number: {index}"
#     else:
#         return array[index]
#
# print(index_display(array_int, 7))
# -----------------------------------------
#
# Exercise 3:
# 1. Create a function that takes in an array of integers. If every element in the
# array is an odd number, the function should return "odds"; otherwise, it should
# return "not odds".
#
# array = [1, 3, 5, 7]
#
# def is_odds(x):
#     if x % 2 == 1:
#         return True
#     else:
#         return False
#
# filtered_array = filter(is_odds, array)
# new_array = list(filtered_array)
#
# if new_array == array:
#     print("odds")
# else:
#     print("not odds")
#--------------------------------------------------
# Exercise 4:
# 1. Create a function that accepts an integer array and a single integer as
# parameters. If the number passed is found within the array, the function
# should return "found". Otherwise, the function should return "not found".
#
#
# array = [1, 2, 3, 4, 5]
#
# def founder(numbers, num):
#     if num in numbers:
#         return True
#     else:
#         return False
#
# print(founder(array, 1))
#------------------------------------------------------
#
# Exercise 5:
# 1. Create a function that accepts an array and two integer numbers. If the first
# value in the array matches the first input parameter and the last value in the
# array matches the second input parameter, then the function should return
# true. Otherwise, the function should return false.
#
# array = [1, 2, 3, 4, 5, 6, 7]
#
# def check_array(numbers, num1, num2):
#     if numbers[0] == num1 and numbers[-1] == num2:
#         return True
#     else:
#         return False
#
#
# print(check_array(array, 7, 8))
#------------------------------------------------------
# Exercise 6:
# 1. Create a function that takes an array as its input. Depending on the condition
# met, the function should return one of the following:
# ● If all array values are less than 50, return "smaller than 50".
# ● If all array values are between 51 and 100, return "between 51 to 100".
# ● If all array values are between 101 and 200, return "between 101 to
# 200". 
# ● If all array values exceed 200, return "greater than 200".
# ● If none of the aforementioned conditions are satisfied, your function
# should display "No condition is met".
#
# array = [6, 66, 64, 67, 62, 68]
#
# def less_than_50(x):
#     if x <= 50:
#         return True
#     else:
#         return False
#
# def between_51_and_100(x):
#     if 51 <= x <= 100:
#         return True
#     else:
#         return False
#
# def between_101_and_200(x):
#     if 101 <= x <= 200:
#         return True
#     else:
#         return False
#
# def over_200(x):
#     if 201 <= x:
#         return True
#     else:
#         return False
#
#
# filtered_lessthan50 = filter(less_than_50, array)
# filtered_between_51_and_100 = filter(between_51_and_100, array)
# filtered_between_101_and_200 = filter(between_101_and_200, array)
# filtered_over_200 = filter(over_200, array)
#
# if array == list(filtered_lessthan50):
#     print("smaller than 50")
# elif array == list(filtered_between_51_and_100):
#     print("between 51 to 100")
# elif array == list(filtered_between_101_and_200):
#     print("between 101 to 200")
# elif array == list(filtered_over_200):
#     print("more than 200")
# else:
#     print("No condition is met")

