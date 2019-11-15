# ImageWatermarker  ![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103) ![version](https://img.shields.io/badge/Version-0.0.1-red)
___

A small GUI to use for watermarking your images. It is done in batch. The GUI is build with PyQt5 and Pillow. For the project structure I used fbs. 

Tested and working with python3.6

When tested on windows the proportions set in the ui change and have to be adapted to personal preference.

___

_My advice is to use a virtual environment_
```
python3.6 -m venv venv
. venv/bin/activate
```

Usage:
```
pip install -r requirements/base.txt
fbs run
```

To make the app a executabele do `fbs freeze`.

if you want to create a installer for your OS (macOS/Windows/Linux) `fbs installer`, important to note is that the app first has to be frozen.