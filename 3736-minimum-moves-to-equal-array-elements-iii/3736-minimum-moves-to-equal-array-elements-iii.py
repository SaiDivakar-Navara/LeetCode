class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            count += max(nums) - nums[i]
        return count
