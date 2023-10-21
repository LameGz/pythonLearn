list_items =input('Enter list items separated by a space').split()
print(f'list are{list_items}')

item_of_list=[]
total_items = int(input('Enter total items'))
for i in range(total_items):
    item = input('Enter item')
    item_of_list.append(item)

print(f'list are{item_of_list}')