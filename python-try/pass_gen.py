import random
import string


def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%^&*()-_=+[]{}")

    remaining = [
        random.choice(string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}")
        for _ in range(length - 4)
    ]

    password_list = [lower, upper, digit, symbol] + remaining
    random.shuffle(password_list)

    return "".join(password_list)


def main():
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()