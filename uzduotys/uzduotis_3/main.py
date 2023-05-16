def is_palindrome(string):
    lowercase_string = string.lower()
    alphanumeric_chars = [char for char in lowercase_string if char.isalnum()]
    reversed_chars = alphanumeric_chars[::-1]
    return alphanumeric_chars == reversed_chars


strings = ["level", "python", "Madam", "12321", "racecar"]

for string in strings:
    print("String:", string)
    if is_palindrome(string):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")
