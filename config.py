from os import path
import random

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 1280 # Largura da tela
HEIGHT = 720 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
PREDIO_WIDTH = 60
PREDIO_HEIGHT = 500

PREDIO_WIDTH1 = 80
PREDIO_HEIGHT1 = 400

SHIP_WIDTH = 80
SHIP_HEIGHT = 50

NUVEM_WIDTH = 160
NUVEM_HEIGHT = 110

PREDIO2_WIDTH = 110 
PREDIO2_HEIGHT = 360
# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

Gravity = 0.5
JOGA = True