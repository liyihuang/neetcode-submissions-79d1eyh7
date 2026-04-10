class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for s in strs:
            c_count = {}
            for c in s:
                c_count[c] = c_count.get(c, 0) + 1
            
            key = frozenset(c_count.items())
            res.setdefault(key, []).append(s)
            
        return list(res.values())