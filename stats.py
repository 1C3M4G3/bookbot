def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    lower_text = text.lower()
    for char in lower_text:
        counts[char] = counts.get(char, 0) +1

    print(counts)
