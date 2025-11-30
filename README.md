# Python Learning Repository

A beginner-friendly Python project to learn data structures and programming fundamentals.

## Project Overview

This project contains:
- **palindrome_checker.py**: A simple palindrome checker implementation
- **test_palindrome_checker.py**: Unit tests for the palindrome checker

## What is a Palindrome?

A palindrome is a word, phrase, or number that reads the same forwards and backwards (ignoring spaces and capitalization).

Examples:
- "racecar"
- "A man a plan a canal Panama"
- "Was it a car or a cat I saw"

## Setup Instructions

### Prerequisites
- Python 3.8+
- Visual Studio Code

### Installation

1. Clone this repository
2. Navigate to the project directory
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

### Running the Code

```bash
python palindrome_checker.py
```

### Running Tests

```bash
python -m unittest test_palindrome_checker.py -v
```

## Debugging in VS Code

1. Open VS Code
2. Open the `palindrome_checker.py` file
3. Click on the line number to set a breakpoint
4. Press `F5` or go to Run → Start Debugging
5. Step through the code using F10 (step over) or F11 (step into)

## Learning Points

- String manipulation in Python
- List slicing and reversal
- Function definition and documentation
- Unit testing with unittest
- Git version control

## Next Steps

- Modify the code to use a stack data structure
- Add support for special characters
- Implement additional data structure problems
- Learn about algorithm complexity

## License

This project is open source and available under the MIT License.
