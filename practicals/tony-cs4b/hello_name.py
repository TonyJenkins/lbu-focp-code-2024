#!/usr/bin/env python3

if __name__ == "__main__":

    name = input("What is your name? ")
    print(f"Hello, {name.title() if name else 'Stranger'}! It is good to meet you.")
