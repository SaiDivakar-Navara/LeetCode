class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        ans = -1
        temp = len(nums)//2
        for i in dic:
            val = dic[i]
            if val > temp:
                ans = i
        return ans
