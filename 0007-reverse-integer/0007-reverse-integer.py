class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        reversed_sign = sign*int(str(abs(x))[::-1]) 
        if reversed_sign > 2**31 -1 or reversed_sign < -2**31:
            return 0
        return reversed_sign
        """
        :type x: int
        :rtype: int
        """
        