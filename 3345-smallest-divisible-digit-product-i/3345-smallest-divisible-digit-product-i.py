class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while (True):
            pro = 1
            for i in str(n):
                pro *= int(i)
            if pro % t == 0:
                return n
            n = n + 1
        

