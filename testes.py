
# class Ship(pygame.sprite.Sprite):
#     def __init__(self, groups, assets):
#         # Construtor da classe mãe (Sprite).
#         pygame.sprite.Sprite.__init__(self)

#         self.image = assets[SHIP_IMG]
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH / 2
#         self.rect.bottom = HEIGHT - 10
#         self.speedy = 0
#         self.groups = groups
#         self.assets = assets

#         # Só será possível atirar uma vez a cada 500 milissegundos
#         self.last_shot = pygame.time.get_ticks()
#         self.shoot_ticks = 500

#     def update(self):
#         # Atualização da posição da nave
         
#         self.speedy -= GRAVITY
#         if self.speedy > 0:
#             self.state = FALLING

#         self.rect.y += self.speedy

#         # Mantem dentro da tela
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left < 0:
#             self.rect.left = 0