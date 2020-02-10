class Solution:
    def solve(self, board: List[List[str]]) -> None:
        try:
            rows = len(board)
            cols = len(board[0])
        except:
            return

        self.board = board

        for row in range(rows):
            self.dfs(row, 0)
            self.dfs(row, cols-1)
        for col in range(cols):
            self.dfs(0, col)
            self.dfs(rows-1, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "?":
                    board[row][col] = "O"

    def dfs(self, row, col):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]) or self.board[row][col] != "O":
            return
        else:
            self.board[row][col] = "?"
            self.dfs(row-1, col)
            self.dfs(row+1, col)
            self.dfs(row, col+1)
            self.dfs(row, col-1)
