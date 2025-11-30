"""
Security Testing & Code Review Guide
====================================

This file demonstrates basic security concepts for penetration testing and code review.
Think of penetration testing as "ethical hacking" - testing your own code for vulnerabilities.
"""

"""
=== SECURITY CONCEPTS FOR BEGINNERS ===

1. INPUT VALIDATION
   - Always validate user input
   - Check data type, length, and format
   - Example: Ensure the input is a string before processing

2. BUFFER OVERFLOW
   - Don't allocate fixed size buffers without bounds checking
   - Python handles this automatically, but other languages (C++) don't

3. INJECTION ATTACKS
   - Be careful with user input in SQL, commands, or file operations
   - Example: If building SQL, use parameterized queries, not string concatenation

4. DENIAL OF SERVICE (DoS)
   - Avoid infinite loops that can be triggered by user input
   - Set limits on recursion depth and input size

5. INFORMATION DISCLOSURE
   - Don't expose sensitive information in error messages
   - Don't log passwords or API keys
"""


def secure_palindrome_checker(text, max_length=10000):
    """
    Secure version of palindrome checker with input validation.
    
    Args:
        text (str): The text to check
        max_length (int): Maximum allowed input length (prevents DoS)
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Raises:
        TypeError: If input is not a string
        ValueError: If input exceeds max_length
    """
    # INPUT VALIDATION - Check type
    if not isinstance(text, str):
        raise TypeError(f"Expected string, got {type(text).__name__}")
    
    # INPUT VALIDATION - Check length (Prevents DoS)
    if len(text) > max_length:
        raise ValueError(f"Input exceeds maximum length of {max_length} characters")
    
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Check palindrome
    is_palindrome_result = cleaned_text == cleaned_text[::-1]
    
    return is_palindrome_result


def test_security():
    """Test security measures of the palindrome checker"""
    
    print("=== SECURITY TESTING ===\n")
    
    # Test 1: Normal input
    print("Test 1: Normal valid input")
    try:
        result = secure_palindrome_checker("racecar")
        print(f"✓ Result: {result}\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")
    
    # Test 2: Type checking (prevents type confusion attacks)
    print("Test 2: Invalid type (number instead of string)")
    try:
        result = secure_palindrome_checker(12321)
        print(f"✓ Result: {result}\n")
    except TypeError as e:
        print(f"✓ Successfully caught error: {e}\n")
    
    # Test 3: None input (prevents NoneType attacks)
    print("Test 3: None input")
    try:
        result = secure_palindrome_checker(None)
        print(f"✓ Result: {result}\n")
    except TypeError as e:
        print(f"✓ Successfully caught error: {e}\n")
    
    # Test 4: DOS attack attempt (very long string)
    print("Test 4: Denial of Service attempt (very long input)")
    try:
        malicious_input = "a" * 100000  # 100,000 character string
        result = secure_palindrome_checker(malicious_input)
        print(f"✓ Result: {result}\n")
    except ValueError as e:
        print(f"✓ Successfully blocked attack: {e}\n")
    
    # Test 5: Empty string (edge case)
    print("Test 5: Edge case - empty string")
    try:
        result = secure_palindrome_checker("")
        print(f"✓ Result: {result}\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")
    
    # Test 6: Special characters (potential injection attempt)
    print("Test 6: Input with special characters")
    try:
        result = secure_palindrome_checker("a!@#$%a")
        print(f"✓ Result: {result}\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")


"""
=== PENETRATION TESTING CHECKLIST FOR YOUR CODE ===

Before deploying code, always check:

1. INPUT VALIDATION ✓
   - Does your code validate input types?
   - Does your code check input length?
   - Does your code sanitize user input?

2. ERROR HANDLING ✓
   - Does your code handle exceptions gracefully?
   - Do error messages reveal sensitive information?
   - Are all edge cases covered?

3. RESOURCE LIMITS ✓
   - Does your code prevent infinite loops?
   - Does your code limit recursion depth?
   - Does your code limit input size?

4. DATA SECURITY ✓
   - Are sensitive values (passwords, tokens) never logged?
   - Are secrets stored securely (not in source code)?
   - Is data encrypted where appropriate?

5. DEPENDENCY SECURITY ✓
   - Are all libraries up to date?
   - Do you know what each library does?
   - Are there known vulnerabilities?

6. CODE REVIEW ✓
   - Has someone else reviewed your code?
   - Are there any hardcoded secrets?
   - Is the code easy to understand?
"""


if __name__ == "__main__":
    test_security()
    
    print("\n=== SUMMARY ===")
    print("Security testing involves:")
    print("1. Testing with invalid inputs")
    print("2. Testing with extreme values")
    print("3. Testing error handling")
    print("4. Testing resource limits")
    print("5. Checking for data leaks")
    print("\nAlways think: 'How could someone break this?'")
