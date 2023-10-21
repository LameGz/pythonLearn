# 字符串切片使用示例
string = "Hello, World!"
sliced_string = string[7:12]
print("切片结果:", sliced_string)

# 字符串连接使用示例
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ", " + string2 + "!"
print("连接结果:", concatenated_string)

# 所有字符串方法使用示例
string = "hello, world!"
print("原始字符串:", string)
print("大写转换:", string.upper())
print("小写转换:", string.lower())
print("首字母大写:", string.capitalize())
print("字符串长度:", len(string))
print("查找子字符串:", string.find("world"))
print("替换子字符串:", string.replace("world", "python"))

# 字符串格式化方法使用示例
name = "Alice"
age = 25
formatted_string = "My name is {} and I'm {} years old.".format(name, age)
print("格式化结果:", formatted_string)
