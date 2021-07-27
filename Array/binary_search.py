# Iterative Binary Search Program
def binary_search(arr, key_val):
    BEG = 0
    END = len(arr) - 1
    MID = 0

    while BEG <= END:
        MID = (END + BEG) // 2

        # If key_val is greater, ignore left half
        if key_val > arr[MID]:
            BEG = MID + 1

        # if key_val is smaller, ignore right half
        elif key_val < arr[MID]:
            END = MID - 1

        else:
            return MID


# Input array
arr = []
items = int(input("Please, Enter how many number of Array Elements you want: "))
for i in range(0, items):
    elements = int(input("Enter your Elements values: "))
    arr.append(elements)

key_val = int(input("Enter Key value you want to search: "))


result = binary_search(arr, key_val)
if result != -1:
    print("Element is present at index: ", str(result))
else:
    print("Element is not present in array")