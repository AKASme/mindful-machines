import torch
from transformers import pipeline
from PIL import Image
import pytesseract
import pyautogui as gui
import keyboard as k #because pyautogui can type but can't detect if a key is pressed????

pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\cheng\AppData\Local\Programs\Python\Python312\Lib\site-packages\pytesseract'
#yes i have just exposed a portion of my computer's files. do i care? no. none of these matter
while True:
    if k.is_pressed("enter"):
            image = gui.screenshot("hi.png", region=(355, 735, 620, 430))
            text = pytesseract.image_to_string("hi.png")
            e = pipe("text")
            if e["label"] == "NEG":
                gui.alert("harmful intentions detected. sending torpedo now.")
    if k.is_pressed("`"):
        break

"""
MIT License

Copyright (c) 2020-2021 VinAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""