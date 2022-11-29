import pygame
import time
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, Gravity 
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Ship, Meteor, Bullet, Explosion, Nuvem, Nuvem2, Predio2, Predio3, Predio4


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()
    all_nuvens = pygame.sprite.Group()
    all_nuvens2 = pygame.sprite.Group()
    all_predios2 = pygame.sprite.Group()
    all_predios3 = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    all_predios4 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_meteors'] = all_meteors
    groups['all_bullets'] = all_bullets
    groups['all_nuvens'] = all_nuvens
    groups['all_nuvens2'] = all_nuvens2
    groups['all_predios2'] = all_predios2
    groups['all_predios3'] = all_predios3
    groups['all_predios4'] = all_predios4


    # Criando o jogador
    player = Ship(groups, assets)
    all_sprites.add(player)
    # Criando os meteoros
    for i in range(8):
        meteor = Meteor(assets)
        all_sprites.add(meteor)
        all_meteors.add(meteor)
    for j in range(2):
        nuvem = Nuvem(assets) 
        all_sprites.add(nuvem)
        all_nuvens.add(nuvem)
    for k in range(2):
        nuvem2 = Nuvem2(assets) 
        all_sprites.add(nuvem2)
        all_nuvens2.add(nuvem2)
    for z in range(8):
        predio2 = Predio2(assets)
        all_sprites.add(predio2)
        all_predios2.add(predio2)
    for w in range(8):
        predio3 = Predio3(assets)
        all_sprites.add(predio3)
        all_predios3.add(predio3)
    for y in range(8):
        predio4 = Predio4(assets)
        all_sprites.add(predio4)
        all_predios4.add(predio4)

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE: 
                        player.speedy -= 12
        
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()   
        if state == PLAYING:
            
            score += 1

            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True, pygame.sprite.collide_mask)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                assets[DESTROY_SOUND].play()
                m = Meteor(assets)
                all_sprites.add(m)
                all_meteors.add(m)

                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(meteor.rect.center, assets)
                all_sprites.add(explosao)

                # Ganhou pontos!
                score += 100
                if score % 1000 == 0:
                    lives += 1

            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_meteors, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                m = Meteor(assets)
                all_sprites.add(m)
                all_meteors.add(m)
                score = 0 

            hits2 = pygame.sprite.spritecollide(player, all_nuvens, True, pygame.sprite.collide_mask)
            if len(hits2) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                n2 = Nuvem(assets)
                all_sprites.add(n2)
                all_nuvens.add(n2)
                score = 0

            hits3 = pygame.sprite.spritecollide(player, all_nuvens2, True, pygame.sprite.collide_mask)
            if len(hits3) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                n3 = Nuvem2(assets)
                all_sprites.add(n3)
                all_nuvens2.add(n3)
                score = 0 
            
            hits4 = pygame.sprite.spritecollide(player, all_predios2, True, pygame.sprite.collide_mask)
            if len(hits4) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                n4 = Predio2(assets)
                all_sprites.add(n4)
                all_predios2.add(n4)
                score = 0 

            hits5 = pygame.sprite.spritecollide(player, all_predios3, True, pygame.sprite.collide_mask)
            if len(hits5) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                n5 = Predio3(assets)
                all_sprites.add(n5)
                all_predios3.add(n5)
                score = 0 

            hits6 = pygame.sprite.spritecollide(player, all_predios4, True, pygame.sprite.collide_mask)
            if len(hits6) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
                n6 = Predio4(assets)
                all_sprites.add(n6)
                all_predios3.add(n6)
                score = 0 



        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives <= 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
        all_nuvens.draw(window)
        all_nuvens2.draw(window)
        all_predios2.draw(window)
        all_predios3.draw(window)
        all_predios4.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
