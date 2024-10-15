# Lecture 03

This week we will look at a single program, that will illustrate most of the programming ideas we have covered so far.

In terms of the work we have done so far, it will be quite a long program (maybe 70-80 lines), so it will be important to break it up into smaller components. 
So we will first develop some *functions* and then glue them together to make the complete program.

As a (somewhat artificial) aside, we will create the functions in a separate file (a *module*) and thus explain something about the structure of a program.

## 1. Introduction
## 2. Using Functions
## 3. Creating Functions
## 4. A Complete Program
## 5. A Summary

### The Program

A simple guessing game works like this.

The first player (which here will be the computer) thinks of a random number between 0 and 100 inclusive. The second player gueses the number; after each
guess the first player responds "Higher" or "Lower" until the guess is correct. The second player must guess correctly within 10 guesses.

### Note

Given that the second player's obvious approach is a Binary Chop (Search) (see https://en.wikipedia.org/wiki/Binary_search), the first player may want to be
slightly cunning in their choice of number.
