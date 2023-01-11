def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

                return list

                print(bubble_sort([3, 2, 1]))
                print(bubble_sort([4, 5, 1, 3, 2]))