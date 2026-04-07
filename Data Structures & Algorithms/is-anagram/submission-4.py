class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict, tdict = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1
            tdict[t[i]] = tdict.get(t[i], 0) + 1
        return sdict == tdict