import pygame
import time
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, Gravity, GREEN 
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Ship, Predio, Bullet, Explosion, Nuvem, Nuvem2, Predio2, Predio3, Predio4


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # criando os grupos
    all_sprites = pygame.sprite.Group()
    all_predios = pygame.sprite.Group()
    all_nuvens = pygame.sprite.Group()
    all_nuvens2 = pygame.sprite.Group()
    all_predios2 = pygame.sprite.Group()
    all_predios3 = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    all_predios4 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_predios'] = all_predios
    groups['all_bullets'] = all_bullets
    groups['all_nuvens'] = all_nuvens
    groups['all_nuvens2'] = all_nuvens2
    groups['all_predios2'] = all_predios2
    groups['all_predios3'] = all_predios3
    groups['all_predios4'] = all_predios4


    # Criando o jogador
    player = Ship(groups, assets)
    all_sprites.add(player)
    # Criando os predios
    for i in range(8):
        predio = Predio(assets)
        all_sprites.add(predio)
        all_predios.add(predio)
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

    #estados do jogo
    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING


    keys_down = {}
    #variaveis que serao utilizadas
    score = 0
    lives = 1
    placar = False

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
                    # Se aperta espaço muda a velocidade
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE: 
                        player.speedy -= 12
        
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos sprites
        all_sprites.update()   
        if state == PLAYING:
            
            score += 1

            # Verifica se houve colisão entre nave e obstaculos
            hits = pygame.sprite.spritecollide(player, all_predios, True, pygame.sprite.collide_mask)
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
                #readiciona os sprites
                m = Predio(assets)
                all_sprites.add(m)
                all_predios.add(m)

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
                #readiciona os sprites
                n2 = Nuvem(assets)
                all_sprites.add(n2)
                all_nuvens.add(n2)

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
                #readiciona os sprites
                n3 = Nuvem2(assets)
                all_sprites.add(n3)
                all_nuvens2.add(n3) 
            
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
                #readiciona os sprites
                n4 = Predio2(assets)
                all_sprites.add(n4)
                all_predios2.add(n4)

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
                #readiciona os sprites
                n5 = Predio3(assets)
                all_sprites.add(n5)
                all_predios3.add(n5)

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
                #readiciona os sprites
                n6 = Predio4(assets)
                all_sprites.add(n6)
                all_predios3.add(n6)

        #encerra o jogo
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives <= 0:
                    state = DONE
                    placar = True
                else:
                    state = PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preta
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando os sprites
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

        #desenhando o score ao final do jogo
        if placar == True:
            text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, RED)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  HEIGHT/3 + 120)
            window.blit(text_surface, text_rect)
            pygame.display.update()
            time.sleep(3)
            

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
