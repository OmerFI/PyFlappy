# -*- coding: utf-8 -*-

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
import pygame
import json
import time

from BirdClass import BirdClass
from Level import Level1, Level2, Level3, Level4, Level5


# initialization
pygame.init()
pygame.font.init()
pygame.mixer.init()

# loading icon
icon = pygame.image.load(os.path.join('Assets', 'icon.png'))

# loading background
background = pygame.image.load(os.path.join('Assets', 'background.jpg'))

# loading musics
MAIN_MENU_MUSIC = pygame.mixer.music.load(
    os.path.join('Assets', 'Musics', 'June Songbirds-High.ogg'))

# loading sounds
BUTTON_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'beeps.wav'))

# playing the music
pygame.mixer.music.play(-1)

# loading info button
info_button = pygame.image.load(os.path.join(
    'Assets', 'main_menu', 'info_button.png'))

# loading back button
back_button = pygame.image.load(os.path.join('Assets', 'level_menu', 'back_button.png'))


# setting background's width and height
WIDTH = 1200
HEIGHT = 700

# setting buttons' x and y positions
PLAY_BUTTON_X = 373.3
PLAY_BUTTON_Y = 454.919
CONTRIBUTORS_BUTTON_X = 626.683
CONTRIBUTORS_BUTTON_Y = 454.919
INFO_BUTTON_X = WIDTH - info_button.get_width() - 30
INFO_BUTTON_Y = 30
BACK_BUTTON_X = 45
BACK_BUTTON_Y = 45

# setting windows, caption, icon
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(icon)

# loading JSON for supporting multi-languages
with open('language.json', 'r') as f:
    language_dict = json.load(f)

LOCALAPPDATA = os.getenv('LOCALAPPDATA')

# loading JSON for configuration
with open(LOCALAPPDATA + '\\PyFlappy\\config.json', 'r') as f:
    config_dict = json.load(f)

mybirdinstance = BirdClass()

# loading birds
for i in range(1, 30):
    exec(f"bird{i} = pygame.transform.scale(pygame.image.load(os.path.join('Assets','birds','{i}.png')),(64,64))")

# loading boundaries
for i in range(1, 11):
    exec(
        f"boundary{i} = pygame.image.load(os.path.join('Assets','boundaries','boundary{i}.png'))")

# loading active level images
for i in range(1, 6):
    exec(f"level{i}_active = pygame.transform.scale(pygame.image.load(os.path.join('Assets','level_menu','level_{i}_active.png')),(100,100))")

# loading inactive level images
for i in range(2, 6):
    exec(f"level{i}_inactive = pygame.transform.scale(pygame.image.load(os.path.join('Assets','level_menu','level_{i}_inactive.png')),(100,100))")

bird_dict = {"bird1": bird1,"bird2": bird2,"bird3": bird3,"bird4": bird4,"bird5": bird5,"bird6": bird6,"bird7": bird7,
            "bird8": bird8,"bird9": bird9,"bird10": bird10,"bird11": bird11,"bird12": bird12,"bird13": bird13,"bird14": bird14,
            "bird15": bird15,"bird16": bird16,"bird17": bird17,"bird18": bird18,"bird19": bird19,"bird20": bird20,"bird21": bird21,
            "bird22": bird22,"bird23": bird23,"bird24": bird24,"bird25": bird25,"bird26": bird26,"bird27": bird27 ,"bird28": bird28,"bird29": bird29}

boundary_list = [0, boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7, boundary8, boundary9, boundary10]

# setting level_text_size and font
LEVEL_TEXT_SIZE = 64
LEVEL_TEXT_FONT = pygame.font.Font(os.path.join('Assets', 'PoetsenOne-Regular.ttf'), LEVEL_TEXT_SIZE)

# setting FPS and VELOCITY
FPS = 60
VEL = 2


