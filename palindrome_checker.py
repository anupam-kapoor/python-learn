"""
Palindrome Checker - A simple data structure problem
This program checks if a string is a palindrome (reads the same forwards and backwards)
"""

def is_palindrome(text):
    """
    Check if a given text is a palindrome.
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if the text is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Remove punctuation for more accurate checking
    cleaned_text = ''.join(char for char in cleaned_text if char.isalnum())
    
    # Compare the text with its reverse
    is_palindrome_result = cleaned_text == cleaned_text[::-1]
    
    return is_palindrome_result


def main():
    """Main function to demonstrate palindrome checking"""
    
    # Test cases
    test_strings = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "python",
        "level"
    ]
    
    print("=== Palindrome Checker ===\n")
    
    for test_string in test_strings:
        result = is_palindrome(test_string)
        status = "✓ Palindrome" if result else "✗ Not a palindrome"
        print(f"'{test_string}' -> {status}")


if __name__ == "__main__":
    main()
