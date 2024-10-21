
arr = [1,2,3,4]

def products(arr):

    n = len(arr)

    before_products = [1] * n
    after_products = [1] * n
    result = [0] * n


    for i in range(1,n):
        before_products[i] = before_products[i - 1] * arr[i - 1]


    for i in range(n - 2, -1, -1):
        after_products[i] = after_products[i + 1] * arr[i + 1]


    for i in range(n):
        result[i] = before_products[i] * after_products[i]


    return result

print(products(arr))
