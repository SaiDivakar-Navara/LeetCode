class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            leftMax = nums[0]
            rightMin = nums[i]
            for j in range(0, i):
                leftMax = max(leftMax, nums[j])
            for j in range(i, n):
                rightMin = min(rightMin, nums[j])
            
            score  = leftMax - rightMin
            if score <= k:
                return i
        return -1