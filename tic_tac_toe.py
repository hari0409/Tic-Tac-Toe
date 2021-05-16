import pygame
import sys
import numpy as np
import random

line_draw=[(237,237,208),(33,9,78),(233,59,129),(247,253,4),(222,137,113),"#f5f7b2","#94d0cc","#21094e","#fbc6a4","#f21170","#f0e3ca"]
screens=[(144, 127, 164),(8,18,129),(245,171,201),(249,178,8),(123,96,121),"#1cc5dc","#eec4c4","#511281","#f4a9a8","#72147e","#ff8303"]
cross=[(166,214,214),(76,161,163),(255,229,226),(255,229,226),(167,208,205),"#890596","#f29191","#4ca1a3","#ce97b0","#fa9905","#a35709"]
circle=[(233,59,129),(165,225,173),(182,201,240),(252,84,4),(255,233,214),"#cf0000","#d1d9d9","#a5e1ad","#afb9c8","#ff5200","#1b1a17"]
n=random.randint(0,len(line_draw))
ld=line_draw[n]
s=screens[n]
x=cross[n]
cc=circle[n]





# Initialise pygame
pygame.init()
# Create screen and config
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(s)


# Console board
board=np.zeros((3,3))
print(board)

# Draw lines
def drawl():
    pygame.draw.line(screen,ld,(0,200),(600, 200),15)  # 1st HL
    pygame.draw.line(screen,ld,(0,400),(600, 400),15)  # 2nd HL
    pygame.draw.line(screen,ld,(200,0),(200, 600),15)  # 1st VL
    pygame.draw.line(screen,ld,(400,0),(400,600),15)  # 2nd VL
drawl()

# Some Function
def mark_square(row,col,player):
    board[row][col]=player

def available_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False

def board_full():
    for i in range(0,3,1):
        for j in range(0,3,1):
            if board[i][j]==0:
                return False
    return True

def draw_fig():
    for i in range(0,3,1):
        for j in range(0,3,1):
            if board[i][j]==1:
                pygame.draw.line(screen,x,(j*200+55,i*200+200-55),(j*200+200-55,i*200+55),30)
                pygame.draw.line(screen,x,(j*200+55,i*200+55),(j*200+200-55,i*200+200-55),30)
            if board[i][j]==2:
                pygame.draw.circle(screen,cc,(int(j*200+100),int(i*200+100)),60,15)

def check(player):
    # vertical winning
    for i in range(0,3,1):
        if board[0][i]==board[1][i]==board[2][i]==player:
            draw_v_wl(i,player)
            # break the function from executing further
            return True
    # horizontal winning
    for j in range(0,3,1):
        if board[j][0]==board[j][1]==board[j][2]==player:
            draw_h_wl(j,player)
            # break the function from executing further
            return True
    # asc diagonal winning
    if board[2][0]==board[1][1]==board[0][2]==player:
        draw_ad_wl(player)
        return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        draw_dd_wl(player)
        return True
    return False
def draw_v_wl(col,player):
    xpos=col*200+100
    if player==1:
        c=x
    elif player==2:
        c=cc
    pygame.draw.line(screen,c,(xpos,15),(xpos,585),15)


def draw_h_wl(row,player):
    ypos = row * 200 + 100
    if player == 1:
        c = x
    elif player == 2:
        c = cc
    pygame.draw.line(screen, c, (15, ypos), (585,ypos), 15)

def draw_ad_wl(player):
    if player == 1:
        c = x
    elif player == 2:
        c = cc
    pygame.draw.line(screen,c,(15,585),(585,15),15)


def draw_dd_wl(player):
    if player == 1:
        c = x
    elif player == 2:
        c = cc
    pygame.draw.line(screen, c, (15, 15), (585, 585), 15)

game_over=False

def restart():
    screen.fill(s)
    drawl()
    player=1
    for i in range(0,3,1):
        for j in range(0,3,1):
            board[i][j]=0
player=1
# Run the mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mos_x=event.pos[0]
            mos_y=event.pos[1]
            clicked_row=int(mos_y//200)
            clicked_col=int(mos_x//200)
            if available_square(clicked_row,clicked_col):
                if player==1:
                    mark_square(clicked_row,clicked_col,1)
                    if check(player):
                        game_over=True
                    player=2
                elif player==2:
                    mark_square(clicked_row,clicked_col,2)
                    if check(player):
                        game_over=True
                    player=1
                draw_fig()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                restart()
                game_over=False
    pygame.display.update()

