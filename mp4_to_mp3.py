import os
from moviepy.editor import *

location = input('請輸入檔案名稱')
name = input('請命名')

mp4_file = location + '.mp4'
mp3_file = name + '.mp3'
videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
    
audioclip.close()
videoclip.close()