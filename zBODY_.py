from moviepy.editor import *
from keys import *
import pyttsx3, os, textwrap, random, boto3, eyed3, shutil
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

#With some experience in this situation I can give you some advice---Occasionally reddit gives you hope that there are others out there just like you---How about some friends? How about your friends? Just help her make some friends first---How about some friends? How about your friends? Just help her make some friends first


def body():
      
  cwd = os.getcwd()
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/ImageFolder"):
    for file in files:
      os.remove(os.path.join(root, file))        
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/SpeechFolder"):
    for file in files:
      if "speech2" in file:
        os.remove(os.path.join(root, file))  

    
  polly_client = boto3.Session(
    aws_access_key_id=id(),
    aws_secret_access_key=key(),
    region_name=region_name()).client(client())


  video = VideoFileClip(r"{}".format(cwd) + "/bac.mp4") 

  l = [*range(0,920,20)]
  random.shuffle(l)
  a = [*range(46)]
  random.shuffle(a)
  number = l[a[3]]

  video = video.subclip(number, int(video.duration))


  wid = int(video.w-video.w*0.06)
  heig = int(video.h-video.h*0.20)
  image = Image.new(mode="RGB", size=(wid, heig), color = "#1a1a1b")
  draw = ImageDraw.Draw(image)
  image.putalpha(0)

  #Drawing the rest of the text
  y_text = 0
  height = int(video.h/30)
  color = "#D7DADC"#(239, 239, 237, 1)
  path = r"{}".format(cwd)
  location = os.path.join(path, "Verdana.ttf")
  font_type1 = ImageFont.truetype(location , int(video.h/30))
  i = 0.1
  
  bannedWords = pd.read_csv("bannedwords.csv")
  
  with open("text.txt", "r") as text:
    text_commen = text.read()  

  text_comment = text_commen
  individual_words = text_comment.split(" ")
  for word in individual_words:
    for badWord in bannedWords["Banned Word"].tolist():
      if word.upper() == badWord:
        index = (bannedWords.index[bannedWords["Banned Word"] == word.upper()].tolist())[0]
        text_comment = (text_comment.replace(word, bannedWords["Replacement"][index]))

  body_text = []
  words_n_stuff = text_comment.replace("&#x200B;","").replace("&nbsp;","")
  words_n_stuff = words_n_stuff.split("...")
  words_n_stuff = [x.split("..") for x in words_n_stuff]
  words_n_stuff = [[y.replace("\n\n","ѪѪѬѬ").replace(",",',ĂĂ').replace(".",".ĂÎ").replace("?","?ÎÎ").replace("<3","") for y in x] for x in words_n_stuff]
  words_n_stuff = ["..ĂÎ".join(x) for x in words_n_stuff]
  words_n_stuff = "...ĂÎ".join(words_n_stuff)
  
  
  body_text.append(words_n_stuff.replace("\n"," "))


  body_text = [x.split("ĂĂ") for x in body_text]
  body_text = [y for x in body_text for y in x]
  body_text = [x.split("ĂÎ") for x in body_text]
  body_text = [y for x in body_text for y in x]
  body_text = [x.split("ÎÎ") for x in body_text]
  body_text = [[x] if "..." in x else x for x in body_text]
  body_text = [y.strip() for x in body_text for y in x]
  
  v_lines = []
  v_lines = body_text

  nr = 0
  s = ""
  text3 = []
  
  nr = 0
  for x in body_text:
    nr += len(x)
    if "ѪѪѬѬ" in x:
      a = sum([1 for y in x if "ѪѪѬѬ" in y])
      nr += a * 90
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
  
  e_lines2.append("Ѩ")
  e_lines2.append("")
  e_lines2.append("Ѧ")
  
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
        
  y_text = 0
  i4 = 0.1
  start = 20 
  for lines in b: 
    for l in lines:
      if "Ѣ" in l:
        start = 60
        l = l.replace("Ѣ","")
      draw.text(((start), y_text), l, font=font_type1, fill=color)
      y_text += height*1.3
    cropped = image.crop((0,0,image.width, y_text + 8))
    y_text = 0
    cropped.save(r"{}".format(cwd) + "/ImageFolder" + "/{}.png".format(round(i4, 1)), 'PNG')
    image = Image.new(mode="RGB", size=(wid, heig), color = "#1a1a1b")
    draw = ImageDraw.Draw(image)
    image.putalpha(0)
    i4 += 0.1
              
  #Starting the naration and length of the video part
  
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)#Voices
  engine.setProperty('rate', 130)#Tempo
  
  v_lines = [x.replace("s it","crap").replace("f  k","screw").replace("f  king","").replace("screwing","").replace("w  re","dor").replace("s  t","bat").replace("b  ch","grinch").replace("c  t","runt").replace("n    r","n word").replace("n   a","n word") for x in v_lines]
  v_lines = [x.replace("ѪѪѬѬ","").replace("\n"," ").replace('[M'," male").replace('M]'," male").replace('[F'," female").replace('F]'," female").replace('(M'," male").replace('M)'," male").replace('(F'," female").replace('F)'," female") for x in v_lines]
  v_lines.append("Now Let's go onto the comments")
  v_lines.append(" ")
  if "" in v_lines:
    v_lines.remove("")
  if " " in v_lines:
    v_lines.remove(" ")
  
  
  
  i = 0.1
  for lines in v_lines:
    print(lines)
    if len(lines) != 0:
      response = polly_client.synthesize_speech(
        VoiceId='Joanna',
        OutputFormat='mp3',
        Engine = 'neural', 
        TextType = "ssml", 
        Text = f"<speak><prosody rate='80%'>{lines}</prosody></speak>")
  
      with open("SpeechFolder/speech2{}.wav".format(round(i,1)), 'wb') as file:
        file.write(response['AudioStream'].read())
      i += 0.1
    elif len(lines) == 0:
      engine.save_to_file(lines, r"{}".format(cwd) + "/SpeechFolder/speech2{}.wav".format(round(i,1)))
      engine.runAndWait()
      i += 0.1
      

 
  for fname in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    shutil.copy2(r"{}".format(cwd) + "/SpeechFolder/" + fname, r"{}".format(cwd) + "/AudioFolder")
  
  times = []
  for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    if "speech2" in x:
      times.append(eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs)
  
  """clips = []
  for x in os.listdir(r"{}".format(cwd) + "/SpeechFolder"):
    time = eyed3.load(r"{}".format(cwd) + "/SpeechFolder/" + x).info.time_secs
    if time != 0:
      clip = AudioFileClip(r"{}".format(cwd) + "/SpeechFolder/" + x)
      clips.append(clip)
    
  speech = concatenate_audioclips(clips)
  back_music = AudioFileClip(r"{}".format(cwd) + "/reddit-music.mp3")
  back_music = back_music.subclip(0, float(speech.duration+0.1))"""
  
  #final_clip = CompositeAudioClip([speech, back_music])

  
  #The movie proces
  path = r"{}".format(cwd) + "/ImageFolder"
  s = 0
  clips = []
  times = iter(times)  # turn the list into an iterator
  for file in os.listdir(path): #Loop through the files in the folder
    f = os.path.join(path, file)
    if os.path.isfile(f):
      try:
        time = next(times) #Chose the next time 
      except:
        time = 0
      print(file)
      images = (ImageClip(path + "/" + file)
        .set_duration(time)                      #Sets the duration and the location of the images on screen
        .set_position((0.03,0.10), relative=True))
        
      part = video.subclip(s, s + time)  #Cuts the clip into subclips, using MATH
      s += time
  
      final = CompositeVideoClip([part, images])  #Overlay the images over each other
      clips.append(final)
  
  video_clip = concatenate_videoclips(clips, method='chain')
  video_clip.write_videofile(r"{}".format(cwd) + "/VideoFolder/video_i2.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
  #.set_audio(final_clip)
            
body()