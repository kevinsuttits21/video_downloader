import pytube.exceptions
from pytube import YouTube, Playlist
import getpass
import os.path
from pathlib import Path
import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print("----------------------------------------")
print("\nVideo downloader\n")
print("----------------------------------------")

location = input("Please enter your download location: ")
if location == "":
    location = location
    print("The download location will be the directory where you are using the code.")
else:
    location = 'C:/Users/' + getpass.getuser() + '/' + str(location)
    print("Checking if directory is valid...")
    path = str(location)
    if_file_exists = os.path.exists(path)
    if if_file_exists == False:
        print("No such folder exists. The download location will be the directory where you are using code.")
        location = ""
    elif if_file_exists == True:
        print("Directory is valid.")
    else:
        print("Error code 101")
        print("Args of location: " + location)
        print("Please report a bug in GitHub: https://github.com/kermonurmeoja/video_downloader/issues")
        exit()

choose = input("Do you want to import one video (\"video\") or playlist (\"playlist\")? ").lower()
if choose == "video":
    url = str(input("Enter the link of YouTube video you want to download:  "))
    try:
        yt = YouTube(url)
    except pytube.exceptions.RegexMatchError:
        print("Please enter a valid URL.")
        exit()
    except Exception:
        print("Error code 102")
        print("Args of location: " + location)
        print("Args of choose: " + choose)
        print("Args of URL: " + url)
        print("Please report a bug in GitHub: https://github.com/kermonurmeoja/video_downloader/issues")
        exit()
    else:
        pass
    yt = YouTube(url)
    try:
        asd = yt.title
    except Exception as viga:
        print("This video is unavailable!")
        print(str(viga))
        exit()

elif choose == "playlist":
    url = str(input("Enter the link of YouTube playlist you want to download:  "))
    try:
        yt = Playlist(url)
    except pytube.exceptions.RegexMatchError:
        print("Please enter a valid URL.")
        exit()
    except Exception:
        print("Error code 103")
        print("Args of location: " + location)
        print("Args of choose: " + choose)
        print("Args of URL: " + url)
        print("Please report a bug in GitHub: https://github.com/kermonurmeoja/video_downloader/issues")
        exit()
    else:
        pass
    yt = Playlist(url)
else:
    print("Please enter a valid selection!")
    exit()

extension = input("Do you want MP3 or MP4? ").lower()
if extension == "mp3":
    nr = 251
    if Path(location + "/" + yt.title + ".mp3").is_file():
        print("File exists. Skipping.")
        exit()
    else:
        pass
elif extension == "mp4":
    nr = 137
    if Path(location + "/" + yt.title + ".mp4").is_file():
        print("File exists. Skipping.")
        exit()
    else:
        print("File doesn't exist")
else:
    print("Please enter a valid selection!")
    exit()

if choose == "video":
    print("----------------------------------------")
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Length of video: ", str(datetime.timedelta(seconds=yt.length)))
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
        print("Args of location: " + location)
        print("Args of choose: " + choose)
        print("Args of URL: " + url)
        print("Args of extension: " + extension)
        print("Please report a bug in GitHub: https://github.com/kermonurmeoja/video_downloader/issues")
        exit()
elif choose == "playlist":
    i = 1
    print("----------------------------------------")
    print("Playlist name: ", yt.title)
    print("Views: ", yt.views)
    print('Number of videos in playlist: %s' % len(yt.video_urls))
    print("----------------------------------------")
    print(f'Downloading: {yt.title}')
    for video in yt.videos:
        try:
            video = video
        except Exception:
            print(f"Video {video.title} is unavailable, skipping." + " (" + str(i) + "/" + str(len(yt.video_urls)) + ")")
            i = i + 1
        else:
            if extension == "mp3":
                video = video.streams.get_by_itag(nr)
                if Path(location + "/" + video.title + ".mp3").is_file() == True:
                    print(f'Video {video.title} is exists, skipping.' + " (" + str(i) + "/" + str(len(yt.video_urls)) + ")")
                    i = i + 1
                else:
                    print(f"Downloading: {video.title}" + " (" + str(i) + "/" + str(len(yt.video_urls)) + ")")
                    downloaded_file = video.download(str(location))
                    base, ext = os.path.splitext(downloaded_file)
                    new_file = base + '.mp3'
                    os.rename(downloaded_file, new_file)
                    print("Download of \"" + str(video.title) + "\" completed")
                    i = i + 1
            elif extension == "mp4":
                vide = video.streams.get_highest_resolution()
                if Path(location + "/" + vide.title + ".mp3").is_file() == True:
                    print(f'Video {vide.title} is exists, skipping.' + " (" + str(i) + "/" + str(len(yt.video_urls)) + ")")
                    i = i + 1
                else:
                    print(f"Downloading: {vide.title}" + " (" + str(i) + "/" + str(len(yt.video_urls)) + ")")
                    vide.download(str(location))
                    print("Download of \"" + str(vide.title) + "\" completed")
                    i = i + 1
            else:
                print("Error code 105")
                print("Args of location: " + location)
                print("Args of choose: " + choose)
                print("Args of URL: " + url)
                print("Args of extension: " + extension)
                print("Please report a bug in GitHub: https://github.com/kermonurmeoja/video_downloader/issues")
                exit()

print("The process is completed.")
input("Press Enter to continue...")
