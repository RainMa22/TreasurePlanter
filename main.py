import pygame

from game.Game import Game


def collidesWith(player1, player2):
    return (player1.x < player2.x + player2.width and
            player1.x + player1.width > player2.x and
            player1.y < player2.y + player2.height and
            player1.y + player1.height > player2.y)


def circumvent(player, item, speed):
    if speed < 1: return
    if player.x + player.width - speed < item.x:
        player.x = item.x - player.width
    elif player.x > item.x + item.width - speed:
        player.x = item.x + item.width
    if player.y + player.height - speed < item.y:
        player.y = item.y - player.height
    elif player.y > item.y + item.height - speed:
        player.y = item.y + item.height
    circumvent(player, item, int(speed / 2))



pygame.init()
screen = pygame.display.set_mode([1280, 720], pygame.HWACCEL | pygame.FULLSCREEN | pygame.SCALED)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    games = {
        "game": Game()
    }
    FPS = 60
    clock = pygame.time.Clock()
    # Set up the drawing window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        games.get("game").main(screen)
        pygame.display.flip()
        clock.tick(FPS)
