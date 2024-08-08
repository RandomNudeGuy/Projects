#campusil_7.2.5
#! DONE WITH CHATGPT
def sequence_del(my_str):
    result = my_str[0]
    for i in range(1, (len(my_str))):
        if my_str[i] != my_str[i -1]:
            result += my_str[i]
    
    return result


print(sequence_del("Heeyyy   yyouuuu!!!"))