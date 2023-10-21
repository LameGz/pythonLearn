def check_for_sort_order(list_items):
    ascending = descending = True
    for i in range(len(list_items)-1):
        if list_items[i] < list_items[i+1]:
            descending = False
        if list_items[i] > list_items[i+1]:
            ascending = False
    if ascending:
        print("is in the ascending order")
    elif  descending:
        print("is in the descending order")
    else:
        print("is not in any order")
def main():
    check_for_sort_order([1,2,3,4,5])
    check_for_sort_order(input())

if __name__ == "__main__":
    main()

