import os

file_handler = open("test.txt", "w")
file_handler.write("Hello World")
file_handler.close()
file_handler = open("test.txt", "r")
print(file_handler.read())
# file_handler.close()
