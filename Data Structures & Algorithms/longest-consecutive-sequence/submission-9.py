class UnionFind: 
    def __init__(self) :
        self.parents = {}
        self.rank = {}
        self.size = {}
        self.nodes = set()

    def insert(self, a) :
        if a in self.nodes :
            return
        self.nodes.add(a)
        self.parents[a] = a
        self.rank[a] = 0
        self.size[a] = 1

        if a - 1 in self.nodes :
            self.union(a, a - 1)
        if a + 1 in self.nodes :
            self.union(a, a + 1)
    
    def find(self, a) :
        if self.parents[a] == a :
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b) :
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root :
            return
        if self.rank[a_root] > self.rank[b_root] :
            self.parents[b_root] = a_root
            self.size[a_root] += self.size[b_root]
        elif self.rank[b_root] > self.rank[a_root] :
            self.parents[a_root] = b_root
            self.size[b_root] += self.size[a_root]
        else :
            self.parents[a_root] = b_root
            self.size[b_root] += self.size[a_root]
            self.rank[b_root] += 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0

        uf = UnionFind()
        for i in nums :
            uf.insert(i)
        
        return max([uf.size[i] for i in uf.size])
        

                
