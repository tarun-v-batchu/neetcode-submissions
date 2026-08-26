class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dic = defaultdict(int)

        for i in range(len(numbers)) :
            if target - numbers[i] in dic :
                return [dic[target - numbers[i]], i + 1]
            dic[numbers[i]] = i + 1
        
        return [-1, -1]

        