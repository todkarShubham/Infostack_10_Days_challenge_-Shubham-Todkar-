

def find_missing_num(arr):
    n = len(arr) + 1  # taking +1, because arr has n-1 numbers
    total_sum = n * (n + 1) // 2
    original_sum = sum(arr)
    missing_sum = total_sum - original_sum

    return missing_sum

print(find_missing_num([1,2,3,4,5,6,7,9,10]))



