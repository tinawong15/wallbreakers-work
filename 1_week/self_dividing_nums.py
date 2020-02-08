class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        for i in range(left, right+1):
            self_dividing = True
            if '0' in str(i):
                continue
            digits = [int(digit) for digit in str(i)]
            for digit in digits:
                if i % digit != 0:
                    self_dividing = False
            if self_dividing:
                self_dividing_nums.append(i)
        return self_dividing_nums


        
