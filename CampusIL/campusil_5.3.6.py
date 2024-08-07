def filter_teens(a=13, b=13, c=13):
    def fix_age(age):
        if 13 <= age <= 14 or 17 <= age <= 19:
            return 0 
        else:
            return age 

    a = fix_age(age=a)
    b = fix_age(age=b)
    c = fix_age(age=c)
    print(a + b + c)

filter_teens(2, 1, 15)
