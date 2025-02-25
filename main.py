from stats import get_num_words, get_num_char, sort_char_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(book_text)
    print(str(num_words) + " words found in the document")

    num_char = get_num_char(book_text)

    # print(num_char)

    ch_sort = sort_char_dict(num_char)

    print(ch_sort)
    
    # for ch in ch_sort:
    #     if str(ch).isalpha() == True:
    #         print(f"{ch}: {ch[1]}")

main()