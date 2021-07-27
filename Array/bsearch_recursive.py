# Recurcive Binary Search Program
def binary_search(arr, low, high, key_val):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == key_val:
            return mid

        elif key_val < arr[mid]:
            return binary_search(arr, low, mid - 1, key_val)

        else:
            return binary_search(arr, mid + 1, high,  key_val)
    
    else:
        return -1


arr = []
items = int(input("Please, Enter how many number of Array Elements you want: "))
for i in range(0, items):
    elements = int(input("Enter your Elements values: "))
    arr.append(elements)

key_val = int(input("Enter Key value you want to search: "))

result = binary_search(arr, 0, len(arr) - 1, key_val)

if result != -1:
    print("Element is present at index: ", str(result))
else:
    print("Element is not present in array")