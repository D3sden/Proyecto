import pygame
from pygame import mixer


# Iniciamos mixer para los sonidos/musica en el juego y pygame
mixer.init()
pygame.init()

# Pantalla
panta = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Juego/ Proyecto")

# Imagenes ; V al final es la imagen volteada
fondo = pygame.image.load(
    "/Users/cafec/Desktop/fondo.png").convert()
n = pygame.image.load(
    "/Users/cafec/Desktop/n.png").convert_alpha()
x = pygame.image.load(
    "/Users/cafec/Desktop/x.png").convert_alpha()
e = pygame.image.load(
    "/Users/cafec/Desktop/e.png").convert_alpha()
p = pygame.image.load(
    "/Users/cafec/Desktop/pm.png").convert_alpha()
awsd = pygame.image.load(
    "/Users/cafec/Desktop/wasd.png").convert_alpha()
flechas = pygame.image.load(
    "/Users/cafec/Desktop/flechas.png").convert_alpha()
fotop1 = pygame.image.load(
    "/Users/cafec/Desktop/P1.png").convert_alpha()
hagachadop1 = pygame.image.load(
    "/Users/cafec/Desktop/Hp1.png").convert_alpha()
hagachadop1V = pygame.image.load(
    "/Users/cafec/Desktop/Hp1V.png").convert_alpha()
fotop1V = pygame.image.load(
    "/Users/cafec/Desktop/P1V.png").convert_alpha()
ataquep1 = pygame.image.load(
    "/Users/cafec/Desktop/p1t.png").convert_alpha()
ataquep1V = pygame.image.load(
    "/Users/cafec/Desktop/p1tV.png").convert_alpha()
muerto1 = pygame.image.load(
    "/Users/cafec/Desktop/Mp1.png").convert_alpha()
p1tH = pygame.image.load(
    "/Users/cafec/Desktop/p1tH.png").convert_alpha()
p1tHV = pygame.image.load(
    "/Users/cafec/Desktop/p1tHV.png").convert_alpha()
fotop2 = pygame.image.load(
    "/Users/cafec/Desktop/p2.png").convert_alpha()
fotop2V = pygame.image.load(
    "/Users/cafec/Desktop/p2V.png").convert_alpha()
ataquep2 = pygame.image.load(
    "/Users/cafec/Desktop/p2tM.png").convert_alpha()
ataquep2V = pygame.image.load(
    "/Users/cafec/Desktop/p2tVM.png").convert_alpha()
muerto2 = pygame.image.load(
    "/Users/cafec/Desktop/Mp2.png").convert_alpha()
hagachadop2 = pygame.image.load(
    "/Users/cafec/Desktop/Hp2.png").convert_alpha()
hagachadop2V = pygame.image.load(
    "/Users/cafec/Desktop/Hp2V.png").convert_alpha()
p2tH = pygame.image.load(
    "/Users/cafec/Desktop/p2tH.png").convert_alpha()
p2tHV = pygame.image.load(
    "/Users/cafec/Desktop/p2tHV.png").convert_alpha()
