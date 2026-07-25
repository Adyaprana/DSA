class Solution(object):
    def isPalindrome(self, s):
        cleaned = "".join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()
        left = 0
        right = len(cleaned)-1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
        