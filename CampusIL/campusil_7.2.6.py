old_list = input("Enter the list: ") #$ !

old_list_listed = list(old_list.split(","))



    

def print_old_list(string): #$ 1 !
    # listed = list(string.split(","))
    listed_join = ", ".join(string)
    return listed_join

def len_old_list(string): #$ 2 !
    # listed = string.split(",")
    length = len(string)
    return length

def is_item_inlist(string): #% 3 !
    if string in old_list_listed:
        return True
    else:
        return False

def how_many_item(string): #$ 4 !
    number_of_item = old_list_listed.count(string)
    return number_of_item

def delete_item_fromlist(num:int): #$ 5 !
    old_list_listed.remove(old_list_listed[num])
    return print_old_list(old_list_listed)

def add_item_fromlist(string): #$ 6 !
    global old_list_listed
    old_list_listed.append(string)
    return print_old_list(old_list_listed)

def illegal_item_print(string): #$ 7 !
    new_list = []
    for i in string:
        if len(i) < 3 or i.isalpha() == False:
            new_list.append(i)
        else:
            continue
    return new_list

def duplicates_item_fromlist(string:list):
    new_list = []
    for i in string:
        if i not in new_list:
            new_list.append(i)
        else:
            continue
    global old_list_listed
    old_list_listed = new_list
    return old_list_listed

def quit(): #$ 9 ! 
    print("Goodbye!")
    return




while True:
    Menu = input("""Welcome to practice 7.2.6
1. Print List
2. List Length
3. Check if item in list
4. Check how many time item in list
5. Delete item from list
6. Add an item to list
7. Print all illegal items
8. Remove Duplicates
9. Quit
Choose an action: """) #$ 1 !
    
    if Menu == "1": #$ 1 !
        print(print_old_list(old_list_listed))

    elif Menu == "2": #$ 2 !
        print(len_old_list(old_list_listed))

    elif Menu == "3": #% 3 !
        item = input("Which Item?: ") #! lower / higher case
        print(is_item_inlist(item))

    elif Menu =="4": #$ 4 !
        item = input(f"Which Item?: ")
        print(how_many_item(item))

    elif Menu == "5": #$ 5 !
        a = len_old_list(old_list_listed)
        item = int(input(f"""Which Item? 0 - {a - 1} : 
{print_old_list(old_list_listed)} """))
        print(delete_item_fromlist(item))

    elif Menu == "6": #$ 6 !
        item = input("Which Item?: ")
        print(add_item_fromlist(item))
    
    elif Menu == "7": #$ 7 !
        print(print_old_list(illegal_item_print(old_list_listed)))

    elif Menu == "8": #$ 8 !
        duplicates_item_fromlist(old_list_listed)
        print("Done!")

    elif Menu == "9": #$ 9 !
        print("Goodbye!")
        break

    else:
        print("Invalid Input")




