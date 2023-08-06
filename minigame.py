import pygame
import os
import random

from drawunit import drawunit
from snake import snakeenemy
from meteor import meteors
from dragon import dragonenemy
from powerup import powerup
from slime import slime
from weapon import weapon
from critters import critters
from explosion import explosion
from pygame.locals import * 


if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((600,343))

    clock = pygame.time.Clock()

    GROUNDLEVEL = 263
    BGHEIGHT = 343
    BGWIDTH = 600

    pictures={
        "slimepic" :          pygame.transform.scale(pygame.image.load(os.path.join("Game Images","slime(hitbox).png")),(60,60)),
        "swordpic" :          pygame.transform.scale(pygame.image.load(os.path.join("Game Images","sword(hitbox).png")),(50,50)),
        "bowpic" :            pygame.transform.scale(pygame.image.load(os.path.join("Game Images","bow.png")),(50,50)),
        "arrow" :             pygame.transform.scale(pygame.image.load(os.path.join("Game Images","arrow(hitbox).png")),(30,10)),
        "bigarrow" :          pygame.transform.scale(pygame.image.load(os.path.join("Game Images","superarrow(hitbox).png")),(50,30)),
        "enemysnake" :        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","snake(hitbox).png")),(70,70)),
        "enemymeteor":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","meteor(hitbox).png")),(30,80)),
        "enemydragon":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","dragon.png")),(120,40)),
        "gameoverpic" :       pygame.transform.scale(pygame.image.load(os.path.join("Game Images","gameover.png")),(600,343)),
        "critter" :           pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "animalspritesheet.png")),(653,422)),
        "explosion" :         pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "explosionspritesheet.png")),(300,120)), 
        "background" :        pygame.image.load(os.path.join("Game Images","night_background.jpg")).convert(),
        "grayfilter":         pygame.image.load(os.path.join("Game Images","grayfilter.png")),
        "heart" :             pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "heart.png")),(25,25)),
        "powerup" :           pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "healthpotion.png")),(35,35)),
        "coin" :              pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "coin.png")),(25,50)),
        "shield" :            pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "shield.png")),(69,69)),
        "play" :              pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "play-icon.png")),(100,100)),
        "pause" :             pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "pause-icon.png")),(25,25)),
        "openmenu" :          pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "menu-icon.png")),(25,25)),
        "menu" :              pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "menu.png")),(600,343)),
        "exitmenu" :          pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "menu-icon.png")),(25,25)),
        "slime_name_text" :   pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "slime_name_text.png")),(100,40)),
        "health_text" :       pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "health_text.png")),(140,40)),
        "level_text" :        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "level_text.png")),(80,40)),
    }

    for scorenumbers in range(0,10):
        pictures[str(scorenumbers)] = pygame.transform.scale(pygame.image.load(os.path.join("Game Images", f"{str(scorenumbers)}.png")),(60,60))

    pictures["menu"].blit(pictures["slime_name_text"],(10,10))
    pictures["menu"].blit(pictures["health_text"],(5,70))
    pictures["menu"].blit(pictures["level_text"],(110,10))

    dArrow_keypress = False
    rArrow_keypress = False
    lArrow_keypress = False
    uArrow_keypress = False
    escape_keypress = False
    ikey_keypress = False
    mouseclick = False
    spacepress = False
    weaponswap = False
    paused = False
    openmenu = False 

    #Loading Objects
    maincharacter=slime(0,(GROUNDLEVEL - 60),60,60,"slime",4)
    sword=weapon(0,0,50,50,"weapon")
    playbutton = drawunit(250,121,100,100,"button")
    pausebutton = drawunit(385,10,25,25,"button")
    menubutton = drawunit(25,300,25,25,"button")
    menuexitbutton = drawunit(550,300,25,25,"button")

    #Spawn Timers
    snakespawntimer=0
    snakespawncounter=random.randint(120,360)
    crittertimer=0
    critterspawncounter=random.randint(180,420)
    meteortimer = 0
    meteorspawncounter=random.randint(180,300)
    dragontimer = 0
    dragonspawncounter=random.randint(180,420)

    #Lists
    objectrenderlist=[]
    explosioncoordinateslist = []

    for rows in range(2):
        for columns in range(5):
            explosioncoordinateslist.append((columns*60,rows*60,59,59))

    backgroundtimer=0
    backgroundx = 0
    background2x = 600
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick = True
                mousetrack = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    dArrow_keypress = True
                if event.key == pygame.K_d:
                    rArrow_keypress = True
                if event.key == pygame.K_a:
                    lArrow_keypress = True
                if event.key == pygame.K_w:
                    uArrow_keypress = True
                if event.key == pygame.K_SPACE:
                    spacepress = True
                if event.key == pygame.K_ESCAPE:
                    escape_keypress = True
                if event.key == pygame.K_q:
                    weaponswap = True
                if event.key == pygame.K_i:
                    ikey_keypress = True
                               
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    dArrow_keypress = False
                if event.key == pygame.K_d:
                    rArrow_keypress = False
                if event.key == pygame.K_a:
                    lArrow_keypress = False
                if event.key == pygame.K_w:
                    uArrow_keypress = False
                if event.key == pygame.K_SPACE:
                    spacepress = False

        #LOGIC:
        if mouseclick:
            if playbutton.checkcollision((mousetrack[0],mousetrack[1],1,1)):
                paused = False 
            if pausebutton.checkcollision((mousetrack[0],mousetrack[1],1,1)):
                paused = True
            if menubutton.checkcollision((mousetrack[0],mousetrack[1],1,1)):
                openmenu = True
            if menuexitbutton.checkcollision((mousetrack[0],mousetrack[1],1,1)):
                openmenu = False
        if escape_keypress:
            paused = not paused
            escape_keypress = False
        if ikey_keypress:
            openmenu = not openmenu
            ikey_keypress = False
        if maincharacter.gethealth() > 0 and not(maincharacter.offscreen()) and not (paused or openmenu):
            objectdeletelist=[]
            if rArrow_keypress:
                maincharacter.changex(1)
            if lArrow_keypress:
                maincharacter.changex(-1)
            if snakespawntimer==snakespawncounter:
                snakehitpoint = 1
                snaketype = "Normal"
                if random.randint(0,100) <= 30:
                    snakehitpoint = 5
                    snaketype = "Big"
                snake=snakeenemy(600,193,70,70,"enemysnake",snakehitpoint,snaketype)
                objectrenderlist.append(snake)
                snakespawntimer=0
                snakespawncounter=random.randint(0,180)
            if meteortimer == meteorspawncounter:
                meteor = meteors(random.randint(50,550),-100,30,80,"enemymeteor")
                objectrenderlist.append(meteor)
                meteortimer = 0
                meteorspawncounter = random.randint(180,360)
            if dragontimer == dragonspawncounter:
                dragon = dragonenemy(BGWIDTH-60,random.randint(34,108),120,40,"enemydragon")
                objectrenderlist.append(dragon)
                dragontimer = 0
                dragonspawncounter = random.randint(180,420)
            if crittertimer == critterspawncounter:
                bunny=critters(0,GROUNDLEVEL-31,31,31,"critter",[(449,166,31,31),(502,166,31,31),(554,166,31,31),(605,166,31,31)])
                objectrenderlist.append(bunny)
                crittertimer=0
                critterspawncounter=random.randint(180,420)
            for objectrender in objectrenderlist:
                if objectrender.offscreen():
                    objectdeletelist.append(objectrender)
                if objectrender.outofhealth():
                    if objectrender.getsnaketype() == "Big":
                        maincharacter.score += 3
                    else:
                        maincharacter.score += 1
                    objectdeletelist.append(objectrender)
                objectrender.frameupdate()
                if objectrender.classtype == "enemysnake":
                    if objectrender.checkcollision(sword.getobjectbody()) and sword.getswingstate():
                        objectrender.losehealth()
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        maincharacter.losehealth()
                if objectrender.classtype == "enemydragon":
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        maincharacter.losehealth()
                        objectdeletelist.append(objectrender)
                if objectrender.classtype =="powerup":
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        objectdeletelist.append(objectrender)
                        maincharacter.restorehealth()
                if objectrender.classtype == "enemymeteor":
                    for otherobject in objectrenderlist:
                        if otherobject.classtype == "enemysnake":
                            if objectrender.checkcollision(otherobject.getobjectbody()):
                                otherobject.losehealth(otherobject.gethealth())  
                        if otherobject.classtype == "enemydragon":
                                if objectrender.checkcollision(otherobject.getobjectbody()):
                                    objectdeletelist.append(otherobject)    
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        maincharacter.losehealth(3)
                    if objectrender.y >= GROUNDLEVEL - 40:
                        explosioneffect = explosion(objectrender.x+(objectrender.width/2)-29.5,objectrender.y,59,59,"explosion", explosioncoordinateslist)
                        objectrenderlist.append(explosioneffect)
                        objectdeletelist.append(objectrender)
                if objectrender.classtype == "explosion":
                    if objectrender.animationstate > 9:
                        objectdeletelist.append(objectrender)
                if  "arrow" in objectrender.classtype:
                    for otherobject in objectrenderlist:
                        if otherobject.classtype == "enemysnake":
                            if objectrender.checkcollision(otherobject.getobjectbody()):
                                if objectrender.classtype == "bigarrow":
                                    otherobject.losehealth(2)
                                else:
                                    otherobject.losehealth()
                                objectdeletelist.append(objectrender)
            
            if mouseclick:
                sword.setswingstate()
                mouseclick=False
                
            if spacepress and not(maincharacter.getjumpstate()):
                maincharacter.startjump()

            if weaponswap:
                sword.toggleweapon()
                weaponswap = False

            for objectrender in objectdeletelist:
                if (objectrender.classtype == "enemysnake" and 
                    not(objectrender.getx() < -150) and random.randint(1,100) >= 50):
                    power=powerup(objectrender.getx() + objectrender.getwidth()/2 - 12,objectrender.gety()+40,25,25,"powerup",600)
                    objectrenderlist.append(power)
                objectrenderlist.remove(objectrender)            

            maincharacter.frameupdate()  

            sword.frameupdate(maincharacter.getposition(),objectrenderlist)

            if backgroundtimer > 2:
                backgroundx-=1
                background2x-=1
                if backgroundx < -600:
                    backgroundx=600 
                elif background2x < -600:
                    background2x=600

                backgroundtimer=0

            backgroundtimer += 1
            snakespawntimer = snakespawntimer+1
            crittertimer += 1
            meteortimer += 1
            dragontimer += 1

        singledigit = str((maincharacter.score%10))
        tenthdigit = str((maincharacter.score//10)%10)
        hundredthdigit = str((maincharacter.score//100)%10)

        #Rendering
        if maincharacter.gethealth() > 0 and not(maincharacter.offscreen()):
            screen.blit(pictures["background"],(backgroundx,0))
            screen.blit(pictures["background"],(background2x,0))
            screen.blit(pictures["openmenu"],(25,300))
            screen.blit(pictures[sword.getweapontype()],(sword.getposition()))
            screen.blit(pictures["slimepic"],(maincharacter.getposition()))
            screen.blit(pictures[hundredthdigit],(420,0))
            screen.blit(pictures[tenthdigit],(480,0))
            screen.blit(pictures[singledigit],(540,0))
            if paused == False:
                screen.blit(pictures["pause"],(pausebutton.x,pausebutton.y))
            for x in range(maincharacter.gethealth()):
                screen.blit(pictures["heart"],(10+30*x,10))
            for x in range(maincharacter.getiframe()):
                screen.blit(pictures["shield"],maincharacter.getposition())
            for objectrender in objectrenderlist:
                if objectrender.classtype == "critter":
                    screen.blit(pictures[objectrender.classtype],(objectrender.getposition()),objectrender.getcoordinates())
                elif objectrender.classtype == "enemydragon":
                    screen.blit(pictures[objectrender.classtype],objectrender.getposition())
                elif objectrender.classtype == "explosion":
                    screen.blit(pictures[objectrender.classtype],(objectrender.getposition()),objectrender.getcoordinates())  
                elif objectrender.classtype == "enemysnake":
                    screen.blit(pictures[objectrender.classtype],objectrender.getposition())
                    heartoffsets=0
                    for x in range(objectrender.gethealth()):
                        if heartoffsets >= 0:
                            heartoffsets = heartoffsets - x
                        else:
                            heartoffsets = heartoffsets + x
                        if objectrender.gethealth()%2 == 1:
                            screen.blit(pictures["heart"],((objectrender.getmiddlex()-25/2)+25*heartoffsets,objectrender.y-35))
                        else:
                            screen.blit(pictures["heart"],((objectrender.getmiddlex())+25*heartoffsets,objectrender.y-35))
                else:
                    screen.blit(pictures[objectrender.classtype],objectrender.getposition())
            if paused:
                screen.blit(pictures["grayfilter"],(0,0))
                screen.blit(pictures["play"],(playbutton.x,playbutton.y))
            if openmenu:
                screen.blit(pictures["menu"],(0,0))
                screen.blit(pictures["exitmenu"],(menuexitbutton.x,menuexitbutton.y))
                for x in range(maincharacter.gethealth()):
                    screen.blit(pictures["heart"],(130+30*x,80))
        else:
            screen.blit(pictures["gameoverpic"],(0,0))

        #Timer
        pygame.display.flip()
        clock.tick(60)