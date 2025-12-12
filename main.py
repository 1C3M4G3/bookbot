from stats import *

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    counts = count_characters(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
        

main()