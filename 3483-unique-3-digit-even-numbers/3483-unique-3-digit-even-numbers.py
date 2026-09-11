class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        res = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (i in (j,k) or j in (i,k) or digits[i] == 0 or digits[k]%2!=0):
                        continue
                    num = (digits[i] * 100) + (digits[j] * 10) + digits[k]
                    res.add(num)
        return len(res)