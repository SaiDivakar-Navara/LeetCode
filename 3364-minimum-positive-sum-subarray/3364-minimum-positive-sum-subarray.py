class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                if l <= length <= r:
                    total = sum(nums[i:j+1])
                    if total > 0:
                        ans = min(ans, total)
        return ans if ans != float('inf') else -1