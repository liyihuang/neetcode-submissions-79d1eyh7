class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for s in strs:
            c_count = {}
            for c in s:
                if c not in c_count:
                    c_count[c] = 1
                else:
                    c_count[c] += 1
            
            key = frozenset(c_count.items())
            
            if key not in res:
                res[key] = []
            res[key].append(s)
            
        return list(res.values())