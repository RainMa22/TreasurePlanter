import pygame

import game
from game import Batch
from game.objects import Object
from game.Utils import generate


class Game:
    def __init__(self):
        from main import collidesWith, circumvent, screen
        self.grid = []
        for i in range(int(screen.get_width() / 16)):
            self.grid.append([])
            for j in range(int(screen.get_width() / 16)):
                self.grid[i].append(0)
        self.collidesWith = collidesWith
        self.circumvent = circumvent
        self.screen = screen
        self.speed = 2
        self.movements = [False, False, False, False]
        self.plants = []
        self.player = Object(8, 8, 16, 16)
        self.list = generate(90, screen.get_size())

    def make_move(self, player, normal=True, speed=2):
        if speed == 1:
            normal = 1 if normal else -1
            speedx = 0
            speedy = 0
            if self.movements[0]:
                speedy -= speed
            if self.movements[1]:
                speedx -= speed
            if self.movements[2]:
                speedy += speed
            if self.movements[3]:
                speedx += speed
            speedx *= normal
            speedy *= normal
            player.x += speedx
            player.y += speedy
        else:
            for i in range(speed):
                self.make_move(player, normal, i)

    def main(self, screen):
        keys = pygame.key.get_pressed()
        self.movements[0] = keys[pygame.K_w]
        self.movements[1] = keys[pygame.K_a]
        self.movements[2] = keys[pygame.K_s]
        self.movements[3] = keys[pygame.K_d]
        # Fill the background with white
        screen.fill((255, 222, 112))
        for item in self.list:
            Batch.draw_rect(screen, item)
            collide = self.collidesWith(self.player, item)
            if collide: self.circumvent(self.player, item, self.speed)
        plant_collides = False
        for plant in self.plants:
            plant.act()
            Batch.draw_rect(screen, plant)
            Batch.draw_text(screen, (plant.x, plant.y), f'{plant.frames / 60:.0f}s')
            plant_collides = plant_collides or self.collidesWith(self.player, plant)
        if keys[pygame.K_e] and not plant_collides:
            plant = game.objects.Plant(self.player.x, self.player.y, self.player.width, self.player.height,
                                       (255, 0, 0))
            self.plants.append(plant)
        Batch.draw_rect(screen, self.player)
        self.make_move(self.player)
