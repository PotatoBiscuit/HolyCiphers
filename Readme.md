## Holy Ciphers
This software was designed to find coincidental matches between languages via vigenere cipher and a user specified key. If you find interesting matches, don't read too deeply into it since it's most likely a coincidence, probably.

### Usage
It is recommended that you put the languages you want to feed into vigenere cipher in the "Start" folder, but you are free to specify which folder that is with flags. The same goes for the "Result" folder, which is used to check if the enciphered text matches any words in its languages.

Language files MUST follow the following format: [Language_Name].txt. Some examples of this are "English.txt" and "French.txt" which can be found in the repo.
```text
usage: HolyCiphers [-h] [-k ORIGINAL_KEY] [-l WORD_LENGTH_REQUIREMENT] [-s START_FOLDER] [-r--result-folder RESULT_FOLDER]

Tries to convert words from Start to random words in Result using vigenere cipher

options:
  -h, --help            show this help message and exit
  -k ORIGINAL_KEY, --key ORIGINAL_KEY
  -l WORD_LENGTH_REQUIREMENT, --min-length WORD_LENGTH_REQUIREMENT
  -s START_FOLDER, --start-folder START_FOLDER
  -r --result-folder RESULT_FOLDER
```

### Example Command
`python HolyCiphers.py -s Start -r Result -k holy -l 5`

#### Output
![](/home/lacksidaisical/Desktop/Ciphers/StandardOutput.jpg) 

### Wordlist Sources
[English Dictionary](https://github.com/dwyl/english-words) (converted to .txt for me)
[English Dictionary Original Source](https://web.archive.org/web/20131118073324/https://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable)
[Finnish Dictionary](https://github.com/pulmark/finnish-dictionary/tree/master)
[German Dictionary](https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4#file-wordlist-german-txt)
[French Dictionary](https://github.com/Vinetos/french-words-dictionary/tree/master?tab=readme-ov-file)
