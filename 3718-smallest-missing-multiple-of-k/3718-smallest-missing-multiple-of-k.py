class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = set(nums)
        mul = k
        while mul in n:
            mul += k
        return mul
