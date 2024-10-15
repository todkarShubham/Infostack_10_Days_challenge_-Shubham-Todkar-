

arr = [34.65,7,89,97,1,3,78]

def max_min(arr):
    max_num = arr[0]
    min_num = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]

    return max_num, min_num

maximum_num, minimum_num = max_min(arr)
print(f"Maximum Number : {maximum_num}, Minimum Numbare : {minimum_num}")


