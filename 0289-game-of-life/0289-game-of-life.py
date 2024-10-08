class Solution(object):
    def gameOfLife(self, board):
        import copy

        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        board_2 = copy.deepcopy(board)

        dx = [-1, 0, 1, 1, 1, 0, -1, -1]
        dy = [-1, -1, -1, 0, 1, 1, 1, 0]

        width, height = len(board[0]), len(board)

        for i in range(height):
            for j in range(width):
                now = board_2[i][j]
                live, die = 0, 0

                for d in range(8):
                    ny = i + dy[d]
                    nx = j + dx[d]

                    if ny >= height or ny < 0 or nx >= width or nx < 0:
                        continue

                    ne = board_2[ny][nx]
                    if ne == 1:
                        live += 1
                    elif ne == 0:
                        die += 1
                    
                if now == 1:
                    if live < 2:
                        board[i][j] = 0
                    elif live == 2 or live == 3:
                        board[i][j] = 1
                    elif live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1
        
        return board

