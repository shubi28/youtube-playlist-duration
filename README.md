# Youtube Playlist Duration

**Steps to run the py script on your local system:** 
1. Clone or download the zip folder to your system and extract the files.
2. Assuming you have python and pip already installed on your system, If not install it first.
3. Next run "pip install pip install google-api-python-client" in your terminal

**Steps to follow to enable the Google Youtube API and start using it:**
1. Go to Google Developers Console(https://developers.google.com/) and Click on Sign In in the upper rightmost corner of the page. Sign In using the credentials of the valid Google Account. If you don’t have a google account, setup a account first and then use the details to Sign In on the Google Developers Homepage.
2. Now navigate to the Developer Dashboard(https://console.developers.google.com/apis/dashboard?project=gurl-project-1541962189248&folder&organizationId) and create a new Project.
3. Click on Enable API option.
4. In the search field, search for Youtube Data API and select the "**Youtube Data API v3**" option that comes in the drop down list.
5. Click on ENABLE option to get started with the API.
6. In the sidebar under APIs & Services, select Credentials.
7. In the Credentials tab, select the Create credentials drop-down list, and choose API key.
8. Copy and paste it in the Playlist.py file at line 6 in place of "**MY_API_KEY**"

**THE PROGRAM IS READY TO RUN**<br>
Just Put any PlaylistID in the Playlist.py file at line 24 and run the code to check the duration of the playlist.

**How to find the playlistID from any youtube video link:**<br>
Everything written after list= is the playlistID. For example if a youtube video link is given as below :<br> 
https://www.youtube.com/watch?v=knfrxj0T5NY&list=PLC1og_v3eb4juFD_2YcJt2nDhytHNzhRU <br>
Then the playlistID would be "PLC1og_v3eb4juFD_2YcJt2nDhytHNzhRU"



# Thanks for reading!
