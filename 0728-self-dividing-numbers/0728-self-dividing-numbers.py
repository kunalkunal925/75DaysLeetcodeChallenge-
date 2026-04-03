class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            temp = num
            is_self_dividing = True
            
            while temp > 0:
                digit = temp % 10
                # Case: zero is present or not divisible by digit
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
                temp //= 10
                
            if is_self_dividing:
                res.append(num)
                
        return res