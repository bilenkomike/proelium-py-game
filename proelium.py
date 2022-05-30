# imports
import os
import pygame
from pygame import *
from pygame.locals import *
from random import randint
import time

# inits
pygame.init()
mixer.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), 0, 0)
screen_game = pygame.display.set_mode((screen_width, screen_height), 0, 0)


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
not_full_blue = (51, 172, 232)
yellow = (255, 255, 0)
brown = (148, 93, 25)
happy_c = (214, 182, 24)


font = None

clock = pygame.time.Clock()
FPS = 30

path = "all/images/"
sound_path = "all/sounds/"

backrounds = [transform.scale(image.load(path + "bg.png"), (800, 500)),# 0
              transform.scale(image.load(path + "game_bg.png"), (800, 500)), # 1
              transform.scale(image.load(path + "shop_bg.png"), (800, 500)), #2
              transform.scale(image.load(path + "fridge_bg.png"), (800, 500)), #3 
              transform.scale(image.load(path + "pharmacy_bg.png"), (800, 500)), #4 
              transform.scale(image.load(path + "playing_room.png"), (800, 500)), #5
              transform.scale(image.load(path + 'play_bg.png'), (800,500)), #6
              transform.scale(image.load(path + 'wardrob.png'), (800, 500)), #7
              transform.scale(image.load(path + 'game_over.png'), (800, 500)),#8
              transform.scale(image.load(path + 'note_screen.png'), (800, 500)) #9
              ]

sleeping_rooms = [
    transform.scale(image.load(path + "light_sleep_room.png"), (800, 500)),
    transform.scale(image.load(path + "dark_sleep_room.png"), (800, 500))
]

right_sign = transform.scale(image.load(path + 'right.png'), (65, 65))
left_sign = transform.scale(image.load(path + 'left.png'), (65, 65))
right_sign_hover = transform.scale(image.load(path + 'right_hover.png'), (65, 65))
left_sign_hover = transform.scale(image.load(path + 'left_hover.png'), (65, 65))
remka = transform.scale(image.load(path + 'remka.png'), (75, 75))
shop_icon = transform.scale(image.load(path + 'shop_icon.png'), (75, 95))
reg_poop = transform.scale(image.load(path + 'poop_reg.png'), (120,120))
rare_poop = transform.scale(image.load(path + 'poop_rare.png'), (120,120))
pharmacy_icon = transform.scale(image.load(path + 'pharmacy_icon.png'), (75, 95))
pss_game_icon = transform.scale(image.load(path + 'pss.png'), (75,75))
gn_game_icon = transform.scale(image.load(path + 'gn.png'), (75,75))
gamepad = transform.scale(image.load(path + 'gamepad.png'), (200, 150))
right_sign_room = transform.scale(image.load(path + 'right.png'), (65, 65))
left_sign_room = transform.scale(image.load(path + 'left.png'), (65, 65))
right_sign_room_hover = transform.scale(image.load(path + 'right_hover.png'), (65, 65))
left_sign_room_hover = transform.scale(image.load(path + 'left_hover.png'), (65, 65))
wb_ic = transform.scale(image.load(path + 'wb_ic.png'), (75, 100))
back_ic = transform.scale(image.load(path + 'back.png'), (75, 75))

heal_potion = transform.scale(image.load(path + 'heal.png'), (120, 120))
anti_virus = transform.scale(image.load(path + 'anti_virus.png'), (120, 120))
energy_potion = transform.scale(image.load(path + 'energy_heal.png'), (120, 120))
prikol_potion = transform.scale(image.load(path + 'prikol.png'), (120, 120))

privet = mixer.Sound(sound_path+"Privet .wav")
hochu_est= mixer.Sound(sound_path+"Hoch kushat.wav")
hochu_igrat = mixer.Sound(sound_path+"Hoch igrat.wav")
hochu_spat = mixer.Sound(sound_path+"Hoch spat.wav")
ploho = mixer.Sound(sound_path+"Ploho.wav")
vkusno = mixer.Sound(sound_path+"Vkusno.wav")
sonic_cost = mixer.Sound(sound_path+"Sonic.wav")
spider_cost = mixer.Sound(sound_path+"Spiderman .wav")
ezhik_cost = mixer.Sound(sound_path+"Ezhik.wav")
mario_cost = mixer.Sound(sound_path + "Mario.wav")
hrap = mixer.Sound(sound_path+"Hrap.wav")
# game elems
stone = transform.scale(image.load(path + 'stone.png'), (75, 75))
paper = transform.scale(image.load(path + 'paper.png'), (75,75))
scissors = transform.scale(image.load(path + 'scissors.png'), (75,75))
# food images
bug = transform.scale(image.load(path + 'bug.png'), (120, 120))
sworm = transform.scale(image.load(path + 'sworm.png'), (120, 120))
red_apple = transform.scale(image.load(path + 'red_apple.png'), (120, 120))
yellow_apple = transform.scale(image.load(path + 'yellow_apple.png'), (120, 120))
mushroom = transform.scale(image.load(path + 'mushroom.png'), (120, 120))
banana = transform.scale(image.load(path + 'banana.png'), (120, 120))
heart = transform.scale(image.load(path + 'heart.png'), (50, 50))
# indicators
energy_ic = transform.scale(image.load(path + 'energy_ic.png'), (65, 65))
starve_e = transform.scale(image.load(path + 'food.png'), (75, 75))
smile = transform.scale(image.load(path + 'smile.png'), (75, 75))
# window settings
game = True
logiks = 50

