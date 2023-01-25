import os 
from install import install_all

cwd = os.getcwd() 

folders = ["ImageFolder","SpeechFolder","VideoFolder","AudioFolder"]

path = str(cwd) + "/"
for folder in folders:
  if not os.path.exists(r"{}{}".format(path, folder)):
    os.makedirs(r"{}{}".format(path, folder))