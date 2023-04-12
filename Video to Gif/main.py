Convert your video to a gif easily with this automation script that uses the Moviepy module. This script will let you convert your favorite videos into gifs in just a few lines of code.

# Video to Gif
# pip install moviepy
from moviepy.editor import *
def Video_To_Gif(video):
    clip = VideoFileClip(video)
    clip.write_gif("output.gif")
Video_To_Gif("video.mp4")
