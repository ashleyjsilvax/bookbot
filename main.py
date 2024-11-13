def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    sorted_letters = sort_characters(book_text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char_dict in sorted_letters:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)



def get_letters_in_book(text):
    letters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters
        
        
def sort_characters(text):
    letters = get_letters_in_book(text)
    char_list = []
    
    def sort_on(dict):
        return dict["num"]
    
    for letter in letters:
        if letter.isalpha():
            letter_dict = {"char": letter, "num": letters[letter]}
            char_list.append(letter_dict)
    
    print("Before sorting:", char_list)  # Debug print
    char_list.sort(reverse=True, key=sort_on)
    print("After sorting:", char_list)   # Debug print
    return char_list
            
            
        



main()