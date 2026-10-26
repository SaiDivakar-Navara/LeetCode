class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        win_sum = 0
        for i in range(k):
            win_sum += nums[i]
        max_sum = win_sum
        for j in range(k, n):
            win_sum += nums[j]
            win_sum -= nums[j - k]
            max_sum = max(max_sum, win_sum)
        return max_sum/k
        
        
