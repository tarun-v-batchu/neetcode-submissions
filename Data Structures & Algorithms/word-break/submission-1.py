class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True
        i = 1
        while i < len(s) + 1 :
            if not dp[i - 1] :
                i += 1
                continue
            for word in wordDict :
                if i + len(word) - 1 < len(dp) and word == s[i - 1: i - 1 + len(word)] :
                    dp[i + len(word) - 1] = True
            i += 1
        return dp[-1]

