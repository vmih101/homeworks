import pygame
import random
from os import path
from PIL import Image, ImageSequence

#window size
display_width = 800 
display_height = 680
fps = 45

# pygame initialization
pygame.init()
pygame.mixer.init()

# window creation
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space invaders')

# frame rate
clock = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# way to game folder
game_folder = path.dirname(__file__)

# way to images and sounds folders
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(path.dirname(__file__), 'snd')

# images and sounds initialization
ship_img = pygame.image.load(path.join(img_folder, 'ship.png')).convert()
meteor_img = pygame.image.load(path.join(img_folder, 'meteor.png')).convert()
laser_img = pygame.image.load(path.join(img_folder, 'laser.png')).convert()
laser_shot_img = pygame.image.load(path.join(img_folder, 'laser_shot.png')).convert()
start_bg = pygame.image.load(path.join(img_folder, 'bg.png')).convert()
logo_title = pygame.image.load(path.join(img_folder, 'logo.png')).convert()
background_rect = start_bg.get_rect()
shoot_sound = pygame.mixer.Sound(path.join(snd_folder, 'laser_shoot.wav'))
explosion_sound = pygame.mixer.Sound(path.join(snd_folder, 'explosion.wav'))
crash_sound = pygame.mixer.Sound(path.join(snd_folder, 'crash.wav'))
select_sound = pygame.mixer.Sound(path.join(snd_folder, 'select.wav'))
# main soundtrack
pygame.mixer.music.load(path.join(snd_folder, 'music.mp3'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

# fucntion for ussing gifs
def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames

# function for text rendering
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('retro.ttf', size)
    text_surface = font.render(text, False, yellow)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# start screen 
def start_end_screen():
    screen.blit(start_bg, background_rect)
    screen.blit(logo_title, (display_width / 2 - 350, 80)) 
    draw_text(screen, f"Score: {score}", 54, display_width / 2, 350)
    draw_text(screen, "Control:", 35, display_width / 2, 450)
    draw_text(screen, "Press arrows to move", 22, display_width / 2, 500)
    draw_text(screen, "and 'space' to fire", 22, display_width / 2, 530)
    draw_text(screen, "Press ENTER to start new game", 18, display_width / 2, 600)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    select_sound.play()
                    waiting = False

# function for adding new asteroids after killing
def new_asteroid():
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)

# All sprites

# Background gif sprite
class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image_index = 0
    def update(self):
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]

# Explosion gif sprite
class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self, images, center):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image_index = 0
        self.image.set_colorkey(black)
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.image_index += 1
            self.image = self.images[self.image_index % len(self.images)]
            if self.image_index == 1:
                explosion_sound.play()            
            if self.image_index == len(self.images):
                self.kill()

# Ship sprite
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship_img
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(ship_img, (80, 80))
        self.rect = self.image.get_rect()
        self.radius = 35
        self.rect.centerx = display_width/2
        self.rect.bottom = display_height - 10
        
        

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -6
        if keystate[pygame.K_RIGHT]:
            self.speedx = 6
        if keystate[pygame.K_UP]:
            self.speedy = -6
        if keystate[pygame.K_DOWN]:
            self.speedy = 6
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > display_width:
            self.rect.right = display_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > display_height:
            self.rect.bottom = display_height

    def shoot(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        all_sprites.add(laser)
        lasers.add(laser)
        laser_shot = Laser_shot(self.rect.centerx, self.rect.top)
        all_sprites.add(laser_shot)

# Asteroid sprite    
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.size = random.choice((range(30, 80, 10)))
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(meteor_img, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(display_width - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(4, 12)   
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > display_height + 10 or self.rect.left < -25 or self.rect.right > display_width + 20:
            self.rect.x = random.randrange(display_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Laser sprite        
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        # self.image = pygame.Surface((10, 10))
        # self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

# Shot flash sprite
class Laser_shot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.last = pygame.time.get_ticks()
        self.cooldown = 0.1
        self.image = laser_shot_img
        self.image.set_colorkey(black)
        # self.image = pygame.Surface((10, 10))
        # self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            shoot_sound.play()
            self.kill()

# convert gif
gif_background = loadGIF('img/space.gif')
background = AnimatedSpriteObject(gif_background)
gif_explosion = loadGIF('img/explosion.gif')

# sprites adding
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
lasers = pygame.sprite.Group()
ship = Ship()
laser_shot = Laser_shot(ship.rect.centerx, ship.rect.centery)
all_sprites.add(background)
all_sprites.add(ship)

# Adjust the value of asteroids
for i in range(8):
    new_asteroid()



# game cycle boolean
running = True
# state of the game
game_over = True

score = 0



# game cycle
while running: 

    # frame rate
    clock.tick(fps) 
    
    if game_over:
        start_end_screen()
        # restart all sprites
        all_sprites = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        lasers = pygame.sprite.Group()
        ship = Ship()
        laser_shot = Laser_shot(ship.rect.centerx, ship.rect.centery)
        all_sprites.add(background)
        all_sprites.add(ship)
        # restart asteroids
        for i in range(8):
            new_asteroid()
        # reset score and state
        score = 0
        game_over = False

    # cycle for checking input
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    # collision detection(beetween ship and asteroid)
    collide = pygame.sprite.spritecollide(ship, asteroids, False, pygame.sprite.collide_circle)
    if collide:
        crash_sound.play()
        game_over = True
    

    # collision detection(beetween lasers and asteroid)
    hits = pygame.sprite.groupcollide(asteroids, lasers, True, True)
    
    # add new mob and initiallize explosion animation
    for hit in hits:
        score += 1
        a = Asteroid()
        all_sprites.add(a) 
        asteroids.add(a)
        expl = AnimatedExplosion(gif_explosion, hit.rect.center)
        all_sprites.add(expl)
                 
    
    all_sprites.update()
    all_sprites.draw(screen)
    draw_text(screen, f'Score: {str(score)}', 25, 90, 10)
    pygame.display.flip()    

# close program
pygame.quit()
exit()





