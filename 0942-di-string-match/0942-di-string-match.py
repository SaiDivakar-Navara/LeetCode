class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left = 0
        right = len(s)
        res = []
        for char in s:
            if char == 'I':
                res.append(left)
                left+=1
            else:
                res.append(right)
                right-=1
        res.append(left)
        return res