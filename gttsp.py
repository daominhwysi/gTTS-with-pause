import os
from pathlib import Path
import random
import string
import shutil
from pydub import AudioSegment
import re
from gttsp import gTTS
def defolder(file_path):
 shutil.rmtree(str(file_path))
def mFolder(folder_path):
    folder_path = Path(folder_path)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
def count_files(folder_path):
    folder_path = Path(folder_path)
    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)
    return file_count
def random_char(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def gttswp(content :str ,pausetime :int):
    sentences = re.split(r'[!?.]+', content)
    filtered_array = []
    for i in sentences:
      if i.strip():
        filtered_array.append(i)
    foldername = random_char(50)
    folder_path = f'src/audio/temp/{foldername}'
    if os.path.exists(folder_path):
      print(f'Please try again!')
      op = [False]
      return op
    else:
      mFolder(folder_path)
      for i, word in enumerate(filtered_array):
        files = f'{folder_path}/file{i}.mp3'
        tts = gTTS(word , lang = 'vi')
        tts.save(files)
      filenum = count_files(folder_path)
      silence_seg = AudioSegment.silent(duration=1000*pausetime) 
    # Create an empty segment to store the final output
      output = AudioSegment.empty()
      for i in range(filenum):
        # Load the audio file
        filename = f"{folder_path}/file%d.mp3" % i
        segment = AudioSegment.from_file(filename)
        # Add the segment to the output
        output += segment + silence_seg
      defolder(folder_path)
      mFolder('src/audio/output')
      outputfile = str(random_char(20))
      outputpath = f"src/audio/output/{outputfile}.mp3"
      output.export(outputpath, format="mp3")
      op = [True,outputpath]
      return op