def main_menu(language:str) -> None:
    """Main menu function

    Args:
        language (str): The language that is wanted to use, can be only 'en' or 'tr'
    """

    # pygame.mixer.music.unpause()

    # loading buttons except info button
    play_button = pygame.image.load(os.path.join(
        'Assets', 'main_menu', language_dict[language]['IMAGES']['PLAY_BUTTON']))
    contributors_button = pygame.image.load(os.path.join(
        'Assets', 'main_menu', language_dict[language]['IMAGES']['CONTRIBUTORS_BUTTON']))

    # creating rectangles
    play_button_rect = pygame.Rect(
        PLAY_BUTTON_X, PLAY_BUTTON_Y, play_button.get_width(), play_button.get_height())
    contributors_button_rect = pygame.Rect(
        CONTRIBUTORS_BUTTON_X, CONTRIBUTORS_BUTTON_Y, play_button.get_width(), play_button.get_height())
    info_button_rect = pygame.Rect(
        INFO_BUTTON_X, INFO_BUTTON_Y, info_button.get_width(), info_button.get_height())

    info_button_radius = info_button_rect.width // 2
    info_button_radius_sqr = info_button_radius**2
    info_button_center = {'x': info_button_rect.x + info_button_rect.width /
                          2, 'y': info_button_rect.y + info_button_rect.height / 2}

    pygame.mouse.set_visible(True)

    clock = pygame.time.Clock()

    num = 0
    while True:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and num < 1:
                if event.key == pygame.K_r:
                    num += 1
                    BUTTON_SOUND.play()
                    button_effects(play_button, contributors_button, play_button_rect,
                                   contributors_button_rect, info_button_rect, language)

                if event.key == pygame.K_i:
                    draw_info_screen(language)

            if mouse_pressed[0] == True:
                if (PLAY_BUTTON_X < mouse_pos[0] < PLAY_BUTTON_X + play_button.get_width()) and (PLAY_BUTTON_Y < mouse_pos[1] < PLAY_BUTTON_Y + play_button.get_height()):
                    BUTTON_SOUND.play()
                    button_effects(play_button, contributors_button, play_button_rect,
                                   contributors_button_rect, info_button_rect, language)

                if (CONTRIBUTORS_BUTTON_X < mouse_pos[0] < CONTRIBUTORS_BUTTON_X + contributors_button.get_width()) and (CONTRIBUTORS_BUTTON_Y < mouse_pos[1] < CONTRIBUTORS_BUTTON_Y + contributors_button.get_height()):
                    BUTTON_SOUND.play()
                    draw_contributors_screen(language)

                if info_button_rect.x <= mouse_pos[0] <= info_button_rect.x + info_button_rect.width:
                    if info_button_radius_sqr >= (info_button_center['x'] - mouse_pos[0])**2 + (info_button_center['y'] - mouse_pos[1])**2:
                        BUTTON_SOUND.play()
                        draw_info_screen(language)

        draw_main_menu(play_button, contributors_button, play_button_rect,
                       contributors_button_rect, info_button_rect)


def draw_info_screen(language:str) -> None:
    """Drawing info screen

    Args:
        language (str): The language that is wanted to use, can be only 'en' or 'tr'
    """

    info_screen = pygame.image.load(os.path.join('Assets', 'main_menu', language_dict[language]['IMAGES']['INFO_SCREEN']))

    CLOSS_BUTTON_LEFT, CLOSS_BUTTON_RIGHT = (1054.8, 1111.8)
    CLOSS_BUTTON_TOP, CLOSS_BUTTON_BOTTOM = (42.8, 99.8)

    ENGLISH_BUTTON_LEFT, ENGLISH_BUTTON_RIGHT = (286.9, 476)
    ENGLISH_BUTTON_TOP, ENGLISH_BUTTON_BOTTOM = (493.6, 569.3)

    TURKISH_BUTTON_LEFT, TURKISH_BUTTON_RIGHT = (634.4, 823.5)
    TURKISH_BUTTON_TOP, TURKISH_BUTTON_BOTTOM = (493.6, 569.3)

    with open(LOCALAPPDATA + '\\PyFlappy\\config.json','r') as f:
        config_dict = json.load(f)

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if mouse_pressed[0] == True:
                if (CLOSS_BUTTON_LEFT < mouse_pos[0] < CLOSS_BUTTON_RIGHT) and (CLOSS_BUTTON_TOP < mouse_pos[1] < CLOSS_BUTTON_BOTTOM):
                    BUTTON_SOUND.play()
                    main_menu(language)

                if language == 'tr' and (ENGLISH_BUTTON_LEFT < mouse_pos[0] < ENGLISH_BUTTON_RIGHT) and (ENGLISH_BUTTON_TOP < mouse_pos[1] < ENGLISH_BUTTON_BOTTOM):
                    config_dict["LANGUAGE"] = "en"
                    with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
                        json.dump(config_dict, f, indent=4)
                    draw_info_screen('en')

                if language == 'en' and (TURKISH_BUTTON_LEFT < mouse_pos[0] < TURKISH_BUTTON_RIGHT) and (TURKISH_BUTTON_TOP < mouse_pos[1] < TURKISH_BUTTON_BOTTOM):
                    config_dict["LANGUAGE"] = "tr"
                    with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
                        json.dump(config_dict, f, indent=4)
                    draw_info_screen('tr')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu(language)

        WIN.blit(info_screen, (0, 0))
        pygame.display.update()


