def get_num_words(filepath):
    with open(filepath) as file:
        return len(file.read().split())
    
def get_num_chars(filepath):
    with open(filepath) as file:
        content = file.read().lower()
    each_let = {}
    for letter in content:
        if letter in each_let:
            temp = each_let[letter] + 1
            each_let[letter] = temp
        else:
            each_let[letter] = 1
    return each_let

def sort_by(items):
    return items["num"]

def get_dict_as_list(dict):
    sorted_list = []
    for dkey in dict:
        item = {"char":dkey, "num":dict[dkey]}
        sorted_list.append(item)
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list