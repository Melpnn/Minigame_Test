import pygame
import os
import random

from snake import snakeenemy
from powerup import powerup
from slime import slime
from weapon import weapon
from critters import critters
from pygame.locals import * 


if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((600,343))

    clock = pygame.time.Clock()

    GROUNDLEVEL = 263

    pictures={
        "slimepic" :    pygame.transform.scale(pygame.image.load(os.path.join("Game Images","slime(hitbox).png")),(60,60)),
        "swordpic" :    pygame.transform.scale(pygame.image.load(os.path.join("Game Images","sword(hitbox).png")),(50,50)),
        "bowpic" :      pygame.transform.scale(pygame.image.load(os.path.join("Game Images","bow.png")),(50,50)),
        "arrow" :    pygame.transform.scale(pygame.image.load(os.path.join("Game Images","arrow.png")),(50,50)),
        "enemy" :    pygame.transform.scale(pygame.image.load(os.path.join("Game Images","snake(hitbox).png")),(70,70)),
        "gameoverpic" : pygame.transform.scale(pygame.image.load(os.path.join("Game Images","gameover.png")),(600,343)),
        "critter" : pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "animalspritesheet.png")),(653,422)),
        "background" :  pygame.image.load(os.path.join("Game Images","night_background.jpg")).convert(),
        "heart" :       pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "heart.png")),(25,25)),
        "powerup" :   pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "jumpboost.png")),(25,25)),
        "shield" :      pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "shield.png")),(69,69)),
    }

    dArrow_keypress = False
    rArrow_keypress = False
    lArrow_keypress = False
    uArrow_keypress = False
    mouseclick = False
    spacepress = False
    weaponswap = False
    jumpframecount = 0 
    maincharacter=slime(0,(GROUNDLEVEL - 60),60,60,"slime",4,)
    sword=weapon(0,0,50,50,"weapon")
    objectrenderlist=[]
    spawntimer=0
    spawncounter=random.randint(120,300)
    critterspawncounter=random.randint(180,420)
    crittertimer=0
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
                if event.key == pygame.K_q:
                    weaponswap = True

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

        if maincharacter.gethealth() > 0:
            objectdeletelist=[]
            if rArrow_keypress:
                maincharacter.changex(1)
            if lArrow_keypress:
                maincharacter.changex(-1)
            if spawntimer==spawncounter:
                snakehitpoint = 1
                if random.randint(0,100) <= 30:
                    snakehitpoint = 5
                snake=snakeenemy(600,193,70,70,"enemy",snakehitpoint)
                objectrenderlist.append(snake)
                spawntimer=0
                spawncounter=random.randint(120,300)
            if crittertimer==critterspawncounter:
                bunny=critters(0,GROUNDLEVEL-31,31,31,"critter",[(449,166,31,31),(502,166,31,31),(554,166,31,31),(605,166,31,31)])
                objectrenderlist.append(bunny)
                crittertimer=0
                critterspawncounter=random.randint(180,420)
            for objectrender in objectrenderlist:
                if objectrender.offscreen():
                    objectdeletelist.append(objectrender)
                if objectrender.outofhealth():
                    objectdeletelist.append(objectrender)
                objectrender.frameupdate()
                if objectrender.classtype == "enemy":
                    if objectrender.checkcollision(sword.getobjectbody()) and sword.getswingstate():
                        objectrender.losehealth()
                    if objectrender.checkcollision(maincharacter.getobjectbody()) and maincharacter.getiframe() == 0:
                        maincharacter.losehealth()
                if objectrender.classtype =="powerup":
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        objectdeletelist.append(objectrender)
                        maincharacter.setjumppower()
                if objectrender.classtype == "arrow":
                    for otherobject in objectrenderlist:
                        if otherobject.classtype == "enemy":
                            if objectrender.checkcollision(otherobject.getobjectbody()):
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
                if (objectrender.classtype == "enemy" and 
                    not(objectrender.getx() < -150) and random.randint(1,100) >= 50):
                    power=powerup(objectrender.getx(),objectrender.gety()+40,25,25,"powerup",180)
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

            backgroundtimer+=1

        #Rendering
        if maincharacter.gethealth() > 0:
            screen.blit(pictures["background"],(backgroundx,0))
            screen.blit(pictures["background"],(background2x,0))
            screen.blit(pictures[sword.getweapontype()],(sword.getposition()))
            screen.blit(pictures["slimepic"],(maincharacter.getposition()))
            for x in range(maincharacter.gethealth()):
                screen.blit(pictures["heart"],(10+30*x,10))
            for x in range(maincharacter.getiframe()):
                screen.blit(pictures["shield"],maincharacter.getposition())
            for objectrender in objectrenderlist:
                if objectrender.classtype == "critter":
                    screen.blit(pictures[objectrender.classtype],(objectrender.getposition()),objectrender.getcoordinates())
                elif objectrender.classtype == "enemy":
                    screen.blit(pictures[objectrender.classtype],objectrender.getposition())
                    screen.blit(pictures["heart"],(objectrender.x+20,objectrender.y-35))
                else:
                    screen.blit(pictures[objectrender.classtype],objectrender.getposition())
        else:
            screen.blit(pictures["gameoverpic"],(0,0))

        #Timer
        pygame.display.flip()
        spawntimer = spawntimer+1
        crittertimer+=1
        clock.tick(60)