class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        win_sum = 0
        max_sum = 0
        left = 0
        for right in range(n):
            x = nums[right]
            freq[x] = freq.get(x, 0) + 1
            win_sum += x
            if right - left + 1 > k:
                y = nums[left]
                freq[y] -= 1
                if freq[y] == 0:
                    del freq[y]
                win_sum -= y
                left += 1
            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, win_sum)
        return max_sum



