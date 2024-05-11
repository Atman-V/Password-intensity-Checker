# Password-Intensity-Checker

## Overview
The **Password-Intensity-Checker** is a Python-based tool that evaluates the strength of a given password. It analyzes various factors such as length, complexity, and character composition to determine the password's intensity level using a graphical user interface (GUI).

## Features
- Evaluates password strength based on predefined criteria.
- Provides a numerical score and feedback.
- Offers suggestions for improving password security.
- Simple and interactive Tkinter-based GUI.

## Installation
Ensure you have Python 3 installed on your system. The script requires the `tkinter` module, which is included by default in most Python installations.

## Usage
Run the script using Python:

```sh
Password-intensity_Checker.py
```

Enter a password in the input field and click **Analyze** to get feedback on its strength.

## Password Strength Criteria
The intensity checker evaluates passwords based on:
- **Length:** At least 8 characters.
- **Character Variety:** Uppercase, lowercase, numbers, and special characters.
- **Common Patterns:** Avoids dictionary words and repeated sequences.

## Example Output
```
Enter your password: P@ssw0rd!
Strength: Strong
Score: 80/100
Feedback:
✅ Good length.
✅ Contains uppercase letters.
✅ Contains lowercase letters.
✅ Contains numbers.
✅ Contains special characters.
```

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests to improve functionality.


## Author
Developed by Sabaris J.

