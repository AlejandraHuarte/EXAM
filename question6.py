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

# my_string[0] = "H"  # We've seen how this has caused a message that says error

# Instead, we need to create a new string
new_string = "H" + my_string[1:]
print("Modified string:", new_string)  # Creates a new string instead of modifying the original
