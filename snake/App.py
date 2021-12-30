import pygame
import random
from pygame import mixer
pygame.mixer.init()

mixer.music.load("background.wav")
mixer.music.play(-1)

class Snake:
    def __init__(self, num, X, Y, sX, sY):
        self.sX = sX
        self.sY = sY
        self.cells = []
        self.direction = "RIGHT"
        self.slower = 0
        self.score=0
        self.time=(0,0)

        self.suterfoodex=False
        cX, cY = X, Y
        temp = SnakeCell(0, 0, 'skin.jpg')
        self.imgsz = temp.img.get_rect().size[1]
        for i in range(num):
            self.cells.append((cX, cY))
            cX += 35 + sX

        self.food = Food(random.randint(100, 1000), random.randint(100, 600),'ramen.png',0.1)

    def update(self):
        punch_sound = mixer.Sound('punch.wav')

        if self.cells[len(self.cells) - 1][0] + self.imgsz > 1200 or self.cells[len(self.cells) - 1][0] < 0 or \
        self.cells[len(self.cells) - 1][1] + self.imgsz > 700 or self.cells[len(self.cells) - 1][1] < 0:

                punch_sound.play()


                if self.time[1]%4==0:

                    return False
        # When it collides to itself
        for i in range(0, len(self.cells) - 3):
            if self.cells[len(self.cells) - 1][0] < self.cells[i][0] + self.imgsz and self.cells[len(self.cells) - 1][
                0] + self.imgsz > self.cells[i][0] \
                    and self.cells[len(self.cells) - 1][1] < self.cells[i][1] + self.imgsz and \
                    self.cells[len(self.cells) - 1][1] + self.imgsz > self.cells[i][1]:
                punch_sound.play()
                if self.time[1] % 2== 0:
                    punch_sound.play()
                    return False
        #     When it collides to menu line
        if (self.cells[len(self.cells) - 1][0] + self.imgsz >= 400 and self.cells[len(self.cells) - 1][0] < 875 and
            self.cells[len(self.cells) - 1][1] < 90) \
                or (self.cells[len(self.cells) - 1][1] + self.imgsz > 0 and self.cells[len(self.cells) - 1][
            1] + self.imgsz < 90 and (
                            self.cells[len(self.cells) - 1][0] > 400 or self.cells[len(self.cells) - 1][0] < 875)):
            punch_sound.play()
            if self.time[1] % 2== 0:
                punch_sound.play()
                return False
        # Eating food

        # ordinary food
        else:
            if self.cells[len(self.cells) - 1][0]+self.imgsz/2  in range(self.food.x, self.food.x + self.food.img.get_rect().size[0]) and\
                self.cells[len(self.cells) - 1][1]+self.imgsz/2 in range(self.food.y, self.food.y + self.food.img.get_rect().size[1]):
                if self.time[0]!=0 and self.time[0]%2==0 and self.time[1] in range(20,40):
                    self.food = Food(random.randint(100, 1000), random.randint(100, 600), 'superfood.png',0.15)
                    slurp_sound = mixer.Sound('superfood.wav')
                    slurp_sound.play()
                    self.score += 2
                else:
                    if self.direction == "DOWN":
                        self.cells.append(
                            (self.cells[len(self.cells) - 1][0], self.cells[len(self.cells) - 1][1] + self.imgsz + 1))
                    if self.direction == "UP":
                        self.cells.append(
                            (self.cells[len(self.cells) - 1][0], self.cells[len(self.cells) - 1][1] - self.imgsz + 1))
                    if self.direction == "RIGHT":
                        self.cells.append(
                            (self.cells[len(self.cells) - 1][0] + self.imgsz + 1, self.cells[len(self.cells) - 1][1]))
                    if self.direction == "RIGHT":
                        self.cells.append(
                            (self.cells[len(self.cells) - 1][0] - self.imgsz + 1, self.cells[len(self.cells) - 1][1]))
                    self.food = Food(random.randint(100, 1000), random.randint(100, 600), 'ramen.png',0.1)
                    slurp_sound = mixer.Sound('slurp.mp3')
                    slurp_sound.play()
                    self.score += 1



        self.slower = self.slower+1

        step=3
        if self.direction == "DOWN":

            if self.slower==step:
                if self.time[1] == 60:
                    self.time = (self.time[0] + 1, 0)
                else:
                    self.time = (self.time[0], self.time[1] + 1)
                self.cells.remove(self.cells[0])
                self.cells.append((self.cells[len(self.cells) - 1][0], self.cells[len(self.cells) - 1][1] + self.imgsz))
                self.slower=0
        elif self.direction == "UP":

            if self.slower == step:
                if self.time[1] == 60:
                    self.time = (self.time[0] + 1, 0)
                else:
                    self.time = (self.time[0], self.time[1] + 1)
                self.cells.remove(self.cells[0])
                self.cells.append((self.cells[len(self.cells) - 1][0], self.cells[len(self.cells) - 1][1] - self.imgsz))
                self.slower = 0
        elif self.direction == "RIGHT":

            if self.slower == step:
                if self.time[1] == 60:
                    self.time = (self.time[0] + 1, 0)
                else:
                    self.time = (self.time[0], self.time[1] + 1)
                self.cells.remove(self.cells[0])
                self.cells.append((self.cells[len(self.cells) - 1][0] + self.imgsz, self.cells[len(self.cells) - 1][1]))
                self.slower = 0
        elif  self.direction == "LEFT":

            if self.slower == step:
                if self.time[1] == 60:
                    self.time = (self.time[0] + 1, 0)
                else:
                    self.time = (self.time[0], self.time[1] + 1)
                self.cells.remove(self.cells[0])
                self.cells.append((self.cells[len(self.cells) - 1][0] - self.imgsz, self.cells[len(self.cells) - 1][1]))
                self.slower = 0
        punch_sound = mixer.Sound('punch.wav')


    def render(self, screen):
        for x, y in self.cells:
            snakecell = SnakeCell(x, y, 'skin.jpg')
            snakecell.render(screen)
        self.drawText(screen)


    # background music

    def drawText(self,screen):
        # Font
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 30)

        # Drawing Text
        screen.blit(font.render('Snake Game Score:{}, Elapsed time: {}:{}'.format(self.score,self.time[0],self.time[1]), False, pygame.Color("White")), (380, 10))
        screen.blit(font.render('_________________________', False, pygame.Color("White")), (400, 20))
        # screen.blit(font.render('.', False, pygame.Color("Yellow")), (875, 30))

