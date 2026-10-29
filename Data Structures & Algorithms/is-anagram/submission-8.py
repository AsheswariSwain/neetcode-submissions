class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False
        ss = self.getmap(s)
        
        tt = self.getmap(t)
        
        for chars in ss:
            if chars not in tt:
                return False
            elif ss[chars] != tt[chars]:
                return False
        return True

    def getmap(self,s):
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
        return map




