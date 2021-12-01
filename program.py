from pytube import YouTube, Playlist
import os

choose = input("Do you want import one song (\"song\") or playlist (\"playlist\")? ".lower())
if choose == "song":
    url = str(input("Enter the link of YouTube video you want to download:  "))
    yt = YouTube(url)
elif choose == "playlist":
    url = str(input("Enter the link of YouTube playlist you want to download:  "))
    yt = Playlist(url)

valik = input("Do you want MP3 or MP4? ")
if valik == "MP3":
    nr = 251
else:
    nr = 137
    
if choose == "song":
    print("----------------------------------------")
    print("Title: ",yt.title)
    print("Views: ",yt.views)
    print("Length of video: ",yt.length) ## teisendada
    print("Rating of video: ", round(yt.rating, 1))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    if valik == "MP3":
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
        if valik == "MP3":
            video = video.streams.get_by_itag(nr)
            downloaded_file = video.download()
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
        else:
            video.streams.get_by_itag(nr)
            video.download()
print("Download completed")