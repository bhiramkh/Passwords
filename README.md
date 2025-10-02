# Overview

A Python-based toolkit for generating secure passwords and analysing password strength through computational attack simulation. This project addresses the critical gap between user convenience and digital security in an era where password breaches remain a leading cause of data compromises. Passwords are essential to securing our digital lives, yet many users still choose weak, predictable ones—even tech-savvy individuals often prioritise convenience over security [<em>(The Economist, 2012)</em>](https://www.economist.com/science-and-technology/2012/03/24/speak-friend-and-enter). Compounding this issue, password reuse across multiple accounts means a single breach can compromise an entire digital footprint, making robust password practices more crucial than ever.


# Features

- ***Password Generator (password_generator.py)***: A customisable function that generates a password based on user-specified criteria:
  - Length of password: User-specified password length
  - Character composition: Options to include uppercase letters, digits, and custom symbols.
This generator uses shuffling to avoid predictable character patterns and features an interactive, user-friendly command-line interface.

- ***Cracking Time Estimator (cracking_time.py)***: A function which estimates how long a hacker would take to crack a given password using common attack methods, such as brute-force.
  Modelled scenarios
  | Scenario | Attempts per Second | Description |
  |----------|--------------------:|-------------|
  | **Online (throttled)** | 10 | Rate-limited login pages |
  | **Online (fast)** | 1,000 | Unprotected web services |
  | **Offline (basic hardware)** | 1,000,000 | CPU-based hash cracking |
  | **Offline (GPU cluster)** | 1,000,000,000 | Coordinated attacks on leaked databases |
  | **Offline (nation state)** | 1,000,000,000,000 | Advanced persistent threats with massive resources |
- ***Time Convertor Utility (time_converter())***: The tool converts computational time estimates into human-readable formats, automatically scaling from seconds to millennia to make security implications immediately understandable.
  - ***Supported units***: seconds → minutes → hours → days → months → years → decades → centuries → millennia


# Limitations
- ***No breach database validation***: This tool does not cross-reference passwords against known compromised password databases or common password lists.
- ***Brute-force focus only***: The analyser models only pure brute-force attacks and does not simulate dictionary or hybrid attack methods.


# References
1. <em>(The Economist, 2012)</em> [Speak, friend, and enter](https://www.economist.com/science-and-technology/2012/03/24/speak-friend-and-enter). Accessed on 05/06/2025.

