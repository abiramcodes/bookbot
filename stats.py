from typing import Optional

# function to get the contents of the file
def get_book_text(file_path: str) -> Optional[str]: 
    try:
        with open(file_path) as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print("Uh oh, File not found")
    except PermissionError:
        print("Bruh, Need Permission")
    except IsADirectoryError:
        print("Nah bro, No Directories!")

# function to get the no of words in the file content
def split_text(text: str) -> int:
    split_words = text.split()
    return len(split_words)

# frequency counter
def count_chars(text_list: list[str]) -> dict:
    char_dict = {}
    for word in text_list:
        for ltr in word:
            lower_ltr = ltr.lower()
            if lower_ltr in char_dict:
                char_dict[lower_ltr] += 1
            else:
                char_dict[lower_ltr] = 1
    return char_dict

# helper function
def sort_on(items):
    return items["num"]
    
# sort the dict in reverse order based on the count
# create a list and append the dict {}
# use the sorted to sort the dict in a reverse order based on "num"
def sort_dict(char_dict: dict) -> list[dict]:
    char_num_dict = []
    for char in char_dict:
        local_dict = {"char": char, "num": char_dict[char]}
        char_num_dict.append(local_dict)

    return sorted(char_num_dict, reverse=True, key=sort_on)
