def binary_search(array, x):
    first = 0
    last = len(array) - 1
    while first <= last:
        middle = (first + last) // 2
        if x == array[middle]:
            return middle
        if x < array[middle]:
            last = middle - 1
        else:
            first = middle + 1

    return -1


array_list = [1, 2, 3, 10, 11, 12, 13, 14, 21, 22, 23, 24, 25, 32, 33, 34, 35, 36, 43, 44, 45, 46, 47, 54, 55, 56, 57,
              58, 65, 66, 67, 68, 69, 76, 77, 78, 79, 80, 81, 87, 88, 89, 90, 91, 98, 99, 100]

search_number = int(input('What number do you want to search in array? '))

if binary_search(array_list, search_number) == -1:
    print(f'Number {search_number} not found in array')
else:
    print(f'Number {search_number} found at index {binary_search(array_list, search_number)}')
