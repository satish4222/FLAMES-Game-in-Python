**FLAMES Game in Python**
Overview :
This project is a Python implementation of the classic FLAMES relationship game.
FLAMES is a fun game used to predict the relationship between two people based on their names.
The program takes two names as input, removes common letters, counts the remaining letters, and uses that count to determine the relationship using the FLAMES logic.

What FLAMES Stands For :

Each letter in FLAMES represents a relationship:

F – Friends

L – Lovers

A – Affection

M – Marriage

E – Enemies

S – Siblings

How the Program Works :
The user enters two names.
Each name is converted into a list of characters.
Common letters between the two names are removed.
The total number of remaining characters is calculated.
The FLAMES list is reduced by repeatedly removing letters based on the calculated count.
When only one letter remains, it is mapped to its relationship meaning.
The final relationship is displayed as output.

Features :
Uses basic Python concepts like lists, loops, conditionals, and dictionaries
Simple and easy-to-understand logic
Beginner-friendly project for learning Python

Requirements :
Python 3.x
No external libraries are required.
