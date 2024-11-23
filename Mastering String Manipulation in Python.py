# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Function to convert string to uppercase
def to_uppercase(s):
    return s.upper()

# Function to convert string to lowercase
def to_lowercase(s):
    return s.lower()

# Function to remove spaces from a string
def remove_spaces(s):
    return s.replace(" ", "")

# Function to check if a string contains only digits
def is_digit(s):
    return s.isdigit()

# Function to count occurrences of a substring in a string
def count_substring(s, substring):
    return s.count(substring)

# Function to replace a substring in a string
def replace_substring(s, old, new):
    return s.replace(old, new)

# Function to find the index of a substring
def find_substring(s, substring):
    return s.find(substring)

# Function to split a string by a delimiter
def split_string(s, delimiter):
    return s.split(delimiter)

# Example usage:
if __name__ == "__main__":
    test_string = "Hello World"
    print("Original String:", test_string)
    print("Reversed:", reverse_string(test_string))
    print("Is Palindrome:", is_palindrome(test_string))
    print("Vowel Count:", count_vowels(test_string))
    print("Uppercase:", to_uppercase(test_string))
    print("Lowercase:", to_lowercase(test_string))
    print("Without Spaces:", remove_spaces(test_string))
    print("Is Digit:", is_digit(test_string))
    print("Count of 'o':", count_substring(test_string, 'o'))
    print("Replace 'World' with 'Python':", replace_substring(test_string, 'World', 'Python'))
    print("Index of 'World':", find_substring(test_string, 'World'))
    print("Split by space:", split_string(test_string, ' '))
