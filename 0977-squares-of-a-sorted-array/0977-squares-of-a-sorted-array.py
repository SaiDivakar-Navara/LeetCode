class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)): 
            res.append(nums[i] * nums[i])
        res.sort()
        return res