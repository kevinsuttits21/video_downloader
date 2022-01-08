from pytube import YouTube, Playlist
import getpass
import os.path
from pathlib import Path
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

location = input("Please enter your download location: ")
if location == "":
    location = location
    print("The download location will be the directory where you are using the code.")
else:
    location = 'C:/Users/' + getpass.getuser() + '/' + str(location)
    print("Checking if directory is valid...")
    path = str(location)
    if_file_exists = os.path.exists(path)
    print(str(if_file_exists))

choose = input("Do you want to import one video (\"video\") or playlist (\"playlist\")? ").lower()
if choose == "video":
    url = str(input("Enter the link of YouTube video you want to download:  ")) ## kui pole url, siis ...
    yt = YouTube(url)
    try:
        asd = yt.title
    except Exception as viga:
        print("This video is unavailable!")
        print(str(viga))
        exit()
elif choose == "playlist":
    url = str(input("Enter the link of YouTube playlist you want to download:  ")) ## kui pole url, siis ...
    yt = Playlist(url)
else:
    print("Error code 102")
    exit()

extension = input("Do you want MP3 or MP4? ").lower()
if extension == "mp3":
    nr = 251
    if Path(location + "/" + yt.title + ".mp3").is_file():
        print("File exist. Skipping.")
        exit()
    else:
        print("File not exist")
elif extension == "mp4":
    nr = 137
    if Path(location + "/" + yt.title + ".mp4").is_file():
        print("File exist. Skipping.")
        exit()
    else:
        print("File not exist")
else:
    print("Error code 103")
    exit()

if choose == "video":
    print("----------------------------------------")
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Length of video: ", yt.length)  ## teisendada
    print("Rating of video: ", (yt.rating, 1))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    if extension == "mp3":
        vide = yt.streams.get_by_itag(nr)
        downloaded_file = vide.download(str(location))
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)
        print("Download completed")
    elif extension == "mp4":
        vide = yt.streams.get_highest_resolution()
        vide.download(str(location))
        print("Download completed")
    else:
        print("Error code 104")
        exit()
elif choose == "playlist":
    print("----------------------------------------")
    print("Playlist name: ", yt.title)
    print("Views: ", {yt.views})
    print("Length of playlist: ", yt.length)  ## teisendada
    print('Number of videos in playlist: %s' % len(yt.video_urls))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    for video in yt.videos:
        try:
            video = video
        except Exception:
            print(f"Video {video} is unavailable, skipping.")
        else:
            if extension == "mp3":
                video = video.streams.get_by_itag(nr)
                if Path(location + "/" + video.title + ".mp3").is_file() == True:
                    print(f'Video {video.title} is exists, skipping.')
                else:
                    downloaded_file = video.download(str(location))
                    base, ext = os.path.splitext(downloaded_file)
                    new_file = base + '.mp3'
                    os.rename(downloaded_file, new_file)
                    print("Download " + str(video.title) + " completed")
            elif extension == "mp4":
                vide = video.streams.get_highest_resolution()
                if Path(location + "/" + vide.title + ".mp3").is_file() == True:
                    print(f'Video {vide.title} is exists, skipping.')
                else:
                    vide.download(str(location))
                    print("Download completed")
            else:
                print("Error code 105")
                exit()

print("The process is completed.")
