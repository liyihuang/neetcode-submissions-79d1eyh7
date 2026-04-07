class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict, tdict = {}, {}
        if len(s) != len(t):
            return False
        for x in s:
            if x not in sdict:
                sdict[x]=1
            else:
                sdict[x]= sdict[x]+1

        for y in t:
            if y not in tdict:
                tdict[y]=1
            else:
                tdict[y]= tdict[y]+1
        return sdict == tdict