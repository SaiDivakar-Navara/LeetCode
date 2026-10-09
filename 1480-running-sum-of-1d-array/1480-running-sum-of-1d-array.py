class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = 0
        arr = []
        for i in range(len(nums)):
            s += nums[i]
            arr.append(s)
        return arr
