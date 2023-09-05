# Prompt the user for student information
name = input("Name: ")
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))

# Compute the average
average = (math + science + english) / 3

# Print the result
print("\nResult:")
print("Average: (Math {}, Science {}, English {}): {:.1f}".format(math, science, english, average))
if average >= 75:
    print("\nCongratulations, You Passed!")