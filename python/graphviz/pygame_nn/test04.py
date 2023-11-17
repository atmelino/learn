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

# svg_string = '<svg height="100" width="500"><ellipse cx="240" cy="50" rx="220" ry="30" style="fill:yellow" /><ellipse cx="220" cy="50" rx="190" ry="20" style="fill:white" /></svg>'
# pygame_surface = pygame.image.load(io.BytesIO(svg_string.encode()))

dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})  # LR = left to right
nodes, edges = set(), set()
# nodes.add(v)
dot.node(
    name="a", label="{ %s | data %.4f | grad %.4f }" % ("type", 3, 4), shape="record"
)
dot.node(
    name="b", label="{ %s | data %.4f | grad %.4f }" % ("type", 3, 4), shape="record"
)
dot.edge("a", "b")
# dot.view()
# mysvg=dot.pipe(format='svg')
mysvg=dot.pipe(encoding='utf-8')
# mysvg=dot.pipe()
print(mysvg)


path = 'graphviz/pygame_nn/Neuron_01.gv'
s = Source.from_file(path)
print(s.source)
s.render('graphviz/pygame_nn/Neuron_01.gv', format='jpg',view=True)
# mysvg=s.pipe(format='svg')
# mysvg=s.pipe(encoding='utf-8').pipe(format='svg')
# print(mysvg)




pygame_surface = pygame.image.load(io.BytesIO(mysvg.encode()))

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

    # window.fill((255, 255, 255))
    # window.blit(pygame_surface, pygame_surface.get_rect(center = window.get_rect().center))
    # pygame.display.flip()

    window.fill((255, 255, 255))
    _image = render_svg(mysvg, 1)
    window.blit(_image, pygame_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()




pygame.quit()
exit()