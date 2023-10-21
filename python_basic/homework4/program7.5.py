def main():
    count_words = dict()
    sentence = input('enter a sentence: ')
    words = sentence.split()
    for each_word in words:
        count_words[each_word] = count_words.get(each_word, 0) + 1
    print("The number of times each word appears in a sentence is")
    print(count_words)
if __name__ == '__main__':
    main()