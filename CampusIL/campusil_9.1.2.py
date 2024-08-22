
#% /Users/mcrandom/Documents/campsusil_9.1.2.txt
while True:
    filepath_input = input("Mac or Win?:  ").lower()
    if filepath_input == "mac":
        filepath = open(r"/Users/mcrandom/Documents/campsusil_9.1.2.txt", "r") #open(fr"{filepath_input}", "r")
        print("showoff nigga")
        break
    elif filepath_input == "win":
        filepath = open(r"I:\Documents\campusil files\campsusil_9.1.2.txt", "r") #open(fr"{filepath_input}", "r")
        print("cheap fuck")
        break
    else:
        print("Wrong Input. Mac or Win only.")
        

action_input = input("Choose action: (Last/ Rev/ Sort)").lower()
filepath_reader = filepath.read()
filepath_readline = filepath.readline()

# reader = filepath.read()
# print(reader)
if action_input == "sort": #$  DONE
    sort_list = []
    for i in filepath_reader.split():
        if i not in sort_list:
            sort_list.append(i)
        elif i in sort_list:
            continue
    filepath.close()
    a = sorted(sort_list)
    print(a)    

if action_input == "rev":
    rev_str = ""
    for line in filepath_readline:
        for i in line:
            # if i == "\n":
            #     continue
            # else:
            rev_str = i + rev_str

    print(rev_str)
