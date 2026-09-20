class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += (i + 1) * (122 - ord(s[i]) + 1)
        return total
            