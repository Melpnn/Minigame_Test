import pygame
import os
import random

from drawunit import drawunit
from worldlevel import worldlevel
from snake import snakeenemy
from meteor import meteors
from dragon import dragonenemy
from ghost import ghostenemy
from powerup import powerup
from slime import slime
from weapon import weapon
from critters import critters
from explosion import explosion
from textbox import threedigittextbox
from displaybar import displaybar
from pygame.locals import * 

GROUNDLEVEL = 263
BGHEIGHT = 343
BGWIDTH = 600

def generateobject(classtype,objectrenderlist):
    if classtype == "enemysnake":
        snakehitpoint = 1
        snaketype = "Normal"
        if random.randint(0,100) <= 30:
            snakehitpoint = 5
            snaketype = "Big"
        snake=snakeenemy(600,193,pictures["enemysnake"]["dimensions"][0],pictures["enemysnake"]["dimensions"][1],"enemysnake",snakehitpoint,snaketype,5)
        objectrenderlist.append(snake)
    elif classtype == "neutralmeteor":       
        meteor = meteors(random.randint(50,550),-100,pictures["neutralmeteor"]["dimensions"][0],pictures["neutralmeteor"]["dimensions"][1],"neutralmeteor")
        objectrenderlist.append(meteor)
    elif classtype == "enemydragon":
        dragon = dragonenemy(BGWIDTH-60,random.randint(34,108),pictures["enemydragon"]["dimensions"][0],pictures["enemydragon"]["dimensions"][1],"enemydragon",10)
        objectrenderlist.append(dragon)
    elif classtype == "enemyghost":
        ghost = ghostenemy(500,193,pictures["enemyghost"]["dimensions"][0],pictures["enemyghost"]["dimensions"][1],"enemyghost",50,20,1,1)
        objectrenderlist.append(ghost)
    elif classtype == "critter_spritesheet":
        bunny=critters(0,GROUNDLEVEL-31,31,31,"critter_spritesheet",[(449,166,31,31),(502,166,31,31),(554,166,31,31),(605,166,31,31)])
        objectrenderlist.append(bunny)
    else:
        print("Unkown Classtype " + classtype)

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((BGWIDTH,BGHEIGHT))

    clock = pygame.time.Clock()

    #Avoid keywords: enemy, arrow
    pictures={
        "slimepic" : {
            "surface":        pygame.image.load(os.path.join("Game Images","slime(hitbox).png")),
            "dimensions" :    (60,60)},
        "swordpic" : {
            "surface":        pygame.image.load(os.path.join("Game Images","sword(hitbox).png")),
            "dimensions" :    (50,50)},
        "bowpic" : {
            "surface":        pygame.image.load(os.path.join("Game Images","bow.png")),
            "dimensions" :    (50,50)},           
        "arrow" : {
            "surface":        pygame.image.load(os.path.join("Game Images","arrow(hitbox).png")),
            "dimensions" :    (30,10)},             
        "bigarrow" : {
            "surface":        pygame.image.load(os.path.join("Game Images","superarrow(hitbox).png")),
            "dimensions" :    (50,30)},               
        "enemysnake" : {
            "surface":        pygame.image.load(os.path.join("Game Images","snake(hitbox).png")),
            "dimensions" :    (70,70)}, 
        "neutralmeteor": {
            "surface":        pygame.image.load(os.path.join("Game Images","meteor(hitbox).png")),
            "dimensions" :    (30,80)},             
        "enemydragon":  {
            "surface":        pygame.image.load(os.path.join("Game Images","dragon.png")),
            "dimensions" :    (120,40)},        
        "enemyghost":  {
            "surface":        pygame.image.load(os.path.join("Game Images","ghost.png")),
            "dimensions" :    (35,60)},           
        "gameoverpic" : {
            "surface":        pygame.image.load(os.path.join("Game Images","gameover.png")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},         
        "critter_spritesheet" :    {
            "surface":        pygame.image.load(os.path.join("Game Images", "animalspritesheet.png")),
            "dimensions" :    (31,31),
            "sheetdimensions": (653,422)},        
        "explosion_spritesheet" :   {
            "surface":        pygame.image.load(os.path.join("Game Images", "explosionspritesheet.png")),
            "dimensions" :    (59,59),
            "sheetdimensions":(300,120)},            
        "bgforest" :  {
            "surface":        pygame.image.load(os.path.join("Game Images","night_background.jpg")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},            
        "bgdesert" :  {
            "surface":        pygame.image.load(os.path.join("Game Images","desert_background.jpg")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},
        "bgice" :  {
            "surface":        pygame.image.load(os.path.join("Game Images","ice_background.jpg")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},
        "bgcastle" :  {
            "surface":        pygame.image.load(os.path.join("Game Images","castle_background.jpg")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},
        "loadingscreen" :  {
            "surface":        pygame.image.load(os.path.join("Game Images","loadingscreen_background.jpg")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},        
        "grayfilter":  {
            "surface":        pygame.image.load(os.path.join("Game Images","grayfilter.png")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},                  
        "heart" :  {
            "surface":        pygame.image.load(os.path.join("Game Images", "heart.png")),
            "dimensions" :    (25,25)},              
        "healthpowerup" :   {
            "surface":        pygame.image.load(os.path.join("Game Images", "healthpotion.png")),
            "dimensions" :    (20,30)},    
        "heartpowerup" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "heartpotion.png")),
            "dimensions" :    (20,30)},
        "attackpowerup" :     {
            "surface":        pygame.image.load(os.path.join("Game Images", "atkpowerup.png")),
            "dimensions" :    (15,25)},             
        "coin" :     {
            "surface":        pygame.image.load(os.path.join("Game Images", "coin.png")),
            "dimensions" :    (25,50)},           
        "enemywisp" :     {
            "surface":        pygame.image.load(os.path.join("Game Images", "wisp.png")),
            "dimensions" :    (20,20)},  
        "shield" :      {
            "surface":        pygame.image.load(os.path.join("Game Images", "shield.png")),
            "dimensions" :    (69,69)},    
        "play" :    {
            "surface":        pygame.image.load(os.path.join("Game Images", "play-icon.png")),
            "dimensions" :    (100,100)},            
        "pause" :    {
            "surface":        pygame.image.load(os.path.join("Game Images", "pause-icon.png")),
            "dimensions" :    (25,25)},     
        "attackbar" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "attack-icon.png")),
            "dimensions" :    (20,20)},       
        "openmenu" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "menu-icon.png")),
            "dimensions" :    (25,25)},            
        "menu" :     {
            "surface":        pygame.image.load(os.path.join("Game Images", "menu.png")),
            "dimensions" :    (BGWIDTH,BGHEIGHT)},         
        "exitmenu" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "menu-icon.png")),
            "dimensions" :    (25,25)},               
        "slime_name_text" :  {
            "surface":        pygame.image.load(os.path.join("Game Images", "slime_name_text.png")),
            "dimensions" :    (100,40)},              
        "health_text" :   {
            "surface":        pygame.image.load(os.path.join("Game Images", "health_text.png")),
            "dimensions" :    (140,40)},       
        "level_text" :    {
            "surface":        pygame.image.load(os.path.join("Game Images", "level_text.png")),
            "dimensions" :    (80,40)},    
        "killcount_text" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "killcounttitle_text.png")),
            "dimensions" :    (150,30)}, 
        "snakekillcount_text" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "snakekillcount_text.png")),
            "dimensions" :    (140,40)}, 
        "dragonkillcount_text" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "dragonkillcount_text.png")),
            "dimensions" :    (140,40)}, 
        "ghostboss_text" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "shadowmonarchtext.png")),
            "dimensions" :    (200,20)}, 
        "expbar" : {
            "surface":        pygame.image.load(os.path.join("Game Images", "expbar_background.jpg")),
            "dimensions" :    (550,10),}
    }

    for scorenumbers in range(10):
        pictures[str(scorenumbers)] = {
            "surface" : pygame.image.load(os.path.join("Game Images", f"{str(scorenumbers)}.png")),
            "dimensions" : (60,60)}
    
    for classtype in pictures:
        if "spritesheet" in classtype:
            pictures[classtype]["surface"] = pygame.transform.scale(pictures[classtype]["surface"],pictures[classtype]["sheetdimensions"])
        else:
            pictures[classtype]["surface"] = pygame.transform.scale(pictures[classtype]["surface"],pictures[classtype]["dimensions"])


    pictures["menu"]["surface"].blit(pictures["slime_name_text"]["surface"],(10,10))
    pictures["menu"]["surface"].blit(pictures["health_text"]["surface"],(5,70))
    pictures["menu"]["surface"].blit(pictures["level_text"]["surface"],(110,10))
    pictures["menu"]["surface"].blit(pictures["killcount_text"]["surface"],(330,15))
    pictures["menu"]["surface"].blit(pictures["snakekillcount_text"]["surface"],(305,50))
    pictures["menu"]["surface"].blit(pictures["dragonkillcount_text"]["surface"],(305,90))

    dArrow_keypress = False
    rArrow_keypress = False
    lArrow_keypress = False
    uArrow_keypress = False
    escape_keypress = False
    ikey_keypress = False
    ekey_keypress = False
    mouseclick = False
    spacepress = False
    weaponswap = False
    paused = False
    openmenu = False 
    loading = False

    #Loading Objects
    maincharacter=slime(0,(GROUNDLEVEL - 60),pictures["slimepic"]["dimensions"][0],pictures["slimepic"]["dimensions"][1],"slime",4)
    sword=weapon(0,0,pictures["swordpic"]["dimensions"][0],pictures["swordpic"]["dimensions"][1],"weapon")
    playbutton = drawunit(250,121,pictures["play"]["dimensions"][0],pictures["play"]["dimensions"][1],"button")
    pausebutton = drawunit(385,10,pictures["pause"]["dimensions"][0],pictures["pause"]["dimensions"][1],"button")
    menubutton = drawunit(25,300,pictures["openmenu"]["dimensions"][0],pictures["openmenu"]["dimensions"][1],"button")
    menuexitbutton = drawunit(550,300,pictures["exitmenu"]["dimensions"][0],pictures["exitmenu"]["dimensions"][1],"button")
    scoreboard = threedigittextbox(420,0,180,60,"textbox",0)
    dragonkc =  threedigittextbox(445,90,120,40,"textbox",0)
    snakekc = threedigittextbox(445,50,120,40,"textbox",0)
    playerlevel = threedigittextbox(500,305,75,25,"textbox",0)
    menulevel = threedigittextbox(175,10,120,40,"textbox",0)
    expbar = displaybar(25,330,550,10,"bar",(0,255,0))

    objectrenderlist = []

    levelone = worldlevel(["enemysnake","critter_spritesheet","enemyghost"],[(120,360),(180,420),(-1,-1)],pictures["bgcastle"]["surface"])
    leveltwo = worldlevel(["enemydragon","enemysnake","neutralmeteor"],[(180,420),(120,360),(180,300)],pictures["bgdesert"]["surface"]) 
    levelthree = worldlevel(["enemysnake","neutralmeteor"],[(120,360),(180,300)],pictures["bgice"]["surface"]) 
    worldlist = [levelone,leveltwo,levelthree]
    stage = 0
    cstage = 0
    loadingtimer = 0
    spawnboss = True
    bossalive = True

    explosioncoordinateslist = []
    for rows in range(2):
        for columns in range(5):
            explosioncoordinateslist.append((columns*60,rows*60,59,59))
    
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
                if event.key == pygame.K_e:
                    ekey_keypress = True
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
        if maincharacter.gethealth() > 0 and not(maincharacter.offscreen()) and not (paused or openmenu) and not (loading):
            objectdeletelist=[]
            if rArrow_keypress:
                maincharacter.changex(maincharacter.speed)
                if maincharacter.offscreen():
                    maincharacter.changex(-1)
            if lArrow_keypress:
                maincharacter.changex(-maincharacter.speed)
                if maincharacter.offscreen():
                    maincharacter.changex(1)

            for objectrender in objectrenderlist:
                if objectrender.offscreen():
                    objectdeletelist.append(objectrender)
                if objectrender.outofhealth():
                    if (objectrender.classtype == "enemysnake" and objectrender.getsnaketype() == "Big") and objectrender.attacker != "neutralmeteor":
                        scoreboard.value += 3
                        scoreboard.dictionaryupdate()
                        snakekc.value += 1
                        snakekc.dictionaryupdate()
                        maincharacter.updateexperience(objectrender.experience)
                    elif (objectrender.classtype == "enemysnake" or objectrender.classtype == "enemydragon") and objectrender.attacker != "neutralmeteor":
                        scoreboard.value += 1
                        scoreboard.dictionaryupdate()
                        if objectrender.classtype =="enemydragon":
                            dragonkc.value += 1
                            dragonkc.dictionaryupdate()
                            maincharacter.updateexperience(objectrender.experience)
                        elif(objectrender.classtype == "enemysnake"):
                            snakekc.value +=1
                            snakekc.dictionaryupdate()
                            maincharacter.updateexperience(objectrender.experience)
                    objectdeletelist.append(objectrender)
                if objectrender.classtype == "enemyghost":
                    objectrender.frameupdate(objectrenderlist)
                else:
                    objectrender.frameupdate()
                #TO DO: WARNING - FRAME UPDATE CHANGES RENDER LIST 
                if "enemy" in objectrender.classtype:
                    if objectrender.checkcollision(sword.getobjectbody()) and sword.getswingstate():
                        objectrender.losehealth(1,"weapon")
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        maincharacter.losehealth(1,objectrender.classtype)
                if objectrender.classtype =="healthpowerup":
                    if objectrender.checkcollision(maincharacter.getobjectbody()) and maincharacter.health < maincharacter.healthcap:
                        objectdeletelist.append(objectrender)
                        maincharacter.restorehealth()
                if objectrender.classtype =="heartpowerup":
                    if objectrender.checkcollision(maincharacter.getobjectbody()) and maincharacter.healthcap < 7:
                        objectdeletelist.append(objectrender)
                        maincharacter.healthcap += 1
                if objectrender.classtype =="attackpowerup":
                    if objectrender.checkcollision(maincharacter.getobjectbody()) and sword.attackbarcount < 3:
                        objectdeletelist.append(objectrender)
                        sword.attackbarcount +=1
                if objectrender.classtype == "neutralmeteor":
                    for otherobject in objectrenderlist:
                        if ((otherobject.classtype == "enemysnake" or otherobject.classtype == "enemydragon") 
                            and objectrender.checkcollision(otherobject.getobjectbody())):
                            otherobject.losehealth(otherobject.gethealth(),objectrender.classtype)  
                    if objectrender.checkcollision(maincharacter.getobjectbody()):
                        maincharacter.losehealth(3,"neutralmeteor")
                    if objectrender.y >= GROUNDLEVEL - 40:
                        explosioneffect = explosion(objectrender.x + (objectrender.width/2) - (pictures["explosion_spritesheet"]["dimensions"][0]/2),
                                                    objectrender.y,
                                                    pictures["explosion_spritesheet"]["dimensions"][0],
                                                    pictures["explosion_spritesheet"]["dimensions"][1],
                                                    "explosion_spritesheet", 
                                                    explosioncoordinateslist)
                        objectrenderlist.append(explosioneffect)
                        objectdeletelist.append(objectrender)
                if  "arrow" in objectrender.classtype:
                    for otherobject in objectrenderlist:
                        if "enemy" in otherobject.classtype:
                            if objectrender.checkcollision(otherobject.getobjectbody()):
                                if objectrender.classtype == "bigarrow":
                                    otherobject.losehealth(2,"bigarrow")
                                else:
                                    otherobject.losehealth(1,"arrow")
                                    objectdeletelist.append(objectrender)
            
            if mouseclick:
                sword.setswingstate()
                mouseclick = False
            
            if ekey_keypress:
                sword.setspecialattackstate()
                ekey_keypress = False

            if spacepress and not(maincharacter.getjumpstate()):
                maincharacter.startjump()

            if weaponswap:
                sword.toggleweapon()
                weaponswap = False

            for objectrender in objectdeletelist:
                if (objectrender.classtype == "enemysnake" and 
                    not(objectrender.getx() < -150) and random.randint(1,100) >= 75):
                    power=powerup(objectrender.getx() + objectrender.getwidth()/2 - (pictures["healthpowerup"]["dimensions"][0]/2),
                                  objectrender.gety() + (objectrender.height - pictures["healthpowerup"]["dimensions"][1]),
                                  pictures["healthpowerup"]["dimensions"][0],
                                  pictures["healthpowerup"]["dimensions"][1],
                                  "healthpowerup",
                                  600)
                    objectrenderlist.append(power)
                elif (objectrender.classtype == "enemydragon" and 
                    not(objectrender.getx() < -150) and random.randint(1,100) >= 80):
                    heartpotion = powerup(objectrender.getx() + objectrender.getwidth()/2 - (pictures["heartpowerup"]["dimensions"][0]/2),
                                  objectrender.gety() + (objectrender.height - pictures["heartpowerup"]["dimensions"][1]),
                                  pictures["heartpowerup"]["dimensions"][0],
                                  pictures["heartpowerup"]["dimensions"][1],
                                  "heartpowerup",
                                  300)
                    objectrenderlist.append(heartpotion)
                elif (objectrender.classtype == "enemywisp"  and 
                    not(objectrender.getx() < -150) and random.randint(1,100) >= 66):
                    bigarrowpowerup = powerup(objectrender.getx() + objectrender.getwidth()/2 - (pictures["attackpowerup"]["dimensions"][0]/2),
                                  objectrender.gety() + (objectrender.height - pictures["attackpowerup"]["dimensions"][1]),
                                  pictures["attackpowerup"]["dimensions"][0],
                                  pictures["attackpowerup"]["dimensions"][1],
                                  "attackpowerup",
                                  300)
                    objectrenderlist.append(bigarrowpowerup)
                elif (objectrender.classtype == "enemyghost"  and 
                    not(objectrender.getx() < -150)):
                        bossalive = False
                try:
                    objectrenderlist.remove(objectrender)     
                except ValueError:
                    print("Object Does Not Exist in List")
                except:
                    print("Unknown Error")

            spawnlist = worldlist[stage].frameupdate()
            maincharacter.frameupdate()  
            playerlevel.frameupdate(maincharacter.level)
            menulevel.frameupdate(maincharacter.level)
            sword.frameupdate(maincharacter.getposition(),objectrenderlist)

            for classtype in spawnlist:
                generateobject(classtype,objectrenderlist)
        
        if snakekc.value > 2 and stage == 0 :
            if spawnboss:
                generateobject("enemyghost",objectrenderlist)
                ghostbosshpbar = displaybar(75,65,450,10,"bar",(150,0,0))
                spawnboss = False
        
        if scoreboard.value >= 10 and scoreboard.value < 20 and not (bossalive):
            stage = 1
            if stage != cstage:
                cstage = stage
                loading = True
                loadingtimer = 60
                objectrenderlist.clear()
                maincharacter.x = 0
                maincharacter.y = GROUNDLEVEL - 60

        elif scoreboard.value >= 20 and not (bossalive):
            stage = 2
            if stage != cstage:
                cstage = stage
                loading = True
                loadingtimer = 60
                objectrenderlist.clear()
                maincharacter.x = 0
                maincharacter.y = GROUNDLEVEL - 60
        
        if loadingtimer > 0:
            loadingtimer -= 1
        else:
            loading = False

        #Rendering

        worldlist[stage].drawobject(screen)

        expbar.drawobject(screen,pictures,maincharacter.getexppercent())
        screen.blit(pictures["openmenu"]["surface"],(25,300))
        screen.blit(pictures[sword.getweapontype()]["surface"],(sword.getposition()))
        screen.blit(pictures["slimepic"]["surface"],(maincharacter.getposition()))
        screen.blit(pictures["level_text"]["surface"],(435,295))
        scoreboard.drawobject(screen,pictures)
        playerlevel.drawobject(screen,pictures)
        if paused == False:
            screen.blit(pictures["pause"]["surface"],(pausebutton.x,pausebutton.y))
        for x in range(maincharacter.gethealth()):
            screen.blit(pictures["heart"]["surface"],(10+30*x,10))
        for x in range(sword.attackbarcount):
            screen.blit(pictures["attackbar"]["surface"],(10+30*x,40))
        for x in range(maincharacter.getiframe()):
            screen.blit(pictures["shield"]["surface"],maincharacter.getposition())
        for objectrender in objectrenderlist:
            if objectrender.classtype == "enemysnake":
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
            elif objectrender.classtype == "enemyghost":
                ghostbosshpbar.drawobject(screen,pictures,objectrender.gethealthpercentage())
                screen.blit(pictures["ghostboss_text"]["surface"],(190,40))
            screen.blit(pictures[objectrender.classtype]["surface"],(objectrender.getposition()),objectrender.getcoordinates())  
        if paused:
            screen.blit(pictures["grayfilter"]["surface"],(0,0))
            screen.blit(pictures["play"]["surface"],(playbutton.x,playbutton.y))

        if openmenu:
            screen.blit(pictures["menu"]["surface"],(0,0))
            screen.blit(pictures["exitmenu"]["surface"],(menuexitbutton.x,menuexitbutton.y))
            for x in range(maincharacter.gethealth()):
                screen.blit(pictures["heart"]["surface"],(130+30*x,80))
            dragonkc.drawobject(screen,pictures)
            snakekc.drawobject(screen,pictures)
            menulevel.drawobject(screen,pictures)
        
        if loading:
            screen.blit(pictures["loadingscreen"]["surface"],(0,0))

        if maincharacter.gethealth() <= 0 or maincharacter.offscreen():
            screen.blit(pictures["grayfilter"]["surface"],(0,0))

        #Timer
        pygame.display.flip()
        clock.tick(60)