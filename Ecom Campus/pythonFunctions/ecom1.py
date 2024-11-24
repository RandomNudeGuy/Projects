from main import add_numbers

FullName = "Jonathan Tzur"
Age = 22
Grade = 100
Grade_Result = (Grade * 3) - 10
printer = FullName, Age, Grade_Result
print(printer)

if __name__ == '__main__':
    print(add_numbers(1, 2))