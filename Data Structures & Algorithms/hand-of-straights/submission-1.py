class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0 :
            return False
        
        count = Counter(hand)
        
        start = min(count.keys())
        while start <= max(count.keys()) - groupSize + 1:
            num = count[start]
            i = start
            while i < start + groupSize :
                # print(start, count[i], num)
                if count[i] < num :
                    return False
                count[i] -= num
                i += 1

            start += 1
        
        
        return len([1 for i in count if count[i] > 0]) == 0



        