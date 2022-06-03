# DeamonThreads

This repository is for understanding the concept of deamon threads in Python

## Definition:
The threads which are always going to run in the background that provides supports to main or non-daemon threads, those background executing threads are considered as Daemon Threads. The Daemon Thread does not block the main thread from exiting and continues to run in the background.

## Problem Statement: 
Run a daemon thread in the background and one main thread which accepts the input Yes/No from the User

## Proposed Solution:
Daemon thread will keep running in the background to count the time the user is logged it. It will exit 

## Specifications to run the program
1. Python Version Used: Python 3.9.12 (Install Python from: https://www.python.org/downloads/)   
2. Clone the repo and go to the location where the file is stored 
3. Run using python3 Deamon.py (Deamon process will start running in the background)

## Exit Condition:
To stop the main thread Type Yes/No in the console. Daemon will also exit along with the main thread




