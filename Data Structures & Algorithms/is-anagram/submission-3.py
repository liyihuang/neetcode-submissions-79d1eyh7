class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict, tdict = {}, {}
        if len(s) != len(t):
            return False
        for x in s:
            sdict[x] = sdict.get(x, 0) + 1

        for y in t:
            tdict[y] = tdict.get(y, 0) + 1
        return sdict == tdict