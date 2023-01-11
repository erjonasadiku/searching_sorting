def binary_search(list, target):
    left = 0
    right = len(list) - 1
    while left <=right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
           elif list[mid] < target:
                left = mid + 1
                else:
                    right = mid - 1
                    return -1

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5], 6))