import globals, artefact_screen, main_game, home_screen, kaart_pak_scherm

bg_index = 0
interval = 250
kaart_pakken_popup = False
artefact_gebruiken_popup = False
possess_artefact = False            # <-- Als je een artefact krijgt, moet deze van False naar True. Als deze op False staat krijg je een popup met "Je hebt geen artefact"
                                    #       Als de len. van player.cards > 1 --> possess_artefact = True ?                                    
player = None                     # <-- hier kan je fixen dat de spelersnaam per beurt naar een andere speler gaat

def setup():
    size(1280, 720)
    frameRate(30)
    textFont(createFont('data/PressStart2P.ttf', 5))
    loadImages()
    
def draw():
    global artefact_gebruiken_popup
    
    cycleBackground()
    
    # Eerste argument is de speler van wie je de kaarten wilt laten zien.
    # Tweede argument is de grootte van de kaarten als tuple. (width, height)
    # Derde argument is de positie van de kaarten als tuple. (x, y)
    # Deze functie kun je vinden op lijn 271 van main_game.py
    main_game.drawCards(player, (180, 90), (655, 595))
    
    textFont(createFont('data/PressStart2P.ttf', 5))
    
    possess_artefact = len(player.cards) > 0
    
    if not home_screen.game_in_progress:
        home_screen.game_in_progress = True
    
    #images
    imageMode(CORNER)
    image(Regels, 10, 10, 175, 55)
    image(GrootLeegvak, 290, 400, 295, 140)       # leeg vlak voor "Kaart pakken"           ------ was eerst 430, test met 400
    image(GrootLeegvak, 710, 400, 295, 140)       # leeg vlak voor "Artefact gebruiken"     ------ was eerst 430, test met 400
    image(GrootLeegvak, 360, 60, 595, 120)        # leeg vlak voor welke speler aan de beurt is
    fill(0)
    rect(350,220,655,130)                         # leeg zwart vlak achter bovenste tekst
    fill(0)
    rect(60,565,575,100)                          # leeg zwart vlak achter onderste tekst
    
    if not kaart_pakken_popup and not artefact_gebruiken_popup:
        if isMouseOnButton(10, 10, 175, 55):
            image(Regels2, 10, 10, 175, 55)
            cursor(HAND)
        elif isMouseOnButton(290, 400, 295, 140):
            image(GrootLeegvak2, 290, 400, 295, 140)
            cursor(HAND)
            cursor(HAND)
        elif isMouseOnButton(710, 400, 295, 140):
            image(GrootLeegvak2, 710, 400, 295, 140)
            cursor(HAND)
        else: cursor(ARROW)
        
    fill(255)        
    textSize(30)
    textAlign(LEFT)  
    text("Huidige kaarten : ", 100, 660)
    text("Kies wat je wilt doen", 360, 305)
    text("Kaart\npakken", 345, 470)
    textSize(27)
    text("Artefact\ngebruiken", 735, 470)
    textAlign(CENTER)
    text(player.name, 650, 140)                      # line met de variable van de huidige speler , check line 4!!!
    textAlign(LEFT)
    
    alles_op_cooldown = len(filter(lambda x: not x.on_cooldown, player.cards)) == 0 and len(player.cards) > 0
    
    if alles_op_cooldown and artefact_gebruiken_popup:                  # als al je artefacten cooldown hebben
        image(GrootLeegvak, 250, 250, 800, 300)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)    
        textSize(20)
        text("Al je artefacten staan op cooldown!", 300, 320)
        textSize(16)  
        text("Je kunt momenteel geen artefact gebruiken.", 295, 420)
    
    if kaart_pakken_popup:               
        image(GrootLeegvak, 250, 250, 800, 300)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)    
        textSize(30)
        text("Pak een kaart", 475, 300)
        textSize(15)  
        text("Pak een kaart van de stapel", 285, 400)

    if not alles_op_cooldown and artefact_gebruiken_popup:   
        if not possess_artefact:
            image(GrootLeegvak, 250, 250, 800, 300)
            image(PijlVerder, 950, 450, 55, 55)
            if isMouseOnButton(950, 450, 55, 55):
                image(PijlVerder2, 950, 450, 55, 55)
                cursor(HAND)
            else:
                cursor(ARROW)
    
            textSize(30)
            text("Je hebt geen artefacten", 315, 320)
            textSize(15)  
            text("Je kunt pas een artefact gebruiken als je \ner minimaal 1 hebt.", 285, 400)
        else:
            artefact_gebruiken_popup = False
            main_game.turn_player_index = globals.players.index(player)
            globals.scherm = 'main'

def mousePressed():
    global kaart_pakken_popup, artefact_gebruiken_popup
    if not kaart_pakken_popup and not artefact_gebruiken_popup:
        
        if isMouseOnButton(10, 10, 175, 55):
            home_screen.screen = 1
            globals.scherm = 'home'                                         #Ga naar regelscherm
            
        if isMouseOnButton(290, 400, 295, 140):                             #Kaarten pak knop
            kaart_pakken_popup = True                                  
            
        if isMouseOnButton(710, 400, 295, 140):                             #Artefact gebruiken knop
            artefact_gebruiken_popup = True
            
    elif kaart_pakken_popup == True:
        if isMouseOnButton(950, 450, 55, 55):
            globals.scherm = 'kaart_pak'
            kaart_pakken_popup = False
            
    elif artefact_gebruiken_popup == True and possess_artefact == True:
        if isMouseOnButton(950, 450, 55, 55):
            main_game.turn_player_index = globals.players.index(player)
            globals.scherm = 'main'                     # !!!Ga naar het scherm van Hayk!!!
            artefact_gebruiken_popup = False
            
    elif artefact_gebruiken_popup == True and possess_artefact == False:
        if isMouseOnButton(950, 450, 55, 55):        
            artefact_gebruiken_popup = False  # !!!Ga Terug naar hetzelfde scherm, je kan alleen op 'kaart pakken' drukken todat je een artefact hebt!!!
        
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
   return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2  else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False
    
def cycleBackground():
    global bg_index, interval
    
    if interval <= 0:
        if bg_index < len(background_animation_images):            
            background(background_animation_images[bg_index])
            bg_index += 1
            if bg_index == 13:
                interval = 250
                bg_index = 0
    else:
        background(background_img)

    interval -= 1     
    
def loadImages():
    global background_img, background_animation_images, Regels, Regels2, GrootLeegvak, GrootLeegvak2, PijlVerder, PijlVerder2
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]
    background_img = loadImage('background/bg0.jpg')
    Regels = loadImage('assets/images/Regels.png')
    Regels2 = loadImage('assets/images/Regels2.png')
    GrootLeegvak = loadImage('assets/images/GrootLeegvak.png')
    GrootLeegvak2 = loadImage('assets/images/GrootLeegvak2.png')
    PijlVerder = loadImage('assets/images/PijlVerderPaars.png')
    PijlVerder2 = loadImage('assets/images/PijlVerder2Paars.png')
