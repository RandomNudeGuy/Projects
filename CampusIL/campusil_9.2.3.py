def who_is_missing(file_name):
    file = open(file_name, "r")
    mis_numbers = []
    temp_num = 1
    readlines = file.readline()
    readlines = readlines.strip()
    readlines = readlines.split(",")
    readlines = sorted(readlines)
    readlines = ",".join(readlines)
    for i in readlines:
        if i == ",":
            continue
        else:
            if i == str(temp_num):
                # print(i)
                temp_num += 1
            else:
                while True:
                    if temp_num < int(i):
                        mis_numbers.append(temp_num)
                        temp_num += 1
                    else:
                        temp_num += 1
                        break


    file.close()
    new_file = open(r"I:\Documents\campusil files\campusil_9.2.3\found.txt", "w")
    new_file.write(str(*mis_numbers))                    
    print(readlines)
    print(mis_numbers)

who_is_missing(r"I:\Documents\campusil files\campusil_9.2.3\findMe.txt")