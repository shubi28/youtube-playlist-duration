import re
from datetime import timedelta
from googleapiclient.discovery import build

# Put your API Key inplace of "MY_API_KEY" below
api_key = "MY_API_KEY"

# creating youtube resource object
youtube = build('youtube', 'v3', developerKey=api_key)

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0

# To handle pagination
nextPageToken = None
while True:
    # First api request
    # To fetch the video IDs of all the videos in a playlist
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId="PLC1og_v3eb4juFD_2YcJt2nDhytHNzhRU",
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    # Saving all the videoIds in vid_ids array
    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    # Second api request
    # To fetch the duration of all the videos corresponding to their videoIds
    vid_request = youtube.videos().list(
        part="contentDetails",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()

        total_seconds += video_seconds

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

# Dividing the total seconds in seconds, minutes and hours
total_seconds = int(total_seconds)

minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

# Printing the total duration of the playlist in HH:MM:SS format
print(f'{hours}:{minutes}:{seconds}')