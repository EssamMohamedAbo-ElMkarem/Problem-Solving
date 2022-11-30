class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map1 = []
        map2 = []
        if len(s) != len(t):
            return False
        else:
            for i, j in zip(s, t):  
                map1.append(s.index(i))
                map2.append(t.index(j))
            return map1 == map2