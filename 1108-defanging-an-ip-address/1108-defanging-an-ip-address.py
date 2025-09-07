class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in address:
            if i == '.':
                res = address.replace(".", "[.]")
        return res