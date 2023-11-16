#!/usr/bin/python3
# -*- coding:utf-8
#
#-- py-pygame-render-svg.py
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
 
DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = (800, 480)
FPS = 60
DPI = 96
  
BACKGROUND_COLOUR = 'cornflowerblue'
  
_icons = {
  'cos' :
    ( '<svg width="500" height="250" style="background:lightgrey">'
      '  <rect width="100%" height="100%" x="1" y="1" style="fill:white"/>'
      '  <svg width="405" height="201" x="50" y="25">'
      '    <!-- Draw horizontal grid lines -->'
      '    <line x1="1" x2="100%" y1="0" y2="0" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="10" y2="10" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="20" y2="20" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="30" y2="30" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="40" y2="40" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="50" y2="50" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="60" y2="60" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="70" y2="70" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="80" y2="80" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="90" y2="90" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="100" y2="100" style="stroke-width:1;stroke:black;"/>'
      '    <line x1="1" x2="100%" y1="110" y2="110" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="120" y2="120" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="130" y2="130" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="140" y2="140" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="150" y2="150" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="160" y2="160" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="170" y2="170" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="180" y2="180" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="190" y2="190" style="stroke-width:0.5;stroke:grey;"/>'
      '    <!-- Draw vertical grid lines -->'
      '    <line x1="10" x2="10" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="20" x2="20" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="30" x2="30" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="40" x2="40" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="50" x2="50" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="60" x2="60" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="70" x2="70" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="80" x2="80" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="90" x2="90" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="100" x2="100" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <line x1="110" x2="110" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="120" x2="120" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="130" x2="130" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="140" x2="140" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="150" x2="150" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="160" x2="160" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="170" x2="170" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="180" x2="180" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="190" x2="190" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="200" x2="200" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <line x1="210" x2="210" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="220" x2="220" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="230" x2="230" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="240" x2="240" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="250" x2="250" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="260" x2="260" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="270" x2="270" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="280" x2="280" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="290" x2="290" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="300" x2="300" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <line x1="310" x2="310" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="320" x2="320" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="330" x2="330" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="340" x2="340" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="350" x2="350" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="360" x2="360" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="370" x2="370" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="380" x2="380" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="390" x2="390" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="400" x2="400" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <path d ="M 0 200 C  72.84, 200  127.16   0, 200   0" style="fill:none;stroke:blue;"/>'
      '    <path d ="M 200   0 C  272.84,   0 327.16 200, 400 200" style="fill:none;stroke:blue;"/>'
      '    <path d ="M 400 200 C  472.84, 200 527.16   0, 600   0" style="fill:none;stroke:blue;"/>'
      '    </svg>'
      '  <text x="465" y="125" style="font-size:10;fill:black;text-anchor:start;dominant-baseline:middle">x</text>'
      '  <text x="45" y="25" style="font-size:10;fill:black;text-anchor:end;dominant-baseline:middle">+1</text>'
      '  <text x="45" y="125" style="font-size:10;fill:black;text-anchor:end;dominant-baseline:middle">0</text>'
      '  <text x="45" y="225" style="font-size:10;fill:black;text-anchor:end;dominant-baseline:hanging">-1</text>'
      '  <text x="5" y="125" style="font-size:10;fill:black;text-anchor:start;dominant-baseline:middle">cos(x)</text>'
      '  <text x="50" y="10" style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:middle">y</text>'
      '  <text x="250" y="245" style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:hanging"> π</text>'
      '  <text x="450" y="245" style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:hanging">2π</text>'
      '  <line x1="50" x2="460" y1="225" y2="225" style="stroke-width:1;stroke:black;"/>'
      '  <line x1="50" x2="50" y1="225" y2="15" style="stroke-width:1;stroke:black;"/>'
      '</svg>'
    ),
  'bar' :
    ( '<svg width="500" height="250" style="background:lightgrey">'
      '  <rect width="100%" height="100%" x="1" y="1" style="fill:white"/>'
      '  <svg width="401" height="201" x="50" y="25">'
      '    <!-- https://stackoverflow.com/questions/14208673 -->'
      '    <defs> <!-- grig pattern definition -->'
      '      <pattern id="smallGrid" width="10" height="10" patternUnits="userSpaceOnUse">'
      '        <path d="M 10 0 L 0 0 0 10" fill="none" stroke="gray" stroke-width="0.5"/>'
      '      </pattern>'
      '      <pattern id="grid" width="100" height="100" patternUnits="userSpaceOnUse">'
      '        <rect width="100" height="100" fill="url(#smallGrid)"/>'
      '        <path d="M 100 0 L 0 0 0 100" fill="none" stroke="gray" stroke-width="1"/>'
      '      </pattern>'
      '    </defs>'
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
      '  </svg>'
      '  <defs> <!-- arrowhead marker definition -->'
      '    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5"'
      '        markerWidth="6" markerHeight="10"'
      '        orient="auto-start-reverse">'
      '      <path d="M 0 0 L 10 5 L 0 10" />'
      '    </marker>'
      '  </defs>'
      '  <line x1="50" x2="460" y1="225" y2="225" marker-end="url(#arrow)" style="stroke-width:1;stroke:black;"/>'
      '  <line x1="50" x2="50" y1="225" y2="15" style="stroke-width:1;stroke:black;"/>'
      '  <text x="45"  y="25"   style="font-size:10;fill:black;text-anchor:end;dominant-baseline:middle">p</text>'
      '  <text x="450"  y="235"  style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:hanging">t</text>'
      '</svg>'
    ),
  'sin' :
    ( '<svg width="500" height="250" style="background:lightgrey">'
      '  <rect width="100%" height="100%" x="1" y="1" style="fill:white"/>'
      '  <svg width="405" height="201" x="50" y="25">'
      '    <!-- Draw horizontal grid lines -->'
      '    <line x1="1" x2="100%" y1="0" y2="0" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="10" y2="10" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="20" y2="20" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="30" y2="30" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="40" y2="40" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="50" y2="50" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="60" y2="60" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="70" y2="70" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="80" y2="80" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="90" y2="90" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="100" y2="100" style="stroke-width:1;stroke:black;"/>'
      '    <line x1="1" x2="100%" y1="110" y2="110" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="120" y2="120" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="130" y2="130" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="140" y2="140" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="150" y2="150" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="160" y2="160" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="170" y2="170" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="180" y2="180" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="1" x2="100%" y1="190" y2="190" style="stroke-width:0.5;stroke:grey;"/>'
      '    <!-- Draw vertical grid lines -->'
      '    <line x1="10" x2="10" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="20" x2="20" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="30" x2="30" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="40" x2="40" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="50" x2="50" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="60" x2="60" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="70" x2="70" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="80" x2="80" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="90" x2="90" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="100" x2="100" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <line x1="110" x2="110" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="120" x2="120" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="130" x2="130" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="140" x2="140" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="150" x2="150" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="160" x2="160" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="170" x2="170" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="180" x2="180" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="190" x2="190" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="200" x2="200" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <line x1="210" x2="210" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="220" x2="220" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="230" x2="230" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="240" x2="240" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="250" x2="250" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="260" x2="260" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="270" x2="270" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="280" x2="280" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="290" x2="290" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="300" x2="300" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <line x1="310" x2="310" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="320" x2="320" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="330" x2="330" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="340" x2="340" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="350" x2="350" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="360" x2="360" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="370" x2="370" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="380" x2="380" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="390" x2="390" y1="0" y2="200" style="stroke-width:0.5;stroke:grey;"/>'
      '    <line x1="400" x2="400" y1="0" y2="200" style="stroke-width:1;stroke:grey;"/>'
      '    <path d ="M-100 200 C  -27.16, 200  27.16   0, 100   0" style="fill:none;stroke:red;"/>'
      '    <path d ="M 100   0 C  172.84,   0 227.16 200, 300 200" style="fill:none;stroke:red;"/>'
      '    <path d ="M 300 200 C  372.84, 200 427.16   0, 500   0" style="fill:none;stroke:red;"/>'
      '    <path d ="M 500   0 C  572.84,   0 627.16 200, 700 200" style="fill:none;stroke:red;"/>'
      '    <path d ="M 700 200 C  772.84, 200 827.16   0, 900   0" style="fill:none;stroke:red;"/>'
      '    </svg>'
      '  <text x="465" y="125" style="font-size:10;fill:black;text-anchor:start;dominant-baseline:middle">x</text>'
      '  <text x="45" y="25" style="font-size:10;fill:black;text-anchor:end;dominant-baseline:middle">+1</text>'
      '  <text x="45" y="125" style="font-size:10;fill:black;text-anchor:end;dominant-baseline:middle">0</text>'
      '  <text x="45" y="225" style="font-size:10;fill:black;text-anchor:end;dominant-baseline:hanging">-1</text>'
      '  <text x="5" y="125" style="font-size:10;fill:black;text-anchor:start;dominant-baseline:middle">sin(x)</text>'
      '  <text x="50" y="10" style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:middle">y</text>'
      '  <text x="250" y="245" style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:hanging"> π</text>'
      '  <text x="450" y="245" style="font-size:10;fill:black;text-anchor:middle;dominant-baseline:hanging">2π</text>'
      '  <line x1="50" x2="460" y1="225" y2="225" style="stroke-width:1;stroke:black;"/>'
      '  <line x1="50" x2="50" y1="225" y2="15" style="stroke-width:1;stroke:black;"/>'
      '</svg>'
    )
}
  
