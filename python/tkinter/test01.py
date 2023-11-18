#python -m pip install tksvg    ---> this is not in IDLE actually, but in cmd!

import tkinter as tk
import tksvg

window = tk.Tk()

d = '''<svg width="0" height="0"><path d="M17.2 26.6l1.4 2.9 3.2.5-2.2 2.3.6 3.2-2.9-1.5-2.9 1.5.6-3.2-2.3-2.3 3.2-.5zM44.8 3.8l2 .3-1.4 1.4.3 2-1.8-.9-1.8.9.3-2L41 4.1l2-.3.9-1.8zM8.9 10l.9 1.8 2 .3-1.4 1.4.3 2-1.8-.9-1.8.9.3-2L6 12.1l2-.3zm37.6 17l.647 1.424 1.553.258-1.165 1.165.26 1.553-1.424-.776-1.295.647.26-1.553-1.165-1.165 1.553-.259zM29.191 1C24.481 2.216 21 6.512 21 11.626c0 6.058 4.887 10.97 10.915 10.97 3.79 0 7.128-1.941 9.085-4.888-.87.224-1.783.344-2.724.344-6.028 0-10.915-4.912-10.915-10.97 0-2.25.674-4.341 1.83-6.082z" fill="#7694b4" fill-rule="evenodd"></path></svg>'''

# if you have a SVG file on disk, use the file parameter:
# svg_image = tksvg.SvgImage( file = 'path/to/file' )

# if you have SVG code from somewhere - in my case I scraped it from a website - use the data parameter:
svg_image = tksvg.SvgImage( data = d )

# You can also resize the image, but using only one of the three available parameters:
# svg_image = tksvg.SvgImage( data = d, scale = 0.5 )
# svg_image = tksvg.SvgImage( data = d, scaletowidth = 200 )
svg_image = tksvg.SvgImage( data = d, scaletoheight = 200 )

tk.Label( image = svg_image ).pack()