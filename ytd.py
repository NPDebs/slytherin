from pytube import YouTube

# Prompt user to input direct link to the YouTube video; store in 'video_link' variable
video_link = input('Paste the link to your video: ')

# Create a YouTube object with the video link
yt_vid = YouTube(video_link)

# Print video information
print("Title: ", yt_vid.title)
print("Views: ", yt_vid.views)

# Choose the stream for download
yt_download = yt_vid.streams.get_highest_resolution()

# Download the video
yt_download.download("../")

# Truncate title if too long
truncated_title = yt_vid.title[:30] + "..." if len(yt_vid.title) > 30 else yt_vid.title
print(f'Your video "{truncated_title}" has been downloaded!')
