def exist(board, word):
    length = len(board)
    width = len(board[0])
    return builder(board, word, board[0][0], 0, 0, length, width)
def builder(board, word, curr, x, y, l, w):
        print (curr, x, y, l, w)
        if curr is word:
            return True
        if x == l-1 or y == w-1:
            return False
        return builder(board, word, curr+board[x+1][y], x+1, y, l, w) or builder(board, word, curr+board[x][y+1], x, y+1, l, w)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCCED"

print(exist(board, word))