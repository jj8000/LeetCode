class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            if sum(account) > max_wealth:
                max_wealth = sum(account)
        return max_wealth

