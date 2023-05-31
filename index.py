from play_sounds import play_file
from pathlib import Path
from time import sleep

fileopen = input('Input Sequence number of your audio folder :')
with open('cache/.cache', 'r') as f:
    data = f.readline().strip()
    print(data)
i = int(data)
filename = 1
while filename < i:
    file_path = Path(f"audio/ {fileopen}/ {filename}.mp3")
    play_file(file_path)
    sleep(5)
    filename += 1
print('Finished!')