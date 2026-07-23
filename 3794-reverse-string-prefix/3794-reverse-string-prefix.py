class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        l = 0
        r = k - 1
        s = list(s)
        if k == 0:
            return s
        else:
            while l < r:
                s[l],s[r] = s[r],s[l]
                l = l + 1
                r = r - 1
            return "".join(s)
