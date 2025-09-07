class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = 0
        for i in stones:
            if i in jewels:
                x+=1
        return x