def draw_contributors_screen(language:str) -> None:
    """Drawing contributors screen

    Args:
        language (str): The language that is wanted to use, can be only 'en' or 'tr'
    """

    line1, line1_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][1], 42, background=True) #Coding
    line2, line2_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][2], 25, background=True) #Ömer Furkan İşleyen
    line3, line3_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][3], 42, background=True) #Design
    line4, line4_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][4], 25, background=True) #Ömer Furkan İşleyen
    line5, line5_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][5], 25, background=True) #Icons made by ...
    line6, line6_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][6], 25, background=True) #Background vector created by ...
    line7, line7_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][7], 42, background=True) #Music
    line8, line8_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][8], 25, background=True) #"beeps-18 1.wav" by ...
    line9, line9_background = display_text(language_dict[language]["TEXTS"]["LINE_TEXTS"][9], 25, background=True) #licensed under CCBY 3.0

    line1_x, line1_y = (28, 705.6)
    line2_x, line2_y = (28, 780)
    line3_x, line3_y = (28, 830.5)
    line4_x, line4_y = (28, 905)
    line5_x, line5_y = (28, 969.7)
    line6_x, line6_y = (28, 1032.6)
    line7_x, line7_y = (28, 1079)
    line8_x, line8_y = (28, 1155.4)
    line9_x, line9_y = (450.4, 1185.4)

    clock = pygame.time.Clock()
    counter = 0
    while True:
        clock.tick(60)

        mouse_pressed = pygame.mouse.get_pressed()

        if line1_y >= 50:
            line1_y -= 0.5
            line2_y -= 0.5
            line3_y -= 0.5
            line4_y -= 0.5
            line5_y -= 0.5
            line6_y -= 0.5
            line7_y -= 0.5
            line8_y -= 0.5
            line9_y -= 0.5
        else:
            if counter < 1:
                start = time.time()
                counter += 1
            else:
                end = time.time()
                if end - start >= 15:
                    main_menu(language)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu(language)
            if mouse_pressed[0]:
                main_menu(language)

        WIN.blit(background, (0, 0))

        for i in range(1, 10):
            exec(f"WIN.blit(line{i}_background, (line{i}_x - 2, line{i}_y + 1))")
            exec(f"WIN.blit(line{i}, (line{i}_x, line{i}_y))")

        pygame.display.update()


def draw_main_menu(play_button:pygame.Surface, contributors_button:pygame.Surface, play_button_rect:pygame.Rect, contributors_button_rect:pygame.Rect, info_button_rect:pygame.Rect) -> None:
    """Drawing main menu

    Args:
        play_button (pygame.Surface)            : Play button
        contributors_button (pygame.Surface)    : Contributors button
        play_button_rect (pygame.Rect)          : Play button rect
        contributors_button_rect (pygame.Rect)  : Contributors button rect
        info_button_rect (pygame.Rect)          : Info button rect
    """

    # drawing background
    WIN.blit(background, (0, 0))

    # drawing buttons
    WIN.blit(play_button, (play_button_rect.x, play_button_rect.y))
    WIN.blit(contributors_button,
             (contributors_button_rect.x, contributors_button_rect.y))
    WIN.blit(info_button, (info_button_rect.x, info_button_rect.y))
    pygame.display.update()


def button_effects(play_button:pygame.Surface, contributors_button:pygame.Surface, play_button_rect:pygame.Rect, contributors_button_rect:pygame.Rect, info_button_rect:pygame.Rect, language:str) -> None:
    """Animating buttons

    Args:
        play_button (pygame.Surface)            : Play button
        contributors_button (pygame.Surface)    : Contributors button
        play_button_rect (pygame.Rect)          : Play button rect
        contributors_button_rect (pygame.Rect)  : Contributors button rect
        info_button_rect (pygame.Rect)          : Info button rect
        language (str)                          : The language that is wanted to use, can be only 'en' or 'tr'.
    """

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        play_button_rect.y += 4
        contributors_button_rect.y += 4
        info_button_rect.y -= 3
        draw_main_menu(play_button, contributors_button, play_button_rect,
                       contributors_button_rect, info_button_rect)
        if play_button_rect.y - 30 > HEIGHT:
            break
    level_menu(language)