class SnakeCell:
    def __init__(self, x, y, cellname):
        self.X = x
        self.Y = y
        self.cellname = cellname
        self.img = pygame.image.load(cellname).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, 0.1)

    def render(self, screen):

        w, h = self.img.get_rect().size
        screen.blit(self.img, (self.X - w / 2, self.Y - h / 2))


class Food:
    def __init__(self, x, y,imgname,size):
        self.x = x
        self.y = y
        self.imgname=imgname

        self.img = pygame.image.load(imgname).convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, size)

    def render(self, screen):
        w, h = self.img.get_rect().size
        screen.blit(self.img, (self.x - w / 2, self.y - h / 2))


class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.snake = None


    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Snake")


        self.background = pygame.image.load('galaxy.jpeg').convert_alpha(self.screen)
        WIDTH = 1280
        HEIGHT = 800
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self.snake = Snake(5, 250, 200, 5, 5)

        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        self.events()

        if self.snake.update() == False:
            self.running = False
        self.snake.update()

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.snake.direction != 'RIGHT':
                self.snake.direction = "LEFT"
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.snake.direction != 'DOWN':
                self.snake.direction = "UP"
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.snake.direction != 'UP':
                self.snake.direction = "DOWN"
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.snake.direction != 'LEFT':
                self.snake.direction = "RIGHT"

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.snake.food.render(self.screen)
        self.snake.render(self.screen)

        self.clock.tick(30)
        pygame.display.flip()

    def cleanUp(self):
        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()