class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = n * (n + 1) / 2
        nums_sum = sum(nums)
        res = total_sum - nums_sum
        return res


        