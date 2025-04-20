from pygame import*
from random import*
from time import time as timer

class PiterParcker(sprite.Sprite):
    def __init__(self,pi,px,py,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pi),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class wall(sprite.Sprite):
    def __init__(self,c1,c2,c3,wax,way,wawi,wahe):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = wawi
        self.heigth = wahe
        self.image = Surface((self.width,self.heigth))
        self.image.fill((c1,c2,c3))
        self.rect = self.image.get_rect()
        self.rect.x = wax
        self.rect.y = way
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Zlodey(PiterParcker):
    def update(self):
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        def colliderect(self, rect):
            return self.rect.colliderect(rect)
class Player(PiterParcker):
    def update(self):
        stena.rect.x += speidx
        stena.rect.y += speidy
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            stena.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < win_heigth - 200:
            stena.rect.y += 5
    def fire1(self):
        pulleto = Pula(dd2,self.rect.centerx,self.rect.top,100,70)
        pulletos.add(pulleto)
    def fire2(self):
        pullet = Pula1('aise.png',self.rect.centerx,self.rect.top,10,1000)

class Player2(PiterParcker):
    def update(self):
        stena2.rect.x += speidx
        stena2.rect.y += speidy
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            stena2.rect.y -= 5
        if keys[K_s] and self.rect.y < win_heigth - 200:
            stena2.rect.y += 5
    def fire(self):
        pullet = Pula1(dd,self.rect.centerx,self.rect.top,100,70)
        pullets.add(pullet)
class Pula1(PiterParcker):
    def update(self):
        self.rect.x += spb
        self.rect.y == ball.rect.y
        if self.rect.x > 1000:
            self.kill()
class Pula(PiterParcker):
    def update(self):
        self.rect.x += spd
        self.rect.y == ball.rect.y
        if self.rect.x < -100:
            self.kill()
win_width = 1000
win_heigth = 600
window = display.set_mode((win_width,win_heigth))
display.set_caption('BKJV')
bacugan = transform.scale(image.load("terraria.png"), (win_width,win_heigth))
ball = Zlodey('ball.png',450,win_heigth-100,60,100)
stena = Player('stena.png',870,300,80,200)
stena2 = Player2('stena2.png',50,300,80,200)

dd = "aise.png"
dd2 = 'aise2.png'
pullets = sprite.Group()
pulletos = sprite.Group()
spd = -6
spb = 6

rel_time1 = False
   
num_fire1 = 0

rel_time2 = False
   
num_fire2 = 0

rx = 920
ry = 550
lx = 30
ly = 550

pulletk5 = PiterParcker('aise2.png',rx,ry,50,40)
pulletk = PiterParcker('aise.png',lx,ly,50,40)



speed_x = 6
speed_y = -3
speidx = 0
speidy = 0
font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None,36)   
win = font1.render('Levii Win!',True,(173, 10, 10))
lose = font1.render('Pravii Win!',False,(173, 10, 10))

w1 = wall(102, 51, 51,0 ,0 ,1000, 1)
w2 = wall(102, 51, 51,0 ,0 ,1, 600)
w3 = wall(102, 51, 51,0 ,599 ,1000, 1)
w4 = wall(102, 51, 51,1000 ,0 ,90, 600)

game = True
FPS = 60
clock = time.Clock()
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_e:
                if num_fire1 < 1 and rel_time1 == False:
                    
                    num_fire1 = num_fire1 + 1
                    stena2.fire()

                    if num_fire1 >= 1 and rel_time1 == False:
                        pulletk.kill()
                        last_time1 = timer()
                        rel_time1 = True                
            if e.key == K_LEFT:
                if num_fire2 < 1 and rel_time2 == False:

                    num_fire2 = num_fire2 + 1
                    stena.fire1()

                if num_fire2 >= 1 and rel_time2 == False:
                    pulletk5.kill()
                    last_time2 = timer()
                    rel_time2 = True 
                

    if finish != True:
        window.blit(bacugan,(0,0))
        ball.update()
        ball.reset()
        stena.update()
        stena.reset()
        stena2.update()
        stena2.reset()
        pulletk.update()
        pulletk.reset()
        pulletk5.update()
        pulletk5.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        pullets.update()
        pullets.draw(window)
        pulletos.update()
        pulletos.draw(window)

        if ball.rect.colliderect(stena.rect):
            speed_x *= -1
        if ball.rect.colliderect(w1.rect):
            speed_y *= -1
        if ball.rect.colliderect(stena2.rect):
            speed_x *= -1
        if ball.rect.colliderect(w3.rect):
            speed_y *= -1
        if ball.rect.colliderect(w4.rect):
            finish = True
            window.blit(win,(400,450))
            stenn = PiterParcker("stena2.png",460,250,80,200)
            stenn.update()
            stenn.reset()
        if ball.rect.colliderect(w2.rect):
            finish = True
            window.blit(lose,(400,450))
            stenn2 = PiterParcker("stena.png",460,250,80,200)
            stenn2.update()
            stenn2.reset()
        if rel_time1 == True:
            now_time1 = timer()
            
            if now_time1 - last_time1 < 5:
                reload1 = font2.render('Всевидящее око перезаряжается...',1,(150,0,0))
                window.blit(reload1,(50,500))
                lx = -100
            else:
                num_fire1 = 0
                rel_time1 = False
        if rel_time2 == True:
            now_time2 = timer()
            
            if now_time2 - last_time2 < 5:
                reload2 = font2.render('Всевидящее око перезаряжается...',1,(150,0,0))
                window.blit(reload2,(560,500))
                lx = -100
            else:
                num_fire2 = 0
                rel_time2 = False
        if sprite.spritecollide(stena,pullets,False):
            finish = True
            window.blit(win,(400,450))
            stenn = PiterParcker("stena2.png",460,250,80,200)
            stenn.update()
            stenn.reset()
        if sprite.spritecollide(stena2,pulletos,False):
            finish = True
            window.blit(lose,(400,450))
            stenn2 = PiterParcker("stena.png",460,250,80,200)
            stenn2.update()
            stenn2.reset()

        
    display.update()
    
    clock.tick(FPS)
