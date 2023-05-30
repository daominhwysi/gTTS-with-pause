const gtts = require('gtts');
const fs = require('fs');
const data = fs.readFileSync('input.txt', 'utf8');
if (data == '') {
    console.log('Input Text in input.txt file')
}

const sentences = data.split(/[.?!]/g).filter(Boolean);

dotCount = sentences.length
console.log(dotCount)
dotCount++
let filenumber = 1

for (let sentence of sentences) {
    const gttsVoice = new gtts(sentence, 'vi');
     if ( dotCount > filenumber) {
      gttsVoice.save(`audio/ ${filenumber}.mp3`, function(err, result) {
        if (err) {
          console.log(err);
        }
      });
      console.log(`${filenumber}.mp3`)
      filenumber++;
    }
  }
const content = `${filenumber}`;
fs.writeFile('cache/filenumber.txt', content, err => {
  if (err) {
    console.error(err);
     return;
  }
  });
