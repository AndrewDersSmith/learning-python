"""
Lists. Creating them, adding stuff, rearranging and removing stuff.
"""


# Lists are created using [].
letters_list = ["a", "b", "c", "d"]
numbers_list = [1, 2, 3, 4]
mixed_list = ["e", 5, "f", 6]

# Printing single and mixed lists.
print("Printing single and mixed lists:")
print("letters_list: ", letters_list)
print("numbers_list: ", numbers_list)
print("numbers_list + mixed_list: ", numbers_list + mixed_list)
print("\n")
# Printing slices of the list.
print("Printing slices of the list:")
print("numbers_list, mixed_list[1], mixed_list[3]: ", numbers_list, mixed_list[1], mixed_list[3])
print("letters_list, mixed_list[0], mixed_list[2] :", letters_list, mixed_list[0], mixed_list[2])
print("numbers_list[:2]: ", numbers_list[:2])
print("numbers_list[2:]: ", numbers_list[2:])
print("\n")

# Changing the content
numbers_list_updated = numbers_list
numbers_list_updated[3] = 5
print("numbers_list_updated[2] = 4: ", numbers_list_updated)