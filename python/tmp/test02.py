import pygame
import io
from graphviz import Digraph
import pprint
import cairosvg
DPI = 96

pp = pprint.PrettyPrinter(indent=4)
dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})  # LR = left to right
nodes, edges = set(), set()
# nodes.add(v)
dot.node(
    name="a", label="{ %s | data %.4f | grad %.4f }" % ("type", 3, 4), shape="record"
)
dot.node(
    name="b", label="{ %s | data %.4f | grad %.4f }" % ("type", 3, 4), shape="record"
)
# dot.view()


pygame.init()
pygame.font.init()

window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()

# mysvg=dot.pipe(format='svg')
mysvg=dot.pipe(encoding='utf-8')
# mysvg=dot.pipe()
print(mysvg)
dot.render("abcd.gv", format="jpg", view=True)

pygame_surface = pygame.image.load(io.BytesIO(mysvg.encode()))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    window.blit(pygame_surface, pygame_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()