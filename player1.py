import socket

import gameboard
from gameboard import BoardClass

RECV_SIZE = 1024
board = BoardClass("player2","player2","player2")

def get_host_info():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = "127.0.0.1"
        PORT = 8089
        # uncomment
        # HOST = input("Enter HOST name: ")
        # PORT = int(input("Enter PORT: "))
        return HOST, PORT
    except Exception as e:
        print(e)


def connect_to_player(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:

        try:
            print(f"Connecting to {host} : {port}")
            client_socket.connect((host, port))
            break
        except Exception as e:
            print(f"Connection error: {e}")
            retry = input("Do you want to try again? (y/n): ").lower()
            if retry != 'y':
                return None
            else:
                # If the user wants to retry, prompt for the host and port again
                host, port = get_host_info()


    return client_socket

def GetMove():
    #to be removed
    for i in range(3):
        for j in range(3):
            if (board[i][j]==" "):
                return (f"{i},{j}")

    move = input("Enter your move: ")
    XY = move.split(",")
    return (XY[0], XY[0])


""" def execute_move(player_socket):
    while True:
        try:
            player_move = input("Enter your move: ")
            XY = player_move.split(",")
            board.updateGameBoard(int(XY[0]), int(XY[1]), 'X')
            player_socket.send(player_move.encode())
            if board.isWinner():
                break
            if board.board_is_full():
                break
        except (gameboard.InvalidMoveError, ValueError):
            print("Invalid Move")
            pass
        else:
            break """

def play_game(player_socket: socket.socket):

   # player_name = input("Enter your username: ")
    player_name = "Player1"
    player_socket.send(player_name.encode())

    player2_username = player_socket.recv(RECV_SIZE).decode()
    print(f"Received player2 username: {player2_username}")

    while True:
        player_move = input("Enter your move: ")
        XY = player_move.split(",")
        board.updateGameBoard(int(XY[0]), int(XY[1]), 'X')
        player_socket.send(player_move.encode())
        if board.isWinner():
            break
        if board.board_is_full():
            break

        # Wait for player 2's move
        opponent_move = player_socket.recv(RECV_SIZE).decode()
        print(f"Player 2's move: {opponent_move}")
        XY = opponent_move.split(",")   
        board.updateGameBoard(int(XY[0]),int(XY[1]), 'O')
        if board.isWinner() or board.board_is_full():
            break

        # Check for game over condition
        # Implement your game logic here

def init_connection():
    while True:
        try:
            host, port = get_host_info()
            player_socket = connect_to_player(host, port)
            if (player_socket is None):
                break
        except Exception as e:
            print(e)
        else:
            return player_socket

def main():
    connection = init_connection()

    while True:
        play_game(connection)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if (play_again == 'y'):
            connection.send("Play Again".encode())
        elif play_again == 'n': 
            connection.send("Fun Times".encode())
            connection.close()
            break
        else:
            print("Not a (y/n)")

if __name__ == "__main__":
    main()
