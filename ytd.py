from pytube import YouTube
from sys import argv

link = argv[1]
yt_vid = YouTube(link)

print("Title: ", yt_vid.title)
print("Views: ", yt_vid.views)

yt_download = yt_vid.streams.get_highest_resolution()
yt_download.download("../")

truncated_title = yt_vid.title[:30] + "..." if len(yt_vid.title) > 30 else yt_vid.title
print(f'Your video "{truncated_title}" has been downloaded!')
