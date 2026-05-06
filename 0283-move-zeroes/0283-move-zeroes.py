class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 
        r = 0
        for i in range(len(nums)):
            if nums[r] == 0:
                r+=1
            elif nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                r+=1
                l+=1



            

        