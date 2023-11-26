import asyncio
import pickle
import random

class Player:
    def __init__(self, character, transport):
        self.character = character
        self.x = 50
        self.y = 50
        self.transport = transport

class ClientHandler:
    def __init__(self, server, transport):
        self.server = server
        self.transport = transport

    def data_received(self, data):
        message = pickle.loads(data)
        self.server.update_world(self, message)

    def connection_lost(self, exc):
        self.server.remove_player(self)

class GameServer:
    def __init__(self):
        self.players = {}

    async def handle_client(self, reader, writer):
        handler = ClientHandler(self, writer)
        character = "George" if len(self.players) % 2 == 0 else "Thunder"
        player = Player(character, writer)
        self.players[handler] = player
        player_info = pickle.dumps(["id update", character])
        writer.write(player_info)

        while True:
            data = await reader.read(100)
            if not data:
                break
            handler.data_received(data)

        handler.connection_lost(None)

    def update_world(self, handler, data):
        print(f"Received data from client: {data}")
        player = self.players.get(handler)
        if not player:
            return

        # Update player position based on received data
        if data[0] == "position update":
            _, x, y = data
            player.x, player.y = x, y
            self.broadcast_positions()

    def broadcast_positions(self):
        update = ["player locations"]
        for player in self.players.values():
            update.append([player.character, player.x, player.y])

        print(f"Broadcasting positions: {update}")

        for handler in self.players:
            try:
                handler.transport.write(pickle.dumps(update))
            except Exception as e:
                print(f"Error sending update: {e}")


    def remove_player(self, handler):
        if handler in self.players:
            del self.players[handler]

async def main(host, port):
    server = GameServer()
    server_coro = await asyncio.start_server(
        server.handle_client, host, port)
    await server_coro.serve_forever()

if __name__ == "__main__":
    asyncio.run(main("134.87.42.233", 54321))
