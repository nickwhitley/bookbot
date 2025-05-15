from stats import count_words
from stats import char_count
from stats import get_report_dicts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    book_result = get_book_text(file_path)
    words_count = count_words(book_result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    char_dict_list = get_report_dicts(char_count(book_result))

    for char_dict in char_dict_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

if __name__=="__main__":
    main()