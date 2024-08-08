old_list = input("Enter the list: ") #$ !

old_list_listed = list(old_list.split(","))



    

def print_old_list(string): #$ 1 !
    listed = list(string.split(","))
    listed_join = ", ".join(listed)
    return listed_join

def len_old_list(string): #$ 2 !
    listed = string.split(",")
    length = len(listed)
    return length

def is_item_inlist(string): #% 3 !
    if string in old_list_listed:
        return True
    else:
        return False

def how_many_item(string): #$ 4 !
    number_of_item = old_list_listed.count(string)
    return number_of_item

# def delete_item_fromlist(num:int):







def quit(): #$ 9 ! 
    print("Goodbye!")
    return

def Main_Menu():#% 2 - 
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
        print(print_old_list(old_list))
        print("Thanks for using!")
        Main_Menu()

    elif Menu == "2": #$ 2 !
        print(len_old_list(old_list))
        print("Thanks for using!")
        Main_Menu()

    elif Menu == "3": #% 3 !
        item = input("Which Item?: ") #! lower / higher case
        print(is_item_inlist(item))
        print("Thanks for using!")
        Main_Menu()

    elif Menu =="4": #$ 4 !
        item = input(f"Which Item?: ")
        print(how_many_item(item))
        print("Thanks for using!")
        Main_Menu()


    elif Menu == "5":
        a = len_old_list(old_list)
        item = input(f"Which Item? 0 - {a - 1} : ")
        print(how_many_item(item))
        print("Thanks for using!")
        Main_Menu()

    # elif Menu == "6":

    # elif Menu == "7":

    # elif Menu == "8":

    elif Menu == "9":
        quit()

    else:
        print("Invalid Input")
        Main_Menu()


Main_Menu()

