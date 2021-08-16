from pytube import YouTube
from pytube import *

link = input('請輸入網址或輸入N結束操作')
location = input('請輸入下載位置')
while link != "N" :
    yt = YouTube(link)
    video = yt.streams.first()
    video.download(location)
    link = input('請輸入網址或輸入N結束操作')