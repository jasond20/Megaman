'''Author: Jason Dai

    Date: May 30, 2017

    Description: Sprite module for the Megaman game.
'''
import pygame,random, os
class Bullet(pygame.sprite.Sprite):
    '''This class defines the sprite for the megaman's bullets.'''
    def __init__(self, screen, player_x, player_y, direction):
        '''This initializer takes a screen surface as a parameter, initializes
        the image attributes of the bullet, as well as damage, dx, and counter'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.__direction = direction
        self.__chargeL1 = []
        self.__chargeR1 = []
        self.__chargeL2 = []
        self.__chargeR2 = []
        self.__charge_counter = 0
        # Sets starting image as a right facing default bullet
        self.image = pygame.image.load(os.path.join("Projectile", "Bullet", "BulletR0.gif"))
        self.rect = self.image.get_rect()
        # Creates the half charge bullets animation images in a list
        for c in range(7):
            charge1 = pygame.image.load(os.path.join("Projectile", "BulletCharge1", "BulletL" + str(c) + ".gif"))
            self.__chargeL1.append(charge1)
            charge1 = pygame.image.load(os.path.join("Projectile", "BulletCharge1", "BulletR" + str(c) + ".gif"))
            self.__chargeR1.append(charge1)            
        # Creates the full charge bullets animation images in a list
        for c in range(11):
            charge2 = pygame.image.load(os.path.join("Projectile", "BulletCharge2", "BulletL" + str(c) + ".gif"))
            self.__chargeL2.append(charge2)
            charge2 = pygame.image.load(os.path.join("Projectile", "BulletCharge2", "BulletR" + str(c) + ".gif"))
            self.__chargeR2.append(charge2)            
        
        self.rect.centerx = player_x
        self.rect.bottom = player_y          
    
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the bullets
        self.__screen = screen
        self.__dx = 22
        self.__damage = 1
        self.__hit = False
    def charge_shot(self):
        ''' Changes bullet to the partly charged bullet'''
        self.__dx = 25
        self.__damage = 2
    def charge_shot_max(self):
        ''' Changes bullet to fully charged'''
        self.__dx = 25
        self.__damage = 3
        
    def get_damage(self):
        ''' Returns the damage the bullet does'''
        return self.__damage 

    def update(self):
        '''This method will be called automatically to reposition the
        bullet sprite on the screen.'''
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the bullet in the same x direction.
        if self.rect.left > 37 and self.rect.right < (self.__screen.get_width() - 37):
            # self.__direction is which direction the player is facing
            # If Player is facing right
            if self.__direction == 1:
                if self.__damage == 2:
                    self.image = self.__chargeR1[self.__charge_counter]
                    self.__charge_counter += 1
                    if self.__charge_counter == 6:
                        self.__charge_counter = 5
                elif self.__damage == 3:
                    self.image = self.__chargeR2[self.__charge_counter]
                    self.__charge_counter += 1
                    if self.__charge_counter == 10:
                        self.__charge_counter = 9
                self.rect.left += self.__dx
            # If Player is facing left
            elif self.__direction == -1:
                self.image = pygame.image.load(os.path.join("Projectile", "Bullet", "BulletL0.gif"))
                if self.__damage == 2:
                    self.image = self.__chargeL1[self.__charge_counter]
                    self.__charge_counter += 1
                    if self.__charge_counter == 6:
                        self.__charge_counter = 5
                elif self.__damage == 3:
                    self.image = self.__chargeL2[self.__charge_counter]
                    self.__charge_counter += 1
                    if self.__charge_counter == 10:
                        self.__charge_counter = 9 
                self.rect.left -= self.__dx
        else:
            self.kill()
            
class BossBullet(pygame.sprite.Sprite):
    '''This class defines the sprite for the boss's bullets.'''
    def __init__(self, screen, player_x, player_y, direction):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the bullets.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.__bulletL = []
        self.__bulletR = []
        self.__bullet_counter = 0
        self.__direction = direction        
        self.image = pygame.image.load(os.path.join("Projectile", "BossBullet", "BulletL0.gif"))
        self.rect = self.image.get_rect()
        for c in range(3):
            bulletL = pygame.image.load(os.path.join("Projectile", "BossBullet", "BulletL" + str(c) + ".gif"))
            self.__bulletL.append(bulletL)
            bulletR = pygame.image.load(os.path.join("Projectile", "BossBullet", "BulletR" + str(c) + ".gif"))
            self.__bulletR.append(bulletR)            
           
        self.rect.centerx = player_x
        self.rect.bottom = player_y   
        
        
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the bullets
        self.__screen = screen
        self.__dx = 15
                
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        # Check if we have reached the left or right end of the screen.
        # If not, then keep moving the bullet in the same x direction.
        if self.rect.left >= 37 and self.rect.right <= (self.__screen.get_width() - 37):
            self.__bullet_counter = 0
            if self.__direction == 1:
                self.image = self.__bulletR[self.__bullet_counter]
                self.rect.left += self.__dx
            elif self.__direction == -1:
                self.image = self.__bulletL[self.__bullet_counter]
                self.rect.left -= self.__dx
            self.__bullet_counter += 1
            if self.__bullet_counter >= 3:
                self.__bulet_counter = 2
        else:
            self.kill()
            
            
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and makes a list for all
        the images in each animation for the Player sprite.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Create lists to hold images to iterate through as animations
        self.__runR = []
        self.__runL = []
        self.__shootrunR = []
        self.__shootrunL = []
        self.__jumpR = []
        self.__jumpL = []
        self.__shootjumpR = []
        self.__shootjumpL = []
        self.__dashR = []
        self.__dashL = []
        self.__shootdashR = []
        self.__shootdashL = []
        self.__standR = []
        self.__standL = []
        self.__shootstandR = []
        self.__shootstandL = []
        self.__hurtR = []
        self.__hurtL = []
        # Define the image attributes for megaman sprite
        # Run left and right animation
        for run in range(14):
            runR = pygame.image.load(os.path.join("Player", "MoveR", "Move" + str(run) + ".gif"))
            self.__runR.append(runR)
            runL = pygame.image.load(os.path.join("Player", "MoveL", "Move" + str(run) + ".gif"))
            self.__runL.append(runL)
            
        # Run Shooting left and right animation
        for run in range(10):
            shootrunR = pygame.image.load(os.path.join("Player", "ShootMoveR", "ShootMove" + str(run) + ".gif"))
            self.__shootrunR.append(shootrunR)
            shootrunL = pygame.image.load(os.path.join("Player", "ShootMoveL", "ShootMove" + str(run) + ".gif"))
            self.__shootrunL.append(shootrunL)   
            
        # Jump and Jump Shootleft and right animation
        for jump in range(7):
            jumpR = pygame.image.load(os.path.join("Player", "JumpR", "Jump" + str(jump) + ".gif"))
            self.__jumpR.append(jumpR)
            jumpL = pygame.image.load(os.path.join("Player", "JumpL", "Jump" + str(jump) + ".gif"))
            self.__jumpL.append(jumpL)
            
            shootjumpR = pygame.image.load(os.path.join("Player", "ShootJumpR", "ShootJump" + str(jump) + ".gif"))
            self.__shootjumpR.append(shootjumpR)
            shootjumpL = pygame.image.load(os.path.join("Player", "ShootJumpL", "ShootJump" + str(jump) + ".gif"))
            self.__shootjumpL.append(shootjumpL)
            
        # Dash and dash shoot left and right animation 
        for dash in range(7):
            dashR = pygame.image.load(os.path.join("Player", "DashR", "Dash" + str(dash) + ".gif"))
            self.__dashR.append(dashR)
            dashL = pygame.image.load(os.path.join("Player", "DashL", "Dash" + str(dash) + ".gif"))
            self.__dashL.append(dashL)
            
            shootdashR = pygame.image.load(os.path.join("Player", "ShootDashR", "ShootDash" + str(dash) + ".gif"))
            self.__shootdashR.append(shootdashR)
            shootdashL = pygame.image.load(os.path.join("Player", "ShootDashL", "ShootDash" + str(dash) + ".gif"))
            self.__shootdashL.append(shootdashL) 
            
        #Stand left and right animation
        for stand in range(3):
            standR = pygame.image.load(os.path.join("Player", "StandR","Stand" + str(stand) + ".gif"))
            self.__standR.append(standR)
            standL = pygame.image.load(os.path.join("Player", "StandL","Stand" + str(stand) + ".gif"))
            self.__standL.append(standL)
            
            shootstandR = pygame.image.load(os.path.join("Player", "ShootStandR","ShootStand" + str(stand) + ".gif"))
            self.__shootstandR.append(shootstandR)
            shootstandL = pygame.image.load(os.path.join("Player", "ShootStandL","ShootStand" + str(stand) + ".gif"))
            self.__shootstandL.append(shootstandL)
            
        # Hurt left and right animation
        for hurt in range(11):
            hurtR = pygame.image.load(os.path.join("Player", "HurtR","Hurt" + str(hurt) + ".gif"))
            self.__hurtR.append(hurtR)
            hurtL = pygame.image.load(os.path.join("Player", "HurtL","Hurt" + str(hurt) + ".gif"))
            self.__hurtL.append(hurtL)
        # Initializes the player standing on left side of the screen
        self.image =  pygame.image.load(os.path.join("Player", "StandR", "Stand0.gif"))
        self.rect = self.image.get_rect()
        self.rect.bottom = 411
        self.rect.left = 37
        
        # Initializes all the counters and possible states of Player variables
        self.__screen = screen
        self.__dx = 0
        self.__dy = 0
        self.__dash = 0
        self.__hit = False
        self.__hitcollide = False
        self.__shooting = False
        self.__hit_counter = 0
        self.__stand_counter = 0
        self.__move_counter = 0
        self.__shootmove_counter = 0
        self.__jump_counter = 0
        self.__shootjump_counter = 0
        self.__dash_counter = 0
        self.__direction = 1
        
    def change_direction(self, xy_change):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        y element from it, and uses this to set the players y direction.'''
        self.__dx = xy_change[0]
        if self.__dx != xy_change and self.__dx != 0:
            self.__direction = self.__dx
    
    def get_direction(self):
        ''' This method returns which direction the player is facing'''
        return self.__direction
    
    def hit(self):
        ''' Sets the hit variable to true'''
        self.__hit = True
    def hit_stop(self):
        ''' Sets the self.__hitcollide variable to true'''
        if not self.__hitcollide:
            self.__hitcollide = True
    def jump(self):
        ''' Sets player's dy direction to 1'''
        if self.__dy == 0:
            self.__dy = 1
    def shooting(self):
        '''This method checks whether the player sprite is shooting or not, and changes it according'''
        if self.__shooting == False:
            self.__shooting = True
        elif self.__shooting == True:
            self.__shooting = False
    def dash(self):
        '''The method sets the self.__dash variable to 9, telling the player to dash'''
        self.__dash = 9
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Checks whether the player is standing still or moving
        # Uses direction variable to tell which way the player is facing
        if ((self.rect.left > 37) and (self.__dx < 0)) or\
           ((self.rect.right < (self.__screen.get_width() - 37)) and (self.__dx > 0)):
            self.rect.centerx += (self.__dx*10)
            if self.__dx == 1:
                if self.__shooting == False:
                    self.image = self.__runR[self.__move_counter]
                elif self.__shooting == True:
                    self.image = self.__shootrunR[self.__shootmove_counter]
                    self.__shootmove_counter += 1
                    if self.__shootmove_counter == 10:
                        self.__shootmove_counter = 0                    
            elif self.__dx == -1:
                if self.__shooting == False:
                    self.image = self.__runL[self.__move_counter]
                elif self.__shooting == True:
                    self.image = self.__shootrunL[self.__shootmove_counter]
                    self.__shootmove_counter += 1
                    if self.__shootmove_counter == 10:
                        self.__shootmove_counter = 0                    
            self.__move_counter += 1
            if self.__move_counter == 14:
                self.__move_counter = 0
        elif self.__dx == 0:
            if self.__direction == 1:
                if self.__shooting == False:
                    self.image = self.__standR[0]
                elif self.__shooting == True:
                    self.image = self.__shootstandR[self.__stand_counter]
            elif self.__direction == -1:
                if self.__shooting == False:
                    self.image = self.__standL[0]
                elif self.__shooting == True:
                    self.image = self.__shootstandL[self.__stand_counter]
            self.__stand_counter += 1
            if self.__stand_counter == 3:
                self.__stand_counter = 0
          

        # Checks if the player should dash        
        if self.__dash >= 5:
            self.rect.centerx += (self.__dx* self.__dash)
            self.__dash -= 1
            if self.__dx == 1:
                if self.__shooting == False:
                    self.image = self.__dashR[self.__dash_counter]
                elif self.__shooting == True:
                    self.image = self.__shootdashR[self.__dash_counter]
            elif self.__dx == -1:
                if self.__shooting == False:
                    self.image = self.__dashL[self.__dash_counter]
                elif self.__shooting == True:
                    self.image = self.__shootdashL[self.__dash_counter]
            # Allows player to dash even if they are not moving
            else:
                if self.__direction == 1:
                    self.rect.centerx += ((self.__direction *2) * self.__dash)
                    if self.__shooting == False:
                        self.image = self.__dashR[self.__dash_counter]
                    elif self.__shooting == True:
                        self.image = self.__shootdashR[self.__dash_counter]
                elif self.__direction == -1:
                    self.rect.centerx += ((self.__direction* 2) * self.__dash)
                    if self.__shooting == False:
                        self.image = self.__dashL[self.__dash_counter]
                    elif self.__shooting == True:
                        self.image = self.__shootdashL[self.__dash_counter]
            self.__dash_counter += 1
            if self.__dash_counter == 7:
                self.__dash_counter = 0 
            if self.rect.right > (self.__screen.get_width() - 37):
                self.rect.right = (self.__screen.get_width() - 37)
                self.__dash_counter = 0
            elif self.rect.left < 37:
                self.rect.left = 37
                self.__dash_counter = 0
                
        # Checks if the player is jumping or not     
        if ((self.rect.top > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom <= 411) and (self.__dy < 0)):
            self.rect.top -= (self.__dy*20)
            if self.__dx == 1:
                if self.__shooting == False:
                    self.image = self.__jumpR[self.__jump_counter]
                elif self.__shooting == True:
                    self.image = self.__shootjumpR[self.__shootjump_counter]
            elif self.__dx == -1:
                if self.__shooting == False:
                    self.image = self.__jumpL[self.__jump_counter]
                elif self.__shooting == True:
                    self.image = self.__shootjumpL[self.__shootjump_counter]
            elif self.__dx == 0:
                if self.__direction == 1:
                    if self.__shooting == False:
                        self.image = self.__jumpR[self.__jump_counter]
                    elif self.__shooting == True:
                        self.image = self.__shootjumpR[self.__shootjump_counter]
                elif self.__direction == -1:
                    if self.__shooting == False:
                        self.image = self.__jumpL[self.__jump_counter]
                    elif self.__shooting == True:
                        self.image = self.__shootjumpL[self.__shootjump_counter]              
            self.__jump_counter += self.__dy
            self.__shootjump_counter += self.__dy
            if self.__jump_counter == 5:
                self.__dy = -1 
            if self.rect.bottom >= 411:
                self.__dy = 0
        
        # Checks if the player is hit and plays animation
        if self.__hit:
            if self.rect.left >= 37 and self.rect.right <= self.__screen.get_width() - 37:
                if self.__hitcollide:
                    self.rect.centerx += (self.__direction * -30)
                elif not self.__hitcollide:
                    self.rect.centerx += (self.__direction * -2)
                if self.__direction == 1:
                    self.image = self.__hurtR[self.__hit_counter]
                elif self.__direction == -1:
                    self.image = self.__hurtL[self.__hit_counter]
                self.__hit_counter += 1
                if self.__hit_counter == 11:
                    self.__hit_counter = 0  
                    self.__hit = False
                    self.__hitcollide = False
                if self.rect.left < 37:
                    self.rect.left = 37
                    self.__hit = False
                if self.rect.right > self.__screen.get_width() - 37:
                    self.rect.right = self.__screen.get_width() - 37
                    self.__hit = False
            
