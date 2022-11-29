import pygame
import os
from config import PREDIO_WIDTH, PREDIO_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR, PREDIO_WIDTH1, PREDIO_HEIGHT1, NUVEM_WIDTH, NUVEM_HEIGHT, PREDIO2_WIDTH, PREDIO2_HEIGHT


BACKGROUND = 'background'
PREDIO_IMG = 'predio_img'
PREDIO_IMG2 = 'predio_img2'
SHIP_IMG = 'ship_img'
SHIP_IMG = 'ship_img'
BULLET_IMG = 'bullet_img'
EXPLOSION_ANIM = 'explosion_anim'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'
DESTROY_SOUND = 'destroy_sound'
PEW_SOUND = 'pew_sound'
NUVEM = 'nuvem'
NUVEM2 = 'nuvem2'
PREDIO2 = 'predio2'
PREDIO3 = 'predio3'
PREDIO4 = 'predio4'

def load_assets():
    assets = {}
    assets[PREDIO4] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial_2.png')).convert_alpha()
    assets[PREDIO4] = pygame.transform.scale(assets['predio4'], (PREDIO2_WIDTH, PREDIO2_HEIGHT))
    assets[PREDIO3] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial.png')).convert_alpha()
    assets[PREDIO3] = pygame.transform.scale(assets['predio3'], (PREDIO_WIDTH, PREDIO_HEIGHT))
    assets[PREDIO2] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial.png')).convert_alpha()
    assets[PREDIO2] = pygame.transform.scale(assets['predio2'], (PREDIO2_WIDTH, PREDIO2_HEIGHT))
    assets[NUVEM] = pygame.image.load(os.path.join(IMG_DIR, 'nuvem.png')).convert_alpha()
    assets[NUVEM] = pygame.transform.scale(assets['nuvem'], (NUVEM_WIDTH, NUVEM_HEIGHT))
    assets[NUVEM2] = pygame.image.load(os.path.join(IMG_DIR, 'nuvem2.png')).convert_alpha()
    assets[NUVEM2] = pygame.transform.scale(assets['nuvem2'], (NUVEM_WIDTH, NUVEM_HEIGHT))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'city_background.png')).convert()
    assets[PREDIO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial.png')).convert_alpha()
    assets[PREDIO_IMG] = pygame.transform.scale(assets['predio_img'], (PREDIO_WIDTH, PREDIO_HEIGHT))
    assets[PREDIO_IMG2] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial_2.png')).convert_alpha()
    assets[PREDIO_IMG2] = pygame.transform.scale(assets['predio_img2'], (PREDIO_WIDTH1, PREDIO_HEIGHT1))
    assets[SHIP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[SHIP_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[BULLET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()
    explosion_anim = []
    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        explosion_anim.append(img)
    assets[EXPLOSION_ANIM] = explosion_anim
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[DESTROY_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[PEW_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets
