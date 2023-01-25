# -*- coding:utf-8 -*-
from tkinter import *
#from Conector import *
from pathlib import Path
from moviepy.editor import *
import pyttsx3, praw, pendulum, os, textwrap, boto3, eyed3, shutil, random
from PIL import Image, ImageDraw, ImageFont, ImageTk
from praw.models import MoreComments
import pandas as pd


def click():
      
  cwd = os.getcwd()
  #Deleting everything in the folders we used
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/ImageFolder"):
      for file in files:
          os.remove(os.path.join(root, file))       
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/SpeechFolder"):
      for file in files:
          os.remove(os.path.join(root, file))

  polly_client = boto3.Session(
    aws_access_key_id='AKIAXVIBDJKGV34E7GVJ',
    aws_secret_access_key='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',
    region_name='us-west-2').client('polly')

  link = textentry.get()
  parts = textentry2.get()

  
  video = VideoFileClip(r"{}".format(cwd) + "/bac.mp4")
  
  l = [*range(0,920,20)]
  random.shuffle(l)
  a = [*range(0,46)]
  random.shuffle(a)
  number = l[a[3]]

  video = video.subclip(number, int(video.duration))

  reddit = praw.Reddit(
  client_id="p1P6xKWngBRm57uUhyZ2NQ",
  client_secret="GgAjznRLhAlE-E35VtWH00Hcn1ptSg",
  user_agent="ScraperBot v1.0 by /u/BallZi2k21",
  username="BallZi2k21",
  password="scothgard", )
  submission = reddit.submission(url=link)
   
  comments = []
  comment_parts = parts.split("---")
  
  submissions = [x for x in submission.comments.list() if not isinstance(x, MoreComments)]
  
  for comment in comment_parts:
    comments.append([id for id in submissions if comment in id.body])
  
  comments = [y.id for x in comments for y in x]
  
  #Finding the path to the reddit font
  path = r"{}".format(cwd)
  location = os.path.join(path, "Verdana.ttf")
  
  wid = int(video.w-video.w*0.06)
  heig = int(video.h-video.h*0.10)
  
  image = Image.new(mode="RGB", size=(wid, heig), color = "#1a1a1b")
  draw = ImageDraw.Draw(image)
  image.putalpha(0)
  
  #Drawing the rest of the text
  y_text = 0
  height = int(video.h/30)
  i = 0.1
  
  chosen_comments = [{"parent_id":"t3","body": "He's your ex"},{"parent_id":"t1","body": "Suck yo mum bruv"}]

  Y = 0
  v_lines = []
  v_names = []
  body_text = []
  while Y < len(comments):  
    for actual_comment in chosen_comments:
      words_n_stuff = ''
      chosen_comment = reddit.comment(comments[Y])
      name = chosen_comment.author
      creation_date = ((pendulum.from_timestamp(chosen_comment.created).diff_for_humans()).replace("years ago", "y").replace("year ago","y").replace("months ago","m").replace("month ago","m").replace("hours ago","h").replace("day ago","d").replace("days ago","d").replace("hour ago","h").replace(" ",""))
      edited_date = ("edited" + " " + (pendulum.from_timestamp(chosen_comment.edited).diff_for_humans()).replace("years ago", "y").replace("year ago","y").replace("months ago","m").replace("month ago","m").replace("hours ago","h").replace("day ago","d").replace("days ago","d").replace("hour ago","h").replace(" ",""))
      nr = int((pendulum.from_timestamp(chosen_comment.edited).diff_for_humans()).replace("years ago", "").replace("year ago","").replace("months ago","").replace("month ago","").replace("hours ago","").replace("day ago","").replace("days ago","").replace("hour ago","").replace(" ",""))
      
      if nr > 48 and "t3" in actual_comment["parent_id"]:
        words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date}\n\nꚈⰔ{actual_comment['body']}"
      elif nr > 48 and "t1" in actual_comment["parent_id"]:
        words_n_stuff = f"ꙂѢⰎ{chosen_comment.author} · {creation_date}\n\nⰔ{actual_comment['body']}"
      elif nr > 48:
        words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date}\n\nⰔ{actual_comment['body']}"
      elif nr < 48 and "t3" in actual_comment["parent_id"]:
        words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date} · {edited_date}\n\nꚈⰔ{actual_comment['body']}"
      elif nr < 48 and "t1" in actual_comment["parent_id"]:
        words_n_stuff = f"ꙂѢⰎ{chosen_comment.author} · {creation_date} · {edited_date}\n\nⰔ{actual_comment['body']}"
      elif nr < 48:
        words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date} · {edited_date}\n\nⰔ{actual_comment['body']}"
      
      if words_n_stuff[-1] != ".":
        words_n_stuff = words_n_stuff + "."
      
      bannedWords = pd.read_csv("bannedwords.csv")
    
      text_comment = submission.selftext
      individual_words = text_comment.split(" ")
      for word in individual_words:
        for badWord in bannedWords["Banned Word"].tolist():
          if word.upper() == badWord:
            index = (bannedWords.index[bannedWords["Banned Word"] == word.upper()].tolist())[0]
            words_n_stuff = (text_comment.replace(word, bannedWords["Replacement"][index]))
  
      v_names.append(f"{chosen_comment.author}")
      
      words_n_stuff = words_n_stuff.split("...")
      words_n_stuff = [x.split("..") for x in words_n_stuff]
      words_n_stuff = [[y.replace("\n\n","ѪѪѬѬ").replace(",",',ĂĂ').replace(".",".ĂÎ").replace("?","?ÎÎ") for y in x] for x in words_n_stuff]
      words_n_stuff = ["..ĂÎ".join(x) for x in words_n_stuff]
      words_n_stuff = "...ĂÎ".join(words_n_stuff)
      
      body_text.append(words_n_stuff)
    
      Y+=1
    
    body_text = [x.split("ĂĂ") for x in body_text]
    body_text = [y for x in body_text for y in x]
    body_text = [x.split("ĂÎ") for x in body_text]
    body_text = [y for x in body_text for y in x]
    body_text = [x.split("ÎÎ") for x in body_text]
    body_text = [[x] if "..." in x else x for x in body_text]
    
    
    body_text = [y.strip() for x in body_text for y in x]
    
    v_lines = body_text
    
    body_text = [x.replace("Ⱄ","") for x in body_text]
    
    nr = 0
    s = ""
    text3 = []
    
    nr = 0
    for x in body_text:
      nr += len(x)
      if "Ꚉ" in x:
          x = x.replace("Ꚉ","")
          s = ''
          nr = 0
      if "ѪѪѬѬ" in x:
          a = sum([1 for y in x if "ѪѪѬѬ" in y])
          nr += a * 90
      if "Ⱁ" in x:
        nr += 90
      if nr >= 970:
        s = ''
        nr = 0
      s += " " + x
      text3.append("Ѩ")
      text3.append(s)
      text3.append("Ѧ")
    
  
  text3 = [x.split("Ѫ") for x in text3]
  text3 = [y for x in text3 for y in x]
  text3 = [x.strip() for x in text3]
  
  
  e_lines2 = []
  
  for lis in text3:
      e = textwrap.wrap(lis, width = 92, replace_whitespace=False)
      e_lines2.append(e)
  
      
  e_lines2 = [y for x in e_lines2 for y in x]
  e_lines2 = [x.split("ѬѬ") for x in e_lines2]
  e_lines2 = [y for x in e_lines2 for y in x]
  
  e_lines2 = [x.split("Ꙃ") for x in e_lines2]
  e_lines2 = [y for x in e_lines2 for y in x]
  
  
  b = []
  c = []
  record = False
  
  for i in e_lines2:
    if i == "Ѧ":
      record = False
      if c != []:
        b.append(c)
      c = []
    if record:
      c.append(i)
    else:
      if i not in ("Ѧ", "Ѩ"):
        b.append(i)
    if i == "Ѩ":
      record = True
  
  
  i4 = 0.1
  for lines in b:
    start = 20 
    for l in lines:
        color = "#D7DADC"
        font_type1 = ImageFont.truetype(location , int(video.h/30)) 
        if "Ⰾ" in l:
            font_type1 = ImageFont.truetype(location , int(video.h/30)-3)
            #color = (165, 164, 164, 1)
            l = l.replace("Ⰾ","")
        if "Ѣ" in l:
            start = 60
            l = l.replace("Ѣ","")
        draw.text(((start), y_text), l.replace("&#x200B;","").replace("&nbsp;",""), font=font_type1, fill=color)
        y_text += height*1.3
    cropped = image.crop((0,0,image.width, y_text + 8))
    y_text = 0
    cropped.save(r"{}".format(cwd) + "/ImageFolder" + "/{}.png".format(round(i4, 1)), 'PNG')
    image = Image.new(mode="RGB", size=(wid, heig), color = "#1a1a1b")
    draw = ImageDraw.Draw(image)
    image.putalpha(0)
    i4 += 0.1
  
  #Chosing the voices "[i]", and the tempo of the voices
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)#Voices
  engine.setProperty('rate', 130)#Tempo
  
  v_lines = [x.replace("s it","crap").replace("f  k","screw").replace("f  king","").replace("screwing","").replace("w  re","dor").replace("s  t","bat").replace("b  ch","grinch").replace("c  t","runt").replace("n    r","n word").replace("n   a","n word") for x in v_lines]

  v_lines = [x.replace("ѪѪѬѬ","").replace("Ꙃ","").replace("Ѣ","").replace("Ꚉ","") for x in v_lines]
  v_lines = [x.split("Ⱄ") for x in v_lines]
  v_lines = [y for x in v_lines for y in x]
  v_lines = [x for x in v_lines if x != ""]
  
  for name in v_names:
    v_lines = ["" if name in x else x for x in v_lines]
  v_lines.insert(len(v_lines),"")
  v_lines.pop(0)
  
  v_lines.append("S")
   
  
  i = 0.1
  for lines in v_lines:
    response = polly_client.synthesize_speech(
      VoiceId='Joanna',
      OutputFormat='mp3',
      Engine = 'neural', 
      TextType = "ssml", 
      Text = f"<speak><prosody rate='80%'>{lines}</prosody></speak>")

    with open("SpeechFolder/speech3{}.wav".format(round(i,1)), 'wb') as file:
      file.write(response['AudioStream'].read())
    i += 0.1

  x = max(os.listdir(r"{}".format(cwd) + "/SpeechFolder"))
  os.remove(r"{}".format(cwd) + "/SpeechFolder/" + x)
  
  for fname in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    shutil.copy2(r"{}".format(cwd) + "/SpeechFolder/" + fname, r"{}".format(cwd) + "/AudioFolder")
  
  
  #Using "Wave" we are able to extract the time nessesary to read the line
  times = []
  for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    times.append(eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs)
  
  
  """clips = []
  for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    time = eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs
    if time != 0:
      clip = AudioFileClip(r"{}".format(cwd) + "/SpeechFolder" + "/" + x)
      clips.append(clip)
    
  speech = concatenate_audioclips(clips)
  back_music = AudioFileClip(r"{}".format(cwd) + "/reddit-music.mp3")
  back_music = back_music.subclip(0, float(speech.duration))"""
  
  #final_clip = CompositeAudioClip([speech, back_music])


  #The movie proces
  path = r"{}".format(cwd) + "/ImageFolder"
  s = 0
  clips = []
  times = iter(times)  # turn the list into an iterator
  for file in os.listdir(path): #Loop through the files in the folder
    f = os.path.join(path, file)
    if os.path.isfile(f):
      time = next(times) #Chose the next time 
      print(file)
      images = (ImageClip(path + "/" + file)
        .set_duration(time)                      #Sets the duration and the location of the images on screen
        .set_position((0.03,0.10), relative=True))
        
      part = video.subclip(s, s + time)  #Cuts the clip into subclips, using MATH
      s += time
  
      final = CompositeVideoClip([part, images])  #Overlay the images over each other
      clips.append(final)
  
  video_clip = concatenate_videoclips(clips, method='chain')
  video_clip.write_videofile(r"{}".format(cwd) + "/VideoFolder/video_i3.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
  
  
  #video_name(vname)
        
window = Tk()
window.title = "BMM"
window.configure(background="black")
folder = Path(__file__).absolute().parent
main_image = Image.open(folder / "Image_backGround.png")
background = ImageTk.PhotoImage(main_image)
Label(window, image = background, bg = "black").grid(row=2, column=0, sticky=W)



textentry = Entry(window, width = 20, bg = "#C4C4C4")
textentry.place(height=40, width=576, x = 650, y = 148)
textentry2 = Entry(window, bg = "#C4C4C4")
textentry2.place(height=145, width=576, x = 650, y = 315)
textentry3 = Entry(window, bg = "#C4C4C4")
textentry3.place(height=40, width=576, x = 650, y = 580)


Button(window, text = "Submit", command = click, bg = "#91DD98").place(height=43, width=168, x = 854.5, y = 666)


window.mainloop()