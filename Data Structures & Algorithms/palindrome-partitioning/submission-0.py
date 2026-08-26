class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s) :
            i,j = 0, len(s) - 1

            while i < j :
                if s[i] != s[j] :
                    return False
                i += 1
                j -= 1
            return True

        
        def recurse(s, i, arr, all_arr) :

            if i >= len(s) :
                return all_arr + [arr]
            
            for j in range(i, len(s)) :
                if is_palindrome(s[i:j+1]) :
                    temp = arr.copy() + [s[i:j+1]]
                    all_arr = recurse(s, j + 1, temp, all_arr)
            
            return all_arr

        return recurse(s, 0, [], [])
