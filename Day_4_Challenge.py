number = 56789

def digits(n):
    count = 0

    while n > 0:
        count += n % 10

        n = n // 10

    return count

print("Total of Digits", digits(number))