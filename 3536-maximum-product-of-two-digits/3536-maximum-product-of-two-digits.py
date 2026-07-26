class Solution:
    def maxProduct(self, n: int) -> int:
        n = list(map(int,str(n)))
        a = sorted(n)
        res = a[-1]*a[-2]
        return res
        