class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            if all(digit == 9 for digit in digits):
                digits.insert(0,0)
            digits[-1] += 1
            i = -2
            while i >= -len(digits):
                if(digits[i+1] == 10):
                    digits[i+1] = 0
                    digits[i] += 1
                i -= 1
        else:
            digits[-1] += 1
        return digits
        
