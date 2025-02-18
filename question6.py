# Lists are mutable
my_list = [1, 2, 3]
print("Original list:", my_list)

my_list[0] = 10  # Modifying the first element
print("Modified list:", my_list)  # The change is shown

my_list.append(4)  # Adding a new element
print("List after append:", my_list)

# Strings are immutable
my_string = "hello"
print("Original string:", my_string)

my_string[0] = "H" # This will cause an error
