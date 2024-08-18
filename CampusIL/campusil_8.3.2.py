my_dict = {"first_name": "Maria", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}

def last_name(last_name):
    return last_name

def maria_month(birthday_value):
    month_num = birthday_value[3:5]
    if month_num == "01":
        month = "Janurary"
    elif month_num == "02":
        month = "Feburary"
    elif month_num == "03":
        month = "March"
    elif month_num == "04":
        month = "April"
    elif month_num == "05":
        month = "May"
    elif month_num == "06":
        month = "June"    
    elif month_num == "07":
        month = "July"
    elif month_num == "08":
        month = "August"   
    elif month_num == "09":
        month = "September"
    elif month_num == "10":
        month = "October"
    elif month_num == "11":
        month = "November"
    elif month_num == "12":
        month = "December"
    
    month_r = f"{month_num} aka {month}"
    return month_r

def hobby_num(hobby):
    a = len(hobby)
    return a

def last_hobby(hobby):
    a = hobby[-1]
    return a

def add_hobby(hobby:list):
    action_5 = input("Add another hobby: ")
    hobby.append(action_5)
    return hobby

while True:
    action = input("Enter your input: (1-7)\n")
    if action == "1":
        print(last_name(my_dict["last_name"]))
        
    elif action == "2":
        print(maria_month(my_dict["birth_date"]))

    elif action == "3":
        print(hobby_num(my_dict["hobbies"]))

    elif action == "4":
        print(last_hobby(my_dict["hobbies"]))

    elif action == "5":
        print(add_hobby(my_dict["hobbies"]))

    elif action == "6":
        

    # elif action == "7":

    else:
        print("Invalid input. 1 - 7 Only.\nTry Again")

