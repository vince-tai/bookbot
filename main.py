from stats import get_num_words, get_num_char, sort_char_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    num_words = get_num_words(book_text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    num_char = get_num_char(book_text)
    ch_sort = sort_char_dict(num_char)
    for ch in ch_sort:
        if str(ch[0]).isalpha() == True:
            print(f"{ch[0]}: {ch[1]}")

main()