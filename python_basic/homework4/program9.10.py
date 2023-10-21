def fnd_unique(*all_words):
    for each_word in all_words:
        unique_character_list = list(set(each_word))
    print(f"Unique characters in the word {each_word} are {unique_character_list}")


def main():
    fnd_unique("egg", "immune", "feed", "vacuum", "goddessship")


if __name__ == "__main__":
    main()
