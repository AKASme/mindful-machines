import torch
from transformers import pipeline
import csv


pipe = pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")

with open("testdata.csv", newline="") as testdata:
    with open("results.csv", "w+", newline="") as results:
        reader = csv.reader(testdata)
        reswriter = csv.writer(results)
        reswriter.writerow(["Prompt", "Correct", "Result", "Score"])
        for row in reader:
            prompt = row[0]
            correct = row[1]
            result = pipe(prompt)[0]
            reswriter.writerow([prompt, correct, result["label"], result["score"]])

        #row[0]: prompt
        #pipe(row[0])[0]: the dictionary (because for some reason pipe() returns a dict in a list)
        


#print(pipe("what's your name?"))