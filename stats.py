def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counts = {}
    lower_text = text.lower()
    for char in lower_text:
        counts[char] = counts.get(char, 0) + 1

    return counts


def sort_on(items):
    return items["num"]


def sort_dict(counts):
    sorted_list = []
    for char, num in counts.items():
        entry = {"char": char, "num": num}
        sorted_list.append(entry)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
