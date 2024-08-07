def seven_boom(end_number:int):
    list1 = []
    x = end_number + 1
    for num in range(x):
        if num % 7 == 0 or "7" in str(num):
            list1.append("BOOM")
            num += 1
        else:
            list1 += [num]
            num += 1
    return list1

print(seven_boom(17))