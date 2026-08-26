class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        arr = [[]]

        for i in nums :
            temp = []
            for s in arr :
                temp += [s + [i], s]
            arr = temp

        return arr
