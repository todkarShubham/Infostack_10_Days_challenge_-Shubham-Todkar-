

def non_repeating_char(w):

    w = w.lower()

    count = {}

    for char in w:
        count[char] = count.get(char,0) + 1


    for char in w:
        if count[char] == 1:
            return char
        
    return -1

print(non_repeating_char("aabbcc"))
print(non_repeating_char("swiss"))
print(non_repeating_char("butter"))
print(non_repeating_char("success"))