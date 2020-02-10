class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        students = len(M[0])

        union_find = UnionFind(students)

        for row in range(len(M)):
            for col in range(students):
                if M[row][col] == 1:
                    union_find.union(row,col)

        return union_find.get_circle_num()

class UnionFind(object):
    def __init__(self, students):
        self.students = students
        self.parent = []
        for i in range(students):
            self.parent.append(i)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b

    def get_circle_num(self):
        results = []
        for i in range(self.students):
            result = self.find(i)
            if result in results:
                continue
            else:
                results.append(result)
        return len(results)
