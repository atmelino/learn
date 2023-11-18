import pygame
import io
from graphviz import Digraph
import pprint
import cairosvg
from graphviz import Source

DPI = 96

pp = pprint.PrettyPrinter(indent=4)

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((800, 300))
clock = pygame.time.Clock()


path = 'graphviz/pygame_nn/Neuron_01.gv'
s = Source.from_file(path)
print(s.source)
mysvg2=s.pipe(format='svg', encoding='utf-8')
print("svg from file")
print(mysvg2)


pygame_surface = pygame.image.load(io.BytesIO(mysvg2.encode()))

def render_svg(_svg, _scale):
    _svg = cairosvg.svg2svg(_svg, dpi=(DPI / _scale))  # Convert svg to svg changing DPI
    _bytes = cairosvg.svg2png(_svg)
    byte_io = io.BytesIO(_bytes)
    return pygame.image.load(byte_io)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    _image = render_svg(mysvg2, 1)
    window.blit(_image, pygame_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()