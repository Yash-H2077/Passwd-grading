# Passwd-grading
Build a tool to check if your password is ready for real world usage

## Requirements
 - Python
 - VScode, jupyter or nano(lightweight)

## Methodology
### 1. Create a python file
```bash
nano passwd-analyzer.py
```
### 2. Write the script
```bash
def password_improvements(passwd):
    suggestions = []

    if len(passwd) < 8:
        suggestions.append("Increase the password length to at least 8 characters.")

    if not any(char.isupper() for char in passwd):
        suggestions.append("Include at least one uppercase letter (A-Z).")

    if not any(char.islower() for char in passwd):
        suggestions.append("Include at least one lowercase letter (a-z).")

    if not any(char.isdigit() for char in passwd):
        suggestions.append("Include at least one digit (0-9).")

    if not any(not char.isalnum() for char in passwd):
        suggestions.append("Include at least one special character (e.g., !, @, #, $).")

    if not suggestions:
        print("Your password looks strong!")
    else:
        print("Your passwd looks weak, Try these to improve your password:")
        for tip in suggestions:
            print(f"- {tip}")

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    password_improvements(pwd)

```
