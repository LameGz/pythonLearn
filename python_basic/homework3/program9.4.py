def main():
    # file_handler = open("rome.txt", "r")
    with open("rome.txt") as file_handler:#与上段代码等价
        print("print a single line from the file")
        print(file_handler.readline(), end='')
        print("print another single line from the file")
        print(file_handler.readline(), end='')


if __name__ == "__main__":
    main()
