class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def findRow(matrix, target) :
            top = 0
            bottom = len(matrix) - 1
            
            while top < bottom :
                mid = (top + bottom)//2
                print(top, mid, bottom)
                if matrix[mid][0] <= target <= matrix[mid][-1] :
                    return mid
                elif target < matrix[mid][0] :
                    bottom = mid - 1
                else :
                    top = mid + 1
            return bottom if matrix[bottom][0] <= target <= matrix[bottom][-1] else top
        
        def findCol(matrix, target) :
            left = 0
            right = len(matrix) - 1
            
            while left < right :
                mid = (left + right)//2

                if  target == matrix[mid] :
                    return mid
                elif target < matrix[mid] :
                    right = mid - 1
                else :
                    left = mid + 1
            
            return left if matrix[left] == target else right if matrix[right] == target else -1
        
        row = findRow(matrix, target)
        # print(row)
        return findCol(matrix[row], target) != -1