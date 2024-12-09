lakes = ["superior", "erie", "huron", "ontario", "powell"]
# print(len(lakes))
# print(any(lakes))
lakes.append("nyon")
# print(lakes)


list_items = input("Enter list items separated with spaces").split()
print(f"List of items are {list_items}")
add_new = input("Add a new item in the list: ")
new_item = list_items.append(add_new)
print(f"List of items are {list_items}")
remove_item = input("Enter the item you wanna remove: ")
new_item = list_items.remove(remove_item)
print(f"List of items are {list_items}")


# contact@ticsummit.org