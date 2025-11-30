# Complete Guide: Your First Python Program

## 📋 Table of Contents
1. [Environment Setup](#environment-setup)
2. [Running Your Code](#running-your-code)
3. [Debugging Your Code](#debugging-your-code)
4. [Git & GitHub Integration](#git--github-integration)
5. [Security & Penetration Testing](#security--penetration-testing)

---

## Environment Setup

### What Happened
I've set up a Python virtual environment in your workspace. This is an isolated Python installation that keeps your project dependencies separate from your system Python.

**Location**: `C:/Users/anupa/source/repos/.venv/`

### Why Virtual Environments Matter
- Keep project dependencies isolated
- Prevent version conflicts between projects
- Easy to share with others (they create their own venv)
- Easy to delete and recreate

### How to Activate (Next Time)
```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# If you get an error, you might need to run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Running Your Code

### Method 1: Terminal (Recommended for Learning)
```bash
cd "c:\Users\anupa\source\repos\python-learning"
C:/Users/anupa/source/repos/.venv/Scripts/python.exe palindrome_checker.py
```

### Method 2: VS Code Run Button
1. Open `palindrome_checker.py`
2. Click the Run button (▶) in the top right
3. Output appears in the terminal

### Output Explained
```
=== Palindrome Checker ===

'racecar' -> ✓ Palindrome
'hello' -> ✗ Not a palindrome
```

The ✓ means it's a palindrome, ✗ means it's not.

---

## Debugging Your Code

### What is Debugging?
Debugging is the process of finding and fixing errors in your code. It's like being a detective looking for bugs!

### Setting a Breakpoint
1. Open `palindrome_checker.py`
2. Click on the line number (left side) where you want to pause execution
3. A red dot appears - that's your breakpoint

**Example**: Click on line 23 in the `is_palindrome` function

### Starting the Debugger
- **Press F5** or go to Run → Start Debugging
- Your program pauses at the first breakpoint
- The Debug Console shows up at the bottom

### Debug Controls
| Button | Hotkey | What It Does |
|--------|--------|--------------|
| Continue | F5 | Resume running until next breakpoint |
| Step Over | F10 | Execute the current line |
| Step Into | F11 | Go into a function call |
| Step Out | Shift+F11 | Exit the current function |
| Restart | Ctrl+Shift+F5 | Start debugging from the beginning |
| Stop | Shift+F5 | Stop debugging |

### Watching Variables
1. In the left sidebar, find the "Variables" panel
2. When paused, you'll see:
   - `text` = the input string
   - `cleaned_text` = the cleaned version
   - Local variables

### Try This
1. Add a breakpoint at line 23 in `is_palindrome`
2. Press F5
3. The debugger pauses when that line is about to execute
4. Look at the Variables panel to see what `text` contains
5. Press F10 to execute the line
6. Watch `cleaned_text` appear in the Variables panel

---

## Git & GitHub Integration

### What We Did
✅ Initialized a Git repository
✅ Created a `.gitignore` file
✅ Made an initial commit

### Understanding Git
- **Repository**: A folder tracked by Git
- **Commit**: A snapshot of your code with a message
- **Branch**: A separate line of development
- **Push**: Send your code to GitHub
- **Pull**: Get code from GitHub

### Check Git Status
```bash
cd "c:\Users\anupa\source\repos\python-learning"
git status
```

### View Your Commits
```bash
git log
```

### Make a New Commit (After Changes)
```bash
git add .
git commit -m "Describe what you changed"
```

### Connecting to GitHub (Next Steps)
1. Create a repository on GitHub.com
2. In terminal:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

---

## Security & Penetration Testing

### What is Penetration Testing?
It's testing your code the way a hacker might try to break it. Not to cause harm, but to find vulnerabilities BEFORE someone malicious does!

### Run the Security Tests
```bash
C:/Users/anupa/source/repos/.venv/Scripts/python.exe security_testing.py
```

### What We Tested

#### 1. **Type Checking** (Type Confusion Attack)
```python
# BAD: No type checking
def process_data(data):
    return data.upper()  # Crashes if data is a number!

# GOOD: With type checking
def process_data(data):
    if not isinstance(data, str):
        raise TypeError(f"Expected string, got {type(data).__name__}")
    return data.upper()
```

#### 2. **Input Length Validation** (Denial of Service)
```python
# BAD: No length check - could freeze your program
def process(text):
    return text[::-1]  # What if text is 1 million characters?

# GOOD: With length limit
def process(text, max_length=10000):
    if len(text) > max_length:
        raise ValueError("Input too long")
    return text[::-1]
```

#### 3. **Edge Cases**
- Empty strings
- None values
- Special characters
- Very large numbers

### Security Checklist
Before sharing your code:
- [ ] Does it validate input types?
- [ ] Does it check input length?
- [ ] Does it handle errors gracefully?
- [ ] Are there hardcoded passwords or keys?
- [ ] Could it loop forever?
- [ ] Are error messages safe to show users?

---

## Project Files Explained

| File | Purpose |
|------|---------|
| `palindrome_checker.py` | Main program - solves the palindrome problem |
| `test_palindrome_checker.py` | Tests to verify the main program works |
| `security_testing.py` | Penetration testing examples |
| `.gitignore` | Tells Git which files to ignore |
| `README.md` | Project documentation (this is for users) |
| `.vscode/launch.json` | VS Code debugging configuration |

---

## Common Issues & Solutions

### Issue: "Python was not found"
**Solution**: The VS Code Python extension wasn't installed. It's being installed now.

### Issue: "Module not found"
**Solution**: Make sure you're using the correct Python path with the venv

### Issue: Breakpoints not working
**Solution**: 
1. Make sure you've selected Python in VS Code
2. Restart VS Code
3. Check that `launch.json` is correct

### Issue: Git commands not found
**Solution**: Install Git from https://git-scm.com/download/win

---

## Your Learning Path

### Week 1: Basics ✓
- [x] Write your first Python script
- [x] Run and test code
- [x] Debug code using breakpoints
- [x] Initialize Git

### Week 2: Data Structures
- [ ] Learn about lists, stacks, queues
- [ ] Modify palindrome checker to use a stack
- [ ] Test edge cases

### Week 3: Algorithms
- [ ] Study algorithm complexity
- [ ] Learn Big O notation
- [ ] Optimize your code

### Week 4: Security
- [ ] Learn about common vulnerabilities
- [ ] Write secure code
- [ ] Perform penetration testing

---

## Next Challenges

1. **Modify the palindrome checker** to use a stack data structure
2. **Add support for punctuation** (currently ignores spaces)
3. **Create a linked list** implementation
4. **Build a queue** data structure
5. **Solve a new problem**: Check if parentheses are balanced

---

## Resources

- [Python Official Docs](https://docs.python.org/3/)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Learning](https://skills.github.com/)
- [Security Best Practices](https://owasp.org/www-project-top-ten/)

---

**You've taken your first step into programming! 🚀**

Remember: Every expert programmer started exactly where you are now.
