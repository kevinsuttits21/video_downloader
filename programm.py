from pytube import YouTube, Playlist
import os
from easygui import *



text = "Do you want to import one video \"video\" or playlist \"playlist\"? "
title = "Youtube Video Downloader"
input_list = ["Answer"]
output2 = multenterbox(text,title,input_list)

kast2 = msgbox
text2 = "Enter the following details"
title2 = "Youtube Video Downloader"  
input_list2 = ["URL", "Video type (mp3, MP3 or mp4, MP4)"]   
output = multenterbox(text2, title2, input_list2)

if "http" not in output[0]:
    title = "Youtube Video Downloader"
    message000 = ("Wrong information! Please relaunch the program and insert the correct details.")
    msgbox(message000, title)
    output.close()
    

title3 = "Youtube Video Downloader"  
message3 = ("Thank you!" + " Please wait for the video to download :)")
kast = msgbox(message3, title3)


choose = input("Do you want to import one video (\"video\") or playlist (\"playlist\")? ".lower())
if choose == "video":
    url = str(input("Enter the link of YouTube video you want to download:  "))
    yt = YouTube(url)
elif choose == "playlist":
    url = str(input("Enter the link of YouTube playlist you want to download:  "))
    yt = Playlist(url)

valik = input("Do you want MP3 or MP4? ")
if valik == "MP3" or "mp3":
    nr = 251
else:
    nr = 137
    
if choose == "video":
    print("----------------------------------------")
    print("Title: ",yt.title)
    print("Views: ",yt.views)
    print("Length of video: ",yt.length) ## teisendada
    print("Rating of video: ", round(yt.rating, 1))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    if valik == "MP3" or "mp3":
        vide = yt.streams.get_by_itag(nr)
        downloaded_file = vide.download()
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)
    else:
        yt.streams.get_by_itag(nr)
elif choose == "playlist":
    print("----------------------------------------")
    print("Playlist name: ",yt.title)
    print("Views: ",yt.views)
    print("Length of playlist: ",yt.length) ## teisendada
    print('Number of videos in playlist: %s' % len(yt.video_urls))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    for video in yt.videos:
        if valik == "MP3" or "mp3":
            video = video.streams.get_by_itag(nr)
            downloaded_file = video.download()
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
        else:
            video.streams.get_by_itag(nr)
            video.download()
print("Download completed")
