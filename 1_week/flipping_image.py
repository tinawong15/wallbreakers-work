class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for l in A:
            for i in range(len(l)//2):
                temp = l[-(i+1)]
                l[-(i+1)] = l[i]
                l[i] = temp
            for i in range(len(l)):
                if l[i] == 0:
                    l[i] = 1
                else:
                    l[i] = 0
        return A
        
