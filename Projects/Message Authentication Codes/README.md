# Message Authentication Codes

**Description:**
A Python client-server application demonstrating encrypted messaging and MAC-based authentication. The server verifies incoming messages by comparing MAC hashes with a 50% chance each packet will be intentionally corrupted. This is to simulate real-world network conditions.

**Technologies Used:**
- Python 3.x

**Features:**
- Encrypted messaging between client and server.
- MAC-based authentication to verify message integrity.
- Simulated 50% packet corruption to demonstrate authentication failure handling.
- Server accepts or rejects messages based on MAC hash comparison.

**How to Run:**
1. Open two command line windows.
2. Navigate to the Message Authentication Codes folder in both windows.
3. Start the server in the first window:
```bash
python server.py
```
4. Start the client in the second window:
```bash
python client.py
```
5. Enter messages in the client window to send encrypted data and MAC values.
6. The server will decrypt each message, compute its own MAC, and accept or reject based on whether the hashes match.
