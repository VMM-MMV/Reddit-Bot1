# -*- coding:utf-8 -*-
from tkinter import *
from Intro import *
#from Body import *
#from Conector import *
from pathlib import Path
from moviepy.editor import *
import pyttsx3, praw, pendulum, os, textwrap, boto3, eyed3, shutil, random
from PIL import Image, ImageDraw, ImageFont, ImageTk
from praw.models import MoreComments
import pandas as pd

#The fact that a 28 year old married man is telling a 16 year old girl he loves her should be reason---The fact that a 28 year old married man is telling a 16 year old girl he loves her should be reason---This man is not an amazing person. This is a man who took a vow to be your faithful partner for life---This man is not an amazing person. This is a man who took a vow to be your faithful partner for life
#I didn't comment on the first thread, though I read it. I just want to say- is this weird?- I am so---I read your post this morning and I am soo glad you updated and left him!---Wow. You actually did it.---I hope she does
#I can see why your mom is uncomfortable. 2 years ago her friend could’ve been arrested for this---That aside I do understand her thoughts, but I want her to understand our perspective too---Have you ever had another gf before this? It’s a pretty big age difference for someone young like---Yeah it's a big age difference but it's not like it bothers me; I like her she likes me---Have sex with her. Have fun with her. But let's not delude ourselves here. You're not capable of---Upvote for chicken and rice (and truths)

def click():
      
  cwd = os.getcwd()

  for root, dirs, files in os.walk(r"{}".format(cwd) + "/ImageFolder"):
    for file in files:
      os.remove(os.path.join(root, file))        
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/SpeechFolder"):
    for file in files:
      os.remove(os.path.join(root, file))  

    

  polly_client = boto3.Session(
    aws_access_key_id=id(),
    aws_secret_access_key=key(),
    region_name=region_name()).client(client())

  link = textentry.get()
  parts = textentry2.get()
  vname = textentry3.get()

  intro(link)
  #body(link)
  
  video = VideoFileClip(r"{}".format(cwd) + "/bac.mp4")
  
  l = [*range(0,920,20)]
  random.shuffle(l)
  a = [*range(0,46)]
  random.shuffle(a)
  number = l[a[3]]

  video = video.subclip(number, int(video.duration))
  
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
  
  Y = 0
  v_lines = []
  v_names = []
  
  
  body_text = ['ⰎMabelisms · 4yѪѪѬѬꚈⰔI can see why your mom is uncomfortable.ĂÎ 2 years ago her friend could’ve been arrested for this.ĂÎ You need to understand and accept *why* people find this disturbing and respect their boundaries.ĂÎ', "ꙂѢⰎKitchenBreakfast · 4yѪѪѬѬⰔ> 2 years ago her friend could’ve been arrested for thisѪѪѬѬYes officer,ĂĂ if I was going 40km/h faster I would've gotten a ticket.ĂÎ  ѪѪѬѬThat aside I do understand her thoughts,ĂĂ but I want her to understand our perspective too.ĂÎ", 'ⰎWolvesKeepYouWarm · 4yѪѪѬѬꚈⰔI don’t know the nature of your relationship but it is striking me as really uncomfortable that this woman who watched you grow up wanted to date you.ĂÎѪѪѬѬHave you ever had another gf before this?ÎÎ It’s a pretty big age difference for someone young like you.ĂÎ', "ꙂѢⰎKitchenBreakfast · 4yѪѪѬѬⰔof course I have,ĂĂ back in hs  ѪѪѬѬYeah it's a big age difference but it's not like it bothers me; I like her she likes me,ĂĂ *boom*  ѪѪѬѬSimple as that.ĂÎ", "ⰎSiren_of_Madness · 4y · edited 4yѪѪѬѬꚈⰔA 31 year old woman dating a 19 year old *boy* who is the *child* of a friend expecting everyone to be cool with the situation is delusional *at best* and is grooming you at *worst*.ĂÎ Either way,ĂĂ as a 41 year old woman sitting across from my 18 year old stepson RIGHT NOW - nothing good can come of this.ĂÎ ѪѪѬѬHave sex with her.ĂÎ Have fun with her.ĂÎ But let's not delude ourselves here.ĂÎ You're not capable of having a relationship with a 31 year old,ĂĂ and a 31 year old who *is* capable of having a relationship with a 19 year old is not mentally or emotionally stable.ĂÎ ѪѪѬѬ*Edit: typing while trying to shovel delicious chicken and rice into my mouth.ĂÎ", 'ꙂѢⰎwoodenhouses · 4yѪѪѬѬⰔUpvote for chicken and rice (and truths).ĂÎ']
  
  
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
            l = l.replace("Ⰾ","").replace("..","")
        if "Ѣ" in l:
            start = 60
            l = l.replace("Ѣ","").replace("..","")
        draw.text(((start), y_text), l.replace("&#x200B;","").replace("&nbsp;","").replace("..",""), font=font_type1, fill=color)
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
  
  v_lines = [x.replace("s it","crap").replace("f  k","screw").replace("w  re","member of the oldest profession").replace("s  t","promiscuous individual").replace("b  ch","female canine").replace("c  t","genitalia").replace("n    r","n word").replace("n   a","n word") for x in v_lines]

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
    if "Ⰾ" not in lines:
        response = polly_client.synthesize_speech(
          VoiceId='Joanna',
          OutputFormat='mp3',
          Engine = 'neural', 
          TextType = "ssml", 
          Text = f"<speak><prosody rate='80%'>{lines}</prosody></speak>")
    
        with open("SpeechFolder/speech3{}.mp3".format(round(i,1)), 'wb') as file:
          file.write(response['AudioStream'].read())
        i += 0.1
    else:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)#Voices
        engine.setProperty('rate', 130)#Tempo
        
        engine.save_to_file(" ", r"{}".format(cwd) + "/SpeechFolder/speech3{}.mp3".format(round(i,1)))
        engine.runAndWait()
        i += 0.1
        
        

  x = max(os.listdir(r"{}".format(cwd) + "/SpeechFolder"))
  os.remove(r"{}".format(cwd) + "/SpeechFolder/" + x)
  
  
  #Using "Wave" we are able to extract the time nessesary to read the line
  times = []
  for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    try:
        times.append(eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs)
    except:
        times.append(0)
        
  
  
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
      #if "speech3" in file:
        try:
            time = next(times) #Chose the next time 
        except:
            pass
        print(file)
        images = (ImageClip(path + "/" + file)
          .set_duration(time)                      #Sets the duration and the location of the images on screen
          .set_position((0.03,0.10), relative=True))
          
        part = video.subclip(s, s + time)  #Cuts the clip into subclips, using MATH
        s += time
    
        final = CompositeVideoClip([part, images])  #Overlay the images over each other
        clips.append(final)
     
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/SpeechFolder"):
    for file in files:
      try:
        if float(eyed3.load(os.path.join(root, file)).info.time_secs) == 0:
          os.remove(os.path.join(root, file)) 
      except:
          os.remove(os.path.join(root, file)) 
   
  for fname in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    shutil.copy2(r"{}".format(cwd) + "/SpeechFolder/" + fname, r"{}".format(cwd) + "/AudioFolder")
  
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