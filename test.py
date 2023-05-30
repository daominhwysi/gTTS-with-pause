from play_sounds import play_file
from pathlib import Path
from time import sleep

with open('cache/filenumber.txt', 'r') as file:
    data = file.read()
    print(data)
i = int(data)
filename = 1
while filename < i:
    file_path = Path(f"audio/ {filename}.mp3")
    play_file(file_path)
    sleep(3) 
    filename += 1

print('Finished!')
    