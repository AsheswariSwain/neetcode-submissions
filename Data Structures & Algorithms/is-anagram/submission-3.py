class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for chars in s:
            if chars in hmap:
                hmap[chars] +=1
            else:
                hmap[chars] = 1
        for chars in t:
            if chars not in hmap:
                return False
            else:
                hmap[chars] -= 1
            if hmap[chars] == 0:
                del hmap[chars]
        return True
                

        


        