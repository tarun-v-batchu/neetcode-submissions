class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s) - 1
        while i < j :
            while i < j and not self.isAlphanumeric(s[i]) :
                i += 1
            while i < j and not self.isAlphanumeric(s[j]) :
                j -= 1
            if ('0' <= s[i] <= '9' or '0' <= s[j] <= '9') and s[i] != s[j] :
                return False
            if s[i].lower() != s[j].lower() :
                return False
            i += 1
            j -= 1
        return True


    def isAlphanumeric(self, letter) :
        if 'a' <=  letter <= 'z' or 'A' <= letter <= 'Z' or '0' <= letter <= '9' :
            return True
        return False