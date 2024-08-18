my_dict = {"first_name": "Maria", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}

def last_name(last_name): #1
    return last_name

def maria_month(birthday_value): #2
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

def hobby_num(hobby): #3
    a = len(hobby)
    return a

def last_hobby(hobby):#4
    a = hobby[-1]
    return a

def add_hobby(hobby:list): #5
    action_5 = input("Add another hobby: ")
    hobby.append(action_5)
    return hobby

def tuple_birthday(birthday): #6
    d = birthday[0:2]
    m = birthday[3:5]
    y = birthday[6:]
    tuple_bday = (d, m, y)
    return tuple_bday

def age_calc(birthday): #7
    y = birthday[6:]
    year = int(y)
    calc = year - 2024
    calc_fix = abs(calc)
    return calc_fix

while True:
    action = input("""Enter your input: (1-7)
1. Last Name
2. Maria Month 
3. Nunber of Hobbies
4. Last Hobby on list
5. Add Hobby
6. Tuple > Birthday
7. Age calc\n""")
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
        print(tuple_birthday(my_dict["birth_date"]))
        
    elif action == "7":
        print(age_calc(my_dict["birth_date"]))

    else:
        print("Invalid input. 1 - 7 Only.\nTry Again")

