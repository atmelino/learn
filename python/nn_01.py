#!/usr/bin/python3
# -*- coding:utf-8
#
# -- py-pygame-render-svg.py
#
#   Demonstrates how to displays SVG graphics using CairoSVG.
#
#   Requires:           python3, python3-pygame, python3-cairosvg
#
#   This program is free software: you can redistribute it and/or modify it
#   under  the terms of the GNU General Public License as published by  the
#   Free Software Foundation, either version 3 of the License, or (at  your
#   option) any later version.
#
#   This  program is distributed in the hope that it will  be  useful,  but
#   WITHOUT   ANY   WARRANTY;   without even  the   implied   warranty   of
#   MERCHANTABILITY  or  FITNESS  FOR A PARTICULAR  PURPOSE.  See  the  GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   <https://stackoverflow.com/questions/29022438/>
#   <https://stackoverflow.com/questions/65649933/>
#
#   21 Feb 21   0.1   - Initial version - MT
#
import sys
import traceback

import cairosvg
import pygame
import io

NAME = "Render SVG"
VERSION = "0.1"

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = (1100, 700)
FPS = 60
DPI = 96

BACKGROUND_COLOUR = "cornflowerblue"

_icons = {
    "bar": (
        '<svg width="500" height="250" style="background:lightgrey">'
        '  <rect width="100%" height="100%" x="1" y="1" style="fill:white"/>'
        '  <svg width="401" height="201" x="50" y="25">'
        "    <!-- https://stackoverflow.com/questions/14208673 -->"
        "    <defs> <!-- grig pattern definition -->"
        '      <pattern id="smallGrid" width="10" height="10" patternUnits="userSpaceOnUse">'
        '        <path d="M 10 0 L 0 0 0 10" fill="none" stroke="gray" stroke-width="0.5"/>'
        "      </pattern>"
        '      <pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse">'
        '        <rect width="100" height="100" fill="url(#smallGrid)"/>'
        '        <path d="M 100 0 L 0 0 0 100" fill="none" stroke="gray" stroke-width="1"/>'
        "      </pattern>"
        "    </defs>"
        '    <rect width="100%" height="100%" fill="url(#grid)"/> <!-- Draw grid -->'
        '    <rect width="10" height="0" x="-5" y="200" style="fill:white"/>'
        '    <rect width="10" height="5" x="5" y="195" style="fill:darkviolet"/>'
        '    <rect width="10" height="10" x="15" y="190" style="fill:blue"/>'
        '    <rect width="10" height="20" x="25" y="180" style="fill:darkturquoise"/>'
        '    <rect width="10" height="30" x="35" y="170" style="fill:limegreen"/>'
        '    <rect width="10" height="50" x="45" y="150" style="fill:mediumseagreen"/>'
        '    <rect width="10" height="90" x="55" y="110" style="fill:yellowgreen"/>'
        '    <rect width="10" height="150" x="65" y="50" style="fill:gold"/>'
        '    <rect width="10" height="180" x="75" y="20" style="fill:orange"/>'
        '    <rect width="10" height="195" x="85" y="5" style="fill:darkorange"/>'
        '    <rect width="10" height="200" x="95" y="0" style="fill:red"/>'
        '    <rect width="10" height="195" x="105" y="5" style="fill:darkorange"/>'
        '    <rect width="10" height="180" x="115" y="20" style="fill:orange"/>'
        '    <rect width="10" height="150" x="125" y="50" style="fill:gold"/>'
        '    <rect width="10" height="90" x="135" y="110" style="fill:yellowgreen"/>'
        '    <rect width="10" height="50" x="145" y="150" style="fill:mediumseagreen"/>'
        '    <rect width="10" height="30" x="155" y="170" style="fill:limegreen"/>'
        '    <rect width="10" height="20" x="165" y="180" style="fill:darkturquoise"/>'
        '    <rect width="10" height="10" x="175" y="190" style="fill:blue"/>'
        '    <rect width="10" height="5" x="185" y="195" style="fill:darkviolet"/>'
        '    <rect width="10" height="0" x="195" y="200" style="fill:white"/>'
        '    <rect width="10" height="5" x="205" y="195" style="fill:darkviolet"/>'
        '    <rect width="10" height="10" x="215" y="190" style="fill:blue"/>'
        '    <rect width="10" height="20" x="225" y="180" style="fill:darkturquoise"/>'
        '    <rect width="10" height="30" x="235" y="170" style="fill:limegreen"/>'
        '    <rect width="10" height="50" x="245" y="150" style="fill:mediumseagreen"/>'
        '    <rect width="10" height="90" x="255" y="110" style="fill:yellowgreen"/>'
        '    <rect width="10" height="150" x="265" y="50" style="fill:gold"/>'
        '    <rect width="10" height="180" x="275" y="20" style="fill:orange"/>'
        '    <rect width="10" height="195" x="285" y="5" style="fill:darkorange"/>'
        '    <rect width="10" height="200" x="295" y="0" style="fill:red"/>'
        '    <rect width="10" height="195" x="305" y="5" style="fill:darkorange"/>'
        '    <rect width="10" height="180" x="315" y="20" style="fill:orange"/>'
        '    <rect width="10" height="150" x="325" y="50" style="fill:gold"/>'
        '    <rect width="10" height="90" x="335" y="110" style="fill:yellowgreen"/>'
        '    <rect width="10" height="50" x="345" y="150" style="fill:mediumseagreen"/>'
        '    <rect width="10" height="30" x="355" y="170" style="fill:limegreen"/>'
        '    <rect width="10" height="20" x="365" y="180" style="fill:darkturquoise"/>'
        '    <rect width="10" height="10" x="375" y="190" style="fill:blue"/>'
        '    <rect width="10" height="5" x="385" y="195" style="fill:darkviolet"/>'
        "  </svg>"
        "  <defs> <!-- arrowhead marker definition -->"
        '    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5"'
        '        markerWidth="6" markerHeight="10"'
        '        orient="auto-start-reverse">'
        '      <path d="M 0 0 L 10 5 L 0 10" />'
        "    </marker>"
        "  </defs>"
        '  <line x1="50" x2="460" y1="225" y2="225" marker-end="url(#arrow)" style="stroke-width:1;stroke:black;"/>'
        '  <line x1="50" x2="50" y1="225" y2="15" style="stroke-width:1;stroke:black;"/>'
        '  <text x="45"  y="25"   style="font-size:10;fill:black;text-anchor:end;dominant-baseline:middle">p</text>'
        '  <text x="450"  y="235"  style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:hanging">t</text>'
        "</svg>"
    ),
    "nn_01": (
        '<svg width="1288pt" height="127pt"                                                                                         '
        ' viewBox="0.00 0.00 1288.00 127.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">         '
        '<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 123)">                                            '
        "<title>%3</title>                                                                                                          "
        '<polygon fill="white" stroke="transparent" points="-4,4 -4,-123 1284,-123 1284,4 -4,4"/>                                   '
        "<!-- 140674273254976 -->                                                                                                   "
        '<g id="node1" class="node">                                                                                                '
        "<title>140674273254976</title>                                                                                             "
        '<polygon fill="none" stroke="black" points="486,-27.5 486,-63.5 807,-63.5 807,-27.5 486,-27.5"/>                           '
        '<text text-anchor="middle" x="512" y="-41.8" font-family="Times,serif" font-size="14.00">v004</text>                       '
        '<polyline fill="none" stroke="black" points="538,-27.5 538,-63.5 "/>                                                       '
        '<text text-anchor="middle" x="548.5" y="-41.8" font-family="Times,serif" font-size="14.00"> </text>                        '
        '<polyline fill="none" stroke="black" points="559,-27.5 559,-63.5 "/>                                                       '
        '<text text-anchor="middle" x="569.5" y="-41.8" font-family="Times,serif" font-size="14.00"> </text>                        '
        '<polyline fill="none" stroke="black" points="580,-27.5 580,-63.5 "/>                                                       '
        '<text text-anchor="middle" x="590.5" y="-41.8" font-family="Times,serif" font-size="14.00"> </text>                        '
        '<polyline fill="none" stroke="black" points="601,-27.5 601,-63.5 "/>                                                       '
        '<text text-anchor="middle" x="652" y="-41.8" font-family="Times,serif" font-size="14.00">data 0.5000</text>                '
        '<polyline fill="none" stroke="black" points="703,-27.5 703,-63.5 "/>                                                       '
        '<text text-anchor="middle" x="755" y="-41.8" font-family="Times,serif" font-size="14.00">grad 1.0000</text>                '
        "</g>                                                                                                                       "
        "<!-- 140674273255168+ -->                                                                                                  "
        '<g id="node4" class="node">                                                                                                '
        "<title>140674273255168+</title>                                                                                            "
        '<ellipse fill="none" stroke="black" cx="879" cy="-72.5" rx="27" ry="18"/>                                                  '
        '<text text-anchor="middle" x="879" y="-68.8" font-family="Times,serif" font-size="14.00">+</text>                          '
        "</g>                                                                                                                       "
        "<!-- 140674273254976&#45;&gt;140674273255168+ -->                                                                          "
        '<g id="edge6" class="edge">                                                                                                '
        "<title>140674273254976&#45;&gt;140674273255168+</title>                                                                    "
        '<path fill="none" stroke="black" d="M801.25,-63.51C816.17,-65.26 830.12,-66.89 841.92,-68.27"/>                            '
        '<polygon fill="black" stroke="black" points="841.79,-71.78 852.13,-69.47 842.6,-64.83 841.79,-71.78"/>                     '
        "</g>                                                                                                                       "
        "<!-- 140674273254976* -->                                                                                                  "
        '<g id="node2" class="node">                                                                                                '
        "<title>140674273254976*</title>                                                                                            "
        '<ellipse fill="none" stroke="black" cx="414" cy="-45.5" rx="27" ry="18"/>                                                  '
        '<text text-anchor="middle" x="414" y="-41.8" font-family="Times,serif" font-size="14.00">*</text>                          '
        "</g>                                                                                                                       "
        "<!-- 140674273254976*&#45;&gt;140674273254976 -->                                                                          "
        '<g id="edge1" class="edge">                                                                                                '
        "<title>140674273254976*&#45;&gt;140674273254976</title>                                                                    "
        '<path fill="none" stroke="black" d="M441.44,-45.5C451.05,-45.5 462.76,-45.5 475.64,-45.5"/>                                '
        '<polygon fill="black" stroke="black" points="475.71,-49 485.71,-45.5 475.71,-42 475.71,-49"/>                              '
        "</g>                                                                                                                       "
        "<!-- 140674273255168 -->                                                                                                   "
        '<g id="node3" class="node">                                                                                                '
        "<title>140674273255168</title>                                                                                             "
        '<polygon fill="none" stroke="black" points="942,-54.5 942,-90.5 1280,-90.5 1280,-54.5 942,-54.5"/>                         '
        '<text text-anchor="middle" x="968" y="-68.8" font-family="Times,serif" font-size="14.00">v005</text>                       '
        '<polyline fill="none" stroke="black" points="994,-54.5 994,-90.5 "/>                                                       '
        '<text text-anchor="middle" x="1007" y="-68.8" font-family="Times,serif" font-size="14.00">L</text>                         '
        '<polyline fill="none" stroke="black" points="1020,-54.5 1020,-90.5 "/>                                                     '
        '<text text-anchor="middle" x="1034.5" y="-68.8" font-family="Times,serif" font-size="14.00">N</text>                       '
        '<polyline fill="none" stroke="black" points="1049,-54.5 1049,-90.5 "/>                                                     '
        '<text text-anchor="middle" x="1061.5" y="-68.8" font-family="Times,serif" font-size="14.00">a</text>                       '
        '<polyline fill="none" stroke="black" points="1074,-54.5 1074,-90.5 "/>                                                     '
        '<text text-anchor="middle" x="1125" y="-68.8" font-family="Times,serif" font-size="14.00">data 0.5000</text>               '
        '<polyline fill="none" stroke="black" points="1176,-54.5 1176,-90.5 "/>                                                     '
        '<text text-anchor="middle" x="1228" y="-68.8" font-family="Times,serif" font-size="14.00">grad 1.0000</text>               '
        "</g>                                                                                                                       "
        "<!-- 140674273255168+&#45;&gt;140674273255168 -->                                                                          "
        '<g id="edge2" class="edge">                                                                                                '
        "<title>140674273255168+&#45;&gt;140674273255168</title>                                                                    "
        '<path fill="none" stroke="black" d="M906.38,-72.5C913.74,-72.5 922.32,-72.5 931.73,-72.5"/>                                '
        '<polygon fill="black" stroke="black" points="931.81,-76 941.81,-72.5 931.81,-69 931.81,-76"/>                              '
        "</g>                                                                                                                       "
        "<!-- 140674273255696 -->                                                                                                   "
        '<g id="node5" class="node">                                                                                                '
        "<title>140674273255696</title>                                                                                             "
        '<polygon fill="none" stroke="black" points="477,-82.5 477,-118.5 816,-118.5 816,-82.5 477,-82.5"/>                         '
        '<text text-anchor="middle" x="503" y="-96.8" font-family="Times,serif" font-size="14.00">v002</text>                       '
        '<polyline fill="none" stroke="black" points="529,-82.5 529,-118.5 "/>                                                      '
        '<text text-anchor="middle" x="542" y="-96.8" font-family="Times,serif" font-size="14.00">L</text>                          '
        '<polyline fill="none" stroke="black" points="555,-82.5 555,-118.5 "/>                                                      '
        '<text text-anchor="middle" x="569.5" y="-96.8" font-family="Times,serif" font-size="14.00">N</text>                        '
        '<polyline fill="none" stroke="black" points="584,-82.5 584,-118.5 "/>                                                      '
        '<text text-anchor="middle" x="597" y="-96.8" font-family="Times,serif" font-size="14.00">b</text>                          '
        '<polyline fill="none" stroke="black" points="610,-82.5 610,-118.5 "/>                                                      '
        '<text text-anchor="middle" x="661" y="-96.8" font-family="Times,serif" font-size="14.00">data 0.0000</text>                '
        '<polyline fill="none" stroke="black" points="712,-82.5 712,-118.5 "/>                                                      '
        '<text text-anchor="middle" x="764" y="-96.8" font-family="Times,serif" font-size="14.00">grad 1.0000</text>                '
        "</g>                                                                                                                       "
        "<!-- 140674273255696&#45;&gt;140674273255168+ -->                                                                          "
        '<g id="edge5" class="edge">                                                                                                '
        "<title>140674273255696&#45;&gt;140674273255168+</title>                                                                    "
        '<path fill="none" stroke="black" d="M795.76,-82.49C812.86,-80.41 828.9,-78.46 842.2,-76.85"/>                              '
        '<polygon fill="black" stroke="black" points="842.74,-80.31 852.24,-75.63 841.89,-73.36 842.74,-80.31"/>                    '
        "</g>                                                                                                                       "
        "<!-- 140674273255744 -->                                                                                                   "
        '<g id="node6" class="node">                                                                                                '
        "<title>140674273255744</title>                                                                                             "
        '<polygon fill="none" stroke="black" points="0,-55.5 0,-91.5 351,-91.5 351,-55.5 0,-55.5"/>                                 '
        '<text text-anchor="middle" x="26" y="-69.8" font-family="Times,serif" font-size="14.00">v001</text>                        '
        '<polyline fill="none" stroke="black" points="52,-55.5 52,-91.5 "/>                                                         '
        '<text text-anchor="middle" x="65" y="-69.8" font-family="Times,serif" font-size="14.00">L</text>                           '
        '<polyline fill="none" stroke="black" points="78,-55.5 78,-91.5 "/>                                                         '
        '<text text-anchor="middle" x="92.5" y="-69.8" font-family="Times,serif" font-size="14.00">N</text>                         '
        '<polyline fill="none" stroke="black" points="107,-55.5 107,-91.5 "/>                                                       '
        '<text text-anchor="middle" x="126" y="-69.8" font-family="Times,serif" font-size="14.00">w1</text>                         '
        '<polyline fill="none" stroke="black" points="145,-55.5 145,-91.5 "/>                                                       '
        '<text text-anchor="middle" x="196" y="-69.8" font-family="Times,serif" font-size="14.00">data 0.5000</text>                '
        '<polyline fill="none" stroke="black" points="247,-55.5 247,-91.5 "/>                                                       '
        '<text text-anchor="middle" x="299" y="-69.8" font-family="Times,serif" font-size="14.00">grad 1.0000</text>                '
        "</g>                                                                                                                       "
        "<!-- 140674273255744&#45;&gt;140674273254976* -->                                                                          "
        '<g id="edge4" class="edge">                                                                                                '
        "<title>140674273255744&#45;&gt;140674273254976*</title>                                                                    "
        '<path fill="none" stroke="black" d="M328.62,-55.49C346.63,-53.36 363.49,-51.36 377.33,-49.72"/>                            '
        '<polygon fill="black" stroke="black" points="377.78,-53.19 387.3,-48.54 376.96,-46.24 377.78,-53.19"/>                     '
        "</g>                                                                                                                       "
        "<!-- 140674273254736 -->                                                                                                   "
        '<g id="node7" class="node">                                                                                                '
        "<title>140674273254736</title>                                                                                             "
        '<polygon fill="none" stroke="black" points="15,-0.5 15,-36.5 336,-36.5 336,-0.5 15,-0.5"/>                                 '
        '<text text-anchor="middle" x="41" y="-14.8" font-family="Times,serif" font-size="14.00">v003</text>                        '
        '<polyline fill="none" stroke="black" points="67,-0.5 67,-36.5 "/>                                                          '
        '<text text-anchor="middle" x="77.5" y="-14.8" font-family="Times,serif" font-size="14.00"> </text>                         '
        '<polyline fill="none" stroke="black" points="88,-0.5 88,-36.5 "/>                                                          '
        '<text text-anchor="middle" x="98.5" y="-14.8" font-family="Times,serif" font-size="14.00"> </text>                         '
        '<polyline fill="none" stroke="black" points="109,-0.5 109,-36.5 "/>                                                        '
        '<text text-anchor="middle" x="119.5" y="-14.8" font-family="Times,serif" font-size="14.00">i</text>                        '
        '<polyline fill="none" stroke="black" points="130,-0.5 130,-36.5 "/>                                                        '
        '<text text-anchor="middle" x="181" y="-14.8" font-family="Times,serif" font-size="14.00">data 1.0000</text>                '
        '<polyline fill="none" stroke="black" points="232,-0.5 232,-36.5 "/>                                                        '
        '<text text-anchor="middle" x="284" y="-14.8" font-family="Times,serif" font-size="14.00">grad 0.5000</text>                '
        "</g>                                                                                                                       "
        "<!-- 140674273254736&#45;&gt;140674273254976* -->                                                                          "
        '<g id="edge3" class="edge">                                                                                                '
        "<title>140674273254736&#45;&gt;140674273254976*</title>                                                                    "
        '<path fill="none" stroke="black" d="M334.25,-36.51C349.98,-38.3 364.65,-39.98 376.97,-41.39"/>                             '
        '<polygon fill="black" stroke="black" points="376.82,-44.89 387.16,-42.55 377.62,-37.94 376.82,-44.89"/>                    '
        "</g>                                                                                                                       "
        "</g>                                                                                                                       "
        "</svg>                                                                                                                     "
        "                                                                                                                           "
    ),
}


