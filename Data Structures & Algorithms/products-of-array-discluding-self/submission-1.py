class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        zero_count = 0
        
        for n in nums:
            if n != 0:
                result *= n
            else:
                zero_count += 1
                
        r_list = []
        
        for x in nums:
            if zero_count >= 2:
                r_list.append(0)
            elif zero_count == 1:
                if x == 0:
                    r_list.append(result)
                else:
                    r_list.append(0)
            else: 
                r_list.append(int(result/x))
                
        return r_list