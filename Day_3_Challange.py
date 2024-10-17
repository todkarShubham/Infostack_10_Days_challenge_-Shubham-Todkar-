

def y_palindrome(s):

    string = s.replace(" ","").lower()

    reversed_str = ""
    for words in string:
        reversed_str = words + reversed_str

    return string == reversed_str

print(y_palindrome("madam"))
print(y_palindrome("A man a plan a canal Panama"))
print(y_palindrome("Hello"))
print(y_palindrome("Navin"))
print(y_palindrome("level"))