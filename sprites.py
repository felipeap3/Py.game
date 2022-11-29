import random
import pygame
import time
from config import WIDTH, HEIGHT, METEOR_WIDTH, METEOR_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, Gravity, METEOR_HEIGHT2, METEOR_WIDTH2, NUVEM_WIDTH, NUVEM_HEIGHT, JOGA, PREDIO2_HEIGHT, PREDIO2_WIDTH
from assets import SHIP_IMG, PEW_SOUND, METEOR_IMG, BULLET_IMG, EXPLOSION_ANIM, METEOR_IMG2, NUVEM, NUVEM2, PREDIO2, PREDIO3, PREDIO4

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[SHIP_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        # self.rect.bottom = HEIGHT - 10
        self.speedy = 0
        self.groups = groups
        self.assets = assets

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        # Atualização da posição da nave
        
        self.speedy += Gravity
        self.rect.y += self.speedy 
        if self.speedy > 7:
            self.speedy -= 1
        # Mantem dentro da tela

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_bullets'].add(new_bullet)
            self.assets[PEW_SOUND].play()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets[METEOR_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH
        self.rect.centery = HEIGHT 
        self.speedx = -4
       
    def update(self):
        # Atualizando a posição do obstaculo
        self.rect.x += self.speedx
        # cria novo obstaculo quando ele sai da tela
        if self.rect.left < 0:
            self.rect.centerx = WIDTH
            self.rect.centery = HEIGHT 
            self.speedx = -4

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BULLET_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

# Classe que representa uma explosão de meteoro
class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = assets[EXPLOSION_ANIM]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Nuvem(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets[NUVEM]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH
        self.rect.centery = random.randint(0, HEIGHT/2)
        self.speedx = -6

    def update(self):
        # Atualizando a posição da nuvem 
        self.rect.x += self.speedx
        # recoloca a nuvem que saiu no inicio da tela 
        if self.rect.left < 0:
            self.rect.centerx = WIDTH 
            self.rect.centery = random.randint(0, HEIGHT/2) 
            self.speedx = -6

class Nuvem2(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets[NUVEM2]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH + WIDTH / 2 
        self.rect.centery = random.randint(0, HEIGHT/2)
        self.speedx = -6

    def update(self):
        # Atualizando a posição da nuvem 
        self.rect.x += self.speedx
        # recoloca a nuvem que saiu no inicio da tela 
        if self.rect.left < 0:
            self.rect.centerx = WIDTH
            self.rect.centery = random.randint(0, HEIGHT/2) 
            self.speedx = -6
            
class Predio2(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets[PREDIO2]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH + WIDTH/1.3  
        self.rect.centery = HEIGHT 
        self.speedx = -4
       
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        # cria novo obstaculo quando ele sai da tela
        if self.rect.left < 0:
            self.rect.centerx = WIDTH
            self.rect.centery = HEIGHT 
            self.speedx = -4

class Predio3(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets[PREDIO3]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH + WIDTH/2
        self.rect.centery = HEIGHT 
        self.speedx = -4
       
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        # cria novo obstaculo quando ele sai da tela
        if self.rect.left < 0:
            self.rect.centerx = WIDTH
            self.rect.centery = HEIGHT 
            self.speedx = -4
    
class Predio4(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets[PREDIO4]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH + WIDTH / 4
        self.rect.centery = HEIGHT 
        self.speedx = -4
       
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        # cria novo obstaculo quando ele sai da tela
        if self.rect.left < 0:
            self.rect.centerx = WIDTH  
            self.rect.centery = HEIGHT 
            self.speedx = -4
