# Battleship with Sockets

**Description:**
A single-player Battleship game implemented in Python using client-server socket communication. One player acts as the server and the other as the client, taking turns guessing ship locations until all ships are sunk.

**Technologies Used:**
- Python 3.x

**Features:**
- Single-player gameplay over a network using sockets.
- Separate client and server scripts for each player.
- Configurable port number for connection.
- Game continues until all ships are sunk.

**How to Run:**
1. Open two command line windows.
2. Navigate to the Battleship with Sockets folder in both windows.
3. Start the server in the first window:
```bash
python server.py 9000
```
4. Start the client in the second window:
```bash
python client.py 9000
```
5. You can replace `9000` with any free port on your computer, but make sure both windows use the same port number.
6. Play the game until all ships are sunk!

