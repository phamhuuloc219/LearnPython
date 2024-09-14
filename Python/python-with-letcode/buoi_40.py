# board = [
#     ["X"," ","O"],
#     ["O","X","O"],
#     ["X"," ","X"],
# ]

# for row in board:
#     for element in row:
#         print(element, end=" ")
#     print()
# print(board[0][0])

# if board[1][1] == "X":
#     print("hang 2 cot 2 laf x")
# else:
#     print("hang 2 cot 2 khong phai x")


from guizero import App, PushButton, Text, Box
app = App(title="tic tac toe")

board = Box(app, layout="grid")


turn = "x"

def clear_board():
    new_board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    for x in range(3):
        for y in range(3):
            button = PushButton(board, text="", grid=[x,y], width=3, args=[x,y], command=choose_square)
            new_board[x][y] = button
    return new_board

def toggle_player():
    global turn
    if turn == "x":
        turn = "o"
    else: turn ="x"
    message.value = "Turn of " + turn

def choose_square(x,y):
    board_square[x][y].text = turn
    board_square[x][y].disable()
    toggle_player()
    
new_game = PushButton(app, text="New game", command=clear_board)
new_game.text_size = 28
new_game.text_color = "red"
message = Text(app,"Turn of, " + turn)
board_square = clear_board()
app.display()