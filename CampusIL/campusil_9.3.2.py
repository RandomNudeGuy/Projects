def my_mp4_playlist(file_path, new_song):
    open_read = open(file_path, "r+")
    
    while True:
        seeker = open_read.seek(0)
        data = open_read.readlines() 
        data_len = len(data)
        print(data_len)
        if data_len >= 3:
            ThirdLine = data[2]
            cd_items = []
            # if ThirdLine.strip():  # This checks if the line is not empty after stripping whitespace.
            split_items = [item for item in ThirdLine.split(";") if item]  # Skip empty strings
            cd_items.append(new_song)
            for i in split_items[1:]:
                cd_items.append(i)
            # cd_items.append(split_items[1:])
            cd_items = ";".join(cd_items)
            break
        else:
            empty_lines = """\n\n\n"""
            open_read.writelines(empty_lines)


    

    data[2] = cd_items
    open_read.close()
    open_write = open(file_path, "w")
    open_write.writelines(data)
    open_write.close()
    open_read = open(file_path, "r")
    data = open_read.read()
    print(data)


 





print(my_mp4_playlist(r"/Users/mcrandom/Library/Mobile Documents/com~apple~CloudDocs/Python Projects/Projects/CampusIL/9.3.1 text file.txt", "Python Love Story"))