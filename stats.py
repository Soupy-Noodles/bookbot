def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    # Create a list of dicts for alphabetical characters only
    char_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    # Sort the list by count descending
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list