# 3. WebSocket Client (Python)
# Now, let's create a Python WebSocket client to send and receive messages. (File: client.py)

# How it works:
# - Connects to ws://localhost:8000/ws
# - Sends messages typed by the user
# Receives and prints responses from the server.

import asyncio
import websockets

async def connect():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter message: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Server says: {response}")

if __name__ == "__main__":
    asyncio.run(connect())
