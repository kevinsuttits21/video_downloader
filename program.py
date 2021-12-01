from pytube import YouTube

url = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(url)
valik = input("Do you want MP3 or MP4? ")

print("----------------------------------------")
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length) ## teisendada
print("Rating of video: ", round(yt.rating, 1))
print("----------------------------------------")

if valik == "MP3":
    vid = yt.streams.get_by_itag(251)
else:
    vid = yt.streams.get_highest_resolution()

print("Downloading...")
vid.download()
print("Download completed")