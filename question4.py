def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# List of numbers (as strings) from the question
numbers = [
    "9847255590886266818998186626880955527489",
    "1414884937242655719669145562427394884141",
    "6892149109325320763773670235239019412986",
    "6800923757255865070000705685527573290086"
]

# Check each number and print if it's a palindrome or not
for num in numbers:
    result = palindrome(num)
    print(f"{num} is a palindrome: {result}")