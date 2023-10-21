def read_key_item():
    key_item = int(input("Enter the key item to search: "))
    return key_item


def linear_search(search_key):
    list_of_items = [10, 20, 30, 40, 50]
    found = False
    for item in range(len(list_of_items)):
     if list_of_items[item] == search_key:
        found = True
        break
    if found:
        print(f"{search_key}item found in {item+1}")
    else:
        print("Key item not found in the list")

def main():
    key_in_list = read_key_item()
    linear_search(key_in_list)


if __name__ == "__main__":
    main()