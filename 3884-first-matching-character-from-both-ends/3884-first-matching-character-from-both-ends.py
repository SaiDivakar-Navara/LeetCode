class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l = 0 
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                return l
            else:
                r = r - 1
                l = l + 1
        return -1