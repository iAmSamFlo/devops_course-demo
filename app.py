# Example of code that will trigger SonarCloud issues

# Hardcoded credentials (security issue)
API_KEY = "12345-abcdef-67890"

# Unused variable (code smell)
unused_variable = 42

# Function with high cyclomatic complexity (maintainability issue)
def complex_function(x):
    if x > 0:
        if x % 2 == 0:
            print("Positive even number")
        else:
            print("Positive odd number")
    elif x < 0:
        if x % 2 == 0:
            print("Negative even number")
        else:
            print("Negative odd number")
    else:
        print("Zero")

# Call the function
complex_function(5)


x = 72