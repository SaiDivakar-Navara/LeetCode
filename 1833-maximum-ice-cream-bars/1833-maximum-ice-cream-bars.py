class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        l = 0 
        c = 0
        while l <len(costs):
            if costs[l] <= coins:
                coins -= costs[l]
                c += 1
                l += 1
            else:
                break
        return c


