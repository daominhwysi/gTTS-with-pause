from gtts import gTTS
from io import BytesIO
import os
from play_sounds import play_file
from pathlib import Path
import re
from function.f88 import mFolder , mFile , clear
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
clear()

print(' _____     __    __        ______     __   __   __   __    \n/\  __-.  /\ "-./  \      /\  ___\   /\ \ / /  /\ "-.\ \   \n\ \ \/\ \ \ \ \-./\ \     \ \  __\   \ \ \'/   \ \ \-.  \  \n \ \____-  \ \_\ \ \_\     \ \_____\  \ \__|    \ \_\\"\_\ \n  \/____/   \/_/  \/_/      \/_____/   \/_/      \/_/ \/_/ ')
file_path = Path('input.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')
if text == '':
 print('Input your text in input.txt')
else :
    print(f'\033[32;1m[1] Write Audio File\n[2] Playing Sound Directly\033[0m')
    options = int(input('Input your option :'))
    delimiters = ".!?"
    NewText = re.split(f"[{delimiters}]", text)
    
    filtered_array = []
    for i in NewText:
        if i.strip():
            filtered_array.append(i)

    if options == 1:
     clear()
     foldername = input('Input Folder Name :')
     clear()
     mFolder('audio')
     if os.path.exists(f'audio/{foldername}'):
       print(f'Folder {foldername} have already existed!')
     else:
      mFolder(f'audio/{foldername}')
      for i, word in enumerate(filtered_array):
        tts = gTTS(word, lang = config.get('Config', 'lang'))
        files = 'audio' + '/' + str(foldername) + '/' + 'file' + str(i) + ".mp3"
        tts.save(files)
        print(f"Created file: {files}")
      print("\033[1;32mDone!\033[0m")
    elif options == 2:
     clear()
    else:
      print('Invalid option')