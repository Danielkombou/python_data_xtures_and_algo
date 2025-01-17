import pygame
import sys
import random

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load game sound
score_sound = pygame.mixer.Sound("Project_II/sound/wow.mp3")
collision_sound = pygame.mixer.Sound("Project_II/sound/hit.mp3")
# background music
pygame.mixer.music.load("Project_II/sound/play.mp3")

# Global variables
screen_height = 600
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))


Running = [
    pygame.image.load("Project_II/images/DinoRun1.png"),
    pygame.image.load("Project_II/images/DinoRun2.png"),
]
Ducking = [
    pygame.image.load("Project_II/images/DinoDuck1.png"),
    pygame.image.load("Project_II/images/DinoDuck2.png"),
]
Jumping = pygame.image.load("Project_II/images/DinoJump.png")
Small_Cactus = [
    pygame.image.load("Project_II/images/SmallCactus1.png"),
    pygame.image.load("Project_II/images/SmallCactus2.png"),
    pygame.image.load("Project_II/images/SmallCactus3.png"),
]
Large_Cactus = [
    pygame.image.load("Project_II/images/LargeCactus1.png"),
    pygame.image.load("Project_II/images/LargeCactus2.png"),
    pygame.image.load("Project_II/images/LargeCactus3.png"),
]
Bird = [
    pygame.image.load("Project_II/images/Bird1.png"),
    pygame.image.load("Project_II/images/Bird2.png"),
]
cloud = pygame.image.load("Project_II/images/Cloud.png")
Bg = pygame.image.load("Project_II/images/Track.png")


# Dinosaur class
class Dinosaur:
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    Jump_Vel = 8.5

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.jump_img = Jumping

        self.dino_duck = False
        self.dino_jump = False
        self.dino_run = True

        self.step_index = 0
        self.image = self.run_img[0]
        self.jump_vel = self.Jump_Vel
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()
        if self.dino_run:
            self.run()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_jump = False
            self.dino_run = True

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.Jump_Vel:
            self.dino_jump = False
            self.jump_vel = self.Jump_Vel

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = screen_width + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = cloud
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Obstacle:
    """Response to upcoming upstacles"""

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Birds(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud_pic = Cloud()
    game_speed = 10
    x_pos_bg = 0
    y_pos_bg = 390
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0

    pygame.mixer.music.play(-1)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            score_sound.play()
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        screen.blit(text, text_rect)

    def backgroung():
        global x_pos_bg, y_pos_bg
        image_width = Bg.get_width()
        screen.blit(Bg, (x_pos_bg, y_pos_bg))
        screen.blit(Bg, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(Bg, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        screen.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        player.draw(screen)
        player.update(user_input)

        # logic for obstacle
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(Small_Cactus))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(Large_Cactus))
            elif random.randint(0, 2) == 2:
                obstacles.append(Birds(Bird))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            # detect collision
            if player.dino_rect.colliderect(obstacle.rect):
                collision_sound.play()
                pygame.mixer.music.stop()
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        backgroung()

        cloud_pic.draw(screen)
        cloud_pic.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        screen.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your score: " + str(points), True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (screen_width // 2, screen_height // 2 + 50)
            screen.blit(score, score_rect)
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2, screen_height // 2)
        screen.blit(text, text_rect)
        screen.blit(Running[0], (screen_width // 2 - 20, screen_height // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    main()


menu(death_count=0)
