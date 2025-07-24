class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        x = 0
        for char in s:
            if char == '(':
                if x > 0:
                    st.append(char)
                x+=1
            else:
                x -= 1
                if x > 0:
                    st.append(char)
        return ''.join(st)