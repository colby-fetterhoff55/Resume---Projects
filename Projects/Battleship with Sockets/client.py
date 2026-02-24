import sys
import socket


BOARD_SIZE = 6


if len(sys.argv) != 2:
    print("Usage: python client.py [PORT_NUMBER]")
    sys.exit(1)


try:
    port = int(sys.argv[1])
except ValueError:
    print("Port must be an integer.")
    sys.exit(1)


display = [['?' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
guess_count = 0


def print_board():
    print("   " + " ".join(str(c+1) for c in range(BOARD_SIZE)))
    for r in range(BOARD_SIZE):
        print(f"{r+1:2} " + " ".join(display[r][c] for c in range(BOARD_SIZE)))
    print()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', port))
    print(f"Connected to server on port {port}.\n")
    print("----Welcome to Battleship with Sockets!----")
    print("Your goal is to sink all ships on the board.")
    print("You need to sink:")
    print("1 length 4 ship.")
    print("1 length 3 ship.")
    print("1 length 2 ship.\n")

    while True:
        print_board()


        try:
            row_input = input("Enter row number (1-6, or q to quit): ").strip()
            if row_input.lower() in ('q', 'quit', 'exit'):
                print("Quitting.")
                sys.exit(0)
            row = int(row_input)
        except ValueError:
            print("Invalid row number.")
            continue


        try:
            col_input = input("Enter column number (1-6, or q to quit): ").strip()
            if col_input.lower() in ('q', 'quit', 'exit'):
                print("Quitting.")
                sys.exit(0)
            col = int(col_input)
        except ValueError:
            print("Invalid column number.")
            continue


        if not (1 <= row <= BOARD_SIZE and 1 <= col <= BOARD_SIZE):
            print("Numbers must be between 1 and 6.")
            continue


        if display[row-1][col-1] in ('X', 'O'):
            print("You already guessed that spot.")
            continue


        message = f"{row} {col}\n"
        s.sendall(message.encode())


        data = b''
        while not data.endswith(b'\n'):
            packet = s.recv(1024)
            if not packet:
                print("Server closed connection.")
                sys.exit(0)
            data += packet


        reply = data.decode().strip()
        parts = reply.split('|')
        result = parts[0]
        status = parts[1] if len(parts) > 1 else "CONTINUE"
        guess_count += 1


        if result == "Hit":
            display[row-1][col-1] = 'X'
            print(f"HIT! Total guesses: {guess_count}")
        else:
            display[row-1][col-1] = 'O'
            print(f"MISS. Total guesses: {guess_count}")


        if status == "WIN":
            print("\n*** All ships sunk! ***")
            print_board()
            print(f"You won in {guess_count} guesses.")
            sys.exit(0)
