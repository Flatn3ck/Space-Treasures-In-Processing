import globals, main_game, new_turn
from globals import Player, Card

artefacts = ['Swap','Haste','Eyedrop','Skip','Exchange','Blockade']
spelers = globals.players
elements = ["Amaterasu", 'Aqua', "Kaytsak"] 
artefactIndex = 0
elementIndex = 0
spelerIndex = 0
bg_index = 0
opacityTooManyCardsMsg = 0
whichCardAdded = artefacts[0] #temp voor pop up als kaart is toegevoegd aan een speler
frame = 1
interval = 250
rollFirstTime = True
roll_dice = False
display_dice = 0
dice_roll_time = 60
popup_artefact_toegevoegd = False
def setup():  
    loadImages()

def draw():
    global scherm, opacityCardAddedMsg, opacityTooManyCardsMsg, frame, dice_roll_time, roll_dice, display_dice, dices
    cycleBackground()

    textFont(createFont('data/PressStart2P.ttf', 5))
    fill(0, 0, 0, 100)
    strokeWeight(0)
    rect(10, 115, 360, 90)
    rect(435, 130, 435, 200)

    #Selecteer knoppen
    #dobbelsteen
    if rollFirstTime == True:
        fill(255)        
        textSize(18)        
        text("Klik op de dobbelsteen\nom te rollen en kijk\nof je het artefact\nmag toevoegen", 22, 135)
        text("Druk op verder als\nje te weinig ogen hebt gegooid\nen dus de artefact niet mag pakken", 500, 600)
    if roll_dice and dice_roll_time > 0 and frame % 5 == 0: 
        display_dice = int(random(1, 7)) - 1  
        dice_roll_time -= 5

    if dice_roll_time == 0:
        roll_dice = False
    frame = frame + 1 if frame < 60 else 1
    
    #Spelers
    if spelerIndex == 0:
        image(PijlTerugIdle, 435, 130, 55, 55)
    else: image(PijlTerug, 435, 130, 55, 55)
    
    if spelerIndex == len(spelers) - 1:
        image(PijlVerderIdle, 815, 130, 55, 55)
    else: image(PijlVerder, 815, 130, 55, 55)
            #Artefacten
    if artefactIndex == 0:
        image(PijlTerugIdle, 435, 250, 55, 55)
    else: image(PijlTerug, 435, 250, 55, 55)

    if artefactIndex == 5:
        image(PijlVerderIdle, 815, 250, 55, 55)
    else: image(PijlVerder, 815, 250, 55, 55)
            #Elementen
    if elementIndex == 0:
        image(PijlTerugIdle, 435, 370, 55, 55)
    else: image(PijlTerug, 435, 370, 55, 55)

    if elementIndex == 2:
        image(PijlVerderIdle, 815, 370, 55, 55)
    else: image(PijlVerder, 815, 370, 55, 55)
    
    #Variabelen en text, images
    image(LeegVak, 495, 130, 315, 55)
    image(LeegVak, 495, 250, 315, 55)
    image(LeegVak, 495, 370, 315, 55)
    image(VerderKnop, 1100, 655, 165, 55)
    image(ToevoegenKnop, 530, 450, 240, 55)
    image(dices[display_dice], 90, 220, 200, 200)

    #berichtje als iemand geen artefacten meer kan toevoegen
    fill(240, opacityTooManyCardsMsg)
    textSize(17)
    tint(opacityTooManyCardsMsg)
    
    if opacityTooManyCardsMsg > 0:
        opacityTooManyCardsMsg -= 2.5
        
    if len(spelers[spelerIndex].cards) == 5 and opacityTooManyCardsMsg > 0:
        image(LeegVak, 435, 640, 435, 70)
        text('Kan niet meer toevoegen\nje mag max 5 kaarten!', 450, 655, 500, 55)
        
    tint(255)
    fill(240)
    textSize(17)
    text('Speler:', 600 , 100, 300, 250)
    text('Kies het artefact:', 505, 220, 500, 500)
    text('Het element van de planeet:', 505, 330, 300, 250)
    textAlign(CENTER)
    text(spelers[spelerIndex].name, 505, 150, 300, 50)
    text(artefacts[artefactIndex], 505, 270, 300, 130)
    text(elements[elementIndex], 505, 390, 300, 250)
    textAlign(CORNER)
    if popup_artefact_toegevoegd == False:
        #muis en image knoppen veranderen wanneer muis op knop
        #verder knop
        if isMouseOnButton(1100, 655, 165, 55):
            image(VerderKnop2, 1100, 655, 165, 55)
            cursor(HAND)
        #toevoegen knop
        elif isMouseOnButton(530, 450, 240, 55):
            image(ToevoegenKnop2, 530, 450, 240, 55)
            cursor(HAND)
        #player knoppen
        elif isMouseOnButton(435, 130, 55, 55) and spelerIndex > 0:
            image(PijlTerug2, 435, 130, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 130, 55, 55) and spelerIndex < len(spelers) - 1:
            image(PijlVerder2, 815, 130, 55, 55)
            cursor(HAND)
        #artefact knoppen
        elif isMouseOnButton(435, 250, 55, 55) and artefactIndex > 0:
            image(PijlTerug2, 435, 250, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 250, 55, 55) and artefactIndex < 5:
            image(PijlVerder2, 815, 250, 55, 55)
            cursor(HAND)
        #element knoppen
        elif isMouseOnButton(435, 370, 55, 55) and elementIndex > 0:
            image(PijlTerug2, 435, 370, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(815, 370, 55, 55) and elementIndex < 2:
            image(PijlVerder2, 815, 370, 55, 55)
            cursor(HAND)
        elif isMouseOnButton(90, 220, 200, 200):
            cursor(HAND)
        else: cursor(ARROW)
    elif popup_artefact_toegevoegd == True:
        image(GrootLeegvak, 250, 250, 800, 300)
        image(PijlVerder, 950, 450, 55, 55)
        if isMouseOnButton(950, 450, 55, 55):
            image(PijlVerder2, 950, 450, 55, 55)
            cursor(HAND)
        else:
            cursor(ARROW)
        textSize(20)  
        text("Leg nu fysiek de kaart\nbij het juiste fiche\nzodat hij uit de stapel blijft.", 290, 350)
    
def mousePressed():
    global rollFirstTime, popup_artefact_toegevoegd, roll_dice, dice_roll_time, artefactIndex, elementIndex, spelerIndex, scherm, opacityCardAddedMsg, opacityTooManyCardsMsg, cardAddedTo, whichCardAdded, spelers
    if  popup_artefact_toegevoegd == False:
        if isMouseOnButton(90, 220, 200, 200):
            roll_dice = True
            dice_roll_time = 60
            rollFirstTime = False
        
        #verder knop
        if isMouseOnButton(1100, 655, 165, 55):
            main_game.turn_player_index = main_game.turn_player_index + 1 if main_game.turn_player_index < len(globals.players) - 1 else 0
            new_turn.player = globals.players[main_game.turn_player_index]
            globals.scherm = 'new_turn'
            return
        
        #Speler selecteer knoppen
        if isMouseOnButton(435, 130, 55, 55):
            if spelerIndex == 0:
                spelerIndex = spelerIndex
            else: spelerIndex -= 1
        if isMouseOnButton(815, 130, 55, 55):
            if spelerIndex == len(spelers) - 1:
                spelerIndex = spelerIndex
            else: spelerIndex += 1        
        #Artefact selecteer knoppen
        if isMouseOnButton(435, 250, 55, 55):
            if artefactIndex == 0:
                artefactIndex = artefactIndex
            else: artefactIndex -= 1                
        if isMouseOnButton(815, 250, 55, 55):
            if artefactIndex == 5:
                artefactIndex = artefactIndex
            else: artefactIndex += 1        
        #Element selecteer knoppen
        if isMouseOnButton(435, 370, 55, 55):
            if elementIndex == 0:
                elementIndex = elementIndex
            else: elementIndex -= 1        
        if isMouseOnButton(815, 370, 55, 55):
            if elementIndex == 2:
                elementIndex = elementIndex
            else: elementIndex += 1                

        #toevoegen knop
        if isMouseOnButton(530, 450, 240, 55): 
            #artefact tevoegen aan speler        
            ply = Player(spelers[spelerIndex].name)
            if len(spelers[spelerIndex].cards) != 5:
                artefact_name = artefacts[artefactIndex]
                if artefact_name in ['Swap', 'Exchange', 'Blockade']:
                    cooldown = 4
                elif artefact_name == 'Skip':
                    cooldown = 3
                else:
                    cooldown = 0
                [ply.cards.append(card) for card in spelers[spelerIndex].cards]
                ply.cards.append(Card(name=artefact_name, cooldown=cooldown, element=elements[elementIndex]))
                spelers[spelerIndex] = ply
                popup_artefact_toegevoegd = True
            elif len(spelers[spelerIndex].cards) >= 5:
                opacityTooManyCardsMsg = 255
            else:
                globals.scherm = 'new_turn'
                
    elif popup_artefact_toegevoegd == True:
        if isMouseOnButton(950, 450, 55, 55):
            popup_artefact_toegevoegd = False
            spelerIndex = spelerIndex + 1 if spelerIndex < len(spelers) - 1 else 0
            main_game.turn_player_index = spelerIndex
            new_turn.player = spelers[spelerIndex]
            globals.scherm = 'new_turn'
def setSpelerIndex(index):
    global spelerIndex
    spelerIndex = index
            
def isMouseOnButton(posX, posY, buttonWidth, buttonHeight, centered = False):
  if centered:
   return True if posX - buttonWidth / 2 < mouseX < posX + buttonWidth / 2 and posY - buttonHeight / 2 < mouseY < posY + buttonHeight / 2  else False
  return True if posX < mouseX < posX + buttonWidth and posY < mouseY < posY + buttonHeight else False

def cycleBackground():
    global bg_index, interval, play_stars_animation
    
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
    global background_img,GrootLeegvak, VerderKnop, VerderKnop2, background_animation_images, PijlVerderIdle, dices, PijlTerugIdle, PijlTerug, PijlTerug2, PijlVerder, PijlVerder2, LeegVak, TerugKnop, TerugKnop2, ToevoegenKnop, ToevoegenKnop2
    dices = []
    for i in range(1, 7):
        dices.append(loadImage('assets/images/bot' + str(i) + '.gif'))
    PijlTerugIdle = loadImage('assets/images/PijlTerugIdle.png')
    PijlVerderIdle = loadImage('assets/images/PijlVerderIdle.png')
    PijlTerug = loadImage('assets/images/PijlTerugPaars.png')
    PijlTerug2 = loadImage('assets/images/PijlTerug2Paars.png')
    PijlVerder = loadImage('assets/images/PijlVerderPaars.png')
    PijlVerder2 = loadImage('assets/images/PijlVerder2Paars.png')
    LeegVak =  loadImage('assets/images/LeegVak.png')
    TerugKnop = loadImage('assets/images/TerugKnop.png')
    TerugKnop2 = loadImage('assets/images/TerugKnop2.png')
    VerderKnop = loadImage('assets/images/VerderKnop.png')
    VerderKnop2 = loadImage('assets/images/VerderKnop2.png')
    ToevoegenKnop = loadImage('assets/images/Toevoegen.png')
    ToevoegenKnop2 = loadImage('assets/images/Toevoegen2.png')
    GrootLeegvak = loadImage('assets/images/GrootLeegvak.png')
    background_img = loadImage('background/bg0.jpg')
    background_animation_images = [loadImage('background/bg' + str(i) + '.jpg') for i in range(1, 14)]

    
