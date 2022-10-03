class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        maxWealth = 0
        # first loop for customer
        for i in range(len(accounts)): 
            wealth = sum(accounts[i])
            if (wealth > maxWealth):
                maxWealth = wealth
                
        return maxWealth