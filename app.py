# Example of code that will trigger SonarCloud issues


def my_function():
    unused_variable = 42
# Function with high cyclomatic complexity (maintainability issue)
def overly_complex(a, b, c, d):
    if a:
        if b:
            if c:
                if d:
                    for i in range(10):
                        if i % 2 == 0 and a or b:
                            print("Too deep")

def check_db():
    # Will trigger python:S2068 (Hardcoded Password)
    db_password = "MyCustomSecretPassphrase99!"


# Will trigger secrets:S6290 (AWS Access Key ID detected)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

def test_sonar_rules():
    # 1. Unused local variable (Code Smell)
    unused_var = 123
    
    # 2. Hardcoded Password (Security Hotspot - Rule python:S2068)
    user_password = "SuperSecretPassword123!"
    
    # 3. AWS Key ID Pattern (Security Hotspot - Rule secrets:S6290)
    aws_key = "AKIAIOSFODNN7EXAMPLE"
    
    return user_password
