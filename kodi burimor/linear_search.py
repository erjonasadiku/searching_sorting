def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
            return -1

            print(linear_search([1, 2, 3, 4, 5], 3))
            print(linear_search([1, 2, 3, 4, 5], 6))