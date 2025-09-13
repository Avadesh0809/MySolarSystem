import pygame
import math

pygame.init()
Screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Solar System")
Clock = pygame.time.Clock()

# Colors
White = (255, 255, 255)
Yellow = (255, 200, 0)
Grey = (169, 169, 169)
Orange = (255, 165, 0)
Red = (255, 69, 0)
Brown = (210, 180, 140)
Cyan = (0, 255, 255)
DarkBlue = (0, 0, 139)
Blue = (0, 0, 255)

#screen
CenterX = 500
CenterY = 400

Running = True
Degree = 0

while Running:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            Running = False

    Screen.fill((0, 0, 0))

    # Sun
    pygame.draw.circle(Screen, Yellow, (CenterX, CenterY), 30)

    # Mercury
    Radius1 = 50
    Rad1 = math.radians(Degree * 4)
    X1 = math.cos(Rad1) * Radius1
    Y1 = math.sin(Rad1) * Radius1
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius1, 1)
    pygame.draw.circle(Screen, Grey, (int(X1) + CenterX, int(Y1) + CenterY), 5)

    # Venus
    Radius2 = 85
    Rad2 = math.radians(Degree * 3)
    X2 = math.cos(Rad2) * Radius2
    Y2 = math.sin(Rad2) * Radius2
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius2, 1)
    pygame.draw.circle(Screen, Orange, (int(X2) + CenterX, int(Y2) + CenterY), 7)

    # Earth
    Radius3 = 120
    Rad3 = math.radians(Degree * 2)
    X3 = math.cos(Rad3) * Radius3
    Y3 = math.sin(Rad3) * Radius3
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius3, 1)
    pygame.draw.circle(Screen, Blue, (int(X3) + CenterX, int(Y3) + CenterY), 8)

    # Mars
    Radius4 = 155
    Rad4 = math.radians(Degree * 1.6)
    X4 = math.cos(Rad4) * Radius4
    Y4 = math.sin(Rad4) * Radius4
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius4, 1)
    pygame.draw.circle(Screen, Red, (int(X4) + CenterX, int(Y4) + CenterY), 6)

    # Jupiter
    Radius5 = 195
    Rad5 = math.radians(Degree * 1.2)
    X5 = math.cos(Rad5) * Radius5
    Y5 = math.sin(Rad5) * Radius5
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius5, 1)
    pygame.draw.circle(Screen, Orange, (int(X5) + CenterX, int(Y5) + CenterY), 14)

    # Saturn
    Radius6 = 235
    Rad6 = math.radians(Degree)
    X6 = math.cos(Rad6) * Radius6
    Y6 = math.sin(Rad6) * Radius6
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius6, 1)
    pygame.draw.circle(Screen, Brown, (int(X6) + CenterX, int(Y6) + CenterY), 12)

    # Uranus
    Radius7 = 275
    Rad7 = math.radians(Degree * 0.8)
    X7 = math.cos(Rad7) * Radius7
    Y7 = math.sin(Rad7) * Radius7
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius7, 1)
    pygame.draw.circle(Screen, Cyan, (int(X7) + CenterX, int(Y7) + CenterY), 10)

    # Neptune
    Radius8 = 315
    Rad8 = math.radians(Degree * 0.6)
    X8 = math.cos(Rad8) * Radius8
    Y8 = math.sin(Rad8) * Radius8
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius8, 1)
    pygame.draw.circle(Screen, DarkBlue, (int(X8) + CenterX, int(Y8) + CenterY), 9)

    # Pluto
    Radius9 = 355
    Rad9 = math.radians(Degree * 0.4)
    X9 = math.cos(Rad9) * Radius9
    Y9 = math.sin(Rad9) * Radius9
    pygame.draw.circle(Screen, White, (CenterX, CenterY), Radius9, 1)
    pygame.draw.circle(Screen, Grey, (int(X9) + CenterX, int(Y9) + CenterY), 5)

    Degree += 1
    pygame.display.update()
    Clock.tick(60)

pygame.quit()
