def find_sun(list_items):
    positive_sum = 0
    negative_sum = 0
    for item in list_items:
        if item > 0:
            positive_sum += item
        else:
            negative_sum += item
    average = (positive_sum + negative_sum) / 5
    print(f"positive_sum is {positive_sum}")
    print(f"negative_sum is {negative_sum}")
    print(f"average is{average}")
    print("-----------------------------------------")
    for item in list_items:
        if item > average:
            print(f"{item} is greater than average")


def main():
    find_sun([-1, -2, -3, -4, -5])


if __name__ == "__main__":
    main()
