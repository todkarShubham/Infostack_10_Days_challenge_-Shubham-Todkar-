
arr = [1,2,3,4,5]

def array_reverse(arr):
    reversed_array=[]

    for i in range(len(arr) - 1,-1,-1):
        reversed_array.append(arr[i])

    return reversed_array
    
reversed_array = array_reverse(arr)
print('Original Array',arr)
print('Reversed Array',reversed_array)

