class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = [0] * 26
        for char in s:
            a[ord(char) - ord('a')] += 1
        for char in t:
            a[ord(char) - ord('a')] -= 1
        for i in range(26):
            if a[i] == -1:
                return chr(i + ord('a'))


            