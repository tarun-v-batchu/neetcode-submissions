class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs :
            string += (i + "\n")
        return string

    def decode(self, s: str) -> List[str]:
        
        i = 0
        running = ""
        arr = []
        
        while i < len(s) :
            if s[i] == "\n" :
                arr.append(running)
                running = ""
            else :
                running += s[i]
            i += 1
        return arr

