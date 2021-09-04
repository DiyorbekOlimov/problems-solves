class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 > x > 2**31 - 1: return 0
        out = 0
        n = 1 if x > 0 else -1
        x = abs(x)

        while x > 0:
            a = x % 10
            x = x // 10
            out = out * 10 + a
        
        out *= n
        if -2**31 > out or out > 2**31 - 1: return 0
        return out
