with open("books/frankenstein.txt") as book:
    file_contents = book.read()
    

def word_count(contents):
    return (len(contents.split()))


def letter_count(contents):
    lower_case = contents.lower()
    letter_dict = {}

    for letter in lower_case:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def report(input, num_words):
    input_list = list(input.items())
    input_list.sort(reverse=True, key=lambda input_list: input_list[1])

    print(f"--- Begin report of books/frankenstein.txt ---\n {num_words} words found in the document\n")
    
    for letter, count in input_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

report(letter_count(file_contents), word_count(file_contents))


