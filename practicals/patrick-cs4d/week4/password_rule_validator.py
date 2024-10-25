#!/usr/bin/env python3
def display_welcome_message(name):
    print(f"Hello {name}")
    print("This is my password checker")
    print("Please use the following rules")
    print("Between 8 and 12 characters long")
    print("Contain at least ONE uppercase letter")
    print("Contain at least ONE lowercase letter")
    print("Contain at least ONE digit")
    print("Contain at least ONE special character")
def is_password_correct_length(password, min=8, max=12):
    if len(password) < min:
        return False
    elif len(password) > max:
        return False
    return True
def does_password_contain_uppercase(password, number=1):
    total = 0
    for letter in password:
        if letter.isupper():
            total += 1
    return total >= number
def does_password_contain_lowercase(password, number=1):
    total = 0
    for letter in password:
        if letter.islower():
            total += 1
    return total >= number
def does_password_contain_digits(password, number=1):
    total = 0
    for letter in password:
        if letter.isdigit():
            total += 1
    return total >= number
def does_password_contain_special_characters(password, number=1):
    total = 0
    for letter in password:
        if not letter.isalnum():
            total += 1
    return total >= number
if __name__ == '__main__':
    display_welcome_message(input("What is your name? "))
    my_string = input("Please enter your password to check: ")

    rules_broken = 0
    if not is_password_correct_length(my_string):
        print("Needs to be between 8 and 12 characters long")
        rules_broken += 1
    if not does_password_contain_uppercase(my_string):
        print("Needs to contain at least ONE uppercase letter")
        rules_broken += 1
    if not does_password_contain_lowercase(my_string):
        print("Needs to contain at least ONE lowercase letter")
        rules_broken += 1
    if not does_password_contain_digits(my_string):
        print("Needs to contain at least ONE digit")
        rules_broken += 1
    if not does_password_contain_special_characters(my_string):
        print("Needs to contain at least ONE special character")
        rules_broken += 1

    if rules_broken == 0:
        print(f"Your password {my_string} is fine")


