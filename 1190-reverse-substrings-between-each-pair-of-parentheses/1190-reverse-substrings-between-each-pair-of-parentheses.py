class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = []
        starts = []
        for ch in s:
            if ch == "(":
                starts.append(len(answer))
            elif ch == ")":
                left = starts.pop()
                right = len(answer) - 1

                while left < right:
                    answer[left], answer[right] = (
                        answer[right],
                        answer[left],
                    )
                    left += 1
                    right -= 1
            else:
                answer.append(ch)

        return "".join(answer)