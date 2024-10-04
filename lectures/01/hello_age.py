#!/usr/bin/env python3

if __name__ == "__main__":
    name = input("What is your name? ")

    year_now = int(input('What is the current year? '))
    year_born = int(input('What year were you born? '))

    age = year_now - year_born

    print()
    print(f"Hello, {name.title()}! It is good to meet you.")
    print(f"This year you will be {age} years old.")