class Player_Hitbox(pygame.sprite.Sprite):
    '''This class defines the sprite for Player's hitbox.'''
    def __init__(self, player_x, player_y):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and the x y according to the player.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Hitbox
 
        self.__player_x = player_x
        self.__player_y = player_y
        self.image = pygame.image.load(os.path.join("Player", "Hitbox", "hitbox.gif"))
        self.rect = self.image.get_rect() 
        self.rect.centerx = player_x
        self.rect.centery = player_y  

class Boss_Hitbox(pygame.sprite.Sprite):
    '''This class defines the sprite for our Boss Hitbox.'''
    def __init__(self, boss_x, boss_y):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y according to Boss'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
 
        self.__boss_x = boss_x
        self.__boss_y = boss_y
        self.image = pygame.image.load(os.path.join("Boss", "Hitbox", "hitbox.gif"))
        self.rect = self.image.get_rect() 
        self.rect.centerx = boss_x
        self.rect.centery = boss_y
        
class Charge(pygame.sprite.Sprite):
    '''This class defines the sprite for Player's charging image.'''
    def __init__(self, screen, player_x, player_y):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y according to Player.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
 
        self.__player_x = player_x
        self.__player_y = player_y

    def charging(self, player_x, player_y, charger):
        if charger > 0 and charger < 10:
            self.image = pygame.image.load(os.path.join("Player", "Charge", "Charge0.gif"))
        if charger > 10 and charger < 30:
            self.image = pygame.image.load(os.path.join("Player", "Charge", "Charge1.gif"))
        elif charger >= 20:
            self.image = pygame.image.load(os.path.join("Player", "Charge","Charge2.gif"))
        self.rect = self.image.get_rect() 
        self.rect.centerx = player_x
        self.rect.centery = player_y        
        
            