tolkaninfo = 0
# time
tick = 15
tick_h = 15
tick_e = 15
sleep_p = 0
is_ate = False
minus_st = False
minus_hp = False
plus_hp = False
reg_p_par = False
rare_p_par = False
sleep = False
minus_e = False
minus_hap = False
pashalka_found = False
ed50 = False
ed25 = False
ed0 = False

# sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class HedgeHog(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, tolkan, days_alive, age):
        super().__init__(player_image, player_x, player_y, width, height)
        self.age = age
        self.days_alive = days_alive
        self.tolkan = tolkan
        self.skin = ''

    def change_cost(self):
        if self.skin == '':
            self.image = transform.scale(image.load(path+'happy_h.png'),(self.width, self.height))
        if self.skin == 'spider':
            self.image = transform.scale(image.load(path+'spider.png'),(self.width, self.height))
        if self.skin == 'sonic':
            self.image = transform.scale(image.load(path+'sonic.png'),(self.width, self.height))
        if self.skin == 'mrpink':
            self.image = transform.scale(image.load(path+'mrpink.png'),(self.width, self.height))
        if self.skin == 'mario':
            self.image = transform.scale(image.load(path+'mario.png'),(self.width, self.height))

    def ploho_func(self):
        ploho.play()
        if self.skin == '':
            self.image = transform.scale(image.load(path + 'ploho_h.png'), (self.width, self.height))
        if self.skin == 'spider':
            self.image = transform.scale(image.load(path + 'spider_sick.png'), (self.width, self.height))
        if self.skin == 'sonic':
            self.image = transform.scale(image.load(path + 'sonic_sick.png'), (self.width, self.height))
        if self.skin == 'mrpink':
            self.image = transform.scale(image.load(path + 'mrpink_sick.png'), (self.width, self.height))
        if self.skin == 'mario':
            self.image = transform.scale(image.load(path + 'mario_sick.png'), (self.width, self.height))
    def sleeping_func(self):
        hrap.play()
        if self.skin == '':
            self.image = transform.scale(image.load(path + 'sleeping_h.png'), (self.width, self.height))
        if self.skin == 'spider':
            self.image = transform.scale(image.load(path + 'spider_sleep.png'), (self.width, self.height))
        if self.skin == 'sonic':
            self.image = transform.scale(image.load(path + 'sonic_sleep.png'), (self.width, self.height))
        if self.skin == 'mario':
            self.image = transform.scale(image.load(path + 'mario_sleep.png'), (self.width, self.height))
        if self.skin == 'mrpink':
            self.image = transform.scale(image.load(path + 'mrpink_sleep.png'), (self.width, self.height))
    def not_sleep_func(self):
        work_minus_e = True
        if self.skin == '':
            self.image = transform.scale(image.load(path + 'happy_h.png'), (self.width, self.height))
        if self.skin == 'spider':
            self.image = transform.scale(image.load(path + 'spider.png'), (self.width, self.height))
        if self.skin == 'sonic':
            self.image = transform.scale(image.load(path + 'sonic.png'), (self.width, self.height))
        if self.skin == 'mario':
            self.image = transform.scale(image.load(path + 'mario.png'), (self.width, self.height))
        if self.skin == 'mrpink':
            self.image = transform.scale(image.load(path + 'mrpink.png'), (self.width, self.height))

hedgehog = HedgeHog(path + 'happy_h.png', 250, 180, 250, 250, 0, 0, 0)

# privet.play()
class Food(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, food_status):
        super().__init__(player_image, player_x, player_y, width, height)
        self.food_status = food_status
        self.class_type = 'food'

    def eating(self):
        global starve_p
        global food_index
        if self.rect.collidepoint(mouse_pos):
            if starve_p < 75:
                vkusno.play()
                starve_p += self.food_status
                spritegroup.remove(spritegroup[food_index])
                if len(spritegroup) > 1 and food_index != 0:
                    food_index -= 1
                if len(spritegroup) > 1 and food_index == 0:
                    food_index += 1

                if starve_p > 75:
                    starve_p = 75

                if starve_p > 50:
                    ed50 = False
                    ed25 = False
                    ed0 = False
        else:
            selected = ''

class Potion(GameSprite):
    def __init__(self, player_image, player_x, player_y, width, height, potion_type,potion_status):
        super().__init__(player_image, player_x, player_y, width, height)
        self.potion_status = potion_status
        self.potion_type = potion_type
        self.class_type = 'potion'
    def drinking(self):
        global healthy_p
        global energy_p
        global sick_a
        global sick
        if self.potion_type == 'healing':
            if healthy_p < 75:
                healthy_p += self.potion_status
                spritegroup.remove(spritegroup[food_index])
            if healthy_p > 75:
                healthy_p = 75

        if self.potion_type == 'energy':
            if energy_p < 75:
                energy_p += self.potion_status
                spritegroup.remove(spritegroup[food_index])
            if energy_p > 75:
                energy_p = 75

        if self.potion_type == 'anti_virus':
            sick = False
            sick_a = 0

        if self.potion_type == 'prikol':
            healthy_p = 0

# methods


