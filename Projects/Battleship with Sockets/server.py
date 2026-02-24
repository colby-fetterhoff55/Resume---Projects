import sys
import socket
import random


BOARD_SIZE = 6
SHIP_LENGTHS = [4, 3, 2]


if len(sys.argv) != 2:
    print("Usage: python server.py [PORT_NUMBER]")
    sys.exit(1)


try:
    port = int(sys.argv[1])
except ValueError:
    print("Port must be an integer.")
    sys.exit(1)


board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


for length in SHIP_LENGTHS:
    placed = False
    while not placed:
        orientation = random.choice(['H', 'V'])
        if orientation == 'H':
            row = random.randrange(BOARD_SIZE)
            col = random.randrange(BOARD_SIZE - length + 1)
            if any(board[row][col + i] == 1 for i in range(length)):
                continue
            for i in range(length):
                board[row][col + i] = 1
            placed = True
        else:
            row = random.randrange(BOARD_SIZE - length + 1)
            col = random.randrange(BOARD_SIZE)
            if any(board[row + i][col] == 1 for i in range(length)):
                continue
            for i in range(length):
                board[row + i][col] = 1
            placed = True


remaining = sum(cell == 1 for row in board for cell in row)
hits = set()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(1)
    print(f"Server listening on port {port}...")


    conn, addr = s.accept()
    print(f"Connected by {addr}")


    with conn:
        while True:
            data = b''
            while not data.endswith(b'\n'):
                packet = conn.recv(1024)
                if not packet:
                    print("Client disconnected.")
                    sys.exit(0)
                data += packet


            text = data.decode().strip()
            parts = text.replace(',', ' ').split()
            if len(parts) < 2:
                conn.sendall(b"Miss|CONTINUE\n")
                continue


            try:
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
            except ValueError:
                conn.sendall(b"Miss|CONTINUE\n")
                continue


            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                conn.sendall(b"Miss|CONTINUE\n")
                continue


            if board[row][col] == 1:
                if (row, col) not in hits:
                    hits.add((row, col))
                    remaining -= 1
                if remaining == 0:
                    conn.sendall(b"Hit|WIN\n")
                    print("All ships sunk. Closing.")
                    sys.exit(0)
                else:
                    conn.sendall(b"Hit|CONTINUE\n")
            else:
                conn.sendall(b"Miss|CONTINUE\n")
