def is_palindrome(s: str) -> bool:
    def is_alphanumeric(c: str) -> bool:
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer to the next valid character
        while left < right and not is_alphanumeric(s[left]):
            left += 1
        # Move right pointer to the previous valid character
        while left < right and not is_alphanumeric(s[right]):
            right -= 1
        
        # Compare characters after converting to lowercase
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers
        left += 1
        right -= 1
    
    return True

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))           