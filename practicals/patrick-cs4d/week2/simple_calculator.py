#!/usr/bin/env python3

if __name__ == '__main__':
    print("-----------------")
    print("Simple Calculator")
    print("-----------------")
    print()
    print("Enter two numbers: ")
    number1 = int(input('Enter number one: '))
    number2 = int(input('Enter number two: '))

    print(f"Addition: {number1 + number2}")
    print(f"Subtraction: {number1 - number2}")
    print(f"Multiplication: {number1 * number2}")
    print(f"Division: {(number1 / number2):.2f}")

    print(f"Division: {type(number1/number2)}") #float even if the value divides as int