class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        arr = [["()"]]
        i = 2
        while i <= n :
            new_arr = ['(' + x + ')' for x in arr[-1]] # (A(x-1))
            x = 0
            while x < len(arr) :
                for j in arr[x] :
                    for j2 in arr[len(arr) - x - 1] :
                        if j+j2 not in new_arr :
                            new_arr.append(j + j2)
                x+=1
            arr.append(new_arr)
            print(new_arr)
            i+=1
        print(arr[-1])
        return arr[-1]

        
        # 0: ()
        # 1: (()) ()()
        # 2: ((())) (()()) (())() ()()() ()(())
        # 3: (((()))) (()())
        
