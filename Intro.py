from moviepy.editor import *
import praw, pendulum, os, textwrap, boto3, shutil, eyed3
from PIL import Image, ImageDraw, ImageFont


def intro(link):
    cwd = os.getcwd()
    for root, dirs, files in os.walk(r"{}".format(cwd) + "/ImageFolder"):
      for file in files:
        os.remove(os.path.join(root, file))        
    for root, dirs, files in os.walk(r"{}".format(cwd) + "/SpeechFolder"):
      for file in files:
        if "speech1" in file:
          os.remove(os.path.join(root, file))  
  
      
    polly_client = boto3.Session(
    aws_access_key_id='AKIAXVIBDJKGV34E7GVJ',
    aws_secret_access_key='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',
    region_name='us-west-2').client('polly')


    video = VideoFileClip(r"{}".format(cwd) + "/bac.mp4")
    reddit = praw.Reddit(
        client_id="p1P6xKWngBRm57uUhyZ2NQ",
        client_secret="GgAjznRLhAlE-E35VtWH00Hcn1ptSg",
        user_agent="ScraperBot v1.0 by u/BallZi2k21",
        username="BallZi2k21",
        password="scothgard",
    )
    submission = reddit.submission(url=link)
    
    text = submission.title
    
    
    text = text.replace("s it","crap").replace("f  k","screw").replace("f  king","").replace("screwing","").replace("w  re","dor").replace("s  t","bat").replace("b  ch","grinch").replace("c  t","runt").replace("n    r","n word").replace("n   a","n word")
    text = text.replace("ѪѪѬѬ","").replace("\n"," ").replace('[M'," male").replace('M]'," male").replace('[F'," female").replace('F]'," female").replace('(M'," male").replace('M)'," male").replace('(F'," female").replace('F)'," female")
    

    i = 0.1
    response = polly_client.synthesize_speech(
      VoiceId='Joanna',
      OutputFormat='mp3',
      Engine = 'neural', 
      TextType = "ssml", 
      Text = f"<speak><prosody rate='80%'>{text}</prosody></speak>")

    with open("SpeechFolder/speech1{}.mp3".format(round(i,1)), 'wb') as file:
      file.write(response['AudioStream'].read())
    i += 0.1
  
    times = []
    for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
      if "speech1" in x:
        times.append(eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs)
    
    clips = []
    for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
        time = eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs
        if time != 0:
          clip = AudioFileClip(r"{}".format(cwd) + "/SpeechFolder" + "/" + x)
          clips.append(clip)
      
    
    clips = []
    for time in times:
        part = video.subclip(time, time*2) 
        clips.append(part)
    
    
    video_clip = concatenate_videoclips(clips, method='chain')
    video_clip.write_videofile(r"{}".format(cwd) + "/VideoFolder/video_i1.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
    
    
#intro("https://www.reddit.com/r/relationships/comments/1a4fyk/i_need_some_future_datingrelationship_advice_for/")