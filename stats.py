def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    lower_text = text.lower()
    for char in lower_text:
        counts[char] = counts.get(char, 0) +1

    return counts

def sort_dict(counts):
    list = []
    for char, num in counts.items():
        entry = {
            "char": char,
            "num": num
        }
        list.append(entry)



def sort_on(items):
   pass

