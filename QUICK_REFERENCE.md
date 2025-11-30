# Quick Reference Card 📚

## Essential Commands

### Running Your Code
```bash
# Change to project directory
cd "c:\Users\anupa\source\repos\python-learning"

# Run the main program
C:/Users/anupa/source/repos/.venv/Scripts/python.exe palindrome_checker.py

# Run all tests
C:/Users/anupa/source/repos/.venv/Scripts/python.exe -m unittest test_palindrome_checker.py -v

# Run security tests
C:/Users/anupa/source/repos/.venv/Scripts/python.exe security_testing.py
```

### Git Commands
```bash
# Check status
git status

# View commit history
git log

# Make a commit
git add .
git commit -m "Your message here"

# Push to GitHub (after setting up remote)
git push origin main
```

### Debugging in VS Code
| Action | Shortcut |
|--------|----------|
| Start Debugging | F5 |
| Step Over | F10 |
| Step Into | F11 |
| Continue | F5 |
| Stop | Shift+F5 |

## Key Concepts

### Palindrome
A word or phrase that reads the same forwards and backwards
- "racecar" ✓
- "hello" ✗

### Virtual Environment
An isolated Python installation for your project
- Prevents conflicts between projects
- Easy to share and recreate

### Unit Testing
Writing code to test your code
- More confidence your code works
- Easier to catch bugs

### Security Testing
Testing your code like a hacker would
- Prevents vulnerabilities
- Catches edge cases

## Project Structure
```
python-learning/
├── .git/                      # Git repository data
├── .vscode/
│   └── launch.json           # VS Code debug settings
├── palindrome_checker.py     # Main program
├── test_palindrome_checker.py # Tests
├── security_testing.py       # Security examples
├── README.md                 # Project info
├── LEARNING_GUIDE.md        # Detailed guide
└── .gitignore               # Files to ignore
```

## Next Steps After Today

### Short Term (This Week)
1. Practice debugging with breakpoints
2. Modify test cases in `test_palindrome_checker.py`
3. Add your own test cases

### Medium Term (This Month)
1. Create GitHub repository
2. Learn about stacks and queues
3. Implement palindrome checker using a stack

### Long Term (This Year)
1. Study data structures (arrays, linked lists, trees)
2. Learn algorithms and complexity analysis
3. Build a portfolio with multiple projects

## Troubleshooting

### Python command not found?
Use the full path: `C:/Users/anupa/source/repos/.venv/Scripts/python.exe`

### Breakpoints not working?
1. Make sure Python extension is installed
2. Restart VS Code
3. Check `.vscode/launch.json` exists

### Git command not found?
Install Git from https://git-scm.com/download/win

## Code Quality Checklist

Before committing code:
- [ ] Does it run without errors?
- [ ] All tests pass?
- [ ] Variables have clear names?
- [ ] Code has comments explaining logic?
- [ ] No hardcoded secrets?
- [ ] Input is validated?

---

**Remember**: Programming is 90% debugging and 10% writing code!
