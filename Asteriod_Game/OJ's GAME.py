#This program was started by OJ Adeyemi from Nov 26, 2021

import pygame, os, random, time
from pygame.locals import *

#set up window
WINDOWWIDTH = 1200
WINDOWHEIGHT = 800

#set up colors
BLACK = (0,0,0)
AQUABLUE = (0,255,255)
WHITE = (255,255,255)
RED = (255,0,0)
VIOLET = (238,130,238)
BLUE = (0,0,255)

#set up player variable
PLAYERSPEED = 10

#set up lives
LIVES = 5

#set up framerate
FRAMERATE = 60

def terminate():
    """This function is called when the user closes the window"""
    pygame.quit()
    os._exit(1)


def drawText(text, font, surface, x, y, textcolour):
    """Draws the text on the surface at a specific location"""
    textobj = font.render(text, 1, textcolour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj,textrect)


def load_image(filename):
    """Loads an image from a file. Returns image and acorresponding rectangle"""
    image = pygame.image.load(filename)
    image = image.convert_alpha()   #Not as fast as .convert(), but wqorks with transparent backgrounds
    return image


def go_back(windowSurface):
    """ Display the back button to switch back and forth between the menus """
    backimage = pygame.image.load("back.png")
    image = pygame.transform.scale(backimage,(100,50))
    windowSurface.blit(image,(10,10))
    

def main_menu(windowSurface):
    mainmenu = True                  #this is set to true while the user is in the main menu
    clickSound = pygame.mixer.Sound('clicksound.mp3')
    image = pygame.image.load("menubg.png")
    bgimage = pygame.transform.scale(image,(WINDOWWIDTH, WINDOWHEIGHT))
    while mainmenu:
        """ Display menu at the beginning of the screen """                            
        windowSurface.blit(bgimage,(0,0))
        basicFont = pygame.font.SysFont("Comic Sans MS", 40)
        menutext = ['Start', 'Controls', 'Credits', 'Quit' ]
        height = 100
        x =WINDOWWIDTH // 2 - 100
        for i in range(len(menutext)):
            drawText(menutext[i], basicFont, windowSurface, x, height, WHITE)
            height += 50

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONUP:
               
                if event.pos[0]> x and event.pos[0] < x + 110 and event.pos[1] > 110 and event.pos[1] < 150:
                        mainmenu = False
                        clickSound.play()
                elif event.pos[0]> x and event.pos[0] < x + 160 and event.pos[1] > 163 and event.pos[1] < 198:
                    clickSound.play()
                    control_menu(windowSurface)
                    mainmenu = False
                        
                elif event.pos[0]> x and event.pos[0] < x + 150 and event.pos[1] > 210 and event.pos[1] < 248:
                    clickSound.play()
                    credits_menu(windowSurface)
                    mainmenu = False
                elif event.pos[0]> x and event.pos[0] < x + 150 and event.pos[1] > 250 and event.pos[1] < 300:
                    clickSound.play()
                    terminate()
                    mainmenu = False
                        
        #draw window onto the screen
        pygame.display.update()

    
def control_menu(windowSurface):
    ctrlmenu = True
    clickSound = pygame.mixer.Sound('clicksound.mp3')
    image = pygame.image.load("menubg.png")
    bgimage = pygame.transform.scale(image,(WINDOWWIDTH, WINDOWHEIGHT))
    while ctrlmenu:
        """ Displays the controls the user can input to play the game and
            based on what the mouse clisck of the user, the game will start,
        open a controls menu, credits menu or quit the game """
        windowSurface.blit(bgimage,(0,0))
        go_back(windowSurface)              #back button
        BigbasicFont = pygame.font.SysFont("Comic Sans MS", 50)
        regularbasicFont = pygame.font.SysFont("Comic Sans MS", 27)
        Bigheight = WINDOWHEIGHT // 8
        regularheight = WINDOWHEIGHT // 3.5
        x = WINDOWWIDTH // 6
        drawText('Controls', BigbasicFont, windowSurface, x , Bigheight, BLUE)
        controlstext = ['Click the left arrow key or "A" to move the player left',
                        'Click the right arrow key or "D" to move the player right',
                        'Click "M" to mute soundtrack and soundeffects']
        for i in range(len(controlstext)):
            drawText(controlstext[i], regularbasicFont, windowSurface,
                     x, regularheight, WHITE)
            regularheight += 70

        for event in pygame.event.get():
            if event.type == QUIT:
                clickSound.play()
                terminate()
            elif event.type == MOUSEBUTTONUP:
                if event.pos[0]> 17 and event.pos[0] < 110 and event.pos[1] > 10 and event.pos[1] < 60:
                    clickSound.play()
                    main_menu(windowSurface)
                    ctrlmenu = False
            elif event.type == KEYUP:                   #goes back to mainmenu if user clicks escape
                if event.key == K_ESCAPE:
                    clickSound.play()
                    main_menu(windowSurface)
                    ctrlmenu = False
        #draw window onto the screen
        pygame.display.update()



