def linear_search(items, num, key_val):
    for i in range(0, num):
        if(items[i] == key_val):
            return i
    return -1


items = []

num = int(input("Enter number of Items: "))
key_val = int(input("Enter value to be searched: "))
# iterating till range
for i in range(0, num):
    element = int(input("Please, Enter Your List Items: "))
    items.append(element) # adding the element

result = linear_search(items, num, key_val)

if(result == -1):
    print("Element not found!!, Sorry")
else:
    print("Element Found at index:", result)