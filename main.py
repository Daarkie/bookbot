import sys

from stats import get_num_words, get_num_chars, get_dict_as_list

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    filepath = arguments[1]
    print(f"Analyzing book found at {filepath}...")
    num_words = get_num_words(filepath)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars_list = get_dict_as_list(get_num_chars(filepath))
    print("--------- Character Count -------")
    for item in chars_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()