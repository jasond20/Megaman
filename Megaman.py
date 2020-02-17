'''Author: Jason Dai

    Date: May 30, 2017

    Description: A game based on the game Megaman X, consists of a room where
    you fight a Boss as megaman.
'''


# I - IMPORT AND INITIALIZE
import pygame, random, os, MegamanSprites
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
pygame.init()


 

def main():
    '''This function defines the 'mainline logic' for our Megaman game.'''
      
    # DISPLAY
    pygame.display.set_caption("Megaman X")
    screen = pygame.display.set_mode((640, 480)) 
    background = pygame.image.load(os.path.join("Environment", "Background.png"))
    screen.blit(background, (0, 0))
    # ENTITIES
    # Creates main character sprites
    megaman = MegamanSprites.Player(screen)
    megamanlife = MegamanSprites.Player_Lifebar()
    boss = MegamanSprites.Boss(screen)
    bosslife = MegamanSprites.Boss_Lifebar()
    # Assigns Music and Sound
    pygame.mixer.music.load(os.path.join("Sound", "Background.ogg"))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    # Boss Sounds
    hit_boss = pygame.mixer.Sound(os.path.join("Sound", "BossHit.wav"))
    hit_boss.set_volume(0.6)
    boss_jump = pygame.mixer.Sound(os.path.join("Sound", "BossJump.wav"))
    boss_jump.set_volume(0.6)   
    boss_dash = pygame.mixer.Sound(os.path.join("Sound", "BossDash.wav"))
    boss_dash.set_volume(0.5) 
    # Megaman Sounds
    megaman_die = pygame.mixer.Sound(os.path.join("Sound", "Die.wav"))
    megaman_die.set_volume(0.8)    
    charge1 = pygame.mixer.Sound(os.path.join("Sound", "Charge1.wav"))
    charge1.set_volume(0.2)
    charge2 = pygame.mixer.Sound(os.path.join("Sound", "Charge2.wav"))
    charge2.set_volume(0.4)
    megaman_jump = pygame.mixer.Sound(os.path.join("Sound", "MegamanJump.wav"))
    megaman_jump.set_volume(0.5)   
    megaman_dash = pygame.mixer.Sound(os.path.join("Sound", "MegamanDash.wav"))
    megaman_dash.set_volume(0.5)    
    megaman_die = pygame.mixer.Sound(os.path.join("Sound", "Die.wav"))
    megaman_die.set_volume(0.8)
    # Bullet sounds
    bullet1 = pygame.mixer.Sound(os.path.join("Sound", "Bullet1.wav"))
    bullet1.set_volume(0.2)
    bullet2 = pygame.mixer.Sound(os.path.join("Sound", "Bullet2.wav"))
    bullet2.set_volume(0.4)
    bullet3 = pygame.mixer.Sound(os.path.join("Sound", "Bullet3.wav"))
    bullet3.set_volume(0.8)
    # Victory Sound
    victory_pose = pygame.mixer.Sound(os.path.join("Sound", "Victory_pose.wav"))
    victory_pose.set_volume(1)
    # Creates the room sprites
    ground = MegamanSprites.Ground()
    wallL = MegamanSprites.Wall(screen, 0)
    wallR = MegamanSprites.Wall(screen, 1)
    walls = [wallL, wallR]
    ceiling = MegamanSprites.Ceiling()
    # Creates an empty list for Megaman and Boss projectiles
    bullets = []
    boss_bullets = []
    allSprites = pygame.sprite.OrderedUpdates(ground, ceiling, walls, megamanlife, bosslife, boss, megaman) 
    
    # ASSIGN 
    # Create a list of Joystick objects.
    joysticks = []
    for joystick_no in range(pygame.joystick.get_count()):
        stick = pygame.joystick.Joystick(joystick_no)
        stick.init()
        joysticks.append(stick)
    
    clock = pygame.time.Clock()
    keepGoing = True
    charge = False
    charge_counter = 1
    ai = random.randrange(100)
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)  

        # EVENT HANDLING: Player uses joystick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.JOYHATMOTION:
                megaman.change_direction(event.value)
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    megaman.jump()
                    megaman_jump.play()
                elif (event.button == 4 or event.button == 5):
                    megaman.dash()
                    megaman_dash.play()
                if event.button == 2:
                    megaman.shooting()                   
                    charge = True
                    # Create the Megaman Charging sprite image
                    player_charge = MegamanSprites.Charge(screen, megaman.rect.centerx, megaman.rect.centery)
                    allSprites.add(player_charge)                    
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 2:
                    # Kills Megaman charging image
                    player_charge.kill()
                    bullet = MegamanSprites.Bullet(screen, megaman.rect.centerx, megaman.rect.centery,\
                                                   megaman.get_direction())
                    # If the player has been charging for 1-9 ticks, bullet is normal
                    # if 10-29 ticks, bullet is second charge, higher is max charge
                    if charge_counter >= 1 and charge_counter < 10:
                        bullet1.play()
                    if charge_counter >= 10 and charge_counter < 30:
                        bullet2.play()
                        bullet.charge_shot()
                    elif charge_counter >= 30:
                        bullet3.play()
                        bullet.charge_shot_max()
                    bullets.append(bullet)
                    charge = False
                    charge_counter = 0
                    megaman.shooting()
                allSprites.add(bullets)
                    
        # Handling event cases
        # checks if player is charging, creates a charging sprite
        if charge == True:            
            charge_counter += 1
            if charge_counter > 0:
                charge2.play()                 
                player_charge.charging(megaman.rect.centerx, megaman.rect.centery,charge_counter)
        
        # Collision detection
        megaman_hitbox = MegamanSprites.Player_Hitbox(megaman.rect.centerx, megaman.rect.centery)
        boss_hitbox = MegamanSprites.Boss_Hitbox(boss.rect.centerx, boss.rect.centery)
        # Checks if player and boss have collided
        if megaman_hitbox.rect.colliderect(boss_hitbox):
            if boss.collided():
                megaman.hit_stop()
                megaman.hit()
                megamanlife.damage(1)
                megaman_die.play()
            else:
                boss.collidedReset()
        # checks if Megaman has collided with the Boss's bullets
        collide_player = pygame.sprite.spritecollide(megaman_hitbox, boss_bullets, False)
        if collide_player:
            for bullet in collide_player:
                bullet.kill()
                megamanlife.damage(2)
                boss_bullets.remove(bullet)
            megaman.hit()
            megaman_die.play()
        # Checks if the boss has collided with the Megaman's bullets
        collide_boss = pygame.sprite.spritecollide(boss_hitbox, bullets, False)
        if collide_boss:
            for bullet in collide_boss:
                bullet.kill()
                bosslife.damage(bullet.get_damage())
                bullets.remove(bullet)
            boss.hit()
            hit_boss.play()
                
        # Checks which way Megaman is, makes Boss face that direction
        if boss.rect.centerx <= megaman.rect.centerx:
            boss.change_direction(1)
        elif boss.rect.centerx > megaman.rect.centerx:
            boss.change_direction(-1)
        # Control Random Boss AI movement, ai is randomized number
        if ai == 0 or ai == 1:
            boss.dash()
            boss_dash.play()
        elif ai == 2 or ai == 3:
            boss.jump()
            boss_jump.play()
        elif ai == 4 or ai == 5: 
            boss_bullet = MegamanSprites.BossBullet(screen, boss.rect.centerx, boss.rect.centery,\
                                           boss.get_direction())               
            boss_bullets.append(boss_bullet)
            boss.shooting()
            bullet2.play()
            allSprites.add(boss_bullets)
        else:
            boss.stand()
        # Checks boss's life, decreases the random range if his health drops below half
        if bosslife.get_damage <= 15:
            ai = random.randrange(100)
        else:
            ai = random.randrange(50)
        
        # Checks if the player or boss has lost all their life, displays message and ends game
        if bosslife.get_damage() == 29:
            boss.rect.bottom = 411
            gameover = MegamanSprites.GameOver(1)
            victory_pose.play()
            allSprites.add(gameover)
            keepGoing = False
        elif megamanlife.get_damage() == 22:
            megaman.hit()
            megaman.rect.bottom = 411
            gameover = MegamanSprites.GameOver(-1)
            megaman_die.play()
            allSprites.add(gameover)
            keepGoing = False            
                                    
            
            
            
        # REFRESH SCREEN    

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)  
        pygame.display.flip()
    
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
    pygame.mixer.music.fadeout(1000)
    pygame.time.delay(3000)
    # Close the game window
    pygame.quit()     
     
# Call the main function
main()    
