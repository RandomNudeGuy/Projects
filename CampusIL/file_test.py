file = open(r"I:\Documents\campusil files\campsusil_9.1.2.txt", "r")

line_number = int(input("Line "))

lines = file.readlines()
file.close()
line = lines[line_number - 1]
print(line)