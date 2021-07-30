def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = []
num = int(input("How many list items: "))
for i in range(0, num):
    element = int(input("Please,  Enter your list items: "))
    arr.append(element)

bubble_sort(arr)

print(arr)
