from Structure import Structure
import pygame


class Snake:

    def __init__(self):
        self.positions = Structure()
        self.length = 1
        self.positions.push_back((10, 45))
        self.segment = pygame.Rect(10, 10, 25, 25)

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def collide(self, head):
        for i in self.positions[:self.positions.get_size() - 1]:
            if head[0] == i[0] and head[1] == i[1] or head[0] == i[0] + 25 and head[1] == i[0] + 25:
                print("YOU LOST\n")
                return True
        return False
