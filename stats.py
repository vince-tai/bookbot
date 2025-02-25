def get_num_words(file_contents):
    return len(file_contents.split())

def get_num_char(file_contents):
    file_list = list(file_contents)
    char_counts_dict = {}

    for char in file_list:
        ch = char.lower()
        if ch not in char_counts_dict:
            char_counts_dict[ch] = 1
        else:
            char_counts_dict[ch] += 1
    
    return char_counts_dict

def sort_char_dict(char_counts_dict):
    char_counts_list = list(char_counts_dict.items())
    char_counts_list.sort(reverse=True, key=sort_item)
    return char_counts_list

def sort_item(item):
    return item[1]
