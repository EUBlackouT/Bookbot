def count_words(text):

    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_characters(char_count):
    # Create a list of dictionaries
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"character": char, "count": count})
    
    # Define a sort function to sort by count
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list from greatest to least by count
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
    

