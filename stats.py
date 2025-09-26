def get_word_count(text):
    list_of_words = text.split()
    return len(list_of_words)

def character_frequency(text):
    my_dict = {}

    for character in text:
        character = character.lower()
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1

    return my_dict

def sorts(char_dict):
    list_of_dicts = []
    for key in char_dict:
        list_of_dicts.append({"char": key, "num": char_dict[key]})

    list_of_dicts.sort(reverse=True, key=lambda count: count["num"])

    return list_of_dicts
