# Lecture 05

This week we will following the usual pattern of looking at a single program, that will illustrate most of the programming ideas we have covered so far.

This program is another previous assignment task. If you look closely you will see it is one of the examples from the slides used in your practicals, but slightly disguised. Realising that helps in creating an answer.

As before, the program will be developed gradually. Commits will mark points where the program has a new feature; this is a good practice because it stores various (possibly useful) versions, and gives a point to retreat to if changes go wrong!

## 1. Introduction
## 2. Git Revisited
## 3. Abstraction
## 4. A Complete Program
## 5. A Summary

### The Program

Poppleton Park Run is a monthly family fun run around Poppleton Park. Family groups run, jog, walk, or crawl
around their local park in a generally friendy way. The organisers publish the times of runners
at various points along the course around the park's perimeter. These times are eventually processed and published
on a website.

Automatic timing apparatus positioned around the park uses advanced computer vision techniques to read the numbers 
on each runner's singlet as they pass, and record this along with the elapsed time. These times need to be 
processed so that they can be poste on the website.

#### The Task

You will write a program that will process the data stream from one of these devices to produce 
some useful statistics. The device is half way round the course, and is is known that every runner will
pass it at most once.

The data stream from the timing apparatus consists of the runner's number (as read from their singlet), and a time
in seconds. A time in seconds is used because runners tend to start at different actual times as they pass a 
designated point. The two elements on the line are separated by two colons (`::`), and each data item 
appears on its own line. So, for example, here:

```text
0012::239
01921::256
```

runner with number `0012` passed 239 seconds after starting, and runner `01921` is slightly slower, passing at
256 seconds.

The data stream ends when the operator powers off the apparatus. Just before shutting down it sends the single 
line `END` to mark the end of the stream.

The required output is:
* The total number of runners who have been seen.
* The average time recorded, rendered in minutes and seconds.
* The fastest time recorded at this point, rendered in minutes and seconds.
* The slowest time recorded at this point, rendered in minutes and seconds.
* The number of the runner recording the fastest time (or the first one to do so, if there are several).

All times should be output, in words, as a number of minutes and seconds.
