class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        arr = []
        
        for i in range(len(accounts)):
            arr.append(sum(accounts[i]))
        return max(arr)

