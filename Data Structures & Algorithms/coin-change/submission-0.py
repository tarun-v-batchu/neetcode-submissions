class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        i = 1
        while i <= amount :
            val = -1
            for coin in coins :
                if i - coin < 0 or dp[i - coin] == -1 :
                    continue
                if val == -1 :
                    val = dp[i - coin] + 1
                else :
                    val = min(dp[i - coin] + 1, val)
            dp += [val]
            i += 1
        return dp[-1]
