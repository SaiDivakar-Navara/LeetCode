class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res