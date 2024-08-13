products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
def MyFn(s):
    return s[-1]

def sort_prices(list_of_tuples):
    for i in list_of_tuples:
        sorted_list = sorted(list_of_tuples, key=MyFn, reverse=True)
    return sorted_list



print(sort_prices(products))