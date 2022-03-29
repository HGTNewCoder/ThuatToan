array = [1, 3, 5, 7, 9, 2, 4, 6, 10]

max = 0
for i in range(1, len(array)):
    if array[i] > max:
        max = array[i]

print(max)