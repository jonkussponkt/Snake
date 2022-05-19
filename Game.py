import Snake
import pygame
import random
import sys


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 750))
        pygame.display.set_caption("Snake")
        self.apple_boxes = []
        self.apple_box_color = (255, 125, 0)
        self.snake = Snake.Snake()

    def display_score(self):
        score_font = pygame.font.SysFont("comicsansms", 30)
        string = score_font.render("Length of Snake:" + str(self.snake.length), True, (170, 255, 0))
        self.screen.blit(string, [0, 0])

    def is_apple_eaten(self, head):
        for i in self.apple_boxes:
            if head[0] < i[0] + 10 and head[0] + 25 > i[0] and head[1] < i[1] + 10 and head[1] + 25 > i[1]:  # squares intersects
                self.apple_boxes.remove(i)
                return True
        return False

    @staticmethod
    def generate_apple(x, y):
        apple_x = random.randint(10, x)
        apple_y = random.randint(45, y)
        apple_x = round(apple_x / 10) * 10
        apple_y = round(apple_y / 10) * 10
        return apple_x, apple_y

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

    def game(self):
        generate_apple = 0
        clock = pygame.time.Clock()
        delta = 0.0
        ticks_per_second = 100.0
        game_lasts = True
        while game_lasts:
            self.handle_events()
            delta += clock.tick() / 5000.0
            while delta > 1 / ticks_per_second:
                delta -= 1 / ticks_per_second

                head = self.snake.positions.back()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
                    if head[0] <= 965:
                        if self.snake.collide(head):
                            game_lasts = False
                            break
                        self.snake.positions.push_back((head[0] + 10, head[1]))
                        if self.is_apple_eaten(head):
                            self.snake.length += 1
                        else:
                            self.snake.positions.pop_front()
                if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
                    if head[0] > 10:
                        # (aX < (bX + bLen) && (aX + aLen) > bX) && (aY < (bY - bLen) && (aY - aLen) > bY)
                        if self.snake.collide(head):
                            game_lasts = False
                            break
                        self.snake.positions.push_back((head[0] - 10, head[1]))
                        if self.is_apple_eaten(head):
                            self.snake.length += 1
                        else:
                            self.snake.positions.pop_front()
                if keys[pygame.K_UP] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_DOWN] == 0:
                    if head[1] > 45:
                        if self.snake.collide(head):
                            game_lasts = False
                            break
                        self.snake.positions.push_back((head[0], head[1] - 10))
                        if self.is_apple_eaten(head):
                            self.snake.length += 1
                        else:
                            self.snake.positions.pop_front()
                if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0:
                    if head[1] <= 715:
                        if self.snake.collide(head):
                            game_lasts = False
                            break
                        self.snake.positions.push_back((head[0], head[1] + 10))
                        if self.is_apple_eaten(head):
                            self.snake.length += 1
                        else:
                            self.snake.positions.pop_front()

            self.screen.fill((0, 0, 0))
            for i in self.snake.positions:
                pygame.draw.rect(self.screen, (0, 150, 255), pygame.Rect(i[0], i[1], 25, 25))
            if generate_apple % 5000 == 0 or len(self.apple_boxes) == 0:
                apple_x, apple_y = self.generate_apple(965, 715)
                while (apple_x, apple_y) in self.apple_boxes:
                    apple_x, apple_y = self.generate_apple(965, 715)
                self.apple_boxes.append((apple_x, apple_y))
            generate_apple += 1
            for i in self.apple_boxes:
                pygame.draw.rect(self.screen, self.apple_box_color, pygame.Rect(i[0], i[1], 10, 10))
            self.display_score()
            pygame.display.flip()
        self.goodbye_window()
        sys.exit(0)

    def goodbye_window(self):
        self.screen.fill((50, 50, 150))
        keys = pygame.key.get_pressed()
        while keys[pygame.K_ESCAPE] == 0:
            self.handle_events()
            font_style = pygame.font.SysFont("comicsansms", 35)
            message_to_lost = font_style.render(f"You lost :( Press ESC to leave", True, (255, 0, 0))
            self.screen.blit(message_to_lost, [350, 315])
            pygame.display.flip()
