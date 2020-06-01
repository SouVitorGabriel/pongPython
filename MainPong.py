from PPlay.window import *
from PPlay.sprite import *

#INICIALIZACAO
janela = Window(1024, 576)
teclado = Window.get_keyboard()

#configurações
ballVely = 350
BallVelx = 450
velpad = 400
velpadEnemy = 200

bola = Sprite ("bola2.png", 8)
bola.set_sequence_time(0,7, 1, True)

balls = [bola]

pad1 = Sprite ("pad.jpg", 1)
pad1.width = 30
pad1.x = 10

pad2 = Sprite ("pad.jpg", 1)
pad2.width = 30

pad2.x = janela.width - pad2.width - 10

iaPad1 = True

pointsPlayer1 = 0
pointsPlayer2 = 0


level = 0

#cenário
sceneCenter = Sprite("pad2.jpg", 1)
sceneCenter.y = 0
sceneCenter.height = janela.height
sceneCenter.width = 10
sceneCenter.x = janela.width/2 - sceneCenter.width / 2





#loop
while (1):
    time = int(janela.time_elapsed() / 1000)
    
    #TEMPO
    

    #ENTRADAS
    if (teclado.key_pressed("UP")):
        if (pad2.y > 0):
            pad2.y -= velpad * janela.delta_time()
    if (teclado.key_pressed("DOWN")):
        if ((pad2.y + pad2.height) < janela.height):
            pad2.y += velpad * janela.delta_time()

    #liga IA
    if(teclado.key_pressed("i")):
        if(iaPad1 == True):
            iaPad1 = False
        else:
            iaPad1 = True

    #IA
    if(iaPad1):
        if(bola.x < janela.width / 2):
            if(bola.y > pad1.y):
                pad1.y += 2 + velpadEnemy * janela.delta_time()
            else:
                pad1.y -= 0.5 + velpadEnemy * janela.delta_time()

            #pad1.y = bola.y
            
            if (pad1.y < 0):
                pad1.y = 0
            if(pad1.y + pad1.height > janela.height):
                pad1.y = janela.height - pad1.height


    else:
        if (teclado.key_pressed("d")):
            if (pad1.y > 0):
                pad1.y -= velpadEnemy * janela.delta_time()
        if (teclado.key_pressed("c")):
            if ((pad1.y + pad2.height) < janela.height):
                pad1.y += velpadEnemy * janela.delta_time()

    #fimIA
    

    #UPDATES

    
    bola.x +=BallVelx*janela.delta_time()
    bola.y += ballVely*janela.delta_time()
    if (bola.x >= janela.width - bola.width)or(bola.x < 0):
        if (bola.x >= janela.width - bola.width):
            pointsPlayer1 += 1
        if (bola.x < 0):
            pointsPlayer2 += 1
        bola.x = janela.width/2
        bola.y = janela.height/2
        BallVelx *= -1
    if (bola.y >= janela.height - bola.height) or (bola.y < 0):
        ballVely *= -1

    bola.update()

    #FISICA
    if bola.collided(pad1) or bola.collided(pad2):
        BallVelx *= -1

    #DESENHO
    janela.set_background_color((0, 0, 0))
    janela.draw_text("{} pontos".format(pointsPlayer2) , 535, 5, 20, (255,255,255), "Arial", True)
    janela.draw_text("{} pontos".format(pointsPlayer1) , 405, 5, 20, (255,255,255), "Arial", True)
    janela.draw_text("Tempo de jogo: {} seg.".format(time) , 525, janela.height - 25, 20, (255,255,255), "Arial", True)
    sceneCenter.draw()


    pad1.draw()
    pad2.draw()
    bola.draw()

    



    janela.update()