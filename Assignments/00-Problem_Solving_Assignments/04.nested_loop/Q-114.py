# Q114. Tic-Tac-Toe Board Analyzer
# Source: 00.Problem_Solving_Assignments/04.nested_for_loop.md
board = []
x_count = o_count = 0
for row in range(3):
    cells = input().upper().split()
    if len(cells) != 3:
        raise ValueError("Enter three cells per row")
    for cell in cells:
        if cell == "X":
            x_count += 1
        elif cell == "O":
            o_count += 1
        elif cell != "-":
            raise ValueError("Use X, O or -")
    board.append(cells)
winners = ""
for player in "XO":
    won = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            won = True
        if board[0][i] == board[1][i] == board[2][i] == player:
            won = True
    if board[0][0] == board[1][1] == board[2][2] == player:
        won = True
    if board[0][2] == board[1][1] == board[2][0] == player:
        won = True
    if won:
        winners += player
if x_count not in (o_count, o_count + 1) or len(winners) == 2 or (winners == "X" and x_count != o_count + 1) or (winners == "O" and x_count != o_count):
    print("Invalid board")
elif winners:
    print(winners, "wins")
elif x_count + o_count == 9:
    print("Draw")
else:
    print("Incomplete")
