
# def create_table():

def add_customer(customers_arrive):
    global tables
    global tables_taken
    if customers_arrive <= 4 and tables_taken < 5:
        if tables == tables_taken:
            tables += 1
            tables_taken += 1
            return tables_taken, tables
        tables_taken += 1
        return tables_taken, tables
    elif customers_arrive > 4:
        return "up to 4 people"
    else:
        return "no more room"

if __name__ == '__main__':
    tables = 3
    tables_taken = 0
    MAX_CUSTOMERS_TABLE = 4
    print(add_customer(4)) # first 4 people success
    print(add_customer(5)) #5 people no success
    print(add_customer(4)) # second 4 people success
    print(add_customer(4)) # third 4 people success
    print(add_customer(4)) # fourth 4 people success
    print(add_customer(4))# fifth 4 people success
    print(add_customer(4)) # sixth 4 people fail, no tables




