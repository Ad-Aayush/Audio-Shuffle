import ran
import os
import pygame
from pygame import mixer
import numpy as np
from time import sleep

pygame.init()


class Button:
    def __init__(self, text, width, height, pos):
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        self.click = False
        self.text_surf = font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color,
                         self.top_rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)
        return self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.click = True
                self.top_color = '#a72525'
            else:
                if self.click == True:
                    self.click = False
                    return True
        else:
            self.top_color = '#475F77'
            return False


os.chdir("Audio")
list = np.array([], dtype=int)
list = ran.update(list)
font = pygame.font.SysFont("Arial", 30)

new = True
mixer.init()

height = 500
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music")
Previous = Button('Previous', 125, 50, (220, 440))
Pause = Button('Pause', 125, 50, (355, 440))
Next = Button('Next', 125, 50, (490, 440))
Play = Button('Play', 125, 50, (355, 440))
run = True
state = 'Play'
i = 0
# Loading the song
mixer.music.load(str(list[i]) + ".mp3")

# Start playing the song
mixer.music.play()
while run:
    screen.fill((39, 48, 71))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    s = "Currently Playing: " + str(list[i]) + ".mp3"
    Text = Button(s, 395, 60, (220, 220))
    Text.draw()
    if Next.draw() or (state == "Play" and not pygame.mixer.music.get_busy()):
        if not pygame.mixer.music.get_busy():
            sleep(1)
        i = i + 1

        if i >= len(list):
            list = ran.update(list)

        # Loading the song
        mixer.music.load(str(list[i]) + ".mp3")
        # Start playing the song

        mixer.music.play()

    if Previous.draw():
        if i != 0:
            i = i - 1
        # Loading the song
        mixer.music.load(str(list[i]) + ".mp3")

        # Start playing the song
        mixer.music.play()
    if state == "Play":
        if Pause.draw():
            state = 'Pause'
            mixer.music.pause()
    else:
        if Play.draw():
            state = 'Play'
            mixer.music.unpause()


    pygame.display.update()

pygame.quit()
