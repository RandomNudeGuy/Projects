list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
                  'ternaries', 'smelters', 'termless', 'salted', 'staled',
                  'greatening', 'lasted', 'resmelts']

# def list_maker(element1, element2):
#     if sorted(element1) == sorted(element2):
        


def sort_anagrams(list_of_strings):
    new_list = []
    for i in list_of_strings:
        for x in list_of_strings:
            if sorted(i) == sorted(x) and x not in i and x not in new_list:
                new_list.append(x)
    
    return new_list

print(sort_anagrams(list_of_words))
