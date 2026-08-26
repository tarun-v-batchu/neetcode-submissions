class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        dp = [[0 for i in range(len(prices) + 1)] for i in range(len(prices) + 1)]

        for i in range(1, len(prices) + 1) :
            for j in range(i, len(prices) + 1) :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], prices[j - 1] - prices[i - 1])
                if i >= 2 :
                    # print(i, j, ":", prices[i-1], prices[j-1], " - ", dp[i][j], dp[i-2][i-2], prices[j - 1] - prices[i - 1])
                    dp[i][j] = max(dp[i][j], dp[i-2][i-2] + prices[j - 1] - prices[i - 1])
        # print(dp)
        return dp[-1][-1]



