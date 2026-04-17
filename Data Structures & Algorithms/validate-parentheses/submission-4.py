class Solution:
    def isValid(self, s: str) -> bool:


        s_list = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                s_list.append(x)
            else:
                if len(s_list) == 0:
                    return False
                r = s_list.pop()
                if x == ')' and r != '(': return False
                if x == ']' and r != '[': return False
                if x == '}' and r != '{': return False
        
        if len(s_list) == 0:
            return True
        else:
            return False

            