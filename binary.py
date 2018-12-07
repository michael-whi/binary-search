def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        print("low=", low, "high", high)
        mid = (low + high)//2
        print("mid=",mid,"len=",len(list))
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(my_list, 11))