class Boss(pygame.sprite.Sprite):
    '''This class defines the sprite for Boss'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and makes a list for all
        the images in each animation for the Boss sprite.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__jumpR = []
        self.__jumpL = []
        self.__dashR = []
        self.__dashL = []
        self.__shootR = []
        self.__shootL = []
        self.__standR = []
        self.__standL = []
        self.__hurtR = []
        self.__hurtL = []
        # Define the image attributes for megaman sprite    
        # Dash and dash shoot left and right animation 
        for dash in range(7):
            dashR = pygame.image.load(os.path.join("Boss", "DashR", "Dash" + str(dash) + ".gif"))
            self.__dashR.append(dashR)
            dashL = pygame.image.load(os.path.join("Boss", "DashL", "Dash" + str(dash) + ".gif"))
            self.__dashL.append(dashL)
            
        for jump in range(9):
            jumpR = pygame.image.load(os.path.join("Boss", "JumpR", "Jump" + str(jump) + ".gif"))
            self.__jumpR.append(jumpR)
            jumpL = pygame.image.load(os.path.join("Boss", "JumpL", "Jump" + str(jump) + ".gif"))
            self.__jumpL.append(jumpL)  
            
        for shoot in range(7):
            shootR = pygame.image.load(os.path.join("Boss", "ShootR", "Shoot" + str(shoot) + ".gif"))
            self.__shootR.append(shootR)
            shootL = pygame.image.load(os.path.join("Boss", "ShootL", "Shoot" + str(shoot) + ".gif"))
            self.__shootL.append(shootL)       
        
        for hit in range(2):
            hitR = pygame.image.load(os.path.join("Boss", "HurtR", "Hurt" + str(hit) + ".gif"))
            self.__hurtR.append(hitR)
            hitL = pygame.image.load(os.path.join("Boss", "HurtL", "Hurt" + str(hit) + ".gif"))
            self.__hurtL.append(hitL)           
        
        self.image =  pygame.image.load(os.path.join("Boss", "StandL", "Stand0.gif"))
        self.__screen = screen
        self.rect = self.image.get_rect()
        self.rect.bottom = 411
        self.rect.right = screen.get_width() - 37


        self.__dx = 0
        self.__dy = 0
        self.__dash = False
        self.__shooting = False
        self.__hit = False
        self.__shoot_counter = 0
        self.__jump_counter = 0
        self.__dash_counter = 0
        self.__hit_counter = 0 
        self.__direction = -1
        self.__collideDamage = False



    def collided(self):
        ''' Checks if the Player and Boss have collided and returns true or false'''
        if not self.__collideDamage:
            self.__collideDamage = True
            return True
        else:
            return False
    def collidedReset(self):
        ''' Sets collideDamage to False'''
        self.__collideDamage = False
    def change_direction(self, direction):
        '''This method takes a direction as a parameter and uses this to set the Bos's y direction.'''
        self.__dx = direction
        if self.__dx == 1 or self.__dx == -1:
            self.__direction = self.__dx        
            
    def get_direction(self):
        ''' Returns the direction the boss is facing'''
        return self.__direction
            
       
    def hit(self):
        ''' Sets Boss's hit variable to true'''
        self.__hit = True
    def stand(self):
        ''' Checks which way boss is facing and makes him stand that way'''
        if self.__direction == 1:
            self.image =  pygame.image.load(os.path.join("Boss", "StandR", "Stand0.gif"))
        elif self.__direction == -1:
            self.image =  pygame.image.load(os.path.join("Boss", "StandL", "Stand0.gif"))
    def shooting(self):
        '''This method checks whether the boss sprite is shooting or not, and changes it according'''
        if self.__shooting == False:
            self.__shooting = True
            
    def dash(self):
        '''The method sets the self.__dash variable to True, telling the boss to dash'''
        if self.__dash == False:
            self.__dash = True
    def jump(self):
        ''' Sets boss's dy to 1 to make boss jump'''
        if self.__dy == 0:
            self.__dy = 1
    def update(self):
        ''' This method is called automatically to update Boss's Position'''
        # Checks if the boss should dash
        if self.__dash:
            self.rect.centerx += self.__direction * random.randrange(10,20)
            if self.__direction == 1:
                self.image = self.__dashR[self.__dash_counter]
            elif self.__direction == -1:
                self.image = self.__dashL[self.__dash_counter]
            self.__dash_counter += 1
            if self.__dash_counter >= 7:
                self.__dash_counter = 0
                self.__dash = False
                self.rect.bottom = 411
            
        # Checks if the player is jumping or not     
        if ((self.rect.top > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom <= 411) and (self.__dy < 0)):
            self.rect.centery -= (self.__dy* random.randrange(5,10))
            self.rect.centerx += (self.__direction * random.randrange(5,10))
            if self.__direction == 1:
                self.image = self.__jumpR[self.__jump_counter]
            elif self.__direction == -1:
                self.image = self.__jumpL[self.__jump_counter]             
            self.__jump_counter += self.__dy
            if self.__jump_counter == 8:
                self.__dy = -1 
            if self.rect.bottom > 411:
                self.rect.bottom = 411
                self.__jump_counter = 0
                self.__dy = 0
            if self.rect.right > (self.__screen.get_width() - 37):
                self.rect.right = (self.__screen.get_width() - 37)
            elif self.rect.left < 37:
                self.rect.left = 37            
        
        
        # Checks if boss is shooting
        if self.__shooting == True:
            if self.__direction == 1:
                self.image =self.__shootR[self.__shoot_counter]
            elif self.__direction == -1:
                self.image = self.__shootL[self.__shoot_counter]
            self.__shoot_counter += 1
            if self.__shoot_counter == 7:
                self.__shoot_counter = 0
                self.__shooting = False

        

            
        # Checks if the player is hit and plays animation
        if self.__hit:
            if self.__direction == 1:
                self.image = self.__hurtR[self.__hit_counter]               
            elif self.__direction == -1:
                self.image = self.__hurtL[self.__hit_counter]               
            self.__hit_counter += 1
            if self.__hit_counter == 2:
                self.__hit_counter = 0
                self.__hit = False      
        
        # Limits the boss sprite to center of the screen
        if self.rect.left <= 99:
            self.rect.left = 100
        elif self.rect.right >= self.__screen.get_width() - 99:
            self.rect.right = self.__screen.get_width() - 100
    
        


            