def bar():
    global healthbar, starve
    healthbar = pygame.draw.rect(screen, green, pygame.Rect(screen_width / 3.2, 0, 75, healthy_p))
    starve = pygame.draw.rect(screen, brown, pygame.Rect(screen_width / 2.2, 0, 75, starve_p))
    happiness_bg = pygame.draw.rect(screen, happy_c, pygame.Rect(screen_width / 1.7, 0, 75, happiness_p))
    energy_bg = pygame.draw.rect(screen, not_full_blue, pygame.Rect(screen_width / 1.38, 0, 75, energy_p))

    health = Rect(screen_width / 2.2, 0, 75, 75)
    happiness = Rect(screen_width / 1.7, 0, 75, 75)
    screen.blit(remka, (screen_width / 3.2, 0))
    screen.blit(heart, (screen_width / 3.05, 17.5))
    screen.blit(remka, (screen_width / 2.2, 0))
    screen.blit(remka, (screen_width / 1.38, 0))
    screen.blit(starve_e, (screen_width / 2.2, 5))
    screen.blit(remka, (screen_width / 1.7, 0))
    screen.blit(smile, (screen_width / 1.7, 2))
    screen.blit(energy_ic, (screen_width / 1.38, 6))

lose_text = 'О нет ты проиграл! Попробуй еще раз!'
win_text = 'Молодец!!! Ты выиграл!'

not_win_not_lose_text = 'Ничья'
pss_text = ''
check_num = 0
    
# Game
game_over = False
wardrobe_screen = False
shop_screen = False
fridge_screen = False
sleeping_room_p = False
playing_room_p = False
game_screen = False
pharmacy_screen = False
game = True
cont_open = False
sick = False
game_room_play = False
work_minus_e = True
hsp =  False
selected = ""
selected_sign = ""
i = 0

signs = [left_sign, left_sign_hover, right_sign, right_sign_hover,left_sign_room, left_sign_room_hover, right_sign_room, right_sign_room_hover]

# main menu

food_list = []

