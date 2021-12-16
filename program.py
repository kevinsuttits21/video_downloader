from pytube import YouTube, Playlist, Search
import os
from easygui import *
import getpass

# my_video = yt.streams.first() my_video.download(r"C:\Users\{user}\Downloads")
# C:\Users\{user}\Downloads
askings = input("Please enter your download location: ")
if askings == "":
    askings = askings
else:
    askings = 'C:/Users/' + getpass.getuser() + '/' + str(askings) 

choose = input("Do you want to import one video (\"video\") or playlist (\"playlist\")? ").lower()


if choose == "video":
    
    search_or_video = str(input("Search or enter link? "))
    if search_or_video == "search":
        search = Search(input("Search: "))
        print(str(len(search.results)) + ": ")
        tulemus = str(search.results)
        url = tulemus[0]
    elif search_or_video == "link":
        url = str(input("Enter the link of YouTube video you want to download:  "))
    else:
        exit()
        
    yt = YouTube(url)
    try:
        asd = yt.title
    except Exception as viga:
        print("This video is unavailable!")
        print(str(viga))
        exit()
elif choose == "playlist":
    url = str(input("Enter the link of YouTube playlist you want to download:  "))
    yt = Playlist(url)

valik = input("Do you want MP3 or MP4? ").lower()
if valik =="mp3":
    nr = 251
elif valik == "mp4":
    nr = 137
else:
    exit()


if choose == "video":
    print("----------------------------------------")
    print("Title: ",yt.title)
    print("Views: ",yt.views)
    print("Length of video: ",yt.length) ## teisendada
    print("Rating of video: ", (yt.rating, 1))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    if valik == "mp3":
        vide = yt.streams.get_by_itag(nr)
        downloaded_file = vide.download(str(askings))
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)
        print("Download completed")
    elif valik == "mp4":
        vide = yt.streams.get_highest_resolution()
        vide.download(str(askings))
        print("Download completed")
    else:
        exit()
elif choose == "playlist":
    print("----------------------------------------")
    print("Playlist name: ",yt.title)
    print("Views: ",yt.views)
    print("Length of playlist: ",yt.length) ## teisendada
    print('Number of videos in playlist: %s' % len(yt.video_urls))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    for video in yt.videos:
        try:
            video = video
        except Exception:
            print(f"Video {video} is unavailable, skipping.")
        else:
            if valik == "mp3":
                video = video.streams.get_by_itag(nr)
                downloaded_file = video.download(str(askings))
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                os.rename(downloaded_file, new_file)
                print("Download completed")
            elif valik == "mp4":
                vide = video.streams.get_highest_resolution()
                vide.download(str(askings))
                print("Download completed")
            else:
                exit()