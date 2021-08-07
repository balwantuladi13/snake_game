import random
import pygame
import os

pygame.mixer.init() # pygame mixer initialize for music play
pygame.init() # pygame initialize to use pygame
GameWindow = pygame.display.set_mode((600,400))  #set window of game with width
pygame.display.set_caption('BALWANT GAMING HOUSE ') #to set title of game
#Colors
white = (255,255,255)
red = (255,0,0)
green=(0,255,0)
l_green = (0,155,0)
blue = (0,0,255)
black = (0,0,0)

clock  = pygame.time.Clock()
font =  pygame.font.SysFont(None,35)

#background image
bimg = pygame.image.load('s_img2.jpg')
bimg = pygame.transform.scale(bimg,(600,400)).convert_alpha()

def text_screen(text,color,tx,ty):
    s_text = font.render(text,True,color)
    GameWindow.blit(s_text,[tx,ty]) #update on screen

def plot_snake(GameWindow,color,snk_list,s_size):
    for x,y in snk_list:
        pygame.draw.rect(GameWindow,color,[x,y,s_size,s_size])
def button(x,y,action):
    pygame.draw.rect(GameWindow,green,[x,y,62,25])
    text_screen(action,red,x,y)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x<mouse[0]<x+62 and y<mouse[1]<y+25:
        pygame.draw.rect(GameWindow,l_green,[x,y,62,25])
        text_screen(action, red, x, y)
        if click == (1,0,0) and action == "PLAY":
            pygame.mixer.music.load('snake.mp3')
            pygame.mixer.music.play()
            game_loop()
        elif click == (1,0,0) and action == "QUIT":
            pygame.quit()
            quit()

def welcome():
    game_exit = False
    while not game_exit:
        GameWindow.fill((230,210,220))
        text_screen('WELCOME TO SNAKE GAME',black,100,100)
        text_screen('Press PLAY or QUIT', black, 150, 150)
        button(100,200,"PLAY")
        button(400,200,"QUIT")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        pygame.display.update()
        clock.tick(60)

#game_lopp
def game_loop():
    # game specific variables
    with open ('highscore.txt','r') as f:
        highscore = int(f.read())
    game_over = False
    game_exit = False
    screen_w = 600
    screen_h = 400
    sx = random.randint(30, screen_w / 2)
    sy = random.randint(30, screen_h / 2)
    s_size = 15
    f_size = 15
    vx = 0
    vy = 0
    foodx = random.randint(20, screen_w / 2)
    foody = random.randint(20, screen_h / 2)
    score = 0
    fps = 60
    speed = 3
    snk_list = []
    snk_len = 1

    while not game_exit:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            GameWindow.fill((230, 195, 220))
            text_screen('GAME OVER', blue, 100, 100)
            button(150, 150, "PLAY")
            button(150, 200, "QUIT")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        vx+=speed
                        vy=0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        vx-=speed
                        vy =0
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        vy-=speed
                        vx=0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        vy+=speed
                        vx=0
            sx+= vx
            sy+= vy

            if abs(sx-foodx)<6 and abs(sy-foody)<6:
                pygame.mixer.music.load('music/s_eat.mp3')
                pygame.mixer.music.play()
                score+=5
                foodx = random.randint(20, screen_w / 2)
                foody = random.randint(20, screen_h / 2)
                snk_len+=5
                if score > highscore:
                    highscore = score
                if score>0 and score%50 == 0:
                    speed+=2
            GameWindow.fill(white)
            GameWindow.blit(bimg,(0,0)) # 0,0 is positon where we want show
            text_screen("SCORE:" + str(score)+"  H_Score:"+str(highscore),green,5,5)
            #pygame.draw.rect(GameWindow,red,[foodx,foody,f_size,f_size])
            #pygame.draw.polygon(GameWindow,red,[foodx,foody,f_size,f_size])
            pygame.draw.ellipse(GameWindow,red,[foodx,foody,f_size+3,f_size])

            head = []
            head.append(sx)
            head.append(sy)
            snk_list.append(head)

            if len(snk_list)>snk_len:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('music/game_over.mp3')
                pygame.mixer.music.play()
            if sx<0 or sx>screen_w or sy<0 or sy>screen_h:
                game_over = True
                pygame.mixer.music.load('music/game_over.mp3')
                pygame.mixer.music.play()
               # print('game over')
            plot_snake(GameWindow,(0,220,240),snk_list,s_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

pygame.mixer.music.load('music/snake2.mp3')
pygame.mixer.music.play()
welcome()
#game_loop()