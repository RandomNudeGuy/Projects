temp_input = input("Enter tempeture: (eg, 30C/F)")

temp_num = float(temp_input[:-1])
# print(temp_num)

if temp_input[-1:].lower() == "f":
    temp = (5 * temp_num - 160) / 9
    print(temp)
elif temp_input[-1:].lower() == "c":
    temp = (9 * temp_num + (32 * 5)) / 5
    print(temp)
else:
    print("INVALID TEMPATURE / INPUT")