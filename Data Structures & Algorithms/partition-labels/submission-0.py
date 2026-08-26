class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {}
        for i, c in enumerate(s) :
            d[c] = i
        
        front = 0
        end = 0
        arr = []

        for i, c in enumerate(s) :

            if d[c] > end :
                end = d[c]
            elif i == end :
                arr += [i - front + 1]
                end += 1
                front = end
            
        if end != front :
            arr += [end - front + 1]
        return arr


             

