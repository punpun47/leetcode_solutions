class Solution:
    def isPalindrome(self, x: int) -> bool:
        # edge case: negative numbers cannot be palindromes
        if x < 0:
            return False

        # convert to string
        s = str(x)

        # Two pointers
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True