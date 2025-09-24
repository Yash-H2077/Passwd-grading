def password_strength(passwd):
    length_ok = len(passwd) >= 8
    has_upper = any(char.isupper() for char in passwd)
    has_digit = any(char.isdigit() for char in passwd)
    has_special = any(not char.isalnum() for char in passwd)

    if all([length_ok, has_upper, has_digit, has_special]):
        return "Strong"
    elif length_ok and (has_upper or has_digit or has_special):
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength = password_strength(pwd)
    print(f"Password strength: {strength}")
