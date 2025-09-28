import sys
from stats import get_book_text, split_text, count_chars, sort_dict
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_content = get_book_text(sys.argv[1]);
    if file_content:
        words_count = split_text(file_content)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("----------- Character Count ----------")
        word_split = file_content.split()
        char_count = count_chars(word_split)
        # loop through the dict and print in a specific way
        for char_dict in sort_dict(char_count):
            print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")
    
    
main()

