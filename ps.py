from play_sounds import play_file
from pathlib import Path
from time import sleep
from function.f88 import count_files, clear
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

folder_name = input('Input Name of your audio folder: ')
filenum = count_files(f'audio/{folder_name}')
print(f'Found {filenum} audio files in {folder_name} folder!')

for i in range(filenum):
    try:
        file_path = Path(f"audio/{folder_name}/file{i}.mp3")
        play_file(file_path)
        sleep(int(config.get('Config', 'breaktime')))
    except Exception as e:
        print(f'Error playing file{i}.mp3: {str(e)}')
    else:
        print(f'Successfully played file{i}.mp3!')

print("\033[1;32mDone!\033[0m")
