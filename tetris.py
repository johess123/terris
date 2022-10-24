import pygame
from copy import deepcopy
from random import randint
import time
import os

def main():
    pygame.init() # 初始化
    res = 800,800
    fps = 60
    screen = pygame.display.set_mode(res)
    levelpng = pygame.image.load("level.png")
    clock = pygame.time.Clock()
    count = 0
    pygame.mixer.init()
    select_sound = pygame.mixer.Sound("select.mp3")
    select_sound.play()
    while True:
        screen.fill(pygame.Color('black'))
        font = pygame.font.Font('font.ttf',60) # 字體
        if count < 20:
            choose_lv = font.render("T E T R I S",True,pygame.Color('red'))
        elif count >= 20 and count < 40:
            choose_lv = font.render("T E T R I S",True,pygame.Color('blue'))
        elif count >= 40 and count < 60:
            choose_lv = font.render("T E T R I S",True,pygame.Color('yellow'))
        else:
            count = 0
            choose_lv = font.render("T E T R I S",True,pygame.Color('red'))
        count += 1
        screen.blit(choose_lv, (220,10))
        font = pygame.font.Font('font.ttf',50) # 字體
        choose_lv = font.render("LEVEL",True,pygame.Color('white'))
        screen.blit(choose_lv, (320,100))
        font = pygame.font.Font('font.ttf',30) # 字體
        num = [" 0"," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16","17","18","19"]
        for i in range(20):
            lv = font.render(num[i],True,pygame.Color('white'))
            screen.blit(lv, (175+i%5*100,250+i//5*100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 關閉
                os._exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0],event.pos[1]
                if x >= 180  and x < 180+30 and y >= 260 and y < 260+30: # level 0
                    select_sound.stop()
                    play(0)
                elif x >= 280 and x <= 280+30 and y >= 260 and y < 260+30:
                    select_sound.stop()
                    play(1)
                elif x >= 380 and x <= 380+30 and y >= 260 and y < 260+30:
                    select_sound.stop()
                    play(2)
                elif x >= 480 and x <= 480+30 and y >= 260 and y < 260+30:
                    select_sound.stop()
                    play(3)
                elif x >= 580 and x <= 580+30 and y >= 260 and y < 260+30:
                    select_sound.stop()
                    play(4)
                elif x >= 180  and x < 180+30 and y >= 360 and y < 360+30: # level 5
                    select_sound.stop()
                    play(5)
                elif x >= 280 and x <= 280+30 and y >= 360 and y < 360+30:
                    select_sound.stop()
                    play(6)
                elif x >= 380 and x <= 380+30 and y >= 360 and y < 360+30:
                    select_sound.stop()
                    play(7)
                elif x >= 480 and x <= 480+30 and y >= 360 and y < 360+30:
                    select_sound.stop()
                    play(8)
                elif x >= 580 and x <= 580+30 and y >= 360 and y < 360+30:
                    select_sound.stop()
                    play(9)
                elif x >= 180  and x < 180+30 and y >= 460 and y < 460+30: # level 10
                    select_sound.stop()
                    play(10)
                elif x >= 280 and x <= 280+30 and y >= 460 and y < 460+30:
                    select_sound.stop()
                    play(11)
                elif x >= 380 and x <= 380+30 and y >= 460 and y < 460+30:
                    select_sound.stop()
                    play(12)
                elif x >= 480 and x <= 480+30 and y >= 460 and y < 460+30:
                    select_sound.stop()
                    play(13)
                elif x >= 580 and x <= 580+30 and y >= 460 and y < 460+30:
                    select_sound.stop()
                    play(14)
                elif x >= 180  and x < 180+30 and y >= 560 and y < 560+30: # level 15
                    select_sound.stop()
                    play(15)
                elif x >= 280 and x <= 280+30 and y >= 560 and y < 560+30:
                    select_sound.stop()
                    play(16)
                elif x >= 380 and x <= 380+30 and y >= 560 and y < 560+30:
                    select_sound.stop()
                    play(17)
                elif x >= 480 and x <= 480+30 and y >= 560 and y < 560+30:
                    select_sound.stop()
                    play(18)
                elif x >= 580 and x <= 580+30 and y >= 560 and y < 560+30:
                    select_sound.stop()
                    play(19)
        pygame.display.flip()
        clock.tick(fps)
    
def check_borders(block): # 檢查是否超出邊界
    if block[0] < 0+8 or block[0] >= w+8: # 左右
        return False
    elif block[1] > h+3-1:
        return False
    elif block[1] < 0+3:
        return 2
    elif field[block[1]][block[0]] != -1:
        return False
    return True

def play(level):
    res = 800,800
    fps = 60
    screen = pygame.display.set_mode(res)
    clock = pygame.time.Clock()
    font = pygame.font.Font('font.ttf',100) # 字體
    wait3 = font.render('3',True,pygame.Color('white'))
    wait2 = font.render('2',True,pygame.Color('white'))
    wait1 = font.render('1',True,pygame.Color('white'))
    count = 0
    pygame.mixer.init()
    count_sound = pygame.mixer.Sound("count.mp3")
    count_sound.play()
    while True:
        screen.fill(pygame.Color('black'))
        if count >= 0 and count < 60:
            screen.blit(wait3, (350,300))
        elif count >= 60 and count < 120:
            screen.blit(wait2, (350,300))
        elif count >= 120 and count < 180:
            screen.blit(wait1, (350,300))
        else:
            playgame(level)
        count += 1
        pygame.display.flip()
        clock.tick(fps)

def playgame(level):
    f = open("score.txt", "r+")
    leaderboard = f.readlines()
    for i in range(len(leaderboard)):
        leaderboard[i] = int(leaderboard[i].replace('\n',""))
    f.close()
    global w
    global h
    w,h = 10,20
    tile = 30
    resolution = w*tile,h*tile
    res = 800,800
    fps = 60

    screen = pygame.display.set_mode(res)
    game_screen = pygame.Surface(resolution)
    clock = pygame.time.Clock()
    # 聲音
    pygame.mixer.init()
    pygame.mixer.music.load("bgm.mp3") # 載入音樂
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1,0) # 播放音樂
    
    #burn_sound = pygame.mixer.Sound("burn.wav")
    victory_sound = pygame.mixer.Sound("ed.mp3")
    topout_sound = pygame.mixer.Sound("topout.mp3")
    tetris_sound = []
    tetris_sound.append(pygame.mixer.Sound("tetris1.mp3"))
    tetris_sound.append(pygame.mixer.Sound("tetris2.mp3"))
    tetris19 = []
    tetris19.append(pygame.mixer.Sound("tetris3.mp3"))
    tetris19.append(pygame.mixer.Sound("tetris4.mp3"))
    move_sound = pygame.mixer.Sound("move.mp3")
    levelup_sound = pygame.mixer.Sound("levelup.mp3")
    rotate_sound = pygame.mixer.Sound("rotate.mp3")
    single_sound = pygame.mixer.Sound("single.mp3")
    double_sound = pygame.mixer.Sound("double.mp3")
    triple_sound = pygame.mixer.Sound("triple.mp3")
    land_sound = pygame.mixer.Sound("land.mp3")
    lose_sound = pygame.mixer.Sound("lose.mp3")
    
    grid = [pygame.Rect(x*tile,y*tile,tile,tile) for x in range(8,w+8) for y in range(3,h+3)]

    all_color = [[(255,255,255) for i in range(10)], # I
                [(255,255,255) for i in range(10)], # O
                [(0,255,255),(153,255,77),(255,179,230),(153,255,77),(153,255,77),(135,206,250),(119,136,153),(176,23,31),(255,0,0),(255,255,0)], # Z
                [(13,51,255),(0,128,0),(186,85,211),(13,51,255),(255,20,147),(0,255,128),(255,0,0),(186,85,211),(13,51,255),(138,43,226)], # S
                [(0,255,255),(153,255,77),(255,179,230),(153,255,77),(153,255,77),(135,206,250),(119,136,153),(176,23,31),(255,0,0),(255,255,0)], # L
                [(13,51,255),(0,128,0),(186,85,211),(13,51,255),(255,20,147),(0,255,128),(255,0,0),(186,85,211),(13,51,255),(138,43,226)], # J
                [(255,255,255) for i in range(10)]] # T
    
    blocks_pos = [[[[0,0],[-1,0],[-2,0],[1,0]], [[0,0],[0,-1],[0,-2],[0,1]], 2, all_color[0]], # I
           [[[-1,0],[-1,1],[0,1],[0,0]], 1, all_color[1]], # O
           [[[0,0],[-1,0],[0,1],[1,1]], [[1,0],[1,-1],[0,0],[0,1]], 2, all_color[2]], # Z
           [[[0,0],[1,0],[0,1],[-1,1]], [[-1,-1],[-1,0],[0,0],[0,1]], 2, all_color[3]], # S
           [[[0,0],[-1,0],[1,0],[-1,1]], [[0,0],[0,1],[0,-1],[1,1]], [[0,0],[1,0],[-1,0],[1,-1]], [[0,0],[0,-1],[0,1],[-1,-1]], 4, all_color[4]], # L
           [[[0,0],[-1,0],[1,0],[1,1]], [[0,0],[0,1],[0,-1],[1,-1]], [[0,0],[1,0],[-1,0],[-1,-1]], [[0,0],[0,-1],[0,1],[-1,1]], 4, all_color[5]], # J
           [[[0,0],[-1,0],[1,0],[0,1]], [[0,0],[0,1],[0,-1],[1,0]], [[0,0],[1,0],[-1,0],[0,-1]], [[0,0],[0,-1],[0,1],[-1,0]], 4, all_color[6]]] # T
    blocks = []
    for i in range(7):
        blocks.append([pygame.Rect(x+w//2+8,y+3,1,1) for x,y in blocks_pos[i][0]])
    block_rect = pygame.Rect(0,0,tile-2,tile-2)
    block_rect1 = pygame.Rect(0,0,tile-10,tile-10)
    block_rect2 = pygame.Rect(0,0,4,4)
    global field
    field = [[-1 for i in range(w+8)] for j in range(h+3)]
    a = randint(0,6)
    block = deepcopy(blocks[a]) # 隨機選方塊
    block.append(a)
    block.append(0)
    block.append(blocks_pos[a][-1])
    drought = 0 # 多久沒出現直條
    if a == 0:
        drought = 0
    else:
        drought += 1
    b = randint(0,6)
    next_block = deepcopy(blocks[b]) # 隨機選下個方塊
    next_block.append(b)
    next_block.append(0)
    next_block.append(blocks_pos[b][-1])

    score,lines = 0,0 # 得分, 行數
    scores = [0,40,100,300,1200] # 消除行數對應得分

    font = pygame.font.Font('font.ttf',24) # 字體

    title_score = font.render('SCORE',True,pygame.Color('white')) # 顯示得分
    title_line = font.render('LINES',True,pygame.Color('white')) # 顯示行數
    title_next = font.render('NEXT',True,pygame.Color('white')) # 顯示下一個
    
    title_leaderboard = font.render('LEADER BOARD',True,pygame.Color('white')) # 顯示排行榜
    title_tetrsRate = font.render('TRT',True,pygame.Color('white')) # 顯示tetris率
    title_drought = font.render('DRT',True,pygame.Color('white')) # 顯示長條多久沒來
    title_level = font.render('LEVEL',True,pygame.Color('white')) # 顯示等級
    title_burn = font.render('BRN',True,pygame.Color('white')) # 顯示連續非四消次數

    drop = 0 # 下降
    allSpeed = [48,43,38,33,28,23,18,13,8,6,5,5,5,4,4,4,3,3,3,2,2,2,2,2,2,2,2,2,2,1]
    advanceLines = [10,20,30,40,50,60,70,80,90,100,100,100,100,100,100,100,110,120,130,130] # 開始所需晉級行數
    speed = allSpeed[level] #速度 
    advanceLine = advanceLines[level] # 起始晉級需要行數
    advanceFirst = False # 起始等級是否晉級
    oldLines = 0
    gameover = False

    lose = pygame.image.load("lose.png")
    again = pygame.image.load("again.png").convert()
    over = pygame.image.load("over.png").convert()
    black = pygame.image.load("black.jpg")
    white = []
    white.append(pygame.image.load("white1.jpg"))
    white.append(pygame.image.load("white2.jpg"))
    white.append(pygame.image.load("white3.png"))
    white.append(pygame.image.load("white4.png"))
    white.append(pygame.image.load("white5.jpg"))
    white.append(pygame.image.load("white6.png"))
    white.append(pygame.image.load("white7.jpg"))
    white.append(pygame.image.load("white8.png"))
    white.append(pygame.image.load("white9.jpg"))
    white.append(pygame.image.load("white10.jpg"))
    white.append(pygame.image.load("white11.jpg"))
    white.append(pygame.image.load("white12.png"))
    gray = pygame.image.load("gray.jpg")
    gray1 = pygame.image.load("gray1.png")
    gray2 = pygame.image.load("gray2.jpg")
    allBg = []
    for i in range(20):
        allBg.append(pygame.image.load("bg"+str(i+1)+".png"))
    bgCount = 0
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    
    tetris = 0 # 四消次數
    burn = 0 # 連續非四消次數
    death = 0 # 是否死亡
    
    startWait = 120 # 開始後先等待兩秒
    flash = False
    flashCount = 0
    cleanAni = False

    whiteNum = 0
    tetrisNum = 0
    tetris19Num = 0
    count19 = 0
    while True:
        if gameover == False:
            displayBg = allBg[bgCount//4]
            screen.blit(displayBg, (-450,0))
            bgCount += 1
            if bgCount >= 60:
                bgCount = 0
            if level%10 == 9:
                screen.blit(gray, (240,90))
            else:
                screen.blit(black, (240,90))
            rotate = 0
            move = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # 關閉
                    os._exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move = -1
                        move_sound.play()
                    elif event.key == pygame.K_RIGHT: # 右
                        move = 1
                        move_sound.play()
                    elif event.key == pygame.K_DOWN: # 旋轉(逆時鐘)
                        rotate = 2
                        rotate_sound.set_volume(0.5)
                        rotate_sound.play()
                    elif event.key == pygame.K_UP: # 旋轉(順時鐘)
                        rotate = 1
                        rotate_sound.set_volume(0.5)
                        rotate_sound.play()
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0: # 旋轉(順時鐘)
                        rotate = 1
                        rotate_sound.set_volume(0.5)
                        rotate_sound.play()
                    elif event.button == 1: # 旋轉(逆時鐘)
                        rotate = 2
                        rotate_sound.set_volume(0.5)
                        rotate_sound.play()
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 1:
                        if event.value <= -1:
                            move = -1
                            move_sound.play()
                        elif event.value >= 1:
                            move = 1
                            move_sound.play()
            if move > 2:
                move = 2
            # 左右移
            for i in range(4): # 4格方塊
                block[i][0] += move # 移動方塊
                if check_borders(block[i]) == False: # 有方塊超出左右邊界
                    for j in range(i+1): # 復原移動過的方塊
                        block[j][0] -= move
                    break
            # 計算等級和速度
            lines = int(lines)
            if advanceFirst == False: # 起始等級還沒晉級
                if lines >= advanceLine:
                    oldLines = advanceLine
                    level += 1
                    if level >= len(allSpeed):
                        speed = allSpeed[len(allSpeed)-1]
                    else:
                        speed = allSpeed[level]
                    levelup_sound.set_volume(3)
                    levelup_sound.play()
                    advanceFirst = True
                    tetris19Num == 0
            else: # 已經過起始等級
                if lines - oldLines >= 10: # 每10條晉級一次
                    oldLines += 10
                    level += 1
                    if level >= len(allSpeed):
                        speed = allSpeed[len(allSpeed)-1]
                    else:
                        speed = allSpeed[level]
                    levelup_sound.set_volume(3)
                    levelup_sound.play()
                    tetris19Num == 0
            # 上下移
            if drop == 0:
                nextDisplay = True
            startWait -= 1
            if startWait <= 0:
                drop += 1
                if drop == speed:
                    drop = 0
                    block1 = deepcopy(block)
                    for i in range(4): # 4格方塊
                        block[i][1] += 1
                        if check_borders(block[i]) == False:
                            land_sound.set_volume(0.5)
                            land_sound.play()
                            for j in range(4):
                                field[block1[j][1]][block1[j][0]] = block[4]
                            block = next_block
                            blockcopy = deepcopy(block)
                            if next_block[-3] == 0:
                                drought = 0
                            else:
                                drought += 1
                            drop -= 18
                            nextDisplay = False
                            c = randint(0,6)
                            next_block = deepcopy(blocks[c])
                            next_block.append(c)
                            next_block.append(0)
                            next_block.append(blocks_pos[c][-1])
                            for j in range(4):
                                if field[block[j][1]][block[j][0]] != -1:
                                    gameover = True
                                    pygame.mixer.music.stop()
                                    topout_sound.play()
                                    time.sleep(1)
                                    if death == 0:
                                        lose_sound.play()
                                        victory_sound.play()
                                    death = 1
                            break
            # 順時鐘旋轉
            if rotate == 1:
                block1 = deepcopy(block)
                success = True
                for i in range(4):
                    shape = block[4]
                    kind = block[5]
                    old_kind = kind
                    kind += 1
                    if kind >= blocks_pos[shape][-2]:
                        kind -= blocks_pos[shape][-2]
                    next_kind = kind
                    block[i][0] = block[i][0] - blocks_pos[shape][old_kind][i][0] + blocks_pos[shape][kind][i][0]
                    block[i][1] = block[i][1] - blocks_pos[shape][old_kind][i][1] + blocks_pos[shape][kind][i][1]
                    kind = old_kind
                    if check_borders(block[i]) == False or check_borders(block[i]) == 2: # 有方塊超出左右邊界
                        block = deepcopy(block1)
                        success = False
                        break
                if success == True:
                    block[5] = next_kind
            # 逆時鐘旋轉
            if rotate == 2:
                block1 = deepcopy(block)
                success = True
                for i in range(4):
                    shape = block[4]
                    kind = block[5]
                    old_kind = kind
                    kind -= 1
                    if kind < 0:
                        kind += blocks_pos[shape][-2]
                    next_kind = kind
                    block[i][0] = block[i][0] - blocks_pos[shape][old_kind][i][0] + blocks_pos[shape][kind][i][0]
                    block[i][1] = block[i][1] - blocks_pos[shape][old_kind][i][1] + blocks_pos[shape][kind][i][1]
                    kind = old_kind
                    if check_borders(block[i]) == False or check_borders(block[i]) == 2: # 有方塊超出左右邊界
                        block = deepcopy(block1)
                        success = False
                        break
                if success == True:
                    block[5] = next_kind
            # 消除
            count = 0 # 消除行數
            cleanLine = []
            for i in range(3,len(field)):
                clean = True
                for j in range(8,len(field[i])):
                    if field[i][j] == -1:
                        clean = False
                if clean == True:
                    cleanLine.append(i)
                    count += 1
            lines += count
            if count == 4:
                tetris += 1
                burn = 0
                flash = True
                if level%10 == 9 and tetris19Num < 2:
                    if tetris19Num == 1:
                        tetris19[tetris19Num].set_volume(2)
                        tetris19[tetris19Num].play()
                    else:
                        tetris19[tetris19Num].play()
                    tetris19Num += 1
                else:
                    tetris_sound[tetrisNum].play()
                    tetrisNum += 1
                    if tetrisNum == 2:
                        tetrisNum = 0
            elif count > 0:
                if count == 1:
                    single_sound.play()
                elif count == 2:
                    double_sound.set_volume(3)
                    double_sound.play()
                elif count == 3:
                    triple_sound.play()
                burn += count
                cleanAni = True
            if lines == 0:
                tetris_rate = 0
            else:
                tetris_rate = int(round(tetris*4/lines*100))
            # 計算分數
            score = int(score)
            score += scores[count]*(level+1)
            score = str(score)
            score = '0'*(6-len(score))+score
            lines = str(lines)
            lines = '0'*(3-len(lines))+lines
            # 消除效果
            if cleanAni == True:
                for i in range(5):
                    for j in range(len(cleanLine)):
                        field[cleanLine[j]][12-i] = -1
                        field[cleanLine[j]][13+i] = -1
                    if level%10 == 9:
                        screen.blit(gray, (240,90))
                    else:
                        screen.blit(black, (240,90))
                    screen.blit(title_score, (600,100))
                    screen.blit(title_line, (600,220))
                    screen.blit(title_next, (600,340))
                    screen.blit(title_tetrsRate, (140,500))
                    screen.blit(title_burn, (140,600))
                    screen.blit(title_drought, (140,400))
                    screen.blit(title_level, (600,520))
                    screen.blit(title_leaderboard, (20,80))

                    screen.blit(font.render(score, True, pygame.Color('white')), (600,150))
                    screen.blit(font.render("     "+lines, True, pygame.Color('white')), (600,270))
                    screen.blit(font.render(str(tetris_rate)+"%", True, pygame.Color('white')), (160,550))
                    screen.blit(font.render("0"*(3-len(str(burn)))+str(burn), True, pygame.Color('white')), (150,650))
                    screen.blit(font.render("0"*(3-len(str(drought)))+str(drought), True, pygame.Color('white')), (150,450))
                    screen.blit(font.render("0"*(2-len(str(level)))+str(level), True, pygame.Color('white')), (660,570))
                    for j in range(5):
                        screen.blit(font.render(str(j+1)+".", True, pygame.Color('white')), (30,120+j*30))
                        screen.blit(font.render("0"*(6-len(str(leaderboard[j])))+str(leaderboard[j]), True, pygame.Color('white')), (100,120+j*30))
                    # 畫背景格(grid)
                    [pygame.draw.rect(screen,(40,40,40), i_grid,1) for i_grid in grid] # 畫面,顏色,網格,線寬
                    
                    # 畫到底的方塊(field)
                    for y in range(len(field)):
                        for x in range(len(field[y])):
                            if field[y][x] != -1:
                                if field[y][x] == 0 or field[y][x] == 1 or field[y][x] ==6:
                                    block_rect[0] = x * tile
                                    block_rect[1] = y * tile
                                    pygame.draw.rect(screen, pygame.Color(all_color[3][level%10]), block_rect)
                                    block_rect1[0] = x * tile+4
                                    block_rect1[1] = y * tile+4
                                    pygame.draw.rect(screen, pygame.Color('white'), block_rect1)
                                    block_rect2[0] = x * tile
                                    block_rect2[1] = y * tile
                                    pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                else:
                                    if (field[y][x] == 2 or field[y][x] == 4) and (level%10 == 9):
                                        block_rect[0] = x * tile
                                        block_rect[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color('black'), block_rect)
                                        block_rect1[0] = x * tile+4
                                        block_rect1[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color(all_color[field[y][x]][level%10]), block_rect1)
                                    else:
                                        block_rect[0] = x * tile
                                        block_rect[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color(all_color[field[y][x]][level%10]), block_rect)
                                        block_rect2[0] = x * tile
                                        block_rect2[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+4
                                        block_rect2[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+8
                                        block_rect2[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+4
                                        block_rect2[1] = y * tile+8
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)

                    # 顯示下一個方塊
                    for j in range(4):
                        if block[-1][level%10] == (255,255,255): # 白色方塊要畫外框
                            block_rect[0] = block[j][0] * tile + 270
                            block_rect[1] = block[j][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color(all_color[3][level%10]), block_rect)
                            block_rect1[0] = block[j][0] * tile + 270+4
                            block_rect1[1] = block[j][1] * tile + 330+4
                            pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect1)
                            block_rect2[0] = block[j][0] * tile + 270
                            block_rect2[1] = block[j][1] * tile + 330
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                        else:
                            if (block[4] == 2 or block[4] == 4) and (level%10 == 9):
                                block_rect[0] = block[j][0] * tile + 270
                                block_rect[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen,pygame.Color('black'), block_rect)
                                block_rect1[0] = block[j][0] * tile + 270+4
                                block_rect1[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect1)
                            else:
                                block_rect[0] = block[j][0] * tile + 270
                                block_rect[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect)
                                block_rect2[0] = block[j][0] * tile + 270
                                block_rect2[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+4
                                block_rect2[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+8
                                block_rect2[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+4
                                block_rect2[1] = block[j][1] * tile + 330+8
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)

                    pygame.display.update()
                    if i != 5:
                        time.sleep(0.05)
                cleanAni = False
                ###
                
            # 四消閃爍效果
            if flash == True:
                for i in range(5):
                    for j in range(len(cleanLine)):
                        field[cleanLine[j]][12-i] = -1
                        field[cleanLine[j]][13+i] = -1
                    if level%10 != 9:
                        count19 = 0
                        screen.blit(white[whiteNum], (240,90))
                    elif (level%10 == 9) and count19 < 10:
                        whiteNum = 0
                        if count19 < 5:
                            screen.blit(gray1, (240,90))
                        else:
                            screen.blit(gray2, (240,90))
                        count19 += 1
                    else:
                        screen.blit(white[whiteNum], (240,90))
                    screen.blit(title_score, (600,100))
                    screen.blit(title_line, (600,220))
                    screen.blit(title_next, (600,340))
                    screen.blit(title_tetrsRate, (140,500))
                    screen.blit(title_burn, (140,600))
                    screen.blit(title_drought, (140,400))
                    screen.blit(title_level, (600,520))
                    screen.blit(title_leaderboard, (20,80))

                    screen.blit(font.render(score, True, pygame.Color('white')), (600,150))
                    screen.blit(font.render("     "+lines, True, pygame.Color('white')), (600,270))
                    screen.blit(font.render(str(tetris_rate)+"%", True, pygame.Color('white')), (160,550))
                    screen.blit(font.render("0"*(3-len(str(burn)))+str(burn), True, pygame.Color('white')), (150,650))
                    screen.blit(font.render("0"*(3-len(str(drought)))+str(drought), True, pygame.Color('white')), (150,450))
                    screen.blit(font.render("0"*(2-len(str(level)))+str(level), True, pygame.Color('white')), (660,570))
                    for j in range(5):
                        screen.blit(font.render(str(j+1)+".", True, pygame.Color('white')), (30,120+j*30))
                        screen.blit(font.render("0"*(6-len(str(leaderboard[j])))+str(leaderboard[j]), True, pygame.Color('white')), (100,120+j*30))
                    # 畫背景格(grid)
                    [pygame.draw.rect(screen,(40,40,40), i_grid,1) for i_grid in grid] # 畫面,顏色,網格,線寬
                    
                    # 畫到底的方塊(field)
                    for y in range(len(field)):
                        for x in range(len(field[y])):
                            if field[y][x] != -1:
                                if field[y][x] == 0 or field[y][x] == 1 or field[y][x] ==6:
                                    block_rect[0] = x * tile
                                    block_rect[1] = y * tile
                                    pygame.draw.rect(screen, pygame.Color(all_color[3][level%10]), block_rect)
                                    block_rect1[0] = x * tile+4
                                    block_rect1[1] = y * tile+4
                                    pygame.draw.rect(screen, pygame.Color('white'), block_rect1)
                                    block_rect2[0] = x * tile
                                    block_rect2[1] = y * tile
                                    pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                else:
                                    if (field[y][x] == 2 or field[y][x] == 4) and (level%10 == 9):
                                        block_rect[0] = x * tile
                                        block_rect[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color('black'), block_rect)
                                        block_rect1[0] = x * tile+4
                                        block_rect1[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color(all_color[field[y][x]][level%10]), block_rect1)
                                    else:
                                        block_rect[0] = x * tile
                                        block_rect[1] = y * tile
                                        pygame.draw.rect(screen, all_color[field[y][x]][level%10], block_rect)
                                        block_rect2[0] = x * tile
                                        block_rect2[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+4
                                        block_rect2[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+8
                                        block_rect2[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+4
                                        block_rect2[1] = y * tile+8
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)

                    # 顯示下一個方塊
                    for j in range(4):
                        if block[-1][level%10] == (255,255,255): # 白色方塊要畫外框
                            block_rect[0] = block[j][0] * tile + 270
                            block_rect[1] = block[j][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color(all_color[3][level%10]), block_rect)
                            block_rect1[0] = block[j][0] * tile + 270+4
                            block_rect1[1] = block[j][1] * tile + 330+4
                            pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect1)
                            block_rect2[0] = block[j][0] * tile + 270
                            block_rect2[1] = block[j][1] * tile + 330
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                        else:
                            if (block[4] == 2 or block[4] == 4) and (level%10 == 9):
                                block_rect[0] = block[j][0] * tile + 270
                                block_rect[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen,pygame.Color('black'), block_rect)
                                block_rect1[0] = block[j][0] * tile + 270+4
                                block_rect1[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color(block[-1][level%10]), block_rect1)
                            else:
                                block_rect[0] = block[j][0] * tile + 270
                                block_rect[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect)
                                block_rect2[0] = block[j][0] * tile + 270
                                block_rect2[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+4
                                block_rect2[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+8
                                block_rect2[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+4
                                block_rect2[1] = block[j][1] * tile + 330+8
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)

                    pygame.display.update()
                    time.sleep(0.05)
                    if level%10 == 9:
                        screen.blit(gray, (240,90))
                    else:
                        screen.blit(black, (240,90))
                    screen.blit(title_score, (600,100))
                    screen.blit(title_line, (600,220))
                    screen.blit(title_next, (600,340))
                    screen.blit(title_tetrsRate, (140,500))
                    screen.blit(title_burn, (140,600))
                    screen.blit(title_drought, (140,400))
                    screen.blit(title_level, (600,520))
                    screen.blit(title_leaderboard, (20,80))
                    
                    screen.blit(font.render(score, True, pygame.Color('white')), (600,150))
                    screen.blit(font.render("     "+lines, True, pygame.Color('white')), (600,270))
                    screen.blit(font.render(str(tetris_rate)+"%", True, pygame.Color('white')), (160,550))
                    screen.blit(font.render("0"*(3-len(str(burn)))+str(burn), True, pygame.Color('white')), (150,650))
                    screen.blit(font.render("0"*(3-len(str(drought)))+str(drought), True, pygame.Color('white')), (150,450))
                    screen.blit(font.render("0"*(2-len(str(level)))+str(level), True, pygame.Color('white')), (660,570))
                    for j in range(5):
                        screen.blit(font.render(str(j+1)+".", True, pygame.Color('white')), (30,120+j*30))
                        screen.blit(font.render("0"*(6-len(str(leaderboard[j])))+str(leaderboard[j]), True, pygame.Color('white')), (100,120+j*30))
                    # 畫背景格(grid)
                    [pygame.draw.rect(screen,(40,40,40), i_grid,1) for i_grid in grid] # 畫面,顏色,網格,線寬
                    
                    # 畫到底的方塊(field)
                    for y in range(len(field)):
                        for x in range(len(field[y])):
                            if field[y][x] != -1:
                                if field[y][x] == 0 or field[y][x] == 1 or field[y][x] == 6:
                                    block_rect[0] = x * tile
                                    block_rect[1] = y * tile
                                    pygame.draw.rect(screen, pygame.Color(all_color[3][level%10]), block_rect)
                                    block_rect1[0] = x * tile+4
                                    block_rect1[1] = y * tile+4
                                    pygame.draw.rect(screen, pygame.Color('white'), block_rect1)
                                    block_rect2[0] = x * tile
                                    block_rect2[1] = y * tile
                                    pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                else:
                                    if (field[y][x] == 2 or field[y][x] == 4) and (level%9 == 9):
                                        block_rect[0] = x * tile
                                        block_rect[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color('black'), block_rect)
                                        block_rect1[0] = x * tile+4
                                        block_rect1[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color(all_color[field[y][x]][level%10]), block_rect1)
                                    else:
                                        block_rect[0] = x * tile
                                        block_rect[1] = y * tile
                                        pygame.draw.rect(screen, all_color[field[y][x]][level%10], block_rect)
                                        block_rect2[0] = x * tile
                                        block_rect2[1] = y * tile
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+4
                                        block_rect2[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+8
                                        block_rect2[1] = y * tile+4
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                        block_rect2[0] = x * tile+4
                                        block_rect2[1] = y * tile+8
                                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)

                    # 顯示下一個方塊
                    for j in range(4):
                        if block[-1][level%10] == (255,255,255): # 白色方塊要畫外框
                            block_rect[0] = block[j][0] * tile + 270
                            block_rect[1] = block[j][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color(all_color[3][level%10]), block_rect)
                            block_rect1[0] = block[j][0] * tile + 270+4
                            block_rect1[1] = block[j][1] * tile + 330+4
                            pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect1)
                            block_rect2[0] = block[j][0] * tile + 270
                            block_rect2[1] = block[j][1] * tile + 330
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                        else:
                            if (block[4] == 2 or block[4] == 4) and (level%10 == 9):
                                block_rect[0] = block[j][0] * tile + 270
                                block_rect[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen,pygame.Color('black'), block_rect)
                                block_rect1[0] = block[j][0] * tile + 270+4
                                block_rect1[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color(block[-1][level%10]), block_rect1)
                            else:
                                block_rect[0] = block[j][0] * tile + 270
                                block_rect[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect)
                                block_rect2[0] = block[j][0] * tile + 270
                                block_rect2[1] = block[j][1] * tile + 330
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+4
                                block_rect2[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+8
                                block_rect2[1] = block[j][1] * tile + 330+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = block[j][0] * tile + 270+4
                                block_rect2[1] = block[j][1] * tile + 330+8
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                    
                    pygame.display.update()
                    time.sleep(0.05)
                flash = False
                whiteNum += 1
                if whiteNum == 10:
                    whiteNum = 0
            # 消除完墜落
            for i in range(len(field)-1, 2, -1):
                line = i
                while line+1 < len(field) and field[line+1] == [-1 for j in range(w+8)]:
                    line += 1
                if line != i:
                    field[line] = field[i]
                    field[i] = [-1 for j in range(w+8)]
            # 畫背景格(grid)
            [pygame.draw.rect(screen,(40,40,40), i_grid,1) for i_grid in grid] # 畫面,顏色,網格,線寬
            
            if nextDisplay == True:
                # 畫方塊(block)
                for i in range(4):
                    if block[-1][level%10] == (255,255,255): # 白色方塊要畫外框
                        block_rect[0] = block[i][0] * tile
                        block_rect[1] = block[i][1] * tile
                        pygame.draw.rect(screen,pygame.Color(all_color[3][level%10]), block_rect)
                        block_rect1[0] = block[i][0] * tile+4
                        block_rect1[1] = block[i][1] * tile+4
                        pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect1)
                        block_rect2[0] = block[i][0] * tile
                        block_rect2[1] = block[i][1] * tile
                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                    else:
                        if (block[4] == 2 or block[4] == 4) and (level%10 == 9):
                            block_rect[0] = block[i][0] * tile
                            block_rect[1] = block[i][1] * tile
                            pygame.draw.rect(screen,pygame.Color('black'), block_rect)
                            block_rect1[0] = block[i][0] * tile+4
                            block_rect1[1] = block[i][1] * tile+4
                            pygame.draw.rect(screen, pygame.Color(block[-1][level%10]), block_rect1)
                        else:
                            block_rect[0] = block[i][0] * tile
                            block_rect[1] = block[i][1] * tile
                            pygame.draw.rect(screen,pygame.Color(block[-1][level%10]), block_rect)
                            block_rect2[0] = block[i][0] * tile
                            block_rect2[1] = block[i][1] * tile
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = block[i][0] * tile+4
                            block_rect2[1] = block[i][1] * tile+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = block[i][0] * tile+8
                            block_rect2[1] = block[i][1] * tile+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = block[i][0] * tile+4
                            block_rect2[1] = block[i][1] * tile+8
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
            
            # 畫到底的方塊(field)
            for y in range(len(field)):
                for x in range(len(field[y])):
                    if field[y][x] != -1:
                        if field[y][x] == 0 or field[y][x] == 1 or field[y][x] == 6:
                            block_rect[0] = x * tile
                            block_rect[1] = y * tile
                            pygame.draw.rect(screen, pygame.Color(all_color[3][level%10]), block_rect)
                            block_rect1[0] = x * tile+4
                            block_rect1[1] = y * tile+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect1)
                            block_rect2[0] = x * tile
                            block_rect2[1] = y * tile
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                        else:
                            if (field[y][x] == 2 or field[y][x] == 4) and (level%10 == 9):
                                block_rect[0] = x * tile
                                block_rect[1] = y * tile
                                pygame.draw.rect(screen, pygame.Color('black'), block_rect)
                                block_rect1[0] = x * tile+4
                                block_rect1[1] = y * tile+4
                                pygame.draw.rect(screen, pygame.Color(all_color[field[y][x]][level%10]), block_rect1)
                            else:
                                block_rect[0] = x * tile
                                block_rect[1] = y * tile
                                pygame.draw.rect(screen, pygame.Color(all_color[field[y][x]][level%10]), block_rect)
                                block_rect2[0] = x * tile
                                block_rect2[1] = y * tile
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = x * tile+4
                                block_rect2[1] = y * tile+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = x * tile+8
                                block_rect2[1] = y * tile+4
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                                block_rect2[0] = x * tile+4
                                block_rect2[1] = y * tile+8
                                pygame.draw.rect(screen, pygame.Color('white'), block_rect2)

            if nextDisplay == True:
                # 顯示下一個方塊
                for i in range(4):
                    if next_block[-1][level%10] == (255,255,255): # 白色方塊要畫外框
                        block_rect[0] = next_block[i][0] * tile + 270
                        block_rect[1] = next_block[i][1] * tile + 330
                        pygame.draw.rect(screen,pygame.Color(all_color[3][level%10]), block_rect)
                        block_rect1[0] = next_block[i][0] * tile + 270+4
                        block_rect1[1] = next_block[i][1] * tile + 330+4
                        pygame.draw.rect(screen,pygame.Color(next_block[-1][level%10]), block_rect1)
                        block_rect2[0] = next_block[i][0] * tile + 270
                        block_rect2[1] = next_block[i][1] * tile + 330
                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                    else:
                        if (next_block[4] == 2 or next_block[4] == 4) and (level%10 == 9):
                            block_rect[0] = next_block[i][0] * tile + 270
                            block_rect[1] = next_block[i][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color('black'), block_rect)
                            block_rect1[0] = next_block[i][0] * tile + 270+4
                            block_rect1[1] = next_block[i][1] * tile + 330+4
                            pygame.draw.rect(screen, pygame.Color(next_block[-1][level%10]), block_rect1)
                        else:
                            block_rect[0] = next_block[i][0] * tile + 270
                            block_rect[1] = next_block[i][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color(next_block[-1][level%10]), block_rect)
                            block_rect2[0] = next_block[i][0] * tile + 270
                            block_rect2[1] = next_block[i][1] * tile + 330
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = next_block[i][0] * tile + 270+4
                            block_rect2[1] = next_block[i][1] * tile + 330+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = next_block[i][0] * tile + 270+8
                            block_rect2[1] = next_block[i][1] * tile + 330+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = next_block[i][0] * tile + 270+4
                            block_rect2[1] = next_block[i][1] * tile + 330+8
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                        
            else:
                # 顯示現在的方塊
                for i in range(4):
                    if blockcopy[-1][level%10] == (255,255,255): # 白色方塊要畫外框
                        block_rect[0] = blockcopy[i][0] * tile + 270
                        block_rect[1] = blockcopy[i][1] * tile + 330
                        pygame.draw.rect(screen,pygame.Color(all_color[3][level%10]), block_rect)
                        block_rect1[0] = blockcopy[i][0] * tile + 270+4
                        block_rect1[1] = blockcopy[i][1] * tile + 330+4
                        pygame.draw.rect(screen,pygame.Color(blockcopy[-1][level%10]), block_rect1)
                        block_rect2[0] = blockcopy[i][0] * tile + 270
                        block_rect2[1] = blockcopy[i][1] * tile + 330
                        pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                    else:
                        if (blockcopy[4] == 2 or blockcopy[4] == 4) and (level%10 == 9):
                            block_rect[0] = blockcopy[i][0] * tile + 270
                            block_rect[1] = blockcopy[i][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color('black'), block_rect)
                            block_rect1[0] = blockcopy[i][0] * tile + 270+4
                            block_rect1[1] = blockcopy[i][1] * tile + 330+4
                            pygame.draw.rect(screen, pygame.Color(blockcopy[-1][level%10]), block_rect1)
                        else:
                            block_rect[0] = blockcopy[i][0] * tile + 270
                            block_rect[1] = blockcopy[i][1] * tile + 330
                            pygame.draw.rect(screen,pygame.Color(blockcopy[-1][level%10]), block_rect)
                            block_rect2[0] = blockcopy[i][0] * tile + 270
                            block_rect2[1] = blockcopy[i][1] * tile + 330
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = blockcopy[i][0] * tile + 270+4
                            block_rect2[1] = blockcopy[i][1] * tile + 330+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = blockcopy[i][0] * tile + 270+8
                            block_rect2[1] = blockcopy[i][1] * tile + 330+4
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
                            block_rect2[0] = blockcopy[i][0] * tile + 270+4
                            block_rect2[1] = blockcopy[i][1] * tile + 330+8
                            pygame.draw.rect(screen, pygame.Color('white'), block_rect2)
        
        # 遊戲結束
        if gameover == True:
            screen.blit(lose, (300,200))
            screen.blit(again, (300,350))
            screen.blit(over, (300,500))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # 關閉
                    os._exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    leaderboard.append(int(score))
                    leaderboard = sorted(leaderboard)
                    leaderboard.pop(0)
                    f1 = open("score.txt", "w+")
                    for i in range(4,-1,-1):
                        f1.write(str(leaderboard[i])+"\n")
                    f1.close()
                    x, y = event.pos[0],event.pos[1]
                    if x > 300 and x <= 300+200 and y >= 350 and y < 475:
                        victory_sound.stop()
                        lose_sound.stop()
                        main()
                    elif x >= 300 and x <= 300+200 and y >= 500 and y < 625:
                        stop = True
                        os._exit(0)
        
        screen.blit(title_score, (600,100))
        screen.blit(title_line, (600,220))
        screen.blit(title_next, (600,340))
        screen.blit(title_tetrsRate, (140,500))
        screen.blit(title_burn, (140,600))
        screen.blit(title_drought, (140,400))
        screen.blit(title_level, (600,520))
        screen.blit(title_leaderboard, (20,80))

        screen.blit(font.render(str(score), True, pygame.Color('white')), (600,150))
        screen.blit(font.render("     "+lines, True, pygame.Color('white')), (600,270))
        screen.blit(font.render(str(tetris_rate)+"%", True, pygame.Color('white')), (160,550))
        screen.blit(font.render("0"*(3-len(str(burn)))+str(burn), True, pygame.Color('white')), (150,650))
        screen.blit(font.render("0"*(3-len(str(drought)))+str(drought), True, pygame.Color('white')), (150,450))
        screen.blit(font.render("0"*(2-len(str(level)))+str(level), True, pygame.Color('white')), (660,570))
        for i in range(5):
            screen.blit(font.render(str(i+1)+".", True, pygame.Color('white')), (30,120+i*30))
            screen.blit(font.render("0"*(6-len(str(leaderboard[i])))+str(leaderboard[i]), True, pygame.Color('white')), (100,120+i*30))
        
        pygame.display.flip()
        clock.tick(fps)

main()