def credits_menu(windowSurface):
    credsmenu = True
    clickSound = pygame.mixer.Sound('clicksound.mp3')
    image = pygame.image.load("menubg.png")
    bgimage = pygame.transform.scale(image,(WINDOWWIDTH, WINDOWHEIGHT))
    while credsmenu:
        """ Display the credits onto the window screen """
        windowSurface.blit(bgimage,(0,0))
        go_back(windowSurface)                      #back button
        BigbasicFont = pygame.font.SysFont("Comic Sans MS", 50)
        basicFont = pygame.font.SysFont("Comic Sans MS", 24)
        x = WINDOWWIDTH // 6
        y = WINDOWHEIGHT // 3.5
        z = WINDOWHEIGHT // 8
        drawText('Credits', BigbasicFont, windowSurface, x, z, BLUE)
        creditstext = ['Written by: OJ Adeyemi','Program used: Python','Sound Effects and Graphics: The Internet','Game SoundTrack: Prey –Original Game Soundtrack– “Everything Is Going to Be Ok”',]
        for i in range(len(creditstext)):
            drawText(creditstext[i], basicFont,
                 windowSurface, x , y, WHITE)
            y += 60

        for event in pygame.event.get():
            if event.type == QUIT:
                clickSound.play()
                terminate()
            elif event.type == MOUSEBUTTONUP:
                if event.pos[0]> 17 and event.pos[0] < 110 and event.pos[1] > 10 and event.pos[1] < 60:
                    clickSound.play()
                    main_menu(windowSurface)
                    credsmenu = False
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:           #goes back to mainmenu if user clicks escape
                    clickSound.play()
                    main_menu(windowSurface)
                    credsmenu = False
        #draw window onto the screen
        pygame.display.update()
                        
def instruction(windowSurface):
    """displays instruction text at the start of the game"""
    basicFont = pygame.font.SysFont("Comic Sans MS", 20)
    x = WINDOWWIDTH // 4
    y = WINDOWHEIGHT // 4
    enddisplay = time.time()
    text = ['Avoid all the obstacles and try to survive. ','There are powerups along the way to help you.','  ','       Goodluck!']
    for i in range(len(text)):
        drawText(text[i], basicFont, windowSurface, x, y, WHITE)
        y += 70
    #draw window onto the screen         
    pygame.display.update()
                        

    
        

class Player(pygame.sprite.Sprite):
    """ The player controlled by the user """
    def __init__(self, image, movespeed, lives):
        pygame.sprite.Sprite.__init__(self)
        self.originalimage = pygame.transform.scale(image,(70,30))  #tranform the image to a smaller size here
        self.smallerimage= pygame.transform.scale(image,(47,20))  #shrinked image of player
        self.image = self.originalimage
        self.rect = self.image.get_rect()                   #get a rectangle that perfectly fits the image

        #Position the player at the bottom of the screen
        self.rect.centerx = WINDOWWIDTH //2
        self.rect.centery = WINDOWHEIGHT - 50

        #set up  movement variables
        self.moveLeft = False
        self.moveRight = False
        self.movespeed = movespeed
        self.shrink = False
        #set up lives
        self.lives = lives

        
    def update(self):
        if self.moveLeft and self.rect.left > 0:
            self.rect.left -= self.movespeed
        elif self.moveRight and self.rect.right < WINDOWWIDTH:
            self.rect.right += self.movespeed



