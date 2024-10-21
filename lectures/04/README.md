# Lecture 04

This week we will following the usual pattern of looking at a single program, that will illustrate most of the programming ideas we have covered so far.

This program is actually a previous assignment task, but it has been simplified. The assignment version read data from a file, and wrote output to another file. We will just use the standard input and output to keep things simple, and will limit the program to processing a single entry.

The main idea here is, again, the process of splitting a problem into smaller parts, and then writing functions to solve each part. This is the essence of programming. The small parts will each be quite simple (most will only be one line), and completing the program will be a case of combining them in a sensible order.

The code in the version here is intended to be *Pythonic*, and does use a few nifty tricks that allow for quite neat and elegant code. Notably, there will be *list comprehensions*.


## 1. Introduction
## 2. Being Pythonic
## 3. List Comprehensions
## 4. A Complete Program
## 5. A Summary

### The Program

The University of Poppleton is required to generate a unique email address for all new students. The email address is based on the student's name, but obviously this cannot be guaranteed to be unique. The format of the email address is therefore the student's initials, their surname (all in lower case), and then four random digits.

The input consists of the student's ID number, and then their name. For example:

```
c1141514 Ellison, Michael William
```

would get an email address something like:

``` 
m.w.ellison2345@poppleton.ac.uk
```

Email addresses cannot contain spaces. Any non-alphabetic characters are to be stripped from the name.
