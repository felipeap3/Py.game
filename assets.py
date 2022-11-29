import pygame
import os
from config import METEOR_WIDTH, METEOR_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR, METEOR_WIDTH2, METEOR_HEIGHT2, NUVEM_WIDTH, NUVEM_HEIGHT


BACKGROUND = 'background'
METEOR_IMG = 'meteor_img'
METEOR_IMG2 = 'meteor_img2'
METEOR_IMG = 'meteor_img'
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

def load_assets():
    assets = {}
    assets[NUVEM] = pygame.image.load(os.path.join(IMG_DIR, 'nuvem.png')).convert_alpha()
    assets[NUVEM] = pygame.transform.scale(assets['nuvem'], (NUVEM_WIDTH, NUVEM_HEIGHT))
    assets[NUVEM2] = pygame.image.load(os.path.join(IMG_DIR, 'nuvem2.png')).convert_alpha()
    assets[NUVEM2] = pygame.transform.scale(assets['nuvem2'], (NUVEM_WIDTH, NUVEM_HEIGHT))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'starfield.png')).convert()
    assets[METEOR_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial.png')).convert_alpha()
    assets[METEOR_IMG] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))
    assets[METEOR_IMG2] = pygame.image.load(os.path.join(IMG_DIR, 'obstaculo_oficial_2.png')).convert_alpha()
    assets[METEOR_IMG2] = pygame.transform.scale(assets['meteor_img2'], (METEOR_WIDTH2, METEOR_HEIGHT2))
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