class Ground(pygame.sprite.Sprite):
    '''This class defines the sprite for our left and right end zones'''
    def __init__(self):
        '''This initializer creates the Ground image'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.image.load(os.path.join("Environment", "Ground.gif"))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.bottom = 480

class Wall(pygame.sprite.Sprite):
    '''This class defines the sprite for our left and right end zones'''
    def __init__(self, screen, x_pos):
        '''This initializer takes a screen surface, and x position  as
        parameters.  For x=0, wall is left, x=1 wall is right'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Our endzone sprite will be a 1 pixel wide black line.
        # Set the rect attributes for the endzone
        if x_pos == 0:
            self.image = pygame.image.load(os.path.join("Environment", "WallL.gif"))
            self.rect = self.image.get_rect()
            self.rect.left = 0
        elif x_pos == 1:
            self.image = pygame.image.load(os.path.join("Environment", "WallR.gif"))
            self.rect = self.image.get_rect()
            self.rect.right = screen.get_width()
            
class Ceiling(pygame.sprite.Sprite):
    '''This class defines the sprite for our ceiling'''
    def __init__(self):
        '''This initializer creates the ceiling image'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.image.load(os.path.join("Environment", "Ceiling.gif"))
        
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.top = 0 


            
class Player_Lifebar(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the Player's Life.'''
    def __init__(self):
        '''This initializer loads the player lifebar images and sets it to position'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__life = []
        for life in range(23):
            health = pygame.image.load(os.path.join("Lifebar", "Player", "Playerbar" + str(life) + ".gif"))
            self.__life.append(health)
        self.image = pygame.image.load(os.path.join("Lifebar", "Player", "Playerbar0.gif"))
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.centery = 130
        self.__damage = 0
    
        
    def damage(self, damage):
        ''' This method adds the damage to the player's life bar and changes the image accordingly'''
        self.__damage += damage
        if self.__damage >= 22:
            self.__damage = 22        
        self.image = pygame.image.load(os.path.join("Lifebar", "Player", "Playerbar" + str(self.__damage) + ".gif"))
    def get_damage(self):
        ''' The method returns the damage to the player's life bar'''
        return self.__damage
        
    
