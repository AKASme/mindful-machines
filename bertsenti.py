import torch
from transformers import pipeline
from PIL import Image
import easyocr as ocr #because pytesseract is super annoying to use
import pyautogui as gui
import keyboard as k #because pyautogui can type but can't detect if a key is pressed????
import time
pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")
reader = ocr.Reader(["en"])
print("started")
while True:
    if k.is_pressed("enter"):
            print("enter pressed")
            time.sleep(1)
            gui.screenshot("hi.png", region=(758, 900, 410, 68))
            text = reader.readtext("hi.png")
            print(text)
            e = pipe(text[0][-2]) #the reader return value is its bounding boxes, then the text, then its confidence
            print(e)
            if e[0]["label"] == "NEG":
                gui.alert("harmful intentions detected. sending torpedo now.")
    if k.is_pressed("`"):
        break

"""
This is the license for Google's BERT model.

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
