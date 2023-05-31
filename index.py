from play_sounds import play_file
from pathlib import Path
from time import sleep

fileopen = input('Input Sequence number of your audio folder :')
with open('cache/.cache', 'r') as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    print(line1)
i = int(line1)
l3 = int(line3)
filename = 1
while filename < i:
    file_path = Path(f"audio/ {fileopen}/ {filename}.mp3")
    play_file(file_path)
    sleep(l3)
    filename += 1
print('Finished!')