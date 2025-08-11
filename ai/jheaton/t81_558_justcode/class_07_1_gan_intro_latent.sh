
ffmpeg -framerate 30 -i frame-%03d.png -pix_fmt yuv420p -c:v libx264 movie.mp4
