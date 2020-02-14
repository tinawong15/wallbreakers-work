class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while(n not in numbers):
            numbers.add(n)
            sum = 0
            for digit in str(n):
                sum += int(digit)*int(digit)
            if(sum == 1):
                return True
            n = sum
        return False
        
