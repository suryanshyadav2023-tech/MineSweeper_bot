from .board_parser import neighbors

def find_moves(board, R, C):
    moves = []
    for r in range(R):
        for c in range(C):
            cell = board[r][c]
            if not cell.startswith("open"):
                continue
            num = int(cell.replace("open", ""))
            neighs = list(neighbors(R, C, r, c))
            covered = [(rr, cc) for rr, cc in neighs if board[rr][cc] == "covered"]
            flagged = [(rr, cc) for rr, cc in neighs if board[rr][cc] == "flag"]

            if len(flagged) == num and covered:
                moves.extend(("click", rr, cc) for rr, cc in covered)
            if len(flagged) + len(covered) == num and covered:
                moves.extend(("flag", rr, cc) for rr, cc in covered)
    return moves
