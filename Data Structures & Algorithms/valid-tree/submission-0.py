class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        pres = defaultdict(list)

        for to, fro in edges :
            pres[to] += [fro]
            pres[fro] += [to]

        visited = set()
        seen = set()
        def recurse(s, prev) :
            if s in visited :
                print(s, "found", visited)
                return False

            visited.add(s)

            for i in pres[s] :
                if i == prev :
                    continue
                if not recurse(i, s) :
                    print("error found at", s, "pointing at", i)
                    return False
            
            return True
        

        return recurse(0, -1) and len(visited) == n
        