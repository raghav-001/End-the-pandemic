import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 700
clock = pygame.time.Clock()
red = (200, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (218, 239, 240, 255)
play_green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SANITIZE, NOT SOCIALIZE!")
character = pygame.image.load('character.jpg')
virus = pygame.image.load('virus.png')
home = pygame.image.load('home.jpg')
bg = pygame.image.load('bg.jpg')
character_width = 80
character_height = 200
virus_width = 110


def place_character(x, y):
    gameDisplay.blit(character, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, green, black)
    return textSurface, textSurface.get_rect()


def text_objects_title(text, font):
    textSurface = font.render(text, True,bright_green, black)
    return textSurface, textSurface.get_rect()

def text_objects_rules(text, font):
    textSurface = font.render(text, True, red,green)
    return textSurface, textSurface.get_rect()

def text_objects_intro(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 6))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def load_virus(virus_x, virus_y):
    gameDisplay.blit(virus, (virus_x, virus_y))


def load_score(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Virus killed by sanitization: " + str(count), True, green, black)
    gameDisplay.blit(text, (0, 0))


virus = pygame.transform.scale(virus, (100, 100))
character = pygame.transform.scale(character, (80, 200))


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(green)
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(virus, (90, 0))
        gameDisplay.blit(character,(350,300))
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf1, TextRect1 = text_objects_title("SANITIZE, NOT SOCIALIZE!", largeText)
        TextSurf2, TextRect2 = text_objects_rules("-> Mask up", largeText)
        TextSurf3, TextRect3 = text_objects_rules("-> Kill the virus using sanitizers", largeText)
        TextSurf4, TextRect4 = text_objects_rules("-> Don't get too close to the virus!", largeText)
        TextSurf5, TextRect5 = text_objects_rules("-> Keep the virus away from your home!", largeText)
        TextRect1.center = ((display_width / 2), (display_height / 8))
        TextRect2.center = ((display_width / 2), (display_height / 5))
        TextRect3.center = ((display_width / 2), (display_height / 4))
        TextRect4.center = ((display_width / 2), (display_height / 3))
        TextRect5.center = ((display_width / 2), (display_height / 2.5))
        gameDisplay.blit(TextSurf1, TextRect1)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 200 + 350 > mouse[0] > 200 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (200, 500, 350, 50))
            if click[0]==1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, play_green, (200, 500, 350, 50))
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects_intro("End the pandemic", smallText)
        TextRect.center = ((200 + (350 / 2)), (500 + (50 / 2)))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.45)
    horizontal_location = 0
    vertical_location = 0
    virus_x = random.randrange(0, display_width - virus_width)
    virus_y = -500
    thing_height = 50
    virus_speed = 3
    screen_size = gameDisplay.get_size()
    bg_size = bg.get_size()
    bg_x = (bg_size[0] - screen_size[0]) // 2
    bg_y = (bg_size[1] - screen_size[1]) // 2
    kills = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    horizontal_location -= 8
                elif event.key == pygame.K_RIGHT:
                    horizontal_location += 8
                elif event.key == pygame.K_UP:
                    vertical_location -= 8
                elif event.key == pygame.K_DOWN:
                    vertical_location += 8
                elif event.key == pygame.K_SPACE:
                    if x + character_width <= virus_x + virus_width and x + character_width >= virus_x:
                        virus_y = 0 - thing_height
                        virus_x = random.randrange(0, display_width - virus_width)
                        kills += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    horizontal_location = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    vertical_location = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bg_x -= 10
        if keys[pygame.K_RIGHT]:
            bg_x += 10
        if keys[pygame.K_UP]:
            bg_y -= 10
        if keys[pygame.K_DOWN]:
            bg_y += 10
        bg_x = max(0, min(bg_size[0] - screen_size[0], bg_x))
        bg_y = max(0, min(bg_size[1] - screen_size[1], bg_y))

        x += horizontal_location
        y += vertical_location

        if virus_y > display_height:
            virus_y = 0 - thing_height
            message_display("Virus entered your home! Stay in quarantine")
            virus_x = random.randrange(0, display_width - virus_width)
        if y < virus_y + thing_height:
            if x > virus_x and x < virus_x + virus_width or x + virus_width > virus_x and x + virus_width < virus_x + virus_width:
                message_display("Infected! Stay at home!")

        if x < 0:
            x = 0
        if x + character_width > display_width:
            x = display_width - character_width
        if y < 0:
            message_display("Went too far!")
        if y > display_height - character_height:
            message_display("Went below your home!")
        gameDisplay.blit(bg, (-bg_x, -bg_y))
        place_character(x, y)
        gameDisplay.blit(home, (300, 500))
        load_virus(virus_x, virus_y)
        virus_y += virus_speed
        load_score(kills)
        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