class Obstacle(pygame.sprite.Sprite):
    """ obstacles the player will have to avoid """

    def __init__(self, image,obstaclespeed,factor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(random.randrange(100,140),random.randrange(90,140)))  #random obstacle sizes
        self.rect = self.image.get_rect()
        self.obstaclespeed = random.randrange(3,6)
        self.factor = factor

        #set the position to a random loscation at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - (self.rect.width // 2))

    def update(self):
        #let the obstacle all travel downwards in a straight line
        self.rect.top += self.obstaclespeed*self.factor

class Obstacle2(pygame.sprite.Sprite):
    """ obstacles the player will have to avoid """

    def __init__(self, image,obstaclespeed,factor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(150,150))  #random obstacle sizes
        self.rect = self.image.get_rect()
        self.obstaclespeed = random.randrange(5,9)
        self.factor = factor

        #set the position to a random location at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - self.rect.width)

    def update(self):
        #let the obstacle all travel downwards in a straight line
        self.rect.top += self.obstaclespeed*self.factor

class Obstacle3(pygame.sprite.Sprite):
    """ obstacles the player will have to avoid """

    def __init__(self, image,obstaclespeed,factor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(130,130))  #random obstacle sizes
        self.rect = self.image.get_rect()
        self.obstaclespeed = random.randrange(5,9)
        self.factor = factor

        #set the position to a random location at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - self.rect.width)

    def update(self):
        #let the obstacle all travel downwards in a straight line
        self.rect.top += self.obstaclespeed*self.factor

