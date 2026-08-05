class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = []
        max_num = max(nums)
        min_num = min(nums)
        for i in range(min_num, max_num):
            if i in nums:
                continue
            else:
                arr.append(i)
        return arr
