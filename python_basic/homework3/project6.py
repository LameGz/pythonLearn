def bubble_sort(list_items):
    for i in range(len(list_items)):
        for j in range(len(list_items) - i - 1):
            if list_items[j] > list_items[j + 1]:
                temp = list_items[j]
                list_items[j] = list_items[j + 1]
                list_items[j + 1] = temp
    print(f"the sort list is {list_items}")


def main():
    items_to_sort = [5, 4, 3, 2, 1]
    bubble_sort(items_to_sort)



