import pygame
pygame.font.init()
w = pygame.display.set_mode((500, 500))
a = 0
b = 0
d = 500 / 9
v= 0
e =[
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]
 

f = pygame.font.SysFont("arial", 40)
g = pygame.font.SysFont("arial", 20)
def h(j):
    global a
    a = j[0]//d
    global b
    b = j[1]//d

def i():
    for k in range(2):
        pygame.draw.line(w, (0, 0, 0), (a * d-3, (b + k)*d), (a * d + d + 3, (b + k)*d), 7)
        pygame.draw.line(w, (0, 0, 0), ( (a + k)* d, b * d ), ((a + k) * d, b * d + d), 7)  
       
def j():
    for l in range (9):
        for m in range (9):
            if e[l][m]!= 0:
                pygame.draw.rect(w, (255, 255, 0), (l * d, m * d, d + 1, d + 1))
                n = f.render(str(e[l][m]), 1, (0, 0, 0))
                w.blit(n, (l * d + 15, m * d + 15))         
    for o in range(10):
        if o % 3 == 0 :
            p = 7
        else:
            p = 1
        pygame.draw.line(w, (0, 0, 0), (0, o * d), (500, o * d), p)
        pygame.draw.line(w, (0, 0, 0), (o * d, 0), (o * d, 500), p)     
 
    
def q(value):
    n = f.render(str(value), 1, (0, 0, 0))
    w.blit(n, (a * d + 15, b * d + 15))   
 

def r():
    n = f.render("Wrong!", 1, (0, 0, 0))
    w.blit(n, (20, 570)) 
def s():
    n = f.render("wrong! Enter a valid key for the game", 1, (0, 0, 0))
    w.blit(n, (20, 570)) 
 
def t(u, k, l, value):
    for it in range(9):
        if u[k][it]== value:
            return False
        if u[it][l]== value:
            return False
    it = k//3
    jt = l//3
    for k in range(it * 3, it * 3 + 3):
        for l in range (jt * 3, jt * 3 + 3):
            if u[k][l]== value:
                return False
    return True
def v(w, k, l):
     
    while w[k][l]!= 0:
        if k<8:
            k+= 1
        elif k == 8 and l<8:
            k = 0
            l+= 1
        elif k == 8 and l == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if t(w, k, l, it)== True:
            w[k][l]= it
            global a, b
            a = k
            b = l
            Window.fill((255, 255, 255))
            j()
            i()
            pygame.display.update()
            pygame.time.delay(20)
            if v(w, k, l)== 1:
                return True
            else:
                w[k][l]= 0
            w.fill((0,0,0))
         
            j()
            i()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 
def x():
    n = f.render("game finished", 1, (0, 0, 0))
    w.blit(n, (20, 570)) 
flag=True  
y = 0
z = 0
rs = 0
error = 0
while flag:
    w.fill((255,182,193))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            y = 1
            pos = pygame.mouse.get_pos()
            h(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                a-= 1
                y = 1
            if event.key == pygame.K_RIGHT:
                a+= 1
                y = 1
            if event.key == pygame.K_UP:
                b-= 1
                y = 1
            if event.key == pygame.K_DOWN:

                b+= 1
                y = 1   
            if event.key == pygame.K_1:
                v = 1
            if event.key == pygame.K_2:
                v = 2   
            if event.key == pygame.K_3:
                v = 3
            if event.key == pygame.K_4:
                v = 4
            if event.key == pygame.K_5:
                v = 5
            if event.key == pygame.K_6:
                v = 6
            if event.key == pygame.K_7:
                v = 7
            if event.key == pygame.K_8:
                v = 8
            if event.key == pygame.K_9:
                v = 9 
            if event.key == pygame.K_RETURN:
                z = 1  
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                z = 0
                e=[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                z = 0
                e  =[
                    [0, 0, 4, 0, 6, 0, 0, 0, 5],
                    [7, 8, 0, 4, 0, 0, 0, 2, 0],
                    [0, 0, 2, 6, 0, 1, 0, 7, 8],
                    [6, 1, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 7, 5, 4, 0, 0, 6, 1],
                    [0, 0, 1, 7, 5, 0, 9, 3, 0],
                    [0, 7, 0, 3, 0, 0, 0, 1, 0],
                    [0, 4, 0, 2, 0, 6, 0, 0, 7],
                    [0, 2, 0, 0, 0, 7, 4, 0, 0],
                ]
    if z == 1:
        if v(e , 0, 0)== False:
            error = 1
        else:
            rs = 1
        z = 0   
    if v != 0:           
        q(v)
        if t(e , int(a), int(b), v)== True:
            e[int(a)][int(b)]= v
            y = 0
        else:
            e[int(a)][int(b)]= 0
            s()  
        v = 0   
       
    if error == 1:
        r() 
    if rs == 1:
        x()       
    j() 
    if y == 1:
        i()      
    pygame.display.update() 
   
pygame.quit()