from stats import get_num_words, count_characters, sort_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counts = count_characters(text)
    sorted_list = sort_dict(counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
