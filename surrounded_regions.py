class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        coords = []
        board_len = len(board)
        row_len = len(board[0]) - 1
        # top
        # coords.append([[0, i] for i, q in enumerate(board[0]) if q == "O"])
        # # bottom
        # coords.append(
        #     [[board_len, i] for i, q in enumerate(board[board_len]) if q == "O"]
        # )
        for i in range(board_len):
            row_coord = [[i,indx] for indx, q in enumerate(board[i]) if q == "O"]
            # import pdb; pdb.set_trace()
            for x in row_coord:
                coords.append(x)
        for x in coords:
            if len(x) == 0:
                continue
            if x[0] == 0:
                print("top border")
            elif x[0] == board_len - 1:
                print("bottom border")
            elif x[1] == 0:
                print("left border")
            elif x[1] == row_len:
                prin("right border")

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
Solution().solve(board)
