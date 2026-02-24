# Simple File Transfer

**Description:**
A Python implementation of a Reliable Data Transfer (RDT) model that simulates sending and reconstructing an image file between a client and server. Demonstrates concepts such as packet corruption, maximum segment size and data integrity.

**Technologies Used:**
- Python 3.x

**Features:**
- Simulated packet corruption with configurable probability.
- Configurable maximum segment size (MSS) for packet transmission.
- Image reconstruction and flipping upon successful transfer.
- Client-server architecture for data transmission.

**How to Run:**
1. Open two command line windows.
2. Navigate to the Simple File Transfer folder in both windows.
3. Start the server in the first window:
```bash
python3 server.py [PORT] [CORRUPTION_PROBABILITY] [MSS]
```
4. Start the client in the second window using the same arguments:
```bash
python3 client.py [PORT] [CORRUPTION_PROBABILITY] [MSS]
```
- `PORT`: An integer port number (e.g. 9000)
- `CORRUPTION_PROBABILITY`: A float between 0 and 1 (e.g. 0.1)
- `MSS`: Maximum message length for a packet (e.g. 512)

5. The scripts will begin sending and receiving data. The server will reconstruct and flip the image upon completion.
