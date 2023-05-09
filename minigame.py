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
        "arrowpic" :    pygame.transform.scale(pygame.image.load(os.path.join("Game Images","arrow.png")),(50,50)),
        "snakepic" :    pygame.transform.scale(pygame.image.load(os.path.join("Game Images","snake(hitbox).png")),(70,70)),
        "gameoverpic" : pygame.transform.scale(pygame.image.load(os.path.join("Game Images","gameover.png")),(600,343)),
        "spritesheet" : pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "animalspritesheet.png")),(653,422)),
        "background" :  pygame.image.load(os.path.join("Game Images","night_background.jpg")).convert(),
        "heart" :       pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "heart.png")),(25,25)),
        "jumpboost" :   pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "jumpboost.png")),(25,25)),
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
    maincharacter=slime(0,(GROUNDLEVEL - 60),60,60,4)
    sword=weapon(0,0,50,50)
    enemylist=[]
    critterlist=[]
    powerupslist=[]
    arrowslist=[]
    spawntimer=0
    spawncounter=random.randint(120,300)
    crittertimer=0
    critterspawncounter=random.randint(180,420)
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
            deadenemies=[]
            deadcritters=[]
            timedoutpowerups=[]
            if rArrow_keypress:
                maincharacter.changex(1)
            if lArrow_keypress:
                maincharacter.changex(-1)
            if spawntimer==spawncounter:
                snake=snakeenemy(600,193,70,70,1)
                enemylist.append(snake)
                spawntimer=0
                spawncounter=random.randint(120,300)
            if crittertimer==critterspawncounter:
                bunny=critters(0,GROUNDLEVEL-31,31,31,[(449,166,31,31),(502,166,31,31),(554,166,31,31),(605,166,31,31)])
                critterlist.append(bunny)
                crittertimer=0
                critterspawncounter=random.randint(180,420)
            for critter in critterlist:
                if critter.getx() > 615:
                    deadcritters.append(critter)
            for enemy in enemylist:
                enemy.changex(-1)
                if enemy.getx() < -150:
                    deadenemies.append(enemy)
                if enemy.checkcollision(sword.getobjectbody()) and sword.getswingstate():
                    deadenemies.append(enemy)
                if enemy.checkcollision(maincharacter.getobjectbody()) and maincharacter.getiframe() == 0:
                    maincharacter.losehealth()
            for bunny in critterlist:
                bunny.changex(1)
                bunny.frameupdate()
            for power in powerupslist:
                if power.checktimer() <= 0:
                    timedoutpowerups.append(power)
                if power.checkcollision(maincharacter.getobjectbody()):
                    timedoutpowerups.append(power)
                    maincharacter.setjumppower()
                      
            if mouseclick:
                sword.setswingstate()
                mouseclick=False
                
            if spacepress and not(maincharacter.getjumpstate()):
                maincharacter.startjump()
            
            if weaponswap:
                sword.toggleweapon()
                weaponswap = False

            for enemy in deadenemies:
                if not(enemy.getx() < -150) and random.randint(1,100) >= 50:
                    power=powerup(enemy.getx(),enemy.gety()+40,25,25,180)
                    powerupslist.append(power)
                enemylist.remove(enemy)
            for critter in deadcritters:
                critterlist.remove(critter)
                print("Enemy was removed")
            for timedpowers in timedoutpowerups:
                powerupslist.remove(timedpowers)                


            maincharacter.frameupdate()  
            sword.frameupdate(maincharacter.getposition())

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
            for enemy in enemylist:
                screen.blit(pictures["snakepic"],enemy.getposition())
            for ability in powerupslist:
                screen.blit(pictures["jumpboost"],ability.getposition())
            for bunny in critterlist:
                screen.blit(pictures["spritesheet"],(bunny.getposition()),bunny.getcoordinates())
        else:
            screen.blit(pictures["gameoverpic"],(0,0))

        #Timer
        pygame.display.flip()
        spawntimer = spawntimer+1
        crittertimer+=1
        clock.tick(60)