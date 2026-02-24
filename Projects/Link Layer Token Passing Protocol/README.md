# Link Layer Token Passing Protocol

**Description:**
A Python simulation of a token-passing network protocol across five nodes. Only the node currently holding the token can transmit packets and each node has a 25% chance to add a new packet after sending or passing the token.

**Technologies Used:**
- Python 3.x

**Features:**
- Five-node token-passing network simulation.
- Configurable send and receive ports for each node.
- Only the token-holding node can transmit packets.
- Each node has a 25% chance to add a new packet after sending or passing the token.

**How to Run:**
1. Open five command line windows.
2. Navigate to the Link Layer Token Passing Protocol folder in each window.
3. Run the following commands, starting with windows 2–5 first, then window 1 last:
```bash
python node.py 8082 8081 3 0 2
python node.py 8083 8082 4 0 3
python node.py 8084 8083 2 0 4
python node.py 8085 8084 1 0 5
python node.py 8081 8085 5 1 1
```
4. Each node's send port should match the next node's receive port.
5. Node 1 starts with the token.
6. Use `Ctrl + C` to stop the program in each terminal when finished.
