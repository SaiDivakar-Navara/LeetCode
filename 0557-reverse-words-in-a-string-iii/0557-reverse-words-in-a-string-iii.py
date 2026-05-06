class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        res = [i[::-1] for i in arr]
        return " ".join(res)