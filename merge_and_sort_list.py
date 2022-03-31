from unittest.util import sorted_list_difference


arrayA = [1, 3, 5]
arrayB = [2, 4, 6]
array = [] # [1, 3, 5, 2, 4, 6]


def dosomething(arrayA, arrayB):
    array = arrayA + arrayB
    for i in range(0, len(array)):
        for k in range(0, len(array)):
            if array[i] < array[k]:
                temp = array[k]
                array[k] = array[i]
                array[i] = temp
    print(array)

dosomething(arrayA, arrayB)