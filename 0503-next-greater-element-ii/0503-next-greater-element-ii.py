class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(2 * n -1, -1, -1):
            if i >= n:
                i = i % n
                stack.append(nums[i])
            else:
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(nums[i])
        return res