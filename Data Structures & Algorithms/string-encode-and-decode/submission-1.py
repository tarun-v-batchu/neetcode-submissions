class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += (i + "\n")
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        suh = ""
        arr = []
        while i < len(s) :
            if s[i] == "\n" :
                arr.append(suh)
                suh = ""
            else:
                suh += s[i]
            i+=1
        return arr