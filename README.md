# gTTS w/ pause 

**gTTS with pause** is a project designed to add custom pauses to a paragraph by using the split method, convert text to speech using gTTS (Google Text to Speech), and concatenate audio.

## Usage

This project is a Discord application, so you need a bot token to run it. After obtaining the token from the Discord Developer Portal, add it to the .```env.example``` file and rename the file to ```.env``` .

```
TOKEN = your-bot-token-here
```
Dont forget to Install FFmpeg because it used for concatenate
<br></br>
    [![<LABEL>](https://img.shields.io/static/v1?label=FFmpeg&message=Download&color=<COLOR>)](<https://ffmpeg.org/>)
<br></br>


Finally, run the src/main.py file and you're Done

### Usage 2 
If don't want use Discord Application you also can 
clone this [gits](https://gist.github.com/DaQMinh/5765340543a7fdb1550433a4ed196dd2) by 
```
git clone https://gist.github.com/5765340543a7fdb1550433a4ed196dd2.git
```
And import it into your project
### Disclaimer

This project is *not* affiliated with Google or Google Cloud. Breaking upstream changes *can* occur without notice. This project is leveraging the undocumented [Google Translate](https://translate.google.com) speech functionality and is *different* from [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

