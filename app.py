# 1
# -----------------------------------------------------------------------------------------------------------
# Reverse a string
# a. Write code that takes a string as input and returns the string reversed
# b. i.e. “Hello” will be returned as “olleH”

# needs_reversed = "Hello"
# for letter in range(len(needs_reversed), -1, -1):
#     print(letter)

# string = "Hello world"
# for letter in range(len(string) - 1, -1, -1):
#     print(string[letter])

# 2
# -----------------------------------------------------------------------------------------------------------
# Capitalize letter
# a. Write code that takes a string as input and capitalize the first letter of each word. Words
# will be separated by only one space. i.e. “hello world” should be outputted as “Hello
# World”

# string = "Hello world i like pie"
# for letter in range(len(string)):
#     if string[letter - 1] == " ":
#         continue
#     else:
#         if string[letter] == " ":
#             next_letter = string[letter + 1]
#             print(" ")
#             print(next_letter.upper())
#         else:
#             print(string[letter])

# 3
# -----------------------------------------------------------------------------------------------------------
# Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to
# "3a5b4c2a3c3b3a3b3a"
# find multiples with for loop and append to different strings for each unique character
# then print length, length * character, then append all to the same empty string
# maybe nest while loop inside to stop after reaching a new character

original_string = "aaabbbbbccccaacccbbbaaabbbaaa"
cache_a = ""
cache_b = ""
cache_c = ""
final_string = ""

for index_num in range(len(original_string)):
    if original_string[index_num] == "a":
        cache_a += original_string[index_num]
    elif original_string[index_num] == "b":
        cache_b += original_string[index_num]
    elif original_string[index_num] == "c":
        cache_c += original_string[index_num]
print(cache_a)

# 4
# -----------------------------------------------------------------------------------------------------------
# BONUS CHALLENGE: Palindrome
# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the
# result

# Range has 2 optional parameters
# range(start number, end number, increment/decrement number)

# practice
# sentence = "aabbc"
# for index_num in range(len(sentence)):
#     print(sentence[index_num])
