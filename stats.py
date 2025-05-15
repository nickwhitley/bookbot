def count_words(content):
    words_count = len(content.split())
    return words_count

def char_count(content):
    char_dict = {}
    char_set = set()
    words = content.split()

    for word in words:
        for char in word:
            char = char.lower()
            if char in char_set:
                char_dict[char] += 1
            else:
                char_set.add(char)
                char_dict[char] = 1

    return char_dict

def get_report_dicts(char_dict):
    dict_list = []
    for char in char_dict:
        pair = {
            "char": char,
            "num": char_dict[char]
        }
        dict_list.append(pair)
    return sorted(dict_list, key=lambda item: item['num'], reverse=True)