life = 12
minus_mon = False
privet.play()
while game:
    clock.tick(FPS)
    pygame.display.set_caption("Tamagocii")
    
    if game_screen == False:
        yycor = 100
        xxcor = 180
        food_con = 0
        food_index = 0
        spritegroup = []
        starve_p = 75
        happiness_p = 75
        healthy_p = 75
        energy_p = 75

        logiks = 50
        # Main Menu UI
        screen.blit(backrounds[0], (0, 0))

        text_lan = text_format("ЯЗЫК", font, 55, black)

        title = text_format("Tamagoci", font, 90, yellow)
        if selected == "start":
            text_start = text_format("НОВАЯ ИГРА", font, 55, yellow)
        else:
            text_start = text_format("НОВАЯ ИГРА", font, 55, black)
        if selected == "quit":
            text_quit = text_format("ВЫХОД", font, 55, yellow)
        else:
            text_quit = text_format("ВЫХОД", font, 55, black)
        if selected == "control":
            text_control = text_format("ПРИМЕЧАНИЯ", font, 55, yellow)
        else:
            text_control = text_format("ПРИМЕЧАНИЯ", font, 55, black)
        if selected == "return":
            text_return = text_format("назад", font, 55, yellow)
        else:
            text_return = text_format("назад", font, 55, black)

        # controll text
        movement_text = text_format('ВЫ ИГРАЕТЕ В ИГРУ ЁЖИК.', font, 35, black)  
        next_page_text = text_format('ВЫ МОЖЕТЕ ПОИГРАТЬ В ИГРУ, МОЖЕТЕ ЕГО ПОКОРМИТЬ.', font, 35, black)  
        num_page_text = text_format('ЕСТЬ ИВЕНТ БОЛЕЗНИ, ВО ВРЕМЯ ЭТОГО ИВЕНТА ВЫ ', font, 35, black)  
        num7_page_text = text_format('ДОЛЖНЫ БУДЕТЕ ЕГО ВЫЛЕЧИТЬ. ', font, 35, black)  
        num1_page_text = text_format('ТАК ЖЕ ВРЕМЯ НАШЕЙ ИГРЫ ОГРАНИЧЕНО - ', font, 35, black)  
        num6_page_text = text_format('ВСЕГО 24 МИНУТЫ.', font, 35, black)  
        num2_page_text = text_format('ЧТО В ПЕРЕВОДЕ НА НАШУ ИГРУ ОЗНАЧАЕТ 1 ГОД.', font, 35, black)  
        num3_page_text = text_format('ЕЩЁ У НАС ЕСТЬ КОСТЮМЫ, КОТОРЫЕ ВЫ МОЖЕТЕ ', font, 35, black)  
        num4_page_text = text_format('ОДЕТЬ В ГАРДЕРОБЕ.', font, 35, black)  
        num5_page_text = text_format('НАЙДИТЕ ПОСХАЛКУ :)', font, 35, black)  
        num10_page_text = text_format('ОСТАНОЛЬНОЕ ВЫ МОЖЕТЕ САМИ НАЙТИ В ИГРЕ.', font, 35, black)  

        title_rect = title.get_rect()
        start_rect = Rect(screen_width / 2.3, 420, 200, 40)
        quit_rect = Rect(screen_width / 5, 420, 120, 40)
        control_rect = Rect(screen_width / 1.4, 420, 200, 40)
        return_rect = Rect(50, 20, 150, 40)

        # Main Menu Text
        if cont_open == False:
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
            screen.blit(text_quit, ((screen_width / 5 - (start_rect[2] / 2), 420)))
            screen.blit(text_control, (screen_width / 1.4 - (quit_rect[2] / 2), 420))
            screen.blit(text_start, (screen_width / 2.35 - (start_rect[2] / 2), 420))
        elif cont_open:
            screen.blit(backrounds[9], (0, 0))
            # hide text
            title_rect = title.get_rect()
            start_rect = Rect(screen_width / 2, 240, 0, 0)
            quit_rect = Rect(screen_width / 2, 360, 0, 0)
            control_rect = Rect(screen_width / 2, 300, 0, 0)
            return_rect = Rect(50, 20, 100, 40)

            # show controll_menu
            screen.blit(text_return, (50, 20,))
            screen.blit(movement_text, (70, 70))
            screen.blit(next_page_text, (70, 100))

            screen.blit(num_page_text, (70, 130))
            screen.blit(num7_page_text, (70, 160))
            screen.blit(num1_page_text, (70, 190))
            screen.blit(num6_page_text, (70, 220))
            screen.blit(num2_page_text, (70, 250))
            screen.blit(num3_page_text, (70, 280))
            screen.blit(num4_page_text, (70, 310))
            screen.blit(num5_page_text, (70, 340))
            screen.blit(num10_page_text, (70, 370))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                selected = "start"
            if quit_rect.collidepoint(mouse_pos):
                selected = "quit"
            if control_rect.collidepoint(mouse_pos):
                selected = "control"
            if return_rect.collidepoint(mouse_pos):
                selected = "return"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                if start_rect.collidepoint(mouse_pos):
                    selected = "start"
                    game_screen = True
                if quit_rect.collidepoint(mouse_pos):
                    selected = "quit"
                    game = False
                if control_rect.collidepoint(mouse_pos):
                    selected = "control"
                    cont_open = True
                if return_rect.collidepoint(mouse_pos):
                    selected = "return"
                    cont_open = False

        pygame.display.update()
    # game
    else:
        check_time = time.time()
        
        if minus_mon == False:
            mon_now = int(time.time())
            mon_end = mon_now + 120
            minus_mon = True
        if minus_mon == True:
            if int(check_time) == mon_end:
                life -= 1
                minus_mon = False

        if minus_hap == False:
            hap_now = int(time.time())
            hap_end = hap_now + 15
            minus_hap = True
        if minus_hap == True:
            if int(check_time) == hap_end:
                happiness_p -= 3
                minus_hap = False




        if energy_p < 25:
            if hsp == False:
                hochu_spat.play()
                hsp = True

        if energy_p > 25:
            hsp  = False

        if work_minus_e == True:
            if minus_e == False:
                entime_now = int(time.time())
                entime_end = entime_now + tick_e
                minus_e = True

            if minus_e == True:
                if int(check_time) == entime_end:
                    energy_p -= 2
                    minus_e = False

        if minus_st == False:
            now = int(time.time())
            end = now + tick
            minus_st = True

        if minus_st == True:
            if int(check_time) == end:
                starve_p -= 3
                minus_st = False

        if sick == False:
            sick_a = 0
            now6 = int(time.time())
            end6 = randint(100, 150) + now6
            sick = True
        if sick == True:
            if int(check_time) == end6:
                if sick_a == 0:
                    hedgehog.ploho_func()
                    sick_a = 1


        if starve_p <= 0 and minus_hp == False or sick_a == 1 and minus_hp == False:
            now2 = int(time.time())
            end2 = now2 + tick_h
            minus_hp = True

        if starve_p <= 50 and ed50 == False:
            hochu_est.play()
            ed50 = True

        if starve_p <= 25 and ed25 == False:
            hochu_est.play()
            ed25 = True

        if starve_p <= 0 and ed0 == False:
            hochu_est.play()
            ed0 = True

        if minus_hp == True:
            if int(check_time) == end2:
                healthy_p -= 5
                minus_hp = False

        if healthy_p <= 0:
            healthy_p = 75
            starve_p = 75
            happiness_p = 75
            game_over = True
        if plus_hp == False:
            if starve_p >= 40:
                now3 = int(time.time())
                end3 = now3 + (tick - 1)
                plus_hp = True
            else:
                pass
               
        if plus_hp == True:
            if healthy_p > 75:
                healthy_p = 75
                plus_hp = False
            if check_time == end3:
                healthy_p += 5



        if wardrobe_screen == False and shop_screen == False and fridge_screen == False and pharmacy_screen == False and playing_room_p == False and sleeping_room_p == False and game_room_play == False and game_over == False:
            screen.blit(backrounds[1], (0, 0))
            
            bar()
            hedgehog.change_cost()
            
            screen.blit(shop_icon, (670, 400))
            screen.blit(pharmacy_icon, (580, 400))
            screen.blit(wb_ic, (0, 400))
            wb_rect = Rect(0,400,75, 75)
            hedgehog.rect.x = 300
            hedgehog.reset()
            
            if reg_p_par == False:
                now4 = int(time.time())
                end4 = now4 + randint(30, 60)
                ab = randint(20, 300)
                reg_p_par = True
        
            if rare_p_par == False:
                    now5 = int(time.time())
                    end5 = now5 + randint(90, 120)
                    a = randint(20, 600)
                    rare_p_par = True

            if reg_p_par == True:
                if int(check_time) == end4:
                    reg_poop_rect = Rect(ab, 300, 120, 120)
                    screen.blit(reg_poop, (ab, 300))
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if reg_poop_rect.collidepoint(mouse_pos):
                            reg_p_par = False
                            logiks += 5

            if rare_p_par == True:
                if int(check_time) == end5:
                    rare_poop_rect = Rect(a, 300, 120, 120)
                    screen.blit(rare_poop, (a, 300))
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rare_poop_rect.collidepoint(mouse_pos):
                            rare_p_par = False
                            logiks += 15
                        
            for i in spritegroup:
                if len(spritegroup) > 0:
                    if i == spritegroup[food_index]:
                        i.reset()

            for k in spritegroup:
                if k != spritegroup[food_index]:
                    k.rect.x = 900
                    k.rect.y = 600

            if selected_sign == 'left':
                screen.blit(signs[1], (screen_width / 3, 420))
            else:
                screen.blit(signs[0], (screen_width / 3, 420))
            if selected_sign == 'right':
                screen.blit(signs[3], (screen_width / 1.7, 420))
            else:
                screen.blit(signs[2], (screen_width / 1.7, 420))

            if selected_sign == 'left_r':
                screen.blit(signs[5], (20, 200))
            else:
                screen.blit(signs[4], (20, 200))

            if selected_sign == 'right_r':
                screen.blit(signs[7], (720, 200))
            else:
                screen.blit(signs[6], (720, 200))

            # hide text
            title_rect = title.get_rect()
            start_rect = Rect(screen_width / 2, 240, 0, 0)
            quit_rect = Rect(screen_width / 2, 360, 0, 0)
            control_rect = Rect(screen_width / 2, 300, 0, 0)
            return_rect = Rect(50, 20, 0, 0)

            left_rect = Rect(screen_width / 3, 420, 65, 65)
            right_rect = Rect(screen_width / 1.7, 420, 65, 65)
            
            
            # 
            
            left_rect_room = Rect(20,200,65,65)
            right_rect_room = Rect(720,200,65,65)
            pashalka_rect = Rect(520,160, 30,30)
            shop_rect = Rect(670, 400, 75, 95)
            pharmacy_rect = Rect(580, 400, 75, 95)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if wb_rect.collidepoint(mouse_pos):
                        wardrobe_screen = True
                    if pashalka_found == False:
                        if pashalka_rect.collidepoint(mouse_pos):
                            logiks += 1000
                            pashalka_found = True
                if right_rect.collidepoint(mouse_pos):
                    selected_sign = 'right'
                if left_rect.collidepoint(mouse_pos):
                    selected_sign = 'left'

                if right_rect_room.collidepoint(mouse_pos):
                    selected_sign = 'right_r'
                if left_rect_room.collidepoint(mouse_pos):
                    selected_sign = 'left_r'

                if shop_rect.collidepoint(mouse_pos):
                    selected = 'shop'
                else:
                    selected = ''
                if pharmacy_rect.collidepoint(mouse_pos):
                    selected = 'pharmacy'
                else:
                    selected = ''
                if left_rect.collidepoint(mouse_pos) == False and right_rect.collidepoint(mouse_pos) == False:
                    selected_sign = ''
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    if selected == 'pharmacy':
                        pharmacy_screen = True
                    if selected == 'shop':
                        shop_screen = True
                    if selected_sign == 'right':
                        if len(spritegroup) == 0:
                            pass
                        elif (food_index + 1) == len(spritegroup):
                            food_index = 0
                            for i in spritegroup:
                                i.rect.x = screen_width / 2.5
                                i.rect.y = 360

                        else:
                            food_index += 1
                            spritegroup[food_index].rect.x = screen_width / 2.5
                            spritegroup[food_index].rect.y = 360
                            spritegroup[food_index].reset()
                            for j in spritegroup:
                                if j != spritegroup[food_index]:
                                    j.rect.x = 900
                                    j.rect.y = 600
                    elif selected_sign == 'left':
                        if len(spritegroup) == 0:
                            pass
                        elif food_index < 0:
                            food_index = len(spritegroup) - 1
                            food_index2 = 0
                            for i in spritegroup:
                                i.rect.x = screen_width / 2.5
                                i.rect.y = 360
                                break
                        else:
                            food_index -= 1
                            spritegroup[food_index].rect.x = screen_width / 2.5
                            spritegroup[food_index].rect.y = 360
                            spritegroup[food_index].reset()
                            for j in spritegroup:
                                if j != spritegroup[food_index]:
                                    j.rect.x = 900
                                    j.rect.y = 600
                    if len(spritegroup) > 0:
                        for i in spritegroup:
                            if i.class_type == 'food':
                                i.eating()
                            elif i.class_type == 'potion':
                                i.drinking()
                    if left_rect_room.collidepoint(mouse_pos):
                        sleeping_room_p = True  
                    if right_rect_room.collidepoint(mouse_pos):
                        playing_room_p = True
                    
            pygame.display.flip()
        elif shop_screen == True:
            
            for prod in spritegroup:
                if prod.class_type == 'food':
                    food_con += 1
                else:
                    pass
            screen.blit(backrounds[2], (0, 0))
            screen.blit(back_ic, (0,0))
            back_rect_ic = Rect(0,0, 75, 75)
            logiks_text = text_format("логики: "+str(logiks), font, 55, black)
            price_ban = text_format('20', font, 45, black)
            price_rp = text_format('10', font, 45, black)
            price_yp = text_format('10', font, 45, black)
            price_bug = text_format('40', font, 45, black)
            price_mush = text_format('20', font, 45, black)
            price_sw = text_format('30', font, 45, black)
            screen.blit(logiks_text,(500,450))
            banana_rect = Rect(180,220, 120, 120)
            red_apple_rect = Rect(180, 100, 120, 120)
            yellow_apple_rect = Rect(340, 100, 120, 120)
            mushroom_rect = Rect(500, 100, 120, 120)
            sworm_rect = Rect(340, 220, 120, 120)
            bug_rect = Rect(500, 230, 120, 120)

            screen.blit(banana,(180,220))
            screen.blit(price_ban, (190, 240))
            #
            screen.blit(red_apple, (180, 100))
            screen.blit(price_rp, (190, 120))
            #
            screen.blit(yellow_apple, (340, 100))
            screen.blit(price_yp, (350, 120))
            #
            screen.blit(mushroom, (500, 100))
            screen.blit(price_mush, (510, 120))
            #
            screen.blit(sworm, (340, 220))
            screen.blit(price_sw, (350, 240))
            #
            screen.blit(bug, (500, 230))
            screen.blit(price_bug, (510, 240))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                mouse_pos = pygame.mouse.get_pos()
                if return_rect.collidepoint(mouse_pos):
                    selected = 'return'
                if banana_rect.collidepoint(mouse_pos):
                    selected = 'banana'
                if red_apple_rect.collidepoint(mouse_pos):
                    selected = 'red_apple'
                if yellow_apple_rect.collidepoint(mouse_pos):
                    selected = 'yellow_apple'
                if bug_rect.collidepoint(mouse_pos):
                    selected = 'bug'
                if mushroom_rect.collidepoint(mouse_pos):
                    selected = 'mushroom'
                if sworm_rect.collidepoint(mouse_pos):
                    selected = 'sworm'
                if sworm_rect.collidepoint(mouse_pos) == False and mushroom_rect.collidepoint(mouse_pos) == False and bug_rect.collidepoint(mouse_pos) == False and yellow_apple_rect.collidepoint(mouse_pos) == False and red_apple_rect.collidepoint(mouse_pos) == False and banana_rect.collidepoint(mouse_pos) == False and return_rect.collidepoint(mouse_pos) == False:
                    selected = ''

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    if back_rect_ic.collidepoint(mouse_pos):
                        shop_screen = False
                    if food_con != 6:
                        if selected == 'banana':
                            if logiks >= 20:
                                logiks -= 20
                                food = Food(path + 'banana.png', screen_width / 2.5, 360, 150, 150, 10)
                                spritegroup.append(food)
                            else:
                                pass
                        if selected == 'mushroom':
                            if logiks >= 20:
                                logiks -= 20
                                food = Food(path + 'mushroom.png', screen_width / 2.5, 360, 150, 150, 10)
                                spritegroup.append(food)
                            else:
                                pass
                        if selected == 'red_apple':
                            if logiks >= 10:
                                logiks -= 10
                                food = Food(path + 'red_apple.png', screen_width / 2.5, 360, 150, 150, 5)
                                spritegroup.append(food)
                            else:
                                pass
                        if selected == 'yellow_apple':
                            if logiks >= 10:
                                logiks -= 10
                                food = Food(path + 'yellow_apple.png', screen_width / 2.5, 360, 150, 150, 5)
                                spritegroup.append(food)
                            else:
                                pass
                        if selected == 'bug':
                            if logiks >= 40:
                                logiks -= 40
                                food = Food(path + 'bug.png', 340, 370, 150, 150, 20)
                                spritegroup.append(food)
                            else:
                                pass
                        if selected == 'sworm':
                            if logiks >= 30:
                                logiks -= 30
                                food = Food(path + 'sworm.png', screen_width / 2.5, 360, 150, 150, 15)
                                spritegroup.append(food)
                            else:
                                pass
        elif fridge_screen == True:
            screen.blit(backrounds[3],(0,0))
            screen.blit(back_ic, (0,0))
            back_rect_ic = Rect(0,0, 75, 75)
            for i in spritegroup:
                if i.class_type == 'food':
                    food_list.append(i)

            
            if len(food_list) == 1:
                screen.blit(food_list[0].image,(180,100))
            elif len(food_list) == 2:
                screen.blit(food_list[0].image,(180,100))
                screen.blit(food_list[1].image,(340,100))
            elif len(food_list) == 3:
                screen.blit(food_list[0].image,(180,100))
                screen.blit(food_list[1].image,(340,100))
                screen.blit(food_list[3].image,(500,100))
            elif len(food_list) == 4:
                screen.blit(food_list[0].image,(180,100))
                screen.blit(food_list[1].image,(340,100))
                screen.blit(food_list[3].image,(500,100))
                screen.blit(food_list[3].image,(180,200))
            elif len(food_list) == 5:
                screen.blit(food_list[0].image,(180,100))
                screen.blit(food_list[1].image,(340,100))
                screen.blit(food_list[3].image,(500,100))
                screen.blit(food_list[3].image,(180,200))
                screen.blit(food_list[4].image,(340,200))
            elif len(food_list) == 6:
                screen.blit(food_list[0].image,(180,100))
                screen.blit(food_list[1].image,(340,100))
                screen.blit(food_list[3].image,(500,100))
                screen.blit(food_list[3].image,(180,200))
                screen.blit(food_list[4].image,(340,200))
                screen.blit(food_list[5].image,(500,200))

         

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                mouse_pos = pygame.mouse.get_pos()
                if return_rect.collidepoint(mouse_pos):
                    selected = 'return'
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    if back_rect_ic.collidepoint(mouse_pos):
                        fridge_screen = False


        elif pharmacy_screen == True:
            screen.blit(backrounds[4],(0,0))
            heal_p_price = text_format('20',font,45,black)
            energy_p_price = text_format('20', font, 45, black)
            anti_virus_price = text_format('30', font, 45, black)
            prikol_p_price = text_format('100', font, 45, black)

            logiks_text = text_format("логики: " + str(logiks), font, 55, black)
            screen.blit(logiks_text,(500,450))
            screen.blit(back_ic, (0,0))
            back_rect_ic = Rect(0,0, 75, 75)
            
            screen.blit(prikol_potion,(340,100))
            screen.blit(prikol_p_price,(320,120))

            screen.blit(energy_potion, (180, 220))
            screen.blit(energy_p_price, (190, 240))

            screen.blit(heal_potion, (340, 220))
            screen.blit(heal_p_price, (350, 240))

            screen.blit(anti_virus, (500, 220))
            screen.blit(anti_virus_price, (510, 240))

            anti_virus_rect = Rect(500,220,120,120)
            heal_rect = Rect(340, 220, 120, 120)
            energy_potion_rect = Rect(180,220,120,120)
            prikol_potion_rect = Rect(340,100,120,120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                mouse_pos = pygame.mouse.get_pos()
                if return_rect.collidepoint(mouse_pos):
                    selected = 'return'
                if anti_virus_rect.collidepoint(mouse_pos):
                    selected = 'anti_virus'
                if heal_rect.collidepoint(mouse_pos):
                    selected = 'heal'
                if prikol_potion_rect.collidepoint(mouse_pos):
                    selected = 'prikol_potion'
                if energy_potion_rect.collidepoint(mouse_pos):
                    selected = 'energy_potion'

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    if back_rect_ic.collidepoint(mouse_pos):
                        pharmacy_screen = False
                    if selected == 'anti_virus':
                        if logiks >= 30:
                            logiks -= 30
                            potion = Potion(path+'anti_virus.png',screen_width / 2.5, 390, 130, 130,'anti_virus',0)
                            spritegroup.append(potion)
                        else:
                            pass
                    if selected == 'heal':
                        if logiks >= 20:
                            logiks -= 20
                            potion = Potion(path + 'heal.png', screen_width / 2.5, 390, 130, 130, 'healing', 40)
                            spritegroup.append(potion)
                        else:
                            pass
                    if selected == 'energy_potion':
                        if logiks >= 20:
                            logiks -= 20
                            potion = Potion(path + 'energy_heal.png', screen_width / 2.5, 390, 130, 130, 'energy', 40)
                            spritegroup.append(potion)
                        else:
                            pass
                    if selected == 'prikol_potion':
                        if logiks >= 100:
                            logiks -= 100
                            potion = Potion(path + 'prikol.png', screen_width / 2.3, 390, 130, 130, 'prikol', 0)
                            spritegroup.append(potion)
                        else:
                            pass
                        
                        
        # playing_room
        elif playing_room_p == True:
            
            screen.blit(backrounds[5], (0,0))
            screen.blit(gamepad, ( 450, 280))
            
            screen.blit(back_ic, (0,0))
            back_rect_ic = Rect(0,0, 75, 75)
            
            screen.blit(pss_game_icon, (430, 425))
            pss_gi = Rect(430, 425, 75, 75)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_rect_ic.collidepoint(mouse_pos):
                        playing_room_p = False
                    
                    if pss_gi.collidepoint(mouse_pos):
                        game_room_play = True
                        selected_game = 'pss'
                        playing_room_p = False
                        
                        
            hedgehog.rect.x = 200
            hedgehog.reset()
            bar()
            
        
        elif game_room_play == True:
            global selected_elem
            screen.blit(backrounds[6], (0,0))
            if selected_game == 'pss':
                if happiness_p >= 75:
                    happiness_p = 75
                else:
                    happiness_p+=5
                    
                screen.blit(back_ic, (0,0))
                back_rect_ic = Rect(0,0, 75, 75)
                
                screen.blit(stone, (200,400))
                screen.blit(paper, (400, 400))
                screen.blit(scissors, (600, 400))
                
                stone_ic = Rect(200,400,100,100)
                paper_ic = Rect(400, 400, 100, 100)
                scissors_ic = Rect(600, 400, 100, 100)
                
                items = ['paper', 'stone', 'scissors']
                selected_elem = 0
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        game = False
                    if selected_game == 'pss':
                        mouse_pos = pygame.mouse.get_pos()
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            mouse_pos = pygame.mouse.get_pos()  
                            if back_rect_ic.collidepoint(mouse_pos):
                                game_room_play = False
                                playing_room_p = True
                                
                            if paper_ic.collidepoint(mouse_pos):
                                selected_elem = randint(0,2)  
                                check_elem = 'paper'
                                if items[selected_elem] == 'stone' and check_elem == 'paper':
                                    pss_text = 'Молодец!!! Ты выиграл!'
                                    logiks += 10
                                elif items[selected_elem] == 'paper' and check_elem == 'paper':
                                    pss_text = 'Ничья!'
                                elif items[selected_elem] == 'scissors' and check_elem == 'paper':
                                    pss_text = 'О нет ты проиграл! Попробуй еще раз!'
                                    logiks -= 5
                                    
                                text_pss = text_format(pss_text, font, 45, black)
                                    
                            if stone_ic.collidepoint(mouse_pos):
                                selected_elem = randint(0,2)  
                                check_elem = 'stone'
                                if items[selected_elem] == 'paper' and check_elem == 'stone':
                                    pss_text = 'О нет ты проиграл! Попробуй еще раз!'
                                    logiks -= 5
                                elif items[selected_elem] == 'scissors' and check_elem == 'stone':
                                    pss_text = 'Молодец!!! Ты выиграл!'
                                    logiks += 10
                                elif items[selected_elem] == 'stone' and check_elem == 'stone':
                                    pss_text = 'Ничья!'
                                    
                               
                                
                                text_pss = text_format(pss_text, font, 45, black)
                            if scissors_ic.collidepoint(mouse_pos):
                                check_elem = 'scissors'
                                if items[selected_elem] == 'stone' and check_elem == 'scissors':
                                    pss_text = 'О нет ты проиграл! Попробуй еще раз!'
                                    logiks -= 5
                                elif items[selected_elem] == 'paper' and check_elem == 'scissors':
                                    pss_text = 'Молодец!!! Ты выиграл!'
                                    logiks += 10
                                elif items[selected_elem] == 'scissors' and check_elem == 'scissors':
                                    pss_text = 'Ничья!'
                                    
                               
                               
                text_pss = text_format(pss_text, font, 45, black)           
                screen.blit(text_pss, (150,150))
                lg_txt = text_format(str(logiks), font, 45, black)                 
                screen.blit(lg_txt, (120,20))
                
                hedgehog.rect.x = 500
                hedgehog.reset()
                
                
                
            
        #    sleep
        elif sleeping_room_p:
            screen.blit(sleeping_rooms[sleep_p], (0, 0))
            lamp_rect = Rect(680, 290, 120, 120)
            screen.blit(back_ic, (0,0))
            back_rect_ic = Rect(0,0, 75, 75)
            bar()
            
            hedgehog.reset()
            
            if sleep == False and sleep_p == 1:
                sleep_now = int(time.time())
                sleep_end = sleep_now + 5
                sleep = True

            if sleep == True and sleep_p == 1:
                if int(check_time) == sleep_end:
                    energy_p += 5
                    sleep = False
                if energy_p >= 75:
                    energy_p = 75
                    sleep_p = 0
                    sleep = False
                    hedgehog.not_sleep_func()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                mouse_pos = pygame.mouse.get_pos()
                
                if lamp_rect.collidepoint(mouse_pos):
                    selected = 'lamp'
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_rect_ic.collidepoint(mouse_pos):
                        sleeping_room_p = False
                    if sick != True:
                        if selected == 'lamp':
                            if sleep_p != 1:
                                sleep_p = 1
                                work_minus_e = False
                                hedgehog.sleeping_func()
                    else:
                        pass
        elif wardrobe_screen == True: 
            screen.blit(backrounds[7], (0,0))
            screen.blit(back_ic, (100,0))
            back_rect_ic = Rect(100,0, 75, 75)
            
            cost_mrpink = transform.scale(image.load(path + 'mrpinkcost.png'), (150,150))
            cost_mario = transform.scale(image.load(path + 'mariocost.png'), (150,150))
            cost_spider = transform.scale(image.load(path + 'spidercost.png'), (150,150))
            cost_sonic = transform.scale(image.load(path + 'soniccost.png'), (150,150))
            
            screen.blit(cost_mrpink, (70,120))
            screen.blit(cost_mario, (245,120))
            screen.blit(cost_spider, (420,120))
            screen.blit(cost_sonic, (595,120))
            
            mrpink_rect = Rect(70,120, 150,150)
            mario_rect = Rect(245,120, 150,150)
            spider_rect = Rect(420,120, 150,150)
            socnic_rect = Rect(595,120, 150,150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_rect_ic.collidepoint(mouse_pos):
                        wardrobe_screen = False             

                    if mrpink_rect.collidepoint(mouse_pos):
                        ezhik_cost.play()
                        hedgehog.skin = 'mrpink'
                    if mario_rect.collidepoint(mouse_pos):
                        mario_cost.play()
                        hedgehog.skin = 'mario'
                    if spider_rect.collidepoint(mouse_pos):
                        spider_cost.play()
                        hedgehog.skin = 'spider'
                    if socnic_rect.collidepoint(mouse_pos):
                        sonic_cost.play()
                        hedgehog.skin = 'sonic'
        elif game_over == True:
            screen.blit(backrounds[8], (0,0))
            reset = text_format('Вернуться в главное меню', font, 45, black)
            screen.blit(reset, (100,120))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                        
        pygame.display.update()