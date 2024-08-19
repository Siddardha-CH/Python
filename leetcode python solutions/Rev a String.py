class Solution:  
    def reverse(self, x: int) -> int:  
        s = -1 if x < 0 else 1  
        abs_x = abs(x)  
        revs = str(abs_x)[::-1]  
        revi = s * int(revs)  
        
        if revi < -2**31 or revi > 2**31 - 1:  
            return 0  
        
        return revi
