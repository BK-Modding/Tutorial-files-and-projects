import pygame

pygame.init()

pygame.font.init()

win_w, win_h = 1000, 1000


win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("First Game")

class Rope:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.line_offset = 0

class Elevator():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def switch_ropes(self, end_rope):
        self.x = end_rope.x - (self.width / 2)

altfont = pygame.font.SysFont('Comic Sans MS', 30)
altitude = 0.4 * win_h

run = True
gameover = False
won = False

A = Rope(0.25 * win_w, 0, 0.02 * win_w, win_h, "green")
B = Rope(0.75 * win_w, 0, 0.02 * win_w, win_h, "yellow")
Elev = Elevator(A.x - (0.3 * win_w / 2), altitude, 0.3 * win_w, 0.2 * win_h, "blue")

inefficiency = 0.05

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if altitude >= win_h:
        gameover = True
        won = False
    elif altitude <= 0:
        gameover = True
        won = True

    if gameover:
        donefont = pygame.font.SysFont('Comic Sans MS', 50)
        displaytext = "You won!" if won else "You lost :("
        done_surf = donefont.render(displaytext, False, (0, 0, 0))

        win.blit(done_surf, (0.5 * win_w, 0.5 * win_h))
        pygame.display.update()
        continue

    win.fill((255, 255, 255))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        Elev.switch_ropes(B)
        altitude += inefficiency * altitude
        Elev.y = altitude

        B.line_offset = (B.line_offset - 5) % 50

        altitude -= 0.1
        print(altitude)
        Elev.y = altitude

    if keys[pygame.K_DOWN]:
        if Elev.x != A.x - (Elev.width / 2):
            Elev.switch_ropes(A)
            altitude += inefficiency * altitude
            Elev.y = altitude

        B.line_offset = (B.line_offset + 5) % 50


    # if keys[pygame.K_DOWN]:
    #     Elev.switch_ropes(A)

    for obj in [A, B, Elev]:
        pygame.draw.rect(win, obj.color, (obj.x, obj.y, obj.width, obj.height))

    for rope in [A, B]:
        for i in range(20):
            pygame.draw.line(win, "black", (rope.x, rope.line_offset + i * 50),(rope.x + rope.width, rope.line_offset + 20 + i * 50))

    alt_surf = altfont.render('Alt: {}'.format(win_h - altitude), False, (0, 0, 0))
    win.blit(alt_surf,(0.85 * win_w,0))
    pygame.display.update()

pygame.quit()