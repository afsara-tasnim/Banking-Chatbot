import nltk
import pickle
import numpy as np
import json
import random
from nltk_utilize import lemmetizer
from nltk_utilize import words
from nltk_utilize import labels, data
from train import model


#Converting words into arrays
def bag_of_words(s, wds):
  stake = [0 for _ in range(len(wds))]

  s_words= nltk.word_tokenize(s)
  s_words = [lemmetizer.lemmatize(wds.lower()) for wds in s_words]

  for se in s_words:
    for i, w in enumerate(words):
      if w == se:
        stake[i] = 1

  return np.array(stake)

bot_name ="Jetbot"


#Using clients texts to predict the best response
def chat_tflearn(msg):
  inp=msg
  results = model.predict([bag_of_words(inp, words)])
  result_index = np.argmax(results)
  ints = labels[result_index]
  tag = ints

  for tg in data["intents"]:
    if tg['tag'] == tag:
      response = tg['responses']
  return random.choice(response)
