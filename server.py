# 1. Install Dependencies - Install FastAPI and websockets: pip install fastapi uvicorn websockets
# 2. WebSocket Server (FastAPI) - Create a WebSocket server using FastAPI that listens for incoming messages and responds to clients in real time. (File: server.py)

# How it works:
# - Starts a FastAPI WebSocket server on ws://localhost:8000/ws
# - Accepts WebSocket connections.
# - Listens for messages and sends responses back to the client.

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def get():
    return HTMLResponse("<h2>WebSocket Server Running</h2>")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")
    
    try:
        while True:
            message = await websocket.receive_text()
            print(f"Received: {message}")
            await websocket.send_text(f"Server received: {message}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
