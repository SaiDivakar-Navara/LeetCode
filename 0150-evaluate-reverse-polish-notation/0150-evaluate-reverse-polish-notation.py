class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i in "+/*-":
                o2 = st.pop()
                o1 = st.pop()
                if i == '+':
                    st.append(o1+o2)
                elif i == '-':
                    st.append(o1-o2)
                elif i == '*':
                    st.append(o1*o2)
                else:
                    st.append(int(o1/o2))
            else:
                st.append(int(i))
        return st[-1]

        