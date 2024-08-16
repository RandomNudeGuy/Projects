list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
                  'ternaries', 'smelters', 'termless', 'salted', 'staled',
                  'greatening', 'lasted', 'resmelts']


#$[['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]
#$[['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening'], ['smelters', 'termless', 'resmelts']]     


def sort_anagrams(list_of_strings):
    new_list = []
    for i in list_of_strings:
        innerlist = []
        if i in innerlist:
            continue
        else:
            for x in list_of_strings:
                if sorted(i) == sorted(x) and x not in innerlist:
                    innerlist.append(x)
            if innerlist not in new_list:
                new_list.append(innerlist)
            else:
                continue

    return new_list

print(sort_anagrams(list_of_words))
