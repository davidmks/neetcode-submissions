class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2. solution (two pointers)
        left, right = 0, len(s) - 1 # O(1) space
        while left < right: # O(n) time
            while left < right and not s[left].isalnum(): # O(1) time
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower(): # O(1) time
                return False
            left += 1
            right -= 1
        return True


        # # 1. solution (check reverse sting)
        # cleaned = [c.lower() for c in s if c.isalnum()] # O(n) time; O(n) space
        # return cleaned == cleaned[::-1] # 2x O(n) time; O(n) space
