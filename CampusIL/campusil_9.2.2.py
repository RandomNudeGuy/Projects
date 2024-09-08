copy_des = open(r"I:\Documents\campusil files\campusil_9.2.2\copy.txt", "r")
paste_des = open(r"I:\Documents\campusil files\campusil_9.2.2\paste.txt", "w+")


def copy_file_content(source, destination):
    for line in source:
        destination.write(line)
    source.close()
    destination.close()
    

copy_file_content(copy_des, paste_des)