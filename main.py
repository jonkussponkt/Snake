import random
import pygame
import Game


game = Game.Game()
game.game()
# pygame.init()   # DONE
# screen = pygame.display.set_mode((1000, 750))  # DONE
# pygame.display.set_caption("Snake")  # DONE
# box = pygame.Rect(10, 10, 25, 25)  # DONE
# apple_boxes = []  # DONE
# apple_box_color = (255, 125, 0)  # DONE
# snake = Snake()
# generate_apple = 0
# clock = pygame.time.Clock()
# delta = 0.0
# ticks_per_second = 100.0
# game = True
# while game:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit(0)
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             sys.exit(0)
#
#     delta += clock.tick()/5000.0
#     while delta > 1/ticks_per_second:
#         delta -= 1/ticks_per_second
#
#         tail = snake.positions[0]
#         head = snake.positions[len(snake.positions) - 1]
#
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
#             if head[0] <= 965:
#                 for i in snake.positions[:len(snake.positions)-1]:
#                     if head[0] == i[0] and head[1] == i[1] or head[0] == i[0]+25 and head[1] == i[0]+25:
#                         print("YOU LOST\n")
#                         game = False
#                         break
#                 snake.positions.append((head[0]+10, head[1]))
#                 for i in apple_boxes:
#                     if head[0] < i[0]+10 and head[0] + 25 > i[0] and head[1] < i[1] + 10 and head[1] + 25 > i[1]:  #  squares intersection
#                         apple_boxes.remove(i)
#                         snake.length += 1
#                         break
#                 else:
#                     snake.positions.pop(0)
#         if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0:
#             if head[0] > 10:
#                 # (aX < (bX + bLen) && (aX + aLen) > bX) && (aY < (bY - bLen) && (aY - aLen) > bY)
#                 for i in snake.positions[:len(snake.positions)-1]:
#                     if head[0] == i[0] and head[1] == i[1] or head[0] == i[0]+25 and head[1] == i[0]+25:
#                         print("YOU LOST\n")
#                         game = False
#                         break
#                 snake.positions.append((head[0] - 10, head[1]))
#                 for i in apple_boxes:
#                     if head[0] < i[0] + 10 and head[0] + 25 > i[0] and head[1] < i[1] + 10 and head[1] + 25 > i[1]:  # squares intersection
#                         apple_boxes.remove(i)
#                         snake.length += 1
#                         break
#                 else:
#                     snake.positions.pop(0)
#         if keys[pygame.K_UP] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_DOWN] == 0:
#             if head[1] > 10:
#                 for i in snake.positions[:len(snake.positions)-1]:
#                     if head[0] == i[0] and head[1] == i[1] or head[0] == i[0]+25 and head[1] == i[0]+25:
#                         print("YOU LOST\n")
#                         game = False
#                         break
#                 snake.positions.append((head[0], head[1]-10))
#                 for i in apple_boxes:
#                     if head[0] < i[0] + 10 and head[0] + 25 > i[0] and head[1] < i[1] + 10 and head[1] + 25 > i[1]:  # squares intersection
#                         apple_boxes.remove(i)
#                         snake.length += 1
#                         break
#                 else:
#                     snake.positions.pop(0)
#         if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0:
#             if head[1] <= 715:
#                 for i in snake.positions[:len(snake.positions)-1]:
#                     if head[0] == i[0] and head[1] == i[1] or head[0] == i[0]+25 and head[1] == i[0]+25:
#                         print("YOU LOST\n")
#                         game = False
#                         break
#                 snake.positions.append((head[0], head[1]+10))
#                 for i in apple_boxes:
#                     # (aX < (bX + bLen) && (aX + aLen) > bX) && (aY < (bY - bLen) && (aY - aLen) > bY)
#                     if head[0] < i[0] + 10 and head[0] + 25 > i[0] and head[1] < i[1] + 10 and head[1] + 25 > i[1]:  # squares intersection
#                         apple_boxes.remove(i)
#                         snake.length += 1
#                         break
#                 else:
#                     snake.positions.pop(0)
#
#     screen.fill((0, 0, 0))
#     for i in snake.positions:
#         pygame.draw.rect(screen, (0, 150, 255), pygame.Rect(i[0], i[1], 25, 25))
#     if generate_apple % 5000 == 0 or len(apple_boxes) == 0:
#         apple_x = random.randint(10, 965)
#         apple_y = random.randint(10, 715)
#         apple_x = round(apple_x / 10) * 10
#         apple_y = round(apple_y / 10) * 10
#
#         while (apple_x, apple_y) in apple_boxes:
#             apple_x = random.randint(10, 965)
#             apple_y = random.randint(10, 715)
#             apple_x = round(apple_x / 10) * 10
#             apple_y = round(apple_y / 10) * 10
#         apple_boxes.append((apple_x, apple_y))
#     generate_apple += 1
#     for i in apple_boxes:
#         pygame.draw.rect(screen, apple_box_color, pygame.Rect(i[0], i[1], 10, 10))
#     snake.your_score()
#     pygame.display.flip()
#
# while not pygame.key.get_pressed()[pygame.K_ESCAPE]:
#     font_style = pygame.font.SysFont("comicsansms", 35)
#     message_to_lost = font_style.render(f"You lost :( Press ESC to leave", True, (255, 0, 0))
#     screen.blit(message_to_lost, [450, 450])
#     pygame.display.flip()
# sys.exit(0)
