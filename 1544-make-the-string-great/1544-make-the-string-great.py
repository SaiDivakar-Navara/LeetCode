class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
            if st and abs(ord(i) - ord(st[-1])) == 32:
                st.pop()
            else:
                st.append(i)
        return ''.join(st)