# Musica
pygame.mixer.music.load("/Users/cafec/Desktop/Mfondo.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)
gp = pygame.mixer.Sound("/Users/cafec/Desktop/gp.wav")
gp.set_volume(0.1)


# Player 1 espec
player1 = pygame.Rect((100, 500), (50, 100))

Izquierda = False
Derecha = False
Salto1 = False
hagacharse = False
speed1 = 2
p1win = False
p1contadorwin = 0
vivo = True
ataque = False
hp1 = 400
vuelta1 = False

# Player 2 espec
player2 = pygame.Rect((900, 500), (45, 100))
Izquierda2 = False
Derecha2 = False
Salto2 = False
hagacharse2 = False
speed2 = 2
p2win = False
p2contadorwin = 0
vivo2 = True
ataque2 = False
hp2 = 400
vuelta2 = False

# General
telon = True
inicio = False
ronda = 0
r = True
font = pygame.font.SysFont("arialblack", 36)
font2 = pygame.font.SysFont("arialblack", 16)
Clok = pygame.time.Clock()
cian = (0, 255, 255)
rojo = (255, 0, 0)

# Rectangulos de "ataque"/ hitbox


def cuadradot1():
    global hp2
    ataque1 = pygame.Rect(player1.right, player1.y, 35, 50)
    if vuelta1 == True:
        ataque1 = pygame.Rect(player1.left-50, player1.y, 35, 50)
    if ataque1.colliderect(player2):
        hp2 -= 1
    #pygame.draw.rect(panta, (0, 255, 0), ataque1)


def cuadradot2():
    global hp1
    # se le resta el ancho y el largo del ataque
    ataque2 = pygame.Rect(player2.right-80, player2.y, 35, 50)
    if vuelta2 == True:
        # Se le suma el ancho
        ataque2 = pygame.Rect(player2.x+45, player2.y, 35, 50)
    if ataque2.colliderect(player1):
        hp1 -= 1
    #pygame.draw.rect(panta, (0, 255, 0), ataque2)

# Barras de vida, el primer rectangulo es el fondo de la barra de vida.


def barravida1(hp1):
    pygame.draw.rect(panta, (255, 0, 0), (0, 200, 400, 30))
    pygame.draw.rect(panta, (255, 255, 0), (0, 200, hp1, 30))


def barravida2(hp2):
    pygame.draw.rect(panta, (255, 0, 0), (600, 200, 400, 30))
    pygame.draw.rect(panta, (0, 0, 255), (600, 200, hp2, 30))

# Funcion para escribir en la pantalla


def escribir_texto(texto, font, panta, x, y):
    texto = font.render(texto, 1, rojo)
    text_rect = texto.get_rect()
    text_rect.topleft = (x, y)
    panta.blit(texto, text_rect)


def escribir():
    escribir_texto("Controles: Player 1", font2, panta, 90, 100)
    escribir_texto("A = Izquierda", font2, panta, 120, 300)
    escribir_texto("D = Derecha", font2, panta, 120, 350)
    escribir_texto("W = Salto", font2, panta, 120, 400)
    escribir_texto("S = Hagacharse", font2, panta, 120, 450)
    escribir_texto("E = Golpear", font2, panta, 120, 500)
    escribir_texto("Controles: Player 2", font2, panta, 780, 100)
    escribir_texto("<- = Izquierda", font2, panta, 810, 300)
    escribir_texto("-> = Derecha", font2, panta, 810, 350)
    escribir_texto("↑ = Salto", font2, panta, 810, 400)
    escribir_texto("↓ = Hagacharse", font2, panta, 810, 450)
    escribir_texto("N = Golpear", font2, panta, 810, 500)
    escribir_texto("P = Controles", font2, panta, 491, 300)
    escribir_texto("X = Salir del juego", font2, panta, 491, 350)


def controles():
    if telon == True:
        panta.fill(cian)
        panta.blit(awsd, (50, 150))
        panta.blit(flechas, (760, 150))
        panta.blit(p, (500, 210))
        panta.blit(x, (550, 210))
        panta.blit(e, (182, 157))
        panta.blit(n, (880, 157))
        escribir_texto("Presiona cualquier tecla para salir",
                       font2, panta, 340, 550)
        escribir_texto("MATA AL OTRO JUGADOR",
                       font2, panta, 401, 20)
        escribir()


while r:
    panta.blit(fondo, (0, 0))
    barravida1(hp1)
    barravida2(hp2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        # Movimiento
        if event.type == pygame.KEYDOWN:
            telon = False
            if event.key == pygame.K_p:
                telon = True
            if event.key == pygame.K_x:
                r = False
            if event.key == pygame.K_a and vivo == True:
                Derecha = False
                Izquierda = True
            if event.key == pygame.K_d and vivo == True:
                Izquierda = False
                Derecha = True
            if event.key == pygame.K_w and vivo == True:
                Salto1 = True
            if event.key == pygame.K_e and vivo == True:
                ataque = True
            if event.key == pygame.K_s and vivo == True:
                hagacharse = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Izquierda = False
            if event.key == pygame.K_d:
                Derecha = False
            if event.key == pygame.K_e:
                ataque = False
            if event.key == pygame.K_s:
                hagacharse = False
            if vivo == False or vivo2 == False:
                if event.key == pygame.K_r:
                    if p1win:
                        p1contadorwin += 1
                    if p2win:
                        p2contadorwin += 1
                    hp1 = 400
                    hp2 = 400
                    vivo = True
                    vivo2 = True
                    player1 = pygame.Rect((100, 500), (50, 100))
                    player2 = pygame.Rect((900, 500), (50, 100))
                    ronda += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and vivo2 == True:
                Derecha2 = False
                Izquierda2 = True
            if event.key == pygame.K_RIGHT and vivo2 == True:
                Izquierda2 = False
                Derecha2 = True
            if event.key == pygame.K_UP and vivo2 == True:
                Salto2 = True
            if event.key == pygame.K_DOWN and vivo2 == True:
                hagacharse2 = True
            if event.key == pygame.K_n and vivo2 == True:
                ataque2 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Izquierda2 = False
            if event.key == pygame.K_RIGHT:
                Derecha2 = False
            if event.key == pygame.K_n:
                ataque2 = False
            if event.key == pygame.K_DOWN:
                hagacharse2 = False
    if Izquierda:
        player1.x -= speed1
    if Derecha:
        player1.x += speed1
    if Salto1:
        player1.y -= speed1 * 1.8
        if player1.y == 380:
            Salto1 = False
    # Hace que caiga p1
    if Salto1 == False and player1.y != 500 and vivo == True:
        player1.y += speed1
    # Para que no pasen la parte superior del mapa saltando
    if player1.y <= 300:
        Salto1 = False
    # para que no se hagache en el aire
    if player1.y < 500:
        hagacharse = False
    if hagacharse == True:
        player1 = pygame.Rect((player1.x, player1.y+50), (50, 100))
    # no se caiga
    if player1.y >= 550:
        player1.y = 550

    if Izquierda2:
        player2.x -= speed2
    if Derecha2:
        player2.x += speed2
    if Salto2:
        player2.y -= speed2 * 1.8
        if player2.y == 380:
            Salto2 = False
    if Salto2 == False and player2.y != 500 and vivo2 == True:
        player2.y += speed2
    # Para que no pasen la parte superior del mapa saltando
    if player2.y <= 300:
        Salto2 = False
    if player2.y < 500:
        hagacharse2 = False
    if hagacharse2 == True:
        player2 = pygame.Rect((player2.x, player2.y+50), (50, 100))
    if player2.y >= 550:
        player2.y = 550
# Posicion, osea si p1 esta detras de p2 o p2 detras de p1
    if player2.centerx > player1.x and vivo == True:
        vuelta1 = False
    else:
        vuelta1 = True
    if player1.centerx < player2.x and vivo2 == True:
        vuelta2 = False
    else:
        vuelta2 = True
# Limites de la pantalla
    if player1.x <= 0:
        player1.x = 0
    if player1.x >= 950:
        player1.x = 950
    if player2.x <= 0:
        player2.x = 0
    if player2.x >= 950:
        player2.x = 950
    # ///Imagenes de los jugadores///
    if ataque == True and vuelta1 == True and vivo == True and player1.y < 550:
        # Imagen de ataque
        panta.blit(ataquep1V, (player1.x-50, player1.y-50))
        # Posición del cuadrado de ataque
        cuadradot1()
    elif ataque == True and vivo == True and player1.y < 550:
        panta.blit(ataquep1, (player1.x, player1.y-50))
        cuadradot1()
    elif vuelta1 == True and vivo == True and player1.y < 550:
        panta.blit(fotop1V, (player1.x, player1.y))
    elif vivo == False:
        panta.blit(muerto1, (player1.x, 500))
    # Si esta hagachado
    elif player1.y >= 550 and vuelta1 == False and ataque == False:
        panta.blit(hagachadop1, (player1.x, player1.y))
    elif player1.y >= 550 and vuelta1 == True and ataque == False:
        panta.blit(hagachadop1V, (player1.x, player1.y))
    elif player1.y >= 550 and vuelta1 == True and ataque == True:
        panta.blit(p1tHV, (player1.x, player1.y))
        cuadradot1()
    elif player1.y == 550 and vuelta1 == False and ataque == True:
        panta.blit(p1tH, (player1.x, player1.y))
        cuadradot1()
    else:
        panta.blit(fotop1, (player1.x, player1.y))
    if ataque2 == True and vuelta2 == True and vivo2 == True and player2.y < 550:
        panta.blit(ataquep2V, (player2.x-10, player2.y))
        cuadradot2()
    elif ataque2 == True and vivo2 == True and player2.y < 550:
        panta.blit(ataquep2, (player2.x-50, player2.y))
        cuadradot2()
    elif vuelta2 == True and vivo2 == True and player2.y < 550:
        panta.blit(fotop2V, (player2.x, player2.y))
    elif vivo2 == False:
        # 560 para que no quede flotando
        panta.blit(muerto2, (player2.x, 560))
    elif player2.y >= 550 and vuelta2 == False and ataque2 == False:
        panta.blit(hagachadop2, (player2.x, player2.y))
    elif player2.y >= 550 and vuelta2 == True and ataque2 == False:
        panta.blit(hagachadop2V, (player2.x, player2.y))
    elif player2.y >= 550 and vuelta2 == True and ataque2 == True:
        panta.blit(p2tHV, (player2.x, player2.y))
        cuadradot2()
    elif player2.y == 550 and vuelta2 == False and ataque2 == True:
        panta.blit(p2tH, (player2.x, player2.y))
        cuadradot2()
    else:
        panta.blit(fotop2, (player2.x, player2.y))
    # Si esta hagachado
    # Vida o no
    if hp1 <= 0:
        escribir_texto("Has ganado PLAYER 2", font, panta, 255, 50)
        p2win = True
        vivo = False
    if hp2 <= 0:
        escribir_texto("Has ganado PLAYER 1", font, panta, 255, 50)
        p1win = True
        vivo2 = False
    if p1contadorwin == 3:
        vivo = vivo2 = True
        inicio = True
    if p2contadorwin == 3:
        vivo = vivo2 = True
        inicio = True
    if inicio == True:
        ronda = 0
        p1contadorwin = 0
        p2contadorwin = 0
        p1win = False
        p2win = False
        inicio = False
    # escribir en pantalla
    if vivo == True or vivo2 == True:
        escribir_texto(str(ronda), font, panta, 500, 195)
        escribir_texto("Gandas player 1:   " +
                       str(p1contadorwin), font2, panta, 0, 350)
        escribir_texto("Gandas player 2:   " +
                       str(p2contadorwin), font2, panta, 800, 350)
    if vivo == False or vivo2 == False:
        escribir_texto("Apreta R para reiniciar", font, panta, 300, 300)
    # Efecto de """"golpes""""
    if ataque == True or ataque2 == True:
        gp.play()
    controles()
    # Pinta los rectangulos de sus cuerpos
    #pygame.draw.rect(panta, (255, 0, 0), player2)
    #pygame.draw.rect(panta, (0, 255, 255), player1)
    Clok.tick(128)
    pygame.display.update()
