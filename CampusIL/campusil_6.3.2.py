# list1 = ["111", "234", "2000", "goru", "birthday", "09"]

# def longest(my_list):
#     a = sorted(my_list, key = len)
#     return a[-1]

# print(longest(list1))

# --------------------

list1 = ["111", "234", "2000", "goru", "birthday", "09"]

def longest(my_list):
    return max(my_list, key = len)

print(longest(list1))
