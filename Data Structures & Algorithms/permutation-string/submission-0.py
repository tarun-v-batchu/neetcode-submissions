class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = "".join(sorted(s1))
        k = len(s1)

        i = 0
        while i < len(s2) - k + 1:

            if "".join(sorted(s2[i : i + k])) == s1 :
                return True
            i += 1
        return False

        
            