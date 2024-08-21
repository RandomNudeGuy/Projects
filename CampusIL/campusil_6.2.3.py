# my_list = ["hydrgoen", "helium", "lithium", "beryllium", "boron", "magnesium"]
# def format_list(my_list):
#     even_list = ", ".join(my_list[0::2])
#     last_list = my_list[-1:]
#     strRes = even_list + ", and",  last_list
#     return strRes

#     # last_list = "".join(my_list[-1:])
#     # x = ", ".join(even_list)
#     # y = "".join(last_list)
#     # strRes = x + ", and",  y
#     # return strRes
#     # print(x + ", and", y)

# strRes2 = format_list(my_list)
# print(strRes2) 

my_list = ["hydrgoen", "helium", "lithium", "beryllium", "boron", "magnesium"]
def format_list(my_list):
    even_list = my_list[0::2]
    last_list = my_list[-1:] 
    SPACE = ", "
    AND = "--AND--"
    x = SPACE.join(even_list)
    y = AND.join(last_list)
    strRes = x + ", and " + y
    return strRes

print(format_list(my_list))



