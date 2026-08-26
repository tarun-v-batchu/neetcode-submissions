class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        arr = sorted([(i, gas[i] - cost[i]) for i in range(len(gas))], key=lambda l: l[1], reverse = True)
        
        print(arr)
        for i in arr :
            total = 0
            print(i[0], "iteration")
            for j in range(len(arr)) :
                print(total, j)
                total += (gas[(i[0] + j) % len(arr)] - cost[(i[0] + j) % len(arr)])
                print("After", total, (i[0] + j) % len(arr))
                if total < 0 :
                    break
            if total >= 0 :
                return i[0]
        return -1

