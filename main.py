# phthon
# in Python

import sys
from stats import get_book_text, get_num_words, get_char_counts, sort_char_counts

if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    counts = get_char_counts(text)
    sorted_items = sort_char_counts(counts)

    for items in sorted_items:
        print(f"{items['char']}: {items['num']}")

    print("============= END ===============")

main()
