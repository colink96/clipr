#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
import requests
import json
from twitch import TwitchHelix
import urllib.request
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

#Unique identifier for any streamer's channel. 191002666 = twitch.tv/cawlink
channelid = '191002666'

#Twitch API Credentials, create a clipr_secrets.json file in the same directory, or input manually
with open('clipr_secrets.json', 'r') as f:
    clipr_secrets = json.load(f)
CLIENT_ID = clipr_secrets['client_id']
token = clipr_secrets['client_token']
helix = TwitchHelix(client_id=CLIENT_ID, oauth_token=token)

clips = helix.get_clips(channelid)

#Get all clips from the current month
monthly_clips = []
month = datetime.now().month
year = datetime.now().year

#Download them locally...
directory ='clips/'+str(month)+str(year)
i = 1
for clip in range(len(clips)):
    if clips[clip]['created_at'].month == month and clips[clip]['created_at'].year == year:
        monthly_clips.append(clips[clip])
clip_links = []
for clip in monthly_clips:
    clip_links.append(clip['thumbnail_url'].replace('-preview-480x272.jpg','.mp4'))
counter = 1
if not os.path.exists(directory):
    os.makedirs(directory)
for link in clip_links:
    clip_name = 'clip'+str(counter)
    urllib.request.urlretrieve(link, directory+'/'+clip_name+'.mp4')
    print('Downloading: '+clip_name+' in: '+directory)
    counter+=1

#Edit them together using MoviePY
directory_ = os.fsencode(directory)
videos = []
for file in os.listdir(directory_):
    filename = os.fsdecode(file)
    if filename.endswith(".mp4"):
        filenamestr = str(filename)
        clip = VideoFileClip(directory+'/'+filenamestr)
        videos.append(clip)
final_clip = concatenate_videoclips(videos)
final_clip.write_videofile(directory+'/'+"MonthlyHighlights"+str(month)+str(year)+".mp4")

#Upload to Youtube via Youtube API, must run in command line first to gen oauth2.json file
youtube_string = 'python upload_video.py --file="'+directory+'/MonthlyHighlights'+str(month)+str(year)+'.mp4" --title="Cawlink Monthly Stream Highlights '+str(month)+'/'+str(year)+'" --description="Hi all, my name is Colin, and this is a monthly compilation of my stream highlights. Check out my stream at https://www.twitch.tv/cawlink. I developed this bot to automate these uploads, inspired by Gloomshot. Check out Gloomshot here: (https://www.youtube.com/channel/UCmuhXyzpbQ1BJt_m3vtfXlA). Thanks for watching!" --keywords="smash,ultimate,games" --category="20" --privacyStatus="public"'

os.system(youtube_string)
