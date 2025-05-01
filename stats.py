def word_count(output):
    count = output.split()
    num = len(count)
    return num

def character_count(output):
    char_count = {}
    out1 = output.lower()
    for char in out1:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def dict_seperate(sort_dict):
    comp_list = []
    # we loop through all key: value pairs in the dict  
    for k, v in sort_dict.items():
    # assign new values here
        newkey = k
        char = k
        num = v
        
    # we then create a new entry for the newkey if it does not exist
        if newkey not in comp_list:
           newkey = {'char': char, 'num': num}
           comp_list.append(newkey)
    return comp_list

def sorted_dict(nums):
        return nums["num"]

def sort_dict_list(complete_list):
    complete_list.sort(reverse=True, key=sorted_dict)
    return complete_list