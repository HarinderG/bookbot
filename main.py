from stats import get_word_count, character_frequency, sorts
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {sys.argv[1]}...')

    print("----------- Word Count ----------")
    num_words = get_word_count(text)
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    char_dict = character_frequency(text)
    # print(char_dict)
    sorted_list_of_chars = sorts(char_dict)

    for d in sorted_list_of_chars:
        if d["char"].isalpha():
            print(f'{d["char"]}: {d["num"]}')

    print("============= END ===============")

main()
