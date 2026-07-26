class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return max(nums[n-1]*nums[n-2]*nums[n-3], nums[0]*nums[1]*nums[-1])
        