# Overview

A Python-based toolkit for generating secure passwords and analysing password strength through computational attack simulation. This project addresses the critical gap between user convenience and digital security in an era where password breaches remain a leading cause of data compromises. Passwords are essential to securing our digital lives, yet many users still choose weak, predictable ones—even tech-savvy individuals often prioritise convenience over security [<em>(The Economist, 2012)</em>](https://www.economist.com/science-and-technology/2012/03/24/speak-friend-and-enter). Compounding this issue, password reuse across multiple accounts means a single breach can compromise an entire digital footprint, making robust password practices more crucial than ever.

#Features

To address this issue, this repository offers two key tools:

- ***Password Generator (password_generator.py)***: A customisable function that generates a password based on user-specified criteria:
  - Length of password: User-specified password length
  - Character composition: Options to include uppercase letters, digits, and custom symbols.
  This generator uses shuffling to avoid predictable character patterns and features an interactive, user-friendly command-line interface.

- ***cracking_time()***: A function which estimates how long a hacker would take to crack a given password using common attack methods, such as brute-force.



# References
1. <em>(The Economist, 2012)</em> [Speak, friend, and enter](https://www.economist.com/science-and-technology/2012/03/24/speak-friend-and-enter). Accessed on 05/06/2025.

