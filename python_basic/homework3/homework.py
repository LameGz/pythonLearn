# 默认参数函数的定义和调用
def greet(name="Guest"):
    print("Hello, " + name + "!")


# 关键字参数的使用
def calculate_total_cost(price, tax_rate=0.1, discount=0):
    total_cost = price + (price * tax_rate) - discount
    return total_cost


# 使用关键字参数调用函数
total = calculate_total_cost(100, tax_rate=0.15, discount=10)


# 动态参数的使用
def print_arguments(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(key + ": " + str(value))


def main():
    greet()  # 输出: Hello, Guest!
    greet("Alice")  # 输出: Hello, Alice!
    print(" 默认参数函数的定义和调用")
    # 使用动态参数调用函数
    print_arguments("apple", "banana", "cherry", color="red", taste="sweet")
    print(" 使用动态参数调用函数")
    print("Total cost:", total)  # 输出: Total cost: 115.0
    print(" 关键字参数的使用")


if __name__ == "__main__":
    main()
