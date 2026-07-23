class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        count = 0
        while l < r:
            if nums[l] == 0 and nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                count += 1
            if nums[l]!=0:
                l+=1
            if nums[r] == 0:
                r -= 1
        return count
                


