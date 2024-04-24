import asyncio
import websockets
import menuHandler as Menu
class Server:

    SERVER_MESSAGE = ""


    def __init__(self):
        self.initialize()
        self.menu = Menu

    async def initialize(self):
        # Start the WebSocket server
        async with websockets.serve(self.handle_client, "localhost", 8888):
            print("WebSocket server started")
            # Keep the server running indefinitely
            await asyncio.Future()  # This line keeps the event loop running

    async def handle_client(self, websocket, path):
        print(f"Accepted connection from {websocket.remote_address}")
        await websocket.send("Welcome to the server!")  # Send a welcome message to the client
        await self.menu.dq
        try:
            while True:

                # Send the word "candy" to the client
                await websocket.send(self.SERVER_MESSAGE)

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



    async def inputHandler(self, input):
        self.SERVER_MESSAGE = input


