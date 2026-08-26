class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[1]+[0 for _ in range(amount)] for _ in range(len(coins) + 1)]

        for i in range(1, len(coins) + 1) :
            for j in range(1, amount + 1) :
                # print(i, j, dp[i][j - coins[i - 1]])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j] + dp[i][j - coins[i - 1]] if j - coins[i-1] >= 0 else 0)
        
        print(dp)
        return dp[-1][-1]