

def my_mp3_playlist(file_path):
    with open(file_path, "r") as file:
        file_read = file.read()
    
    file_split = file_read.split("\n")
    cd_items = []
    
    for element in file_split:
        if element.strip():  # This checks if the line is not empty after stripping whitespace.
            split_items = [item for item in element.split(";") if item]  # Skip empty strings
            cd_items.append(split_items)

    SongLength = []
    for i in cd_items:
        SongLength.append(i[-1])
    print(sorted(SongLength, reverse=True))
    

print(my_mp3_playlist(r"/Users/mcrandom/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/Projects/CampusIL/9.3.1 text file.txt"))