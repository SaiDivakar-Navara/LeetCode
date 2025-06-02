class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for i in operations:
            if i == '+':
                top1 = st[-1]
                top2 = st[-2]
                st.append(top1+top2)
            elif i =='D':
                top_ele = st[-1]
                st.append(top_ele * 2)
            elif i == 'C':
                st.pop()
            else:
                st.append(int(i))
        return sum(st)
            
        