def _scan():
    event = (
        pygame.event.poll()
    )  # Will return NOEVENT if there are no events in the queue.
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            return False
    elif event.type == pygame.MOUSEBUTTONUP:
        return False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pass
    return True


def render_svg(_svg, _scale):
    _svg = cairosvg.svg2svg(_svg, dpi=(DPI / _scale))  # Convert svg to svg changing DPI
    _bytes = cairosvg.svg2png(_svg)
    byte_io = io.BytesIO(_bytes)
    return pygame.image.load(byte_io)


try:
    pygame.init()
    pygame.font.init()

    _icon = pygame.Surface((32, 32))  # Create a blank icon (32 x 32) for the window
    _icon.fill(pygame.Color("black"))
    _icon.set_colorkey(pygame.Color("black"))  # Make it compleatly transparent
    pygame.display.set_icon(
        _icon
    )  # Set it as the window's icon (or rather don't display an icon at all)
    pygame.display.set_caption(NAME)  # Set window caption

    _screen = pygame.display.set_mode((DISPLAY_SIZE))
    _screen.fill(pygame.Color("black"))
    _background = pygame.Surface(
        (DISPLAY_SIZE)
    )  # Create a drawing surface for the background
    _background.fill(pygame.Color(BACKGROUND_COLOUR))

    _screen.blit(_background, (0, 0))

    _x_offset = 25
    _y_offset = 25
    _x_delta = (_screen.get_width() - (500 + 2 * _x_offset)) // (len(_icons) - 1)
    _y_delta = (_screen.get_height() - (250 + 2 * _y_offset)) // (len(_icons) - 1)

    for _name in _icons:
        _svg = " ".join(
            _icons[_name].split()
        )  # Remove whitespace (not really necessary but it tidies things up)
        _image = render_svg(_svg, 1)
        # DEBUG -- sys.stdout.write (_name + " " + str(_image.get_size()) + "\n" + _svg + '\n')
        _screen.blit(_image, (_x_offset, _y_offset))  # Draw the image..
        _x_offset += _x_delta
        _y_offset += _y_delta

        while _scan():  # Wait for the user
            pygame.display.flip()  # Update the display
            pygame.time.Clock().tick(FPS)

    pygame.quit()

except KeyboardInterrupt:  # Ctrl-C
    pass

except (
    Exception
) as exception:  # Catch all other errors - otherwise the script will just fail silently!
    import traceback

    sys.stderr.write(
        traceback.format_exc()
    )  # Display the default traceback on the console

    exit(1)

exit()
