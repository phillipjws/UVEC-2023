import asyncio
import pygame
import sys
import scenes
from characters.thunder_the_viking import Thunder
from characters.george_the_peacock import George
import pickle

frame = 50
clock = pygame.time.Clock()

class DoNotMissFinal:
    def __init__(self):
        pygame.init()

        # Initialize player sprites
        self.player = None
        self.other_players = {}

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Don't let Thunder miss the final!")
        self.clock = pygame.time.Clock()
        self.running_scene = scenes.starting_scene()

        # Network setup
        self.loop = asyncio.get_event_loop()
        # self.loop.run_until_complete(self.connect_to_server("127.0.0.1", 54321))

    async def connect_to_server(self, host, port):
        self.reader, self.writer = await asyncio.open_connection(host, port)
        print("Connected to server.")

    async def handle_server_messages(self):
        while True:
            data = await self.reader.read(2048)
            if data:
                message = pickle.loads(data)
                self.process_server_message(message)

    def process_server_message(self, message):
        # print(f"Message received from server: {message}")
        if message[0] == 'id update':
            character = message[1]
            self.player = Thunder(320, 240, 0, 0) if character == "Thunder" else George(320, 240, 0, 0)
        elif message[0] == 'player locations':
            self.update_other_players(message[1:])

    def update_other_players(self, player_data):
        for character, x, y in player_data:
            # print(f"Updating player {character} to position ({x}, {y})")
            if character != self.player.character:
                if character not in self.other_players:
                    self.other_players[character] = George(x, y, 0, 0) if character == "George" else Thunder(x, y, 0, 0)
                else:
                    self.other_players[character].position = (x, y)

    async def run(self):
        asyncio.create_task(self.handle_server_messages())

        while self.running_scene is not None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Handle keyboard input for player movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif event.key == pygame.K_UP:
                        self.player.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down()
                    elif event.key == pygame.K_a:
                        self.player2.move_left()
                    elif event.key == pygame.K_d:
                        self.player2.move_right()
                    elif event.key == pygame.K_w:
                        self.player2.move_up()
                    elif event.key == pygame.K_s:
                        self.player2.move_down()

            if self.player:
                self.player.update()
                update = ['position update', self.player.position[0], self.player.position[1]]
                self.send_to_server(update)

            # Update the display
            self.screen.fill((0, 0, 0))  # Clear the screen with black color
            if self.player:
                self.screen.blit(self.player.image, self.player.position)
            for player in self.other_players.values():
                self.screen.blit(player.image, player.position)
            pygame.display.flip()

            clock.tick(frame)
            await asyncio.sleep(0)

    def send_to_server(self, message):
        # print(f"Sending to server: {message}")
        if self.writer is not None:
            self.writer.write(pickle.dumps(message))
            asyncio.create_task(self.writer.drain())

async def main():
    game = DoNotMissFinal()
    await game.connect_to_server("134.87.42.233", 54321)  # Connect to server here
    await game.run()

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()