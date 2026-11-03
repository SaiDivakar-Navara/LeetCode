class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        mid = len(nums) // 2
        for i in range(len(nums)):
            count += abs(nums[mid] - nums[i])
        return count