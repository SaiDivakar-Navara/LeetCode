class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        def climbStairsHelper(n):
            if n <= 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = climbStairsHelper(n - 1) + climbStairsHelper(n - 2)
            return dp[n]
        return climbStairsHelper(n)