def read_key_item():
    key_item = int(input("Enter the key item: "))
    return key_item


def liner_serach(search_key):
    list_of_items =[10,20,30,40,50]
    found = False
    for item_index in range(len(list_of_items)):
        if list_of_items[item_index] == search_key:
            found = True
            break
        if item_index == len(list_of_items)-1:
            found = False
            break