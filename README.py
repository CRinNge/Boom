from pygame import*
game = True
clock = time.Clock()
okno = display.set_mode((500,500))
back1 = transform.scale(image.load("asd.jpg"), (500,500))
back2 = transform.scale(image.load("asd.jpg"), (500,500))
back3 = transform.scale(image.load("asd.jpg"), (500,500))
x1 = 0
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (90,50))
        self.image = transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class ship(GameSprite):
    def control(self):
        knopka = key.get_pressed()
        if knopka[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if knopka[K_RIGHT] and self.rect.x < 450:
            self.rect.x += 5
        
class pula(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (30,30))
        self.image = transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def letit(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.y -= 10

from random import*
class enemy(GameSprite):
    def taran(self):
        self.ris()
        self.rect.y += 3
        if self.rect.y > 500:
            self.rect.x = randint(0,450)
            self.rect.y = -50
            #self.image = transform.rotate(self.image, 50)


            

golova = ship("sf.png",130,450)
p1 = pula("ga.png",130,450)

invad = [
enemy("asdf2.jpg", 0,0),
enemy("asdf2.jpg", 0,0),
enemy("asdf2.jpg", 0,0)]

finish = False

#переносим фонт.инит
font.init()
lives = 5 #создаем счётчик жизней
UI = font.Font(None, 40) # создаем объект для рисования игровой информации

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYUP:
            if i.key == K_SPACE and p1.rect.y <0:
                p1.rect.x = golova.rect.x
                p1.rect.y = golova.rect.y
    okno.blit(back1,(0,-500-x1))
    okno.blit(back2,(0, 0-x1))
    okno.blit(back3,(0,500-x1))
    zhizn = UI.render(str(lives), True, (255,255,0)) #генерим надпись с текущим количеством жизней
    okno.blit(zhizn, (400, 30)) #помещаем на экран
    x1 -= 1
    golova.ris()
    golova.control()
    p1.letit() #отрисовка пули
    for i in invad:   # invad = это теперь список!
        i.taran()
        if sprite.collide_rect(i, p1):
            i.rect.x = randint(0,450)
            i.rect.y = -50
        if sprite.collide_rect(i, golova):
            finish = True
            #game = False
            i.rect.x = randint(0,450)
            i.rect.y = -50
        #invad.image = transform.rotate(invad.image, 50)
    if x1 >499:
        x1=0
    if x1 < -499:
        x1 = 0
    clock.tick(60)
    display.update()

pisatel = font.Font(None, 70) #создание объекта создающего надписи
text = pisatel.render("Ты проиграл", True, (0,0,0)) # даем ему команду создать надпись

while finish:
    for i in event.get():
        if i.type == QUIT:
            finish = False
    okno.fill((100,0,0)) #окно заливается краской
    okno.blit(text, (100,250)) # окно показывает надпись
    display.update()


