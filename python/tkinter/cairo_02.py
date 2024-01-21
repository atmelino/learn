#!/usr/bin/env python3
# File: svgs-tkinter-python3.py
# License: CC-BY-SA 4.0
# Author: bgstack15
# Startdate: 2019-06-21 10:09
# Title: 
# Purpose: 
# History:
# Usage:
# References:
#    http://effbot.org/tkinterbook/button.htm
#    http://effbot.org/tkinterbook/tkinter-application-windows.htm
#    http://effbot.org/tkinterbook/
#    https://stackoverflow.com/questions/18537918/set-window-icon#18538416
#    https://pillow.readthedocs.io/en/stable/reference/ImageTk.html
# Improve:
# Dependencies:
#    devuan: python3-tk python3-pil.imagetk python3-cairosvg
#    el7: python36-tkinter python36-pillow-tk ( pip3 install cairosvg )

import re
import tkinter as tk
from PIL import Image, ImageTk, PngImagePlugin

LM_USE_SVG = 0
try:
   from cairosvg import svg2png
   LM_USE_SVG = 1
except:
   print("WARNING: Unable to import cairosvg. No svg images will be displayed.")
   LM_USE_SVG = 0

# graphical classes and functions
print("Loading graphics...")

def photoimage_from_svg(filename = "",size = "48"):
   # this one works, but does not allow me to set the size.
   # this is kept as an example of how to open a svg without saving to a file.
   # open svg
   item = svg2png(url=filename, parent_width = size, parent_height = size)
   return ImageTk.PhotoImage(data=item)

def empty_photoimage(size=24):
   photo = Image.new("RGBA",[size,size])
   return ImageTk.PhotoImage(image=photo)

def image_from_svg(filename = "",size = 0):
   # open svg
   if LM_USE_SVG == 1:
      if size == 0:
         # unscaled
         svg2png(url=filename,write_to="/tmp/example_temp_image.png")
      else:
         svg2png(url=filename,write_to="/tmp/example_temp_image.png",parent_width = size,parent_height = size)
      photo = Image.open("/tmp/example_temp_image.png")
   else:
      photo = Image.new("RGBA",[size,size])
   return photo

def get_scaled_icon(iconfilename, size = 0):

   try:
      print("Opening icon file",iconfilename)
      # try an svg
      if re.compile(".*\.svg").match(iconfilename):
         photo = image_from_svg(filename=iconfilename, size=size)
      else:
         photo = Image.open(iconfilename)
   except Exception as f:
      print("Error with icon file:", f)
      return empty_photoimage()

   if size != 0 and (type(photo) is Image or type(photo) is PngImagePlugin.PngImageFile):
      photo.thumbnail(size=[size, size])

   if not type(photo) is ImageTk.PhotoImage:
      try:
         photo = ImageTk.PhotoImage(photo)
      except Exception as e:
         print("Error was ",e)
   return photo

class App:
   def __init__(self, master):
      frame = tk.Frame(master)
      frame.grid(row=0)

      self.photo1 = get_scaled_icon("images/example.svg", 200)
      self.button1 = tk.Button(frame, text="Scaled to 24x24", image=self.photo1, compound=tk.LEFT)
      self.button1.grid(row=0,column=0)

      self.photo2 = get_scaled_icon("images/hello.svg")
      self.button2 = tk.Button(frame, text="Unscaled", image=self.photo2, compound=tk.LEFT)
      self.button2.grid(row=0,column=1)

      self.buttonCancel = tk.Button(frame, text="Cancel", underline=0, command=self.quitaction)
      self.buttonCancel.grid(row=1,columnspan=8,sticky=tk.W+tk.E)

   def quitaction(self,b=None):
      print("Closing the window...")
      root.destroy()

root = tk.Tk()

# MAIN LOOP
root.title("SVG examples")
imgicon = get_scaled_icon("tkinter/hello.svg", 24)
root.tk.call('wm','iconphoto', root._w, imgicon)
app = App(root)
root.mainloop()
try:
   root.destroy()
except:
   pass
