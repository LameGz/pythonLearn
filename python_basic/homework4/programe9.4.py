def sort_words(user_input):
    list_of_words = user_input.split()
    words = list()
    for each_word in list_of_words:
        words.append((len(each_word), each_word))
    words.sort(reverse=True)
    print("After sorting")
    for length, word in words:
        print(f'The word "{word}" is of {length} characters')

def main():
    sentence = input("Enter a sentence: ")
    sort_words(sentence)

if __name__ == "__main__":
    main()