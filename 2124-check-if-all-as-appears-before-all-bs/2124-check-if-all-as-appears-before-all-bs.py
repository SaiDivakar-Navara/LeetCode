class Solution:
    def checkString(self, s: str) -> bool:
        foundB = False
        for i in s:
            if i == 'b':
                foundB = True
            if i == 'a' and foundB:
                return False
        return True