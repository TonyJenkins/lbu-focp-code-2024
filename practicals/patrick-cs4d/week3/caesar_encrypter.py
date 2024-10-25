#!/usr/bin/env python3
#A program to simple encrypt a word

if __name__ == '__main__':
    my_word = input("Please enter a word to encrypt: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caesar_key = 31
    encrypted_word=""
    #hello => mjqqt
    for i in my_word:
        start_count = alphabet.find(i)
        new_letter = alphabet[(start_count+caesar_key) % 26]
        encrypted_word += new_letter

    print(encrypted_word)