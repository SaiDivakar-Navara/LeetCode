class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        if start == len(nums) - 1:
            result.append(str(nums[start]))
        elif nums:
            result.append(f"{nums[start]}->{nums[-1]}")
        return result