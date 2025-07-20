class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        st=[]
        l = True
        for char in word:
            if char == ch and l:
                st.append(char)
                st = st[::-1]
                l = False
            else:
                st.append(char)
        return "".join(st)
                