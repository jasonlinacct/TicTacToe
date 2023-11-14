import socket
from gameboard import BoardClass

RECV_SIZE = 1024
gameBoard = BoardClass("player2","player2","player2")

def accept_connection():
    #establish a connection
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = "127.0.0.1"
        PORT = 8089
        # uncomment
        # HOST = input("Enter HOST name: ")
        # PORT = int(input("Enter PORT: "))
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print("Waiting for a connection from Player 1...")
        connection, address = server_socket.accept()

        #play_game(connection)

    except Exception as e:
        print(f"An connection error occured: {e}")

    return connection


def GetMove():
    #to be removed
    for i in range(3):
        for j in range(3):
            if (gameBoard.board[i][j]==" "):
                return (f"{i},{j}")

    move = input("Enter your move: ")
    XY = move.split(",")
    return (XY[0], XY[0])

def play_game(player_socket: socket.socket) -> None:
    """
    Play a game with another player over the provided socket.

    Parameters:
    - player_socket (socket.socket): The socket for communication with the other player.

    Returns:
    None
    """
    RECV_SIZE = 1024
    try:
        # Wait for Player 1's username
        player1_username = player_socket.recv(RECV_SIZE).decode()
        print(f"Received Player 1's username: {player1_username}")

        # Send Player 2's username to Player 1
        player_socket.send("player2".encode())

        while True:
            # Wait for Player 1's move
            player1_move = player_socket.recv(RECV_SIZE).decode()
            print(f"Player 1's move: {player1_move}")
            XY = player1_move.split(",")
            gameBoard.updateGameBoard(int(XY[0]), int(XY[1]),  'X')
            gameBoard.print_board()
            if gameBoard.isWinner() is True:
                break

            # Get Player 2's move
            player2_move = GetMove()            
            player_socket.send(player2_move.encode())
            XY = player2_move.split(",")
            gameBoard.updateGameBoard(int(XY[0]), int(XY[1]),  'O')
            print(f"Player 2's move: {player2_move}")
            gameBoard.print_board()
            if gameBoard.isWinner() is True:
                break
            # Check for game over condition
            # Implement your game logic here
            #then break out of the loop
    except Exception as e:
        print(f"An error occurred during the game: {e}")

def main():
    connection = accept_connection()
    while True:

        play_game(connection)

        #add (if game logic checks to see if the game end then do this)
        try:
            play_again = connection.recv(RECV_SIZE).decode()

            if play_again != 'Play Again':
                gameBoard.print_stats()
                break

        except Exception as e:
            print(e)

    connection.close()

if __name__ == "__main__":
    main()
