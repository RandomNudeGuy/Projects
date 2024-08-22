
#% /Users/mcrandom/Documents/campsusil_9.1.2.txt

#filepath_input = input("Enter File Path: ")
filepath = open(r"/Users/mcrandom/Documents/campsusil_9.1.2.txt", "r") #open(fr"{filepath_input}", "r")
action_input = input("Choose action: (Last/ Rev/ Sort)").lower()
filepath_reader = filepath.read()

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
    for line in filepath_reader:
        for i in line:
            rev_str = i + rev_str

    print(rev_str)
