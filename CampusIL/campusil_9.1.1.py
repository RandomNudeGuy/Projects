file1 = open(r"/Users/mcrandom/Documents/campsusil_test2.rtf", "r")
file2 = open(r"/Users/mcrandom/Documents/campsusil_test.rtf", "r")

def are_files_equal(file1, file2):
    if file1.read() == file2.read():
        return True
    else:
        return False

print(are_files_equal(file1, file2))