# Prompt the user for a string
string = input("Enter a string: ")

# Initialize counters
lowercase = 0
uppercase = 0
digits = 0
special = 0

# Count characters
for char in string:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

# Print the counts
print("\nCounts:")
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Digits:", digits)
print("Special symbols:", special)