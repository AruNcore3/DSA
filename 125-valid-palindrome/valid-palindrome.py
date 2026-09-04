class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(char.lower() for char in s if char.isalnum())
        if result == result[::-1]:
            return True
        return False