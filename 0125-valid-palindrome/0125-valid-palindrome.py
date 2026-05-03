class Solution:
    def isPalindrome(self, s: str) -> bool:
        sr = "".join(char for char in s.lower() if char.isalnum())
        l = 0
        r = len(sr) - 1
        while l <= r:
            if sr[l] != sr[r]:
                return False
            else:
                l +=1
                r -=1
        return True
