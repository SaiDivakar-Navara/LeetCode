class Solution:
    def calculate(self, s: str) -> int:
        st = []
        num = 0
        op = '+'
        for i in range(len(s) + 1):
            ch = '+' if i == len(s) else s[i]
            if ch.isdigit():
                num = num *10 + int(ch)
            elif ch != ' ':
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                elif op == '*':
                    st.append(st.pop() * num)
                elif op == '/':
                    st.append(int(st.pop()/num))
                
                op = ch
                num = 0
        return sum(st)