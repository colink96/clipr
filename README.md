# clipr
ABOUT CLIPR:
Scrapes Twitch clips from any streamer, edits them into a video, and uploads the video to Youtube.

SETUP:
  - API Authorization
    - Register your app for Twitch via https://dev.twitch.tv/docs/api/ to get proper client credentials and input them into 'clipr_secrets.json'
    - Register your app for Youtube via https://developers.google.com/youtube/v3/guides/uploading_a_video
      - Generate a 'client_secrets.json' file via your Google Developers Console and add it to the same directory as upload_video.py
      - Run \'python upload_video.py' on your command line to generate a valid 'oauth2.json' file
      - The Google account you use will be the Youtube channel the video will be uploaded on
  - Packages
    - Clipr uses the following packages, install them by typing the following in your command line:
      - \'pip install requests json python-twitch-client moviepy ffmpeg urllib'
      
USING CLIPR:
  - Every channel on Twitch is identified via a unique Broadcaster ID which can be found on https://www.twitch.tv/settings/connections under the
    League of Legends subcategory next to "ttv-XXXXXXXXX", replace the default channelID with your desired ID in 'clipr_public.py'
  - youtube_string contains several parameters for uploading your video
    - --file: specify the directory for the video to be uploaded
    - --title: specify the title of the video
    - --description: specify description of video
    - --keywords: specify relevant tags for your video
    - --category: specify relevant category (codes can be found here: https://gist.github.com/dgp/1b24bf2961521bd75d6c)
    - --privacyStatus: public, private, or unlisted
  - Run \'python clipr_public.py' on your command line to run the full script, I use Task Scheduler on my local laptop to regularly upload these videos.
 
