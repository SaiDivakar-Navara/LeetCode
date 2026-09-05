class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            max_count = 0
            current_count = 0
            n = len(nums)
            for i in range(0, n):
                if nums[i] == 1:
                    current_count += 1
                else:
                    max_count = max(max_count, current_count)
                    current_count = 0
            return max(max_count, current_count)