# -*- coding:utf-8 -*-
from tkinter import *
from keys import *
from pathlib import Path
from moviepy.editor import *
import praw, pendulum, os
import pandas as pd
from PIL import Image, ImageTk
from praw.models import MoreComments



def click():
      
  cwd = os.getcwd()

  link = textentry.get()
  parts = textentry2.get()
  
  reddit = praw.Reddit(
        client_id=reddit_id(),
        client_secret=reddit_secret(),
        user_agent=user_agent(),
        username=user_agent(),
        password=password(),
    )
  submission = reddit.submission(url=link)

  
  comments = []
  comment_parts = parts.split("---")
  
  submissions = [x for x in submission.comments.list() if not isinstance(x, MoreComments)]
  
  for comment in comment_parts:
      comments.append([id for id in submissions if comment in id.body])
  
  comments = [y.id for x in comments for y in x]
  

  #Deleting everything in the folders we used
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/ImageFolder"):
      for file in files:
          os.remove(os.path.join(root, file))
          
  for root, dirs, files in os.walk(r"{}".format(cwd) + "/SpeechFolder"):
      for file in files:
          os.remove(os.path.join(root, file))

  
  Y = 0
  body_text = []
  while Y < len(comments):  
    words_n_stuff = ''
    chosen_comment = reddit.comment(comments[Y])
    creation_date = ((pendulum.from_timestamp(chosen_comment.created).diff_for_humans()).replace("years ago", "y").replace("year ago","y").replace("months ago","m").replace("month ago","m").replace("hours ago","h").replace("day ago","d").replace("days ago","d").replace("hour ago","h").replace(" ",""))
    edited_date = ("edited" + " " + (pendulum.from_timestamp(chosen_comment.edited).diff_for_humans()).replace("years ago", "y").replace("year ago","y").replace("months ago","m").replace("month ago","m").replace("hours ago","h").replace("day ago","d").replace("days ago","d").replace("hour ago","h").replace(" ",""))
    nr = int((pendulum.from_timestamp(chosen_comment.edited).diff_for_humans()).replace("years ago", "").replace("year ago","").replace("months ago","").replace("month ago","").replace("hours ago","").replace("day ago","").replace("days ago","").replace("hour ago","").replace(" ",""))
    
    if nr > 48 and "t3" in chosen_comment.parent_id:
      words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date}\n\nꚈⰔ{chosen_comment.body}"
    elif nr > 48 and "t1" in chosen_comment.parent_id:
      words_n_stuff = f"ꙂѢⰎ{chosen_comment.author} · {creation_date}\n\nⰔ{chosen_comment.body}"
    elif nr > 48:
      words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date}\n\nⰔ{chosen_comment.body}"
    elif nr < 48 and "t3" in chosen_comment.parent_id:
      words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date} · {edited_date}\n\nꚈⰔ{chosen_comment.body}"
    elif nr < 48 and "t1" in chosen_comment.parent_id:
      words_n_stuff = f"ꙂѢⰎ{chosen_comment.author} · {creation_date} · {edited_date}\n\nⰔ{chosen_comment.body}"
    elif nr < 48:
      words_n_stuff = f"Ⰾ{chosen_comment.author} · {creation_date} · {edited_date}\n\nⰔ{chosen_comment.body}"
    
    if words_n_stuff[-1] != ".":
      words_n_stuff = words_n_stuff + "."
    
    bannedWords = pd.read_csv("bannedwords.csv")
  
    text_comment = words_n_stuff
    individual_words = text_comment.split(" ")
    for word in individual_words:
      for badWord in bannedWords["Banned Word"].tolist():
        if word.upper() == badWord.replace("*",""):
          index = (bannedWords.index[bannedWords["Banned Word"] == word.upper()].tolist())[0]
          words_n_stuff = (text_comment.replace(word, bannedWords["Replacement"][index]))
    
    words_n_stuff = words_n_stuff.split("...")
    words_n_stuff = [x.split("..") for x in words_n_stuff]
    words_n_stuff = [[y.replace("\n\n","ѪѪѬѬ").replace("\n","\n\n").replace(". .",".").replace("\n\n","ѪѪѬѬ").replace(",",',ĂĂ').replace(".",".ĂÎ").replace("?","?ÎÎ").replace("shit","s it").replace("SHIT","s it") for y in x] for x in words_n_stuff]
    words_n_stuff = ["..ĂÎ".join(x) for x in words_n_stuff]
    words_n_stuff = "...ĂÎ".join(words_n_stuff)
    
    body_text.append(words_n_stuff)
     
    Y+=1
  
  print(body_text)
  
  body_text = [x.split("ĂĂ") for x in body_text]
  body_text = [y for x in body_text for y in x]
  body_text = [x.split("ĂÎ") for x in body_text]
  body_text = [y for x in body_text for y in x]
  body_text = [x.split("ÎÎ") for x in body_text]
  body_text = [[x] if "..." in x else x for x in body_text]
  
  
  body_text = [y.strip() for x in body_text for y in x]
  
  body_text = [x.replace("Ⱄ","") for x in body_text]
  
  for a in body_text:
    print("")
    print(a)
        
  
#The fact that a 28 year old married man is telling a 16 year old girl he loves her should be reason enough already.---Or he's consciously manipulating the 16yo, perhaps? That's what I expected, anyway, that he was---could very well be. Too bad it doesn't make the situation any better for OP.---I have so much secondhand rage right now. Time for me to get off the internet.---I seriously want to choke her husband.---If your husband and his best friend think a 16 year old girl is "mature for her age" neither of them---I wish I could give you more than one upvote.

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
