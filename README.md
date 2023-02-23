# Path Finder - Codecademy Computer Science Project

This is a solution to the Second Chapter of the Computer Science Course in Codecademy: Introduction to Data Structures.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [About the game](#about-the-game)
- [Run the game](#run-the-game)
- [The Rules](#the-rules)
  - [Player setup](#player-setup)
  - [Soldiers setup](#soldiers-setup)
  - [Position and range](#position-and-range)
  - [Initiative](#initiative)
  - [Health points](#health-points)
  - [Attack and defence](#attack-and-defence)
  - [Arrow protection](#arrow-protection)
  - [Game flow](#game-flow)
- [Author](#author)

## Overview

### The challenge

The goal of the project was to create an interactive terminal recommendation program in Python.
The program should suggest a specific category for the user, by entering letters into the terminal.
If the user is intersted in thecategory, the program will provide a variety of realetd recomandations to the user.

### About the program

The Path Finder (PF) contains a virtual representation of Arkham Horror 2nd edition board game's board.
The PF reflects connections between places and resources which can be found there. Useres are said to write
a resource that they want to find. Then the program provides information where the resource is possible to notice.
Users choose one of possibliteis, delivers starting place and move points. The program calculates the shortest path between indicated locations. The program data is organized in linked lists and a graph.

## Run the program

To run the game copy files: `data.py`, `script.py`, `graph.py`, `vertex.py`, `linked_list.py` and `node.py`.
Type in your terminal:
```
$ python3 script.py
```

## Instructions

### Choose a resource

The program asks users to type single letters and words to find suitable resorces. If there is no results or there are more than one, The PF repeats request until one solution is found. 

```

    ****************************
    *** Search for utilities ***
    ****************************


What resource available in Arkham city would you like to find?
Type the beginning of that resource and press enter: s
-- spells
-- skills

What resource available in Arkham city would you like to find?
Type the beginning of that resource and press enter:

```

When the PF finds one solution users have possibility to repeat search.

### Set the locations

See an examplery search results:
```
You can find skills in:
~~~~~~~~~~~~~~~~~~~~
Name: Historical Association
Resources: skills, spells
Neighboring places: Southside
~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~
Name: The Administration Building
Resources: money, skills
Neighboring places: University
~~~~~~~~~~~~~~~~~~~~


Where do you want to go?
Choose a number from list below:
-- 1 - Historical Association
-- 2 - The Administration Building
Your choice:
```
In the second step users enter a number connected to a location name. Then in the terminal appears the full locations list, from which starting location should be chosen and a request for a move points number. The PF calculates the shortest way between selected places and shows where to go in each turn.

```
It takes you 2 round(s) to arrive to The Administration Building from Church.
You can go this way: 
1: Church -> Southside -> French Hill
2: French Hill -> University -> The Administration Building
```

Users can repeat whole process before exiting program.

## Programming concepts
### Data structure

Inintial data is deliverd in `data.py` in the Python dictionary object. 

### Algoritms

.....

### Issues and future upgrades

.....

## Author

- Website - [Krzysztof Łęczycki](https://krzysztofleczycki.github.io/portfolio/)

