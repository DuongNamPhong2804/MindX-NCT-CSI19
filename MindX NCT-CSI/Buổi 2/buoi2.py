"""
# Problem: 1. Tìm vị trí của một số trong list
number_list = [5, 4, 1, 99, 8, 76, 74, 90, 100]
number = int(input("Enter a number: "))
if number in number_list:
    print(f"{number} is at index {number_list.index(number)}")
else:
    print(f"{number} is not in the list")


# Bài chữa
number_list = [5, 4, 1, 99, 8, 76, 74, 90, 100]
number = int(input("Enter a number: "))

def liner_search(data_list, value):
    for i, ele in enumerate(data_list):
        if ele == value:
            return i
    return -1

def find_number(data_list, value):
    index = liner_search(data_list, value)
    if index >= 0:
        print('{} is found at index {}'.format(value, index))
    else:
        print("Not found")

find_number(number_list, number)


def binary_search(data_list, value):
    left = 0
    right = len(data_list) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_value = data_list[middle]
        if middle_value < value:
            left = middle + 1
        elif middle_value > value:
            right = middle - 1
        else:
            return middle
    return -1

def print_result(data_list, value):
    index = binary_search(data_list, value)
    if index >= 0:
        print("Exists")
    else:
        print("Not exists")

number_list = [5, 4, 1, 99, 8, 76, 74, 90, 100]
number_list.sort()
print_result(number_list, number)
"""

scope_test = [('Nam', 10), ('Hoa', 20), ('Bang', 30), ('Linh', 40), ('Lan', 50), ('Tung', 60)]

def compare(tup, num):
    if tup[1] > num:
        return -1
    elif tup[1] < num:
        return 1
    else:
        return 0
    
def binary_search_comp(data_list, value, compare_result):
    left = 0
    right = len(data_list) - 1
    while left <= right:
        middle = (left + right) // 2
        middle_value = data_list[middle]

        compare = compare_result(middle_value, value)
        if compare == -1:
            left = middle + 1
        elif compare == 1:
            right = middle - 1
        else:
            return middle
    return -1
    
def display_result(data_list, value):
    index = binary_search_comp(data_list, value, compare)
    if index >= 0:
        print("{} exists".format(data_list[index][0]))
    else:
        print("Not exists")