def _scan():
  event = pygame.event.poll() # Will return NOEVENT if there are no events in the queue.
  if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()
  elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE :
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
    _svg = cairosvg.svg2svg(_svg, dpi = (DPI / _scale)) # Convert svg to svg changing DPI
    _bytes = cairosvg.svg2png(_svg)
    byte_io = io.BytesIO(_bytes)
    return pygame.image.load(byte_io)
    
try:
  pygame.init() 
  pygame.font.init()
    
  _icon = pygame.Surface((32, 32)) # Create a blank icon (32 x 32) for the window
  _icon.fill(pygame.Color('black')) 
  _icon.set_colorkey(pygame.Color('black')) # Make it compleatly transparent
  pygame.display.set_icon(_icon) # Set it as the window's icon (or rather don't display an icon at all)
  pygame.display.set_caption(NAME) # Set window caption  
    
  _screen = pygame.display.set_mode((DISPLAY_SIZE))
  _screen.fill(pygame.Color('black'))
  _background = pygame.Surface((DISPLAY_SIZE)) # Create a drawing surface for the background    
  _background.fill(pygame.Color(BACKGROUND_COLOUR))
    
  _screen.blit(_background, (0, 0))
  
  _x_offset = 25
  _y_offset = 25
  _x_delta = (_screen.get_width() - (500 + 2 * _x_offset)) // (len(_icons) - 1)
  _y_delta = (_screen.get_height() - (250 + 2 * _y_offset)) // (len(_icons) - 1)
    
  for _name in _icons:
    _svg = " ".join(_icons[_name].split()) # Remove whitespace (not really necessary but it tidies things up)
    _image = render_svg(_svg, 1)
    # DEBUG -- sys.stdout.write (_name + " " + str(_image.get_size()) + "\n" + _svg + '\n')
    _screen.blit(_image, (_x_offset, _y_offset)) # Draw the image..
    _x_offset += _x_delta
    _y_offset += _y_delta
    
    while _scan(): # Wait for the user
      pygame.display.flip() # Update the display
      pygame.time.Clock().tick(FPS)
 
  pygame.quit()
 
except KeyboardInterrupt: # Ctrl-C
  pass
 
except Exception as exception: # Catch all other errors - otherwise the script will just fail silently!
  import traceback
  sys.stderr.write (traceback.format_exc()) # Display the default traceback on the console
 
  exit(1)
  
exit()