class Obstacle4(pygame.sprite.Sprite):
    """ obstacles the player will have to avoid """

    def __init__(self, image,obstaclespeed,factor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(110,90))  #random obstacle sizes
        self.rect = self.image.get_rect()
        self.obstaclespeed = random.randrange(6,9)
        self.factor = factor

        #set the position to a random location at the top of the screen
        self.rect.top = random.randrange(0, WINDOWHEIGHT//4 )
        self.rect.left = random.randrange(WINDOWWIDTH- self.rect.width, WINDOWWIDTH)

    def update(self):
        #let the obstacle all travel downwards in a straight line
        self.rect.top += self.obstaclespeed*self.factor
        self.rect.left -= self.obstaclespeed*self.factor

        
class ExtraLives(pygame.sprite.Sprite):
    """Extra lives for the player"""
    def __init__(self, image, livesspeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(40,20))
        self.rect = self.image.get_rect()
        self.livesspeed = livesspeed

        #set the position to a random location at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - self.rect.width)
        
    def update(self):
        #let the extralives powerup all travel downwards in a straight or slant line
        self.rect.top += self.livesspeed

        
        
class Shrink(pygame.sprite.Sprite):
    """Makes the player shrink for a temporary amount of time"""
    def __init__(self,image,shrinkspeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(25,25))
        self.rect = self.image.get_rect()
        self.shrinkspeed = shrinkspeed

        #set the position to a random location at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - self.rect.width)
        
    def update(self):
        #let the shrink powerup all travel downwards in a straight or slant line
        self.rect.top += self.shrinkspeed



class Slowdown(pygame.sprite.Sprite):
    """Makes the obstacles slow down their spawn timing and speed"""
    def __init__(self,image,slowdownspeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(35,30))
        self.rect = self.image.get_rect()
        self.slowdownspeed = slowdownspeed

        #set the position to a random location at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - self.rect.width)
        
    def update(self):
        #let the slowdown powerup all travel downwards in a straight or slant line
        self.rect.top += self.slowdownspeed



class Addscore(pygame.sprite.Sprite):
    """Makes the obstacles slow down their spawn timing and speed"""
    def __init__(self,image,addscorespeed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image,(35,30))
        self.rect = self.image.get_rect()
        self.addscorespeed =  addscorespeed

        #set the position to a random location at the top of the screen
        self.rect.top = 0 #top of the screen
        self.rect.left = random.randrange(0, WINDOWWIDTH - self.rect.width)
        
    def update(self):
        #let the slowdown powerup all travel downwards in a straight or slant line
        self.rect.top += self.addscorespeed



        
class Game():
    """ This class represents an instance of the game. If we need to reset
        the game we'd just need to create a new instance of this class. """

    def __init__(self):
        """Constructor. Create all our attributes and initialize the game.
            The stats provided custimize the game. """

        #set to true once player runs out of lives
        self.game_over = False

        #controls when new obstacles and powerups are added
        self.startobstacle = time.time()
        self.startobstacle2 = time.time()
        self.startobstacle3 = time.time()
        self.startobstacle4 = time.time()
        self.startlives = time.time()
        self.startfactor = time.time()
        self.startshrink = time.time()
        self.startslowdown = time.time()
        self.startaddscore = time.time()
        self.increaseobsspeed = time.time()

        #help with starting the score count
        self.startscore = time.time()

        self.score = 0

        #initialize these variables 
        self.newobstacle = 0.65              #new obstacle
        self.newobstacle2 = random.randrange(50,100)    #new obstacle
        self.newobstacle3 = random.randrange(40,100)    #new obstacle
        self.newobstacle4 = random.randrange(55,100)    #new obstacle
        self.scorecount = 0.3     #every 0.3 seconds is one score point
        self.newlives = random.randrange(25,60)         #add a extra lives powerup 
        self.addfactor = random.randrange(10,15)            #this variable will make the obstacle fall faster over time
        self.newshrink = random.randrange(20,70)      #adds a shrink powerup
        self.newslowdown = random.randrange(40,100)      #adds a slow down power up
        self.newscore = random.randrange(15,60)
        self.addobstaclespeed = random.randrange(8,19)
        
        #set up the player, obstacles and powerups          
        self.all_sprites = pygame.sprite.Group()

        #background image
        self.bgimage = pygame.image.load("bg.jpg")
       
        
        pimage = load_image("spaceship.png")
        self.player = Player(pimage, PLAYERSPEED, LIVES)          
        self.all_sprites.add(self.player)


        self.obstacles = pygame.sprite.Group()
        self.obsimage = load_image("asteriod.png")
        self.obstaclespeed = random.randrange(3,6)
        self.factor = 1
        
        for i in range(0):                          
            anobstacle = Obstacle(self.obsimage,self.obstaclespeed,self.factor)  #pass in random speed
            self.obstacles.add(anobstacle)
            self.all_sprites.add(anobstacle)

        self.obstacles2 = pygame.sprite.Group()
        self.obsimage2 = load_image("asteriod2.png")
        self.obstaclespeed2 = random.randrange(5,8)
        self.factor = 0.8
        
        for i in range(0):                          
            anobstacle2 = Obstacle2(self.obsimage2,self.obstaclespeed2,self.factor)  #pass in random speed
            self.obstacles2.add(anobstacle2)
            self.all_sprites.add(anobstacle2)

        self.obstacles3 = pygame.sprite.Group()
        self.obsimage3 = load_image("asteriod3.png")
        self.obstaclespeed3 = random.randrange(2,6)
        self.factor = 1
        
        for i in range(0):                          
            anobstacle3 = Obstacle3(self.obsimage3,self.obstaclespeed3,self.factor)  #pass in random speed
            self.obstacles3.add(anobstacle3)
            self.all_sprites.add(anobstacle3)
            
        self.obstacles4 = pygame.sprite.Group()
        self.obsimage4 = load_image("asteriod4.png")
        self.obstaclespeed4 = random.randrange(5,9)
        self.factor = 0.8
        
        for i in range(0):                          
            anobstacle4 = Obstacle4(self.obsimage4,self.obstaclespeed4,self.factor)  #pass in random speed
            self.obstacles4.add(anobstacle4)
            self.all_sprites.add(anobstacle4)
        
        self.extralives = pygame.sprite.Group()
        self.livesimage = load_image("Heart.png")
        self.livesspeed = random.randrange(2,4)
        for i in range(0):
            extralives = ExtraLives(self.livesimage,self.livesspeed)
            self.extralives.add(extralives)
            self.all_sprites.add(extralives)

        self.shrink = pygame.sprite.Group()
        self.shrinkimage = load_image("shrink..png")  
        self.shrinkspeed = 2
        for i in range(0):
            shrink = Shrink(self.shrinkimage,self.shrinkspeed)
            self.shrink.add(shrink)
            self.all_sprites.add(shrink)

        self.slowdown = pygame.sprite.Group()
        self.slowdownimage = load_image("clock.png") 
        self.slowdownspeed = random.randrange(2,5)
        for i in range(0):
            slowdown = Slowdown(self.slowdownimage,self.slowdownspeed)
            self.slowdown.add(slowdown)
            self.all_sprites.add(slowdown)
        
    
        self.addscore = pygame.sprite.Group()
        self.addscoreimage = load_image("Plus100.png")            #find new image
        self.addscorespeed = random.randrange(2,4)
        for i in range(0):
            addscore = Addscore(self.addscoreimage,self.addscorespeed)
            self.addscore.add(addscore)
            self.all_sprites.add(addscore)

        # set up music and sound effects
        self.pickUpSound = pygame.mixer.Sound('pickup1.wav')
        self.slowdownSound = pygame.mixer.Sound('slowdown.mp3')
        self.obstacleSound = pygame.mixer.Sound('obstaclesound.mp3')
        self.shrinkSound = pygame.mixer.Sound('shrinksound.mp3')
        self.clickSound = pygame.mixer.Sound('clicksound.mp3')
        pygame.mixer.music.load('spacetheme.mp3')
        self.gameOverSound = pygame.mixer.Sound('gameover.wav')

        # Play the background music
        pygame.mixer.music.play(-1, 0.0)
        self.musicPlaying = True


        
    def process_events(self, windowSurface):
        """ Process all of the keyboard and mouse events """

        for event in pygame.event.get():
            if event.type ==QUIT:
                terminate()
                
            elif event.type == KEYDOWN:
                #change the keyboard variables
                if event.key ==K_LEFT or event.key == ord('a'):
                    self.player.moveLeft = True
                    self.player.moveRight = False
                elif event.key ==K_RIGHT or event.key == ord ('d'):
                    self.player.moveRight = True
                    self.player.moveLeft = False
                    
            elif event.type == KEYUP:
                #change the keyboard variables
                if event.key ==K_LEFT or event.key == ord('a'):
                    self.player.moveLeft = False
                elif event.key ==K_RIGHT or event.key == ord ('d'):
                    self.player.moveRight = False
                elif event.key == ord('m'):
                # toggles the background music
                    if self.musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 5.0)
                    self.musicPlaying = not self.musicPlaying
                
            elif event.type == MOUSEBUTTONDOWN:
                #The user clicks to restart the game when it is over
                if self.game_over:
                    #start a new game
                    main_menu(windowSurface)
                    self.__init__()


    def run_logic(self):
        """ Checks for collisions, loss of life, highscore and time to add new obstacle """
        if not self.game_over:
            for obstacle in self.obstacles:                 #delete obstacles when they are not on the screen
                if obstacle.rect.top > WINDOWHEIGHT-2:
                    obstacle.kill()
            for obstacle in self.obstacles2:                 #delete obstacles when they are not on the screen
                if obstacle.rect.top > WINDOWHEIGHT-2:
                    obstacle.kill()
            for obstacle in self.obstacles3:                 #delete obstacles when they are not on the screen
                if obstacle.rect.top > WINDOWHEIGHT-2:
                    obstacle.kill()
            for obstacle in self.obstacles4:                 #delete obstacles when they are not on the screen
                if obstacle.rect.top > WINDOWHEIGHT:
                    obstacle.kill()
            for powerup in self.extralives:                 #delete powerup when they are not on the screen
                if powerup.rect.top > WINDOWHEIGHT:
                    powerup.kill()
            for powerup in self.shrink:                 #delete powerup when they are not on the screen
                if powerup.rect.top > WINDOWHEIGHT:
                    powerup.kill()
            for powerup in self.slowdown:                 #delete powerup when they are not on the screen
                if powerup.rect.top > WINDOWHEIGHT:
                    powerup.kill()
            for powerup in self.addscore:                 #delete powerup when they are not on the screen
                if powerup.rect.top > WINDOWHEIGHT:
                    powerup.kill()
                    

            #lose a life when player collides with any of the obstacles

            obstaclelist = pygame.sprite.spritecollide(self.player, self.obstacles, True)
            if obstaclelist:                        #if player collides with an obstacle lose a life 
                self.player.lives -= 1
            if self.musicPlaying:
                for obstacles in obstaclelist:
                    self.obstacleSound.play()
                    
            obstaclelist2 = pygame.sprite.spritecollide(self.player, self.obstacles2, True)
            if obstaclelist2:                        #if player collides with an obstacle lose a life 
                self.player.lives -= 1
            if self.musicPlaying:
                for obstacles in obstaclelist2:
                    self.obstacleSound.play()
                    
            obstaclelist3 = pygame.sprite.spritecollide(self.player, self.obstacles3, True)
            if obstaclelist3:                        #if player collides with an obstacle lose a life 
                self.player.lives -= 1
            if self.musicPlaying:
                for obstacles in obstaclelist3:
                    self.obstacleSound.play()

            obstaclelist4 = pygame.sprite.spritecollide(self.player, self.obstacles4, True)
            if obstaclelist4:                        #if player collides with an obstacle lose a life 
                self.player.lives -= 1
            if self.musicPlaying:
                for obstacles in obstaclelist4:
                    self.obstacleSound.play()
                    
            extraliveslist = pygame.sprite.spritecollide(self.player, self.extralives, True)
            if extraliveslist:                        #if player collides with a extra live power up, add a life
                self.player.lives += 1

            # Play the pickup sound for each poweruptaken
            if self.musicPlaying:
                for powerup in extraliveslist:
                    self.pickUpSound.play()

            shrinklist = pygame.sprite.spritecollide(self.player, self.shrink, True)
            if shrinklist:                          #if  player collides with shrink power, shrink player size
                self.player.image = self.player.smallerimage
                self.shrinktime = time.time()
                self.player.shrink = True

            # Play the pickup sound for each poweruptaken
            if self.musicPlaying:
                for powerup in shrinklist:
                    self.pickUpSound.play()
                    self.shrinkSound.play()

            if self.player.shrink:
                if time.time() - self.shrinktime > 15:
                    self.player.image = self.player.originalimage
                    self.player.shrink = False
                

            slowdownlist = pygame.sprite.spritecollide(self.player, self.slowdown, True)
            if slowdownlist:                    #if player collides with slowdown powerup, slow the speed and spawn time of obstacles
                self.factor -= 0.15
                self.newobstacle +=0.1

            # Play the pickup sound for each poweruptaken
            if self.musicPlaying:
                for powerup in slowdownlist:
                    self.pickUpSound.play()
                    self.slowdownSound.play()
                
            scorelist = pygame.sprite.spritecollide(self.player, self.addscore, True)  #add 100 points to score
            if scorelist:
                self.score += 100

            # Play the pickup sound for each poweruptaken
            if self.musicPlaying:
                for powerup in scorelist:
                    self.pickUpSound.play()

                
            endtime = time.time()
            
            if endtime - self.startobstacle >= self.newobstacle:
                #reset counter and add a new obstacle
                self.startobstacle = time.time()
                anobstacle = Obstacle(self.obsimage,self.obstaclespeed,self.factor)
                self.obstacles.add(anobstacle)
                self.all_sprites.add(anobstacle)

            if endtime - self.startobstacle2 >= self.newobstacle2:
                #reset counter and add a new obstacle
                self.startobstacle2 = time.time()
                anobstacle2 = Obstacle2(self.obsimage2,self.obstaclespeed2,self.factor)
                self.obstacles2.add(anobstacle2)
                self.all_sprites.add(anobstacle2)

            if endtime - self.startobstacle3 >= self.newobstacle3:
                #reset counter and add a new obstacle
                self.startobstacle3 = time.time()
                anobstacle3 = Obstacle3(self.obsimage3,self.obstaclespeed3,self.factor)
                self.obstacles3.add(anobstacle3)
                self.all_sprites.add(anobstacle3)
                
            if endtime - self.startobstacle4 >= self.newobstacle4:
                #reset counter and add a new obstacle
                self.startobstacle4 = time.time()
                anobstacle4 = Obstacle4(self.obsimage4,self.obstaclespeed4,self.factor)
                self.obstacles4.add(anobstacle4)
                self.all_sprites.add(anobstacle4)
            
            if endtime - self.startlives >= self.newlives:
                #reset counter and add a new extra lives powerup
                self.startlives = time.time()
                extralives = ExtraLives(self.livesimage,self.livesspeed)
                self.extralives.add(extralives)
                self.all_sprites.add(extralives)


            if endtime - self.startshrink >= self.newshrink:
                #reset counter and add a new extra lives powerup
                self.startshrink = time.time()
                shrink = Shrink(self.shrinkimage,self.shrinkspeed)
                self.shrink.add(shrink)
                self.all_sprites.add(shrink)


            if endtime - self.startslowdown >=self.newslowdown:             #slows down the game
                #reset counter and add a slowdown powerup
                self.startslowdown = time.time()
                slowdown = Slowdown(self.slowdownimage,self.slowdownspeed)
                self.slowdown.add(slowdown)
                self.all_sprites.add(slowdown)

                
            if endtime - self.startaddscore >=self.newscore:             #slows down the game
                #reset counter and add a score powerup
                self.startaddscore = time.time()
                addscore = Addscore(self.addscoreimage,self.addscorespeed)
                self.addscore.add(addscore)
                self.all_sprites.add(addscore)

                
            if endtime - self.startscore >= self.scorecount:
                self.startscore = time.time()                           #adds up score
                self.score = self.score + 1

            #speeds up game overtime
            if endtime - self.startfactor >=self.addfactor:             
                self.startfactor = time.time()
                self.factor += 0.07
                self.newobstacle2 -=1
                self.newobstacle3 -=2
                self.newobstacle4 -=1

            if endtime - self.increaseobsspeed >= self.addobstaclespeed:
                self.increaseobsspeed = time.time()
                self.newobstacle -= 0.04


            #check if its game over when the player loses all his life
            if self.player.lives <= 0:
                self.game_over = True
                pygame.mixer.music.stop()
                self.gameOverSound.play()


    def display_frame (self, windowSurface):
        """ Displays everything to the screen for the game. """
        #set up fonts
        basicFont = pygame.font.SysFont("Comic Sans MS", 20)
        basicfont = pygame.font.SysFont('arial', 25)

        #draw the background onto the surface
        windowSurface.blit(self.bgimage,(0,0))
        
        displaylives = "Lives: " + str(self.player.lives)
        displayscore = "Score: " + str(self.score)
        if self.game_over:
            #The user will click to restart the game
            x = WINDOWWIDTH // 2 - 120
            y = WINDOWHEIGHT // 2 - 20
            if self.score <= 300:
                text = " :(    Click anywhere to restart"
            elif 300 < self.score <= 500:
                text = " Good try! Click anywhere to restart"
            elif 500 < self.score <= 700:
                text = "Nice try!  Click to restart"
            elif 700< self.score <= 1000:
                text = "Great score!!  Click anywhere to restart"
            elif 1000< self.score <= 2000:
                text = " Amazing Score!!!  Click anywhere to restart"
            elif self.score > 2000:
                text = " IMPRESSIVE!!!!!!!  Click anywhere to restart"
            drawText(text, basicFont, windowSurface, x-40 ,y, WHITE)
            drawText(displayscore, basicFont, windowSurface, x ,y+60, WHITE)

        else:
            #draw lives and score at top of the screen
           
            drawText(displaylives, basicfont, windowSurface, 0, 0, VIOLET)
           
            drawText(displayscore,basicfont, windowSurface, WINDOWWIDTH - 200 ,0, VIOLET)

            #draw the player and obstacles onto the surface
            self.all_sprites.draw(windowSurface)
        
        #draw the window onto the sreen
        pygame.display.update()



def main():
    """The Mainline for the program"""
    #set up pygame
    pygame.init()
    mainClock = pygame.time.Clock()

    #set caption of game
    pygame.display.set_caption("OJ's Game")

    #set up the window
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

    #display a menu at the beginning
    main_menu(windowSurface)
    
    game = Game()
    
    game.display_frame(windowSurface)

    instruction(windowSurface)
    time.sleep(3)

   
    #run the game loop until the user quits
    while True:
        #process events
        game.process_events(windowSurface)

        #update the player's, obstacles and powerups position  on the screen
        game.player.update()

        game.obstacles.update()

        game.obstacles2.update()

        game.obstacles3.update()

        game.obstacles4.update()

        game.extralives.update()

        game.shrink.update()

        game.slowdown.update()

        game.addscore.update()

        #add new obstacles and check for collision and loss of lives
        game.run_logic()

        #draw the current frame
        game.display_frame(windowSurface)

        mainClock.tick(FRAMERATE)

main()


        
        


