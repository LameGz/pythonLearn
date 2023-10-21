def main():
    f = open("workfile.txt", "wb")
    f.write(b"abcdef")
    f = open("workfile.txt", "rb")
    byte = f.read(1)
    print("print each byte in the file")
    while byte:
        print(byte)
        byte=f.read(1)
if __name__ == '__main__':
    main()