def level_menu(language:str) -> None:
    """Drawing level menu and setting button actions.

    Args:
        language (str): The language that is wanted to use, can be only 'en' or 'tr'.
    """

    level1_list = [level1_active, level2_inactive, level3_inactive, level4_inactive, level5_inactive]
    level2_list = [level1_active, level2_active, level3_inactive, level4_inactive, level5_inactive]
    level3_list = [level1_active, level2_active, level3_active, level4_inactive, level5_inactive]
    level4_list = [level1_active, level2_active, level3_active, level4_active, level5_inactive]
    level5_list = [level1_active, level2_active, level3_active, level4_active, level5_active]

    level_button_radius = level1_list[0].get_width()//2     # 50
    level_button_radius_sqr = level_button_radius ** 2      # 2500
    level_button_x = [150, 350, 550, 750, 950]
    level_button_y = [300, 300, 300, 300, 300]
    level_button_width = [100, 100, 100, 100, 100]
    level_button_higth = [100, 100, 100, 100, 100]

    back_button_radius = back_button.get_width()/2
    back_button_radius_sqr = back_button_radius ** 2

    with open(LOCALAPPDATA + '\\PyFlappy\\config.json','r') as f:
        config_dict = json.load(f)
    level_int = config_dict["LEVEL"]

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        distance = 150

        WIN.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu(language)

            if mouse_pressed[0] == True:
                if level_button_x[0] < mouse_pos[0] < level_button_x[0] + level_button_width[0]:
                    if ((level_button_x[0] + level_button_width[0]/2 - mouse_pos[0])**2 + (level_button_y[0] + level_button_higth[0]//2 - mouse_pos[1])**2 <= level_button_radius_sqr):
                        BUTTON_SOUND.play()
                        level_object = Level1()
                        main(level_object, 1, language)
                elif level_button_x[1] < mouse_pos[0] < level_button_x[1] + level_button_width[1]:
                    if ((level_button_x[1] + level_button_width[1]/2 - mouse_pos[0])**2 + (level_button_y[1] + level_button_higth[1]//2 - mouse_pos[1])**2 <= level_button_radius_sqr) and level_int >= 2:
                        BUTTON_SOUND.play()
                        level_object = Level2()
                        main(level_object, 2, language)
                elif level_button_x[2] < mouse_pos[0] < level_button_x[2] + level_button_width[2]:
                    if ((level_button_x[2] + level_button_width[2]/2 - mouse_pos[0])**2 + (level_button_y[2] + level_button_higth[2]//2 - mouse_pos[1])**2 <= level_button_radius_sqr) and level_int >= 3:
                        BUTTON_SOUND.play()
                        level_object = Level3()
                        main(level_object, 3, language)
                elif level_button_x[3] < mouse_pos[0] < level_button_x[3] + level_button_width[3]:
                    if ((level_button_x[3] + level_button_width[3]/2 - mouse_pos[0])**2 + (level_button_y[3] + level_button_higth[3]//2 - mouse_pos[1])**2 <= level_button_radius_sqr) and level_int >= 4:
                        BUTTON_SOUND.play()
                        level_object = Level4()
                        main(level_object, 4, language)
                elif level_button_x[4] < mouse_pos[0] < level_button_x[4] + level_button_width[4]:
                    if ((level_button_x[4] + level_button_width[4]/2 - mouse_pos[0])**2 + (level_button_y[4] + level_button_higth[4]//2 - mouse_pos[1])**2 <= level_button_radius_sqr) and level_int >= 5:
                        BUTTON_SOUND.play()
                        level_object = Level5()
                        main(level_object, 5, language)
                elif (BACK_BUTTON_X < mouse_pos[0] < BACK_BUTTON_X + back_button.get_width()) and BACK_BUTTON_Y < mouse_pos[1] < BACK_BUTTON_Y + back_button.get_height():
                    if (BACK_BUTTON_X + back_button.get_width() / 2 - mouse_pos[0]) ** 2 + (BACK_BUTTON_Y + back_button.get_height() /2 - mouse_pos[1])**2 <= back_button_radius_sqr:
                        BUTTON_SOUND.play()
                        main_menu(language)


        WIN.blit(back_button, (BACK_BUTTON_X, BACK_BUTTON_Y))

        with open(LOCALAPPDATA + '\\PyFlappy\\config.json','r') as f:
            config_dict = json.load(f)

        if config_dict["LEVEL"] == 1:
            for image in level1_list:
                WIN.blit(image, (distance, HEIGHT//2 - image.get_height()//2))
                distance += image.get_width() + 100
            pygame.display.update()

        elif config_dict["LEVEL"] == 2:
            for image in level2_list:
                WIN.blit(image, (distance,HEIGHT//2 - image.get_height()//2))
                distance += image.get_width() + 100
            pygame.display.update()

        elif config_dict["LEVEL"] == 3:
            for image in level3_list:
                WIN.blit(image, (distance,HEIGHT//2 - image.get_height()//2))
                distance += image.get_width() + 100
            pygame.display.update()

        elif config_dict["LEVEL"] == 4:
            for image in level4_list:
                WIN.blit(image, (distance,HEIGHT//2 - image.get_height()//2))
                distance += image.get_width() + 100
            pygame.display.update()

        elif config_dict["LEVEL"] == 5:
            for image in level5_list:
                WIN.blit(image, (distance,HEIGHT//2 - image.get_height()//2))
                distance += image.get_width() + 100
            pygame.display.update()


def main(level_object, level_int:int, language:str) -> None:
    """Game starting function

    Args:
        level_object    : Can be only Level1/Level2/Level3/Level4/Level5 object
        level_int (int) : Level integer
        language (str)  : The language that is wanted to use, can be only 'en' or 'tr'
    """

    # pygame.mixer.music.pause()
    birdrect = pygame.Rect(30, HEIGHT // 2 - bird1.get_height() //
                           2, bird1.get_width(), bird1.get_height())

    boundary1rect = pygame.Rect(level_object.boundary1x, level_object.boundary1y, boundary1.get_width(), boundary1.get_height())
    boundary2rect = pygame.Rect(level_object.boundary2x, level_object.boundary2y, boundary1.get_width(), boundary1.get_height())
    boundary3rect = pygame.Rect(level_object.boundary3x, level_object.boundary3y, boundary1.get_width(), boundary1.get_height())
    boundary4rect = pygame.Rect(level_object.boundary4x, level_object.boundary4y, boundary1.get_width(), boundary1.get_height())
    boundary5rect = pygame.Rect(level_object.boundary5x, level_object.boundary5y, boundary1.get_width(), boundary1.get_height())
    boundary6rect = pygame.Rect(level_object.boundary6x, level_object.boundary6y, boundary1.get_width(), boundary1.get_height())
    boundary7rect = pygame.Rect(level_object.boundary7x, level_object.boundary7y, boundary1.get_width(), boundary1.get_height())
    boundary8rect = pygame.Rect(level_object.boundary8x, level_object.boundary8y, boundary1.get_width(), boundary1.get_height())
    boundary9rect = pygame.Rect(level_object.boundary9x, level_object.boundary9y, boundary1.get_width(), boundary1.get_height())
    boundary10rect = pygame.Rect(level_object.boundary10x, level_object.boundary10y, boundary1.get_width(), boundary1.get_height())

    boundaryrect_list = [0, boundary1rect, boundary2rect, boundary3rect, boundary4rect, boundary5rect, boundary6rect, boundary7rect, boundary8rect, boundary9rect, boundary10rect]

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(False)

    while True:
        clock.tick(FPS)

        mybird = mybirdinstance.get_bird()
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause(birdrect, mybird, level_object, language)

                if event.key == pygame.K_ESCAPE:
                    pause(birdrect, mybird, level_object, language)

        bird_movement(keys_pressed, birdrect, mybird, boundaryrect_list, level_object, level_int, language)
        draw_window(birdrect, mybird, level_object, level_int)


def pause(birdrect:pygame.Rect, mybird:str, level_object, language:str) -> None:
    """Pauses the game and shows a pause_screen

    Args:
        birdrect (pygame.Rect)  : Bird rect
        mybird (str)            : The string that is used for choosing the bird
        level_object            : Can be only Level1/Level2/Level3/Level4/Level5 object
        language (str)          : The language that is wanted to use, can be only 'en' or 'tr'
    """
    clock = pygame.time.Clock()

    # setting mouse visibility
    pygame.mouse.set_visible(True)

    # loading pause screen
    pause_screen = pygame.image.load(os.path.join('Assets', 'pause_menu', language, 'pause_screen.png'))

    # loading temp images for masking for pixel perfect collision detection
    left = pygame.image.load(os.path.join('Assets', 'pause_menu', language, 'left.png'))
    right = pygame.image.load(os.path.join('Assets', 'pause_menu', language, 'right.png'))
    top = pygame.image.load(os.path.join('Assets', 'pause_menu', language, 'top.png'))
    mouse_image = pygame.image.load(os.path.join('Assets', 'pause_menu', 'mouse.png'))

    # setting coordinates
    pause_screen_x = WIDTH / 2 - pause_screen.get_width() / 2 # 257    256.5    256.5
    pause_screen_y = HEIGHT / 2 - pause_screen.get_height() / 2 # 53   52.5     5
    left_x, left_y = (282.434, 91.425)
    right_x, right_y = (729, 91.425)
    top_x, top_y = (469.715, 59)

    # creating rects for masking for pixel perfect collision
    left_rect = pygame.Rect(left_x, left_y, left.get_width(), left.get_height())
    right_rect = pygame.Rect(right_x, right_y, right.get_width(), right.get_height())
    top_rect = pygame.Rect(top_x, top_y, top.get_width(), top.get_height())

    left_mask = Masking(pause_mask = left, pause_mask_rect = left_rect)
    right_mask = Masking(pause_mask = right, pause_mask_rect = right_rect)
    top_mask = Masking(pause_mask = top, pause_mask_rect = top_rect)

    run = True
    while run:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break

            if mouse_pressed[0] == True:
                mouse_rect = pygame.Rect(mouse_pos[0] - 0.5, mouse_pos[1] - 0.5, 1, 1)
                mouse_mask = Masking(pause_mask = mouse_image, pause_mask_rect = mouse_rect)
                if pygame.sprite.collide_mask(mouse_mask, left_mask):
                    BUTTON_SOUND.play()
                    main_menu(language)
                elif pygame.sprite.collide_mask(mouse_mask, right_mask):
                    BUTTON_SOUND.play()
                    pygame.quit()
                    sys.exit()
                elif pygame.sprite.collide_mask(mouse_mask, top_mask):
                    BUTTON_SOUND.play()
                    run = False
                    break


        # drawing background
        WIN.blit(background, (0, 0))

        # drawing boundaries
        WIN.blit(boundary1, (level_object.boundary1x, level_object.boundary1y))
        WIN.blit(boundary2, (level_object.boundary2x, level_object.boundary2y))
        WIN.blit(boundary3, (level_object.boundary3x, level_object.boundary3y))
        WIN.blit(boundary4, (level_object.boundary4x, level_object.boundary4y))
        WIN.blit(boundary5, (level_object.boundary5x, level_object.boundary5y))
        WIN.blit(boundary6, (level_object.boundary6x, level_object.boundary6y))
        WIN.blit(boundary7, (level_object.boundary7x, level_object.boundary7y))
        WIN.blit(boundary8, (level_object.boundary8x, level_object.boundary8y))
        WIN.blit(boundary9, (level_object.boundary9x, level_object.boundary9y))
        WIN.blit(boundary10, (level_object.boundary10x, level_object.boundary10y))

        # drawing birds
        exec(f"WIN.blit({mybird},({birdrect.x}, {birdrect.y}))")

        # drawing pause menu
        WIN.blit(pause_screen, (pause_screen_x, pause_screen_y))
        # WIN.blit(left, (left_x, left_y))
        # WIN.blit(right, (right_x, right_y))
        # WIN.blit(top, (top_x, top_y))

        pygame.display.update()


class Masking(pygame.sprite.Sprite):
    """The class for making pixel perfect collision detection
    It accepts only keyword arguments

    Kwargs:
        bird (pygame.Surface): Bird image
        birdrect (pygame.Rect): Bird rect
        boundary_list (list): The list that includes the boundary images
        boundaryrect_list (list): The list that includes the boundary rects
        num (int): When the boundary_list and boundaryrect_list kwarg is used, this must be used for choosing the boundary image and boundary rect from the boundary_list and boundaryrect_list
        pause_mask (pygame.Surface): Mouse image (1x1 px)
        pause_mask_rect (pygame.Rect): Mouse rect
    """

    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)

        if "bird" in kwargs.keys():
            self.image = kwargs['bird']
        elif "boundary_list" and "num" in kwargs.keys():
            self.image = kwargs['boundary_list'][kwargs['num']]
        elif "pause_mask" in kwargs.keys():
            self.image = kwargs['pause_mask']

        if "birdrect" in kwargs.keys():
            self.rect = kwargs['birdrect']
        elif "boundaryrect_list" and "num" in kwargs.keys():
            self.rect = kwargs['boundaryrect_list'][kwargs['num']]
        elif "pause_mask_rect" in kwargs.keys():
            self.rect = kwargs['pause_mask_rect']


def bird_movement(keys_pressed:pygame.key.ScancodeWrapper, birdrect:pygame.Rect, mybird:str, boundaryrect_list:list, level_object, level_int:int, language:str) -> None:
    """Moving the bird

    Args:
        keys_pressed (pygame.key.ScancodeWrapper): Pressed keys
        birdrect (pygame.Rect): Bird rect
        mybird (str): The string that is used for choosing the bird
        boundaryrect_list (list): The list that includes the boundary rects
        level_object ([type]): Can be only Level1/Level2/Level3/Level4/Level5 object
        level_int (int): Level integer
        language (str): The language that is wanted to use, can be only 'en' or 'tr'
    """

    # increasing the bird's x coordinate
    birdrect.x += VEL

    # winning
    if birdrect.x + birdrect.width + 5 >= WIDTH:
        with open(LOCALAPPDATA + '\\PyFlappy\\config.json', 'r') as f:
            config_dict = json.load(f)

        if isinstance(level_object, Level1):
            if config_dict["LEVEL"] == 1:
                config_dict["LEVEL"] = level_int + 1
                with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
                    json.dump(config_dict, f, indent=4)
            level_object = Level2()
            main(level_object, level_int + 1, language)
        elif isinstance(level_object, Level2):
            if config_dict["LEVEL"] == 2:
                config_dict["LEVEL"] = level_int + 1
                with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
                    json.dump(config_dict, f, indent=4)
            level_object = Level3()
            main(level_object, level_int + 1, language)
        elif isinstance(level_object, Level3):
            if config_dict["LEVEL"] == 3:
                config_dict["LEVEL"] = level_int + 1
                with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
                    json.dump(config_dict, f, indent=4)
            level_object = Level4()
            main(level_object, level_int + 1, language)
        elif isinstance(level_object, Level4):
            if config_dict["LEVEL"] == 4:
                config_dict["LEVEL"] = level_int + 1
                with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
                    json.dump(config_dict, f, indent=4)
            level_object = Level5()
            main(level_object, level_int + 1, language)
        else:
            winning(language)

    if keys_pressed[pygame.K_SPACE] and birdrect.y > 0:
        birdrect.y -= VEL * 2.5
    else:
        birdrect.y += VEL * 2

    if birdrect.colliderect(boundaryrect_list[1]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=1)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[2]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=2)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[3]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=3)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[4]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=4)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[5]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=5)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[6]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=6)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[7]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=7)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[8]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=8)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[9]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=9)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.colliderect(boundaryrect_list[10]):
        bird_mask = Masking(bird=bird_dict[mybird], birdrect=birdrect)
        boundary_mask = Masking(boundary_list=boundary_list, boundaryrect_list=boundaryrect_list, num=10)
        if pygame.sprite.collide_mask(bird_mask, boundary_mask):
            main(level_object, level_int, language)
    elif birdrect.y + birdrect.height >= HEIGHT:
        main(level_object, level_int, language)


def draw_window(birdrect:pygame.Rect, mybird:str, level_object, level_int:int) -> None:
    """Drawing game screen

    Args:
        birdrect (pygame.Rect)  : Bird rect
        mybird (str)            : The string that is used for choosing the bird
        level_object            : Can be only Level1/Level2/Level3/Level4/Level5 object
        level_int (int)         : The language that is wanted to use, can be only 'en' or 'tr'
    """

    # drawing background
    WIN.blit(background, (0, 0))

    # drawing boundaries
    WIN.blit(boundary1, (level_object.boundary1x, level_object.boundary1y))
    WIN.blit(boundary2, (level_object.boundary2x, level_object.boundary2y))
    WIN.blit(boundary3, (level_object.boundary3x, level_object.boundary3y))
    WIN.blit(boundary4, (level_object.boundary4x, level_object.boundary4y))
    WIN.blit(boundary5, (level_object.boundary5x, level_object.boundary5y))
    WIN.blit(boundary6, (level_object.boundary6x, level_object.boundary6y))
    WIN.blit(boundary7, (level_object.boundary7x, level_object.boundary7y))
    WIN.blit(boundary8, (level_object.boundary8x, level_object.boundary8y))
    WIN.blit(boundary9, (level_object.boundary9x, level_object.boundary9y))
    WIN.blit(boundary10, (level_object.boundary10x, level_object.boundary10y))

    # drawing birds
    exec(f"WIN.blit({mybird},({birdrect.x}, {birdrect.y}))")

    # drawing the level text
    if level_int == 1:
        draw_level_text = display_text(text="1", size=LEVEL_TEXT_SIZE, color=(27, 34, 77))
        draw_level_text_background = display_text(text="1", size=LEVEL_TEXT_SIZE, color=(255, 255, 255))
    elif level_int == 2:
        draw_level_text = display_text(text="2", size=LEVEL_TEXT_SIZE, color=(27, 34, 77))
        draw_level_text_background = display_text(text="2", size=LEVEL_TEXT_SIZE, color=(255, 255, 255))
    elif level_int == 3:
        draw_level_text = display_text(text="3", size=LEVEL_TEXT_SIZE, color=(27, 34, 77))
        draw_level_text_background = display_text(text="3", size=LEVEL_TEXT_SIZE, color=(255, 255, 255))
    elif level_int == 4:
        draw_level_text = display_text(text="4", size=LEVEL_TEXT_SIZE, color=(27, 34, 77))
        draw_level_text_background = display_text(text="4", size=LEVEL_TEXT_SIZE, color=(255, 255, 255))
    elif level_int == 5:
        draw_level_text = display_text(text="5", size=LEVEL_TEXT_SIZE, color=(27, 34, 77))
        draw_level_text_background = display_text(text="5", size=LEVEL_TEXT_SIZE, color=(255, 255, 255))

    # drawing level text
    WIN.blit(draw_level_text_background, (13, 1))
    WIN.blit(draw_level_text, (15, 0))

    # updating the screen
    pygame.display.update()


def display_text(text:str, size:int, color:tuple = (27, 34, 77), antialias:int = 1, fontpath:str = os.path.join('Assets', 'PoetsenOne-Regular.ttf'), background:bool=False, background_color:tuple = (255, 255, 255), **kwargs) -> pygame.Surface:
    """Displaying text

    Args:
        text (str): The text that is wanted to show
        size (int): The text size that is wanted to show
        color (tuple, optional): The text color that is wanted to show. Defaults to (27, 34, 77).
        antialias (int, optional): The antialias is wanted to show. Defaults to 1.
        fontpath (str, optional): The fontpath that is wanted to show. Defaults to os.path.join('Assets', 'PoetsenOne-Regular.ttf').
        background (bool, optional): Determines whether to make a background. Defaults to False.
        background_color (tuple, optional): Background color. Defaults to (255, 255, 255).

    Kwargs:
        background_size (int, optional): Background size. Defaults to the 'size' arg

    Returns:
        pygame.Surface: The surface that can be used for showing onto the screen. If the background arg was set to True this function returns two pygame.Surface object.
    """

    display_font = pygame.font.Font(fontpath, size)
    display_text = display_font.render(text, antialias, color)
    if background == True:
        if "background_size" in kwargs.keys():
            display_font_background = pygame.font.Font(fontpath, kwargs["background_size"])
            display_text_background = display_font_background.render(text, antialias, background_color)
        elif "background_size" not in kwargs.keys():
            display_text_background = display_font.render(text, antialias, background_color)
        return (display_text, display_text_background)
    return display_text


def winning(language:str) -> None:
    """Drawing winning screen

    Args:
        language (str): The language that is wanted to use, can be only 'en' or 'tr'
    """

    # setting winner size and text
    WINNER_SIZE = 136
    WINNER_TEXT = language_dict[language]['TEXTS']['WINNER_TEXT']

    delay = 0
    while delay < 5:
        # drawing background
        WIN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # drawing winner.
        draw_winner = display_text(text=WINNER_TEXT, size=WINNER_SIZE, color=(27, 34, 77))
        draw_winner_background = display_text(text=WINNER_TEXT, size=WINNER_SIZE, color=(255, 255, 255))

        WIN.blit(draw_winner_background, (WIDTH // 2 - draw_winner_background.get_width() //
                                          2 - 2, HEIGHT // 2 - draw_winner_background.get_height() // 2 + 1))
        WIN.blit(draw_winner, (WIDTH // 2 - draw_winner.get_width() //
                               2, HEIGHT // 2 - draw_winner.get_height() // 2))
        pygame.display.update()

        pygame.time.delay(100)
        delay += 0.1
    main_menu(language)


if __name__ == '__main__':

    if config_dict["FIRST_OPENING"] == True:

        config_dict["FIRST_OPENING"] = False
        with open(LOCALAPPDATA + '\\PyFlappy\\config.json','w') as f:
            json.dump(config_dict, f, indent=4)

        draw_info_screen(config_dict["LANGUAGE"])
    else:
        main_menu(config_dict["LANGUAGE"])
