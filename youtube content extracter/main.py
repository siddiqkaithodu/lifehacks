Need help extracting youtube video comments then this automation script is for you. With a few lines of code, you can extract comments from any youtube video.

This script is very handy when you have to fetch comments for multiple videos.

# Youtube Comment Extractor
# pip install youtube-comment-scraper-python
import youtube_comment_scraper_python as ycs
def FetchComments(url):
ycs.youtube.open(url)
    result = ycs.youtube.video_comments()
    comments = result['body']
    print(comments)
FetchComments("Youtube Video URL")
