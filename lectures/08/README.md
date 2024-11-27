# Lecture 08

This week we will look at an example program that illustrates most of the programming ideas we have coveted in the module.

We will include some file handling, so much of what we need will be "boilerplate code" from a previous program.

An important issue will be choosing the "best" way to solve the problem. The problem we have can be solved in a bunch of different ways (we will probably use two). Choosing which path to follow often comes down to simply picking the one that results in the most clear code.

*Note: The Security boffins among us will probably know whether this is code, cypher, or encryption. We'll just call it encoding!*

## 1. Introduction
## 2. Simple Cyphers
## 3. A Summary

### The Problem: A Simple Cypher

A very simple substitution cypher could work like this. The letters of the alphabet are shuffled into a random order, and this becomes the key, which is shared. Any message can be encoded by simply looking up the corresponding character for a letter in the key. For example, if the key was:

```text
xukdeqilngsftamvczpjywhobr
```

the letter ``a`` would be encoded as ``x``, ``b`` as ``u``, and so on.

This is obviously very easy to crack by a simple brute force attack based on counting letter frequencies. A slightly more secure code can be created by using a key that consists of upper and lower case letters. So (probably) upper case ``A`` and lower case ``a`` will be encoded to different letters. And the case of letters may not match.

The second one above is the approach we will use here. So the key will be something like:

```text
CDryzhpZTAHbaxSqinwMkJvGfRNoFIXePLlmEOsdButgQWVjUcKY
```

The ``encode`` program will save the key and encoded message in separate files. The message itself will be provided in a file as a command-line argument. The ``decode`` program will need the key file and the encoded message file, and will display the message on the standard output (probably the terminal).
