class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        max_val = (nums[n-1] - 1) * (nums[n-2] - 1)
        return max_val