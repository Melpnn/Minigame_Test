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

GROUNDLEVEL = 263
BGHEIGHT = 343
BGWIDTH = 600

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((BGWIDTH,BGHEIGHT))

    clock = pygame.time.Clock()

    pictures={
        "slimepic" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","slime(hitbox).png")),(60,60)),
            "dimensions" :    (60,60),
            "width"  :        60,
            "height" :        60, },
        "swordpic" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","sword(hitbox).png")),(50,50)),
            "dimensions" :    (50,50),
            "width"  :        50,
            "height" :        50, },
        "bowpic" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","bow.png")),(50,50)),
            "dimensions" :    (50,50),
            "width"  :        50,
            "height" :        50, },           
        "arrow" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","arrow(hitbox).png")),(30,10)),
            "dimensions" :    (30,10),
            "width"  :        30,
            "height" :        10, },             
        "bigarrow" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","superarrow(hitbox).png")),(50,30)),
            "dimensions" :    (50,30),
            "width"  :        50,
            "height" :        30, },               
        "enemysnake" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","snake(hitbox).png")),(70,70)),
            "dimensions" :    (70,70),
            "width"  :        70,
            "height" :        70, },        
        "enemymeteor": {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","meteor(hitbox).png")),(30,80)),
            "dimensions" :    (30,80),
            "width"  :        30,
            "height" :        80, },             
        "enemydragon":  {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","dragon.png")),(120,40)),
            "dimensions" :    (120,40),
            "width"  :        120,
            "height" :        40, },               
        "gameoverpic" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","gameover.png")),(BGWIDTH,BGHEIGHT)),
            "dimensions" :    (BGWIDTH,BGHEIGHT),
            "width"  :        BGWIDTH,
            "height" :        BGHEIGHT, },         
        "critter" :    {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "animalspritesheet.png")),(653,422)),
            "dimensions" :    (653,422),
            "width"  :        653,
            "height" :        422, },        
        "explosion" :   {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "explosionspritesheet.png")),(300,120)), 
            "dimensions" :    (300,120),
            "width"  :        300,
            "height" :        120, },            
        "background" :  {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","night_background.jpg")),(BGWIDTH,BGHEIGHT)),
            "dimensions" :    (BGWIDTH,BGHEIGHT),
            "width"  :        BGWIDTH,
            "height" :        BGHEIGHT, },            
        "grayfilter":  {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images","grayfilter.png")),(BGWIDTH,BGHEIGHT)),
            "dimensions" :    (BGWIDTH,BGHEIGHT),
            "width"  :        BGWIDTH,
            "height" :        BGHEIGHT, },                  
        "heart" :  {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "heart.png")),(25,25)),
            "dimensions" :    (25,25),
            "width"  :        25,
            "height" :        25, },              
        "powerup" :   {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "healthpotion.png")),(20,30)),
            "dimensions" :    (20,30),
            "width"  :        20,
            "height" :        30, },         
        "coin" :     {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "coin.png")),(25,50)),
            "dimensions" :    (25,50),
            "width"  :        25,
            "height" :        50, },           
        "shield" :      {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "shield.png")),(69,69)),
            "dimensions" :    (69,69),
            "width"  :        69,
            "height" :        69, },           
        "play" :    {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "play-icon.png")),(100,100)),
            "dimensions" :    (100,100),
            "width"  :        100,
            "height" :        100, },            
        "pause" :    {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "pause-icon.png")),(25,25)),
            "dimensions" :    (25,25),
            "width"  :        25,
            "height" :        25, },            
        "openmenu" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "menu-icon.png")),(25,25)),
            "dimensions" :    (25,25),
            "width"  :        25,
            "height" :        25, },            
        "menu" :     {
            "surface":           pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "menu.png")),(BGWIDTH,BGHEIGHT)),
            "dimensions" :    (BGWIDTH,BGHEIGHT),
            "width"  :        BGWIDTH,
            "height" :        BGHEIGHT, },         
        "exitmenu" : {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "menu-icon.png")),(25,25)),
            "dimensions" :    (25,25),
            "width"  :        25,
            "height" :        25, },               
        "slime_name_text" :  {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "slime_name_text.png")),(100,40)),
            "dimensions" :    (100,40),
            "width"  :        100,
            "height" :        40, },              
        "health_text" :   {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "health_text.png")),(140,40)),
            "dimensions" :    (140,40),
            "width"  :        140,
            "height" :        40, },       
        "level_text" :    {
            "surface":        pygame.transform.scale(pygame.image.load(os.path.join("Game Images", "level_text.png")),(80,40)),
            "dimensions" :    (80,40),
            "width"  :        80,
            "height" :        40, },     
    }

    for scorenumbers in range(10):
        pictures[str(scorenumbers)] = {
            "surface" : pygame.transform.scale(pygame.image.load(os.path.join("Game Images", f"{str(scorenumbers)}.png")),(60,60)),
            "dimensions" :    (60,60),
            "width" :   60,
            "height" :  60, }

    pictures["menu"]["surface"].blit(pictures["slime_name_text"]["surface"],(10,10))
    pictures["menu"]["surface"].blit(pictures["health_text"]["surface"],(5,70))
    pictures["menu"]["surface"].blit(pictures["level_text"]["surface"],(110,10))

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
    maincharacter=slime(0,(GROUNDLEVEL - 60),pictures["slimepic"]["width"],pictures["slimepic"]["height"],"slime",4)
    sword=weapon(0,0,pictures["swordpic"]["width"],pictures["swordpic"]["height"],"weapon")
    playbutton = drawunit(250,121,pictures["play"]["width"],pictures["play"]["height"],"button")
    pausebutton = drawunit(385,10,pictures["pause"]["width"],pictures["pause"]["height"],"button")
    menubutton = drawunit(25,300,pictures["openmenu"]["width"],pictures["openmenu"]["height"],"button")
    menuexitbutton = drawunit(550,300,pictures["exitmenu"]["width"],pictures["exitmenu"]["height"],"button")

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
                snake=snakeenemy(600,193,pictures["enemysnake"]["width"],pictures["enemysnake"]["height"],"enemysnake",snakehitpoint,snaketype)
                objectrenderlist.append(snake)
                snakespawntimer=0
                snakespawncounter=random.randint(0,180)
            if meteortimer == meteorspawncounter:
                meteor = meteors(random.randint(50,550),-100,pictures["enemymeteor"]["width"],pictures["enemymeteor"]["height"],"enemymeteor")
                objectrenderlist.append(meteor)
                meteortimer = 0
                meteorspawncounter = random.randint(180,360)
            if dragontimer == dragonspawncounter:
                dragon = dragonenemy(BGWIDTH-60,random.randint(34,108),pictures["enemydragon"]["width"],pictures["enemydragon"]["height"],"enemydragon")
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
                    power=powerup(objectrender.getx() + objectrender.getwidth()/2 - 12,objectrender.gety()+40,pictures["powerup"]["width"],pictures["powerup"]["height"],"powerup",600)
                    objectrenderlist.append(power)
                try:
                    objectrenderlist.remove(objectrender)     
                except ValueError:
                    print("Object Does Not Exist in List")
                except:
                    print("Unknown Error")

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
            screen.blit(pictures["background"]["surface"],(backgroundx,0))
            screen.blit(pictures["background"]["surface"],(background2x,0))
            screen.blit(pictures["openmenu"]["surface"],(25,300))
            screen.blit(pictures[sword.getweapontype()]["surface"],(sword.getposition()))
            screen.blit(pictures["slimepic"]["surface"],(maincharacter.getposition()))
            screen.blit(pictures[hundredthdigit]["surface"],(420,0))
            screen.blit(pictures[tenthdigit]["surface"],(480,0))
            screen.blit(pictures[singledigit]["surface"],(540,0))
            if paused == False:
                screen.blit(pictures["pause"]["surface"],(pausebutton.x,pausebutton.y))
            for x in range(maincharacter.gethealth()):
                screen.blit(pictures["heart"]["surface"],(10+30*x,10))
            for x in range(maincharacter.getiframe()):
                screen.blit(pictures["shield"]["surface"],maincharacter.getposition())
            for objectrender in objectrenderlist:
                if objectrender.classtype == "critter":
                    screen.blit(pictures[objectrender.classtype]["surface"],(objectrender.getposition()),objectrender.getcoordinates())
                elif objectrender.classtype == "enemydragon":
                    screen.blit(pictures[objectrender.classtype]["surface"],objectrender.getposition())
                elif objectrender.classtype == "explosion":
                    screen.blit(pictures[objectrender.classtype]["surface"],(objectrender.getposition()),objectrender.getcoordinates())  
                elif objectrender.classtype == "enemysnake":
                    screen.blit(pictures[objectrender.classtype]["surface"],objectrender.getposition())
                    heartoffsets=0
                    for x in range(objectrender.gethealth()):
                        if heartoffsets >= 0:
                            heartoffsets = heartoffsets - x
                        else:
                            heartoffsets = heartoffsets + x
                        if objectrender.gethealth()%2 == 1:
                            screen.blit(pictures["heart"]["surface"],((objectrender.getmiddlex()-25/2)+25*heartoffsets,objectrender.y-35))
                        else:
                            screen.blit(pictures["heart"]["surface"],((objectrender.getmiddlex())+25*heartoffsets,objectrender.y-35))
                else:
                    screen.blit(pictures[objectrender.classtype]["surface"],objectrender.getposition())
            if paused:
                screen.blit(pictures["grayfilter"]["surface"],(0,0))
                screen.blit(pictures["play"]["surface"],(playbutton.x,playbutton.y))
            if openmenu:
                screen.blit(pictures["menu"]["surface"],(0,0))
                screen.blit(pictures["exitmenu"]["surface"],(menuexitbutton.x,menuexitbutton.y))
                for x in range(maincharacter.gethealth()):
                    screen.blit(pictures["heart"]["surface"],(130+30*x,80))
        else:
            screen.blit(pictures["gameoverpic"]["surface"],(0,0))

        #Timer
        pygame.display.flip()
        clock.tick(60)