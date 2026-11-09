class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans
