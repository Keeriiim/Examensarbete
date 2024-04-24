import asyncio
import websockets
from menuHandler import Menu

menu = Menu()
'''
async def handle_client(websocket):
    print(f"Accepted connection from {websocket.remote_address}")
    await websocket.send("Welcome to the server!") # Send a welcome message to the client
    try:
        while True:

            # Send the word "candy" to the client
            await websocket.send()

            # Receive the client's response
            response = await websocket.recv()
            print(f"Received response from {websocket.remote_address}: {response}")

            # Check if the client wants to close the connection
            if response.strip().lower() == "close":
                break

    except Exception as e:
        print(f"An error occurred: {e}")




    finally:
        # Close the WebSocket connection
        print(f"Closing connection with {websocket.remote_address}")
        await websocket.close()


async def main():
    # Start the WebSocket server
    async with websockets.serve(handle_client, "localhost", 8888):
        print("WebSocket server started")
        # Keep the server running indefinitely
        await asyncio.Future()  # This line keeps the event loop running


if __name__ == "__main__":
    asyncio.run(main())
    '''
