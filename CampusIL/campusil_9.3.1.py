

def my_mp3_playlist(file_path):
    with open(file_path, "r") as file:
        file_read = file.read()
    
    file_split = file_read.split("\n")
    cd_items = []
    song_amount = 0
    
    for element in file_split:
        if element.strip():  # This checks if the line is not empty after stripping whitespace.
            split_items = [item for item in element.split(";") if item]  # Skip empty strings
            cd_items.append(split_items)

    SongLength = []
    SongName = []
    for i in cd_items:
        song_amount += 1
        SongName.append(i[1])
        SongLength.append(i[-1])
    
    SongLengthSorted = sorted(SongLength, reverse=True)
    for i in cd_items:
        if i[-1] == SongLengthSorted[0]:
            global SongLengthResult
            SongLengthResult = i[0]
    temp_sn_list = []
    
    for i in SongName:
        first_counter = SongName.count(i)
        if first_counter not in temp_sn_list:
            temp_sn_list.append(first_counter)
            temp_sn_list.sort()
        else:
            continue
    for i in SongName:
        if SongName.count(i) == temp_sn_list[-1]:
            global SongNameResult
            SongNameResult = i
            break
        else:
            continue
    
    return (SongLengthResult, song_amount, SongNameResult)


    
print(my_mp3_playlist(r"/Users/mcrandom/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/Projects/CampusIL/9.3.1 text file.txt"))