class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            count = 0
            while i > 0:
                i = i//10
                count += 1
            if count % 2 == 0:
                res += 1
        return res
            