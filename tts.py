from gtts import gTTS
import os
import re
from function.f88 import mFolder , mFile , clear , random_char , count_files , defolder
import configparser
import time
from pydub import AudioSegment

config = configparser.ConfigParser()
start = time.time()
config.read('config.ini')
clear()
print(' _____     __    __        ______     __   __   __   __    \n/\  __-.  /\ "-./  \      /\  ___\   /\ \ / /  /\ "-.\ \   \n\ \ \/\ \ \ \ \-./\ \     \ \  __\   \ \ \'/   \ \ \-.  \  \n \ \____-  \ \_\ \ \_\     \ \_____\  \ \__|    \ \_\\"\_\ \n  \/____/   \/_/  \/_/      \/_____/   \/_/      \/_/ \/_/ ')
mFile('input.txt','')
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')
if text == '':
 print('Input your text in input.txt')
else :
    delimiters = ".!?"
    NewText = re.split(f"[{delimiters}]", text)
    
    filtered_array = []
    for i in NewText:
        if i.strip():
            filtered_array.append(i)

    mFolder('audio')
    mFolder('audio/temp')
    foldername = random_char(10)
    folder_path = f'audio/temp/{foldername}'
    if os.path.exists(folder_path):
       print(f'Please try again!')
    else:
      outputfile = input('Name of output audio :')
      mFolder(folder_path)
      for i, word in enumerate(filtered_array):
        tts = gTTS(word, lang = config.get('Config', 'lang'))
        files = 'audio' + '/' + 'temp' + '/' + str(foldername) + '/' + 'file' + str(i) + ".mp3"
        tts.save(files)
        print(f"Created file: {files}")
      filenum = count_files(folder_path)
      breaktime = float(config.get('Config', 'breaktime'))
      silence_seg = AudioSegment.silent(duration=1000*breaktime) 
    # Create an empty segment to store the final output
      output = AudioSegment.empty()
      for i in range(filenum):
        # Load the audio file
        filename = f"{folder_path}/file%d.mp3" % i
        segment = AudioSegment.from_file(filename)
        
        # Add the segment to the output
        output += segment + silence_seg
      output.export(f"audio/{outputfile}.mp3", format="mp3")
    defolder(folder_path)
    print("\033[1;32mDone!\033[0m")
    end = time.time()
    print('[Finished in ' + str(round(end - start,2)) + ']')