class Boss_Lifebar(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the boss's lifebar.'''
    def __init__(self):
        '''This initializer loads the boss's lifebar image and position'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__life = []
        for life in range(29):
            health = pygame.image.load(os.path.join("Lifebar", "Boss", "Bossbar" + str(life) + ".gif"))
            self.__life.append(health)            
        self.image = pygame.image.load(os.path.join("Lifebar", "Boss", "Bossbar0.gif"))
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.centery = 135
        self.__damage = 0
    
        
    def damage(self, damage):
        ''' This method adds the damage to the player's life bar and changes the image accordingly'''
        self.__damage += damage
        if self.__damage >= 29:
            self.__damage = 29
        self.image = pygame.image.load(os.path.join("Lifebar", "Boss", "Bossbar" + str(self.__damage) + ".gif"))
    
    def get_damage(self):
        ''' The method returns the damage to the player's life bar'''
        return self.__damage
    
class GameOver(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self, winner):
        '''This initializer loads the system's winner to winner'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__winner = winner
        
    def update(self):
        ''' This method is automatically called to change the message'''
        if self.__winner == 1:
            self.__font = pygame.font.Font(os.path.join("Resources", "MegamanText.ttf"), 40)
            self.message = "You Win!"
            self.image = self.__font.render(self.message, 1, (255, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (320, 240)
        elif self.__winner == -1:
            self.__font = pygame.font.Font(os.path.join("Resources", "MegamanText.ttf"), 40)
            self.message = "Game Over!"
            self.image = self.__font.render(self.message, 1, (255, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = (320, 240)            
        
         
