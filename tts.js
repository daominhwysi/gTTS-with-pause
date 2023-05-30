const gtts = require('gtts');
const fs = require('fs');
const { lang } = require('./config.json');

const cache = fs.readFileSync('cache/.cache', 'utf8').split('\n');
var line2 = cache[1];

const data = fs.readFileSync('input.txt', 'utf8');
if (data == '') {
    console.log('Input Text in input.txt file')
}

const sentences = data.split(/[.?!]/g).filter(Boolean);
dotCount = sentences.length
dotCount++
let fileCount = 1
if (line2 == undefined){
  fs.mkdir('./audio/0', { recursive: true }, (err) => {
    if (err) throw err;
  });  
} else {
  line2++
  fs.mkdir(`./audio/ ${line2}`, { recursive: true }, (err) => {
    if (err) throw err;
  });  
}
for (let sentence of sentences) {
    const gttsVoice = new gtts(sentence, `${lang}`);
     if ( dotCount > fileCount) {
      if (line2 == undefined) {
      gttsVoice.save(`audio/0/ ${fileCount}.mp3`, function(err, result) {
        if (err) {
          console.log(err);
        }
      })} else {
        gttsVoice.save(`audio/ ${line2}/ ${fileCount}.mp3`, function(err, result) {
          if (err) {
            console.log(err);
          }
        })
      }
      console.log(`${fileCount}.mp3`)
      fileCount++;
    }
  }

if (line2 == undefined){
  let content = `${fileCount}\n0`
  fs.writeFile('cache/.cache', content, err => {
    if (err) {
      console.error(err);
       return;
    }
    });
} else {
  var line2 = Number(line2)
  let content = `${fileCount}\n${line2}`
  fs.writeFile('cache/.cache', content, err => {
    if (err) {
      console.error(err);
       return;
    }
    });  
}