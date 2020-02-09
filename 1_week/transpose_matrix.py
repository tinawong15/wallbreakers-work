class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        A_transpose = []
        if A != []:
            i = 0
            for i in range(len(A[0])):
                l = []
                for row in A:
                    l.append(row[i])
                A_transpose.append(l)
        return A_transpose
