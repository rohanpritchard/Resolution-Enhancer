from __future__ import division
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import random


def show_image(img):
    if len(img) == 64:
        new = []
        for i in range(8):
            new.append(img[8*i:8*(i+1)])
        img = new
    plt.gray()
    plt.matshow(img)
    plt.show()

def gen_random():
    grid = []
    for _ in range(64):
            grid.append(random.randint(0, 16))
    return grid

clf = MLPClassifier()

digits = load_digits()

Xtrain = list(digits.data[::2])
Ytrain = [1] * (len(digits.data)//2 + 1)
Xtest = list(digits.data[1::2])
Ytest = [1] * (len(digits.data)//2 + 1)

show_image(Xtest[898])

for _ in range(len(digits.data)//2):
    Xtrain.append(gen_random())
    Xtest.append(gen_random())
    Ytrain.append(0)
    Ytest.append(0)

clf.fit(Xtrain,Ytrain)


# Predict test data
results = clf.predict(Xtest)
answers = Ytest

# Compare results
guessAnswerPair = zip(results, answers)
correct = 0
total = 0
for i, (guess, answer) in enumerate(guessAnswerPair):
    if guess==answer:
        correct+=1
    else:
        show_image(Xtest[i])
        print(i)
        if guess == 1: print("Thought it was a digit.")
        else: print("Thought it wasn't a digit.")
    total+=1

print "Correctly identified %s out of %s data points. Success rate of: %s." % (correct, total, round(correct/total, 3))


