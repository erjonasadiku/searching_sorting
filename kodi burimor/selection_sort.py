def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i 
        for j in range(i+1, len(list)):
        if list[j] < list[min_index]:
            min_index = j
            list[i],   list[min_index] =  list[min_index],  list[i]
            return list

            print(selection_sort([3, 2, 1]))
            print(selection_sort([4, 5, 1, 3, 2]))