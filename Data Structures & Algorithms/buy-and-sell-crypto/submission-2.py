class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0 :
            return 0
        
        # 2 3 4 1 6 7 8
        mini = prices[0]
        maxi = prices[0]
        max_diff = 0
        

        i = 1
        while i < len(prices) :
            if mini > prices[i] :
                max_diff = maxi - mini
                mini = prices[i]
                maxi = prices[i]
            elif prices[i] > maxi :
                maxi = prices[i]
                if max_diff < maxi - mini :
                    max_diff = maxi - mini

                
            print(mini, maxi)
            i += 1

        return max_diff