# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from IPython.display import clear_output

    print('Welcome to Tic Tac Toe!')


    def display_board(board):

        print(f" {board[7]}  | {board[8]}   | {board[9]}")
        print("--------------")
        print(f" {board[4]}  | {board[5]}   | {board[6]}")
        print("--------------")
        print(f" {board[1]}  | {board[2]}   | {board[3]}")


    def player_input():
        choice = 'WRONG'
        b = ['X', 'O']
        while choice != True:
            marker = input("Enter marker as 'X' or 'O': ").upper()
            if marker not in b:
                print("Sorry! Wrong input.  Kindly enter input as 'X' or 'O' ")
            else:
                choice = True
        return marker


    def player_position():
        choice = 'WRONG'
        c = list(range(1, 10))
        #         print(c)
        while choice != True:
            pos = input("Enter a position where you want to place: ")
            #             print(pos)
            if pos.isdigit() and int(pos) in c:
                choice = True
                break
            else:
                print("Sorry! Wrong input.")

        return int(pos)


    def place_marker(board, marker, position):
        board[position] = marker


    #     display_board(test_board)

    def win_check(board, mark):
        return ((board[1] == mark and board[2] == mark and board[3] == mark) or

                (board[4] == mark and board[5] == mark and board[6] == mark) or

                (board[7] == mark and board[8] == mark and board[9] == mark) or

                (board[1] == mark and board[4] == mark and board[7] == mark) or

                (board[2] == mark and board[5] == mark and board[8] == mark) or

                (board[3] == mark and board[6] == mark and board[9] == mark) or

                (board[1] == mark and board[5] == mark and board[9] == mark) or

                (board[3] == mark and board[5] == mark and board[7] == mark))


    def space_check(board, position):
        if board[position]:
            return False
        else:
            return True


    def full_board_check(board):
        for i, j in enumerate(board):
            if j:
                continue
            else:
                return False
        return True


    def replay():

        choice = 'WRONG'
        while choice != True:
            replay = input("Would you like to play again? Enter 'Y' or 'N': ").upper()
            if replay == 'Y':
                choice = True
                return True
            elif replay == 'N':
                choice = True
                return False
            else:
                print('Please enter a correct choice! ')


    board = ['#', '', '', '', '', '', '', '', '', '']
    display_board(board)


    def player_pick():
        player1 = ""
        player2 = ""
        game_on = True
        while game_on:
            print(" To decide player1 picks X or O")
            if player_input() == 'X':
                player1 = "X"
                player2 = "O"
                game_on = False
                print(f"Player1 is {player1} and Player2 is {player2}")
            else:
                player1 = "O"
                player2 = "X"
                game_on = False
                print(f"Player1 is {player1} and Player2 is {player2}")
        return (player1, player2)

    # pick player choice
    (player1, player2) = player_pick()
    turn = 1
    count = 0
    position = 0
    # until board is full, take position, check if its empty and fill accordingly turn wise
    while full_board_check(board) == False:

        if turn == 1:
            count += 1
            print(f"\n Player 1 turn: {player1}")
            position = player_position()
            if space_check(board, position):
                clear_output()
                place_marker(board, player1, position)
                display_board(board)
                turn = 2
                # check if any player has won
                if win_check(board, player1):
                    print(f"\n Player1:{player1} has Won !!!")
                    if replay():
                        board = ['#', '', '', '', '', '', '', '', '', '']
                        (player1, player2) = player_pick()
                        continue
                    else:
                        print("Game Over!!")
                        break
            # elif count == 9:
            #     print(f"count is {count}")
            #     print("Board is full and its a TIE!!!")
            #     break
            else:
                print("Position is already filled. Choose another position")
                turn = 1
                continue
        if turn == 2:
            if count == 9:
                print("Board is full and its a TIE!!!")
                break
            count += 1
            print(f" \n Player 2 turn: {player2}")
            position = player_position()
            if space_check(board, position):
                clear_output()
                place_marker(board, player2, position)
                display_board(board)
                turn = 1
                # check if any player has won
                if win_check(board, player2):
                    print(f"\n Player2:{player2} has Won !!")
                    if replay():
                        board = ['#', '', '', '', '', '', '', '', '', '']
                        (player1, player2) = player_pick()
                        continue
                    else:
                        print("Game Over!!")
                        break
            else:
                print("Position is already filled. Choose another position")
                turn = 2
                continue