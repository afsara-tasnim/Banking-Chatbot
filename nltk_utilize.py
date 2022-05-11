import nltk
import tflearn
import pickle
import numpy
import json
import random
from tensorflow.python.framework import ops
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Word Lemmatizer
from nltk.stem import WordNetLemmatizer
lemmetizer = WordNetLemmatizer()


#importing Json file
with open('janata.json') as file:
  data = json.load(file)


#Cleaning and sorting data for training and testing
try:
  with open("data.pickle","rb") as f:
    words,labels,training,output = pickle.load(f)
except:
  words = []
  labels = []
  ignore_words = ["?",".",",","/","&","!","'","$"]
  doc_x= []
  doc_y = []

  for intent in data["intents"]:
    for pattern in intent["patterns"]:
      word = nltk.word_tokenize(pattern)
      words.extend(word)
      doc_x.append(word)
      doc_y.append(intent["tag"])

      if intent["tag"] not in labels:
        labels.append(intent["tag"])

  words = [lemmetizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
  words = sorted(list(set(words)))
  labels= sorted(labels)

  training = []
  output = []
  out_empty = [0 for _ in range(len(labels))]


  for x, doc in enumerate(doc_x):
    bag = []
    wrds = [lemmetizer.lemmatize(w) for w in doc]

    for w in words:
      if w in wrds:
        bag.append(1)
      else:
        bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(doc_y[x])] = 1

    training.append(bag)
    output.append(output_row)


  training = numpy.array(training)
  output = numpy.array(output)

  with open("data.pickle","wb") as f:
    pickle.dump((words,labels,training,output), f)


#mute after One run
# words = []
# labels = []
# ignore_words = ["?", ".", ",", "/", "&", "!", "'", "$"]
# doc_x = []
# doc_y = []
#
# for intent in data["intents"]:
#   for pattern in intent["patterns"]:
#     word = nltk.word_tokenize(pattern)
#     words.extend(word)
#     doc_x.append(word)
#     doc_y.append(intent["tag"])
#
#     if intent["tag"] not in labels:
#       labels.append(intent["tag"])
#
# words = [lemmetizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
# words = sorted(list(set(words)))
# labels = sorted(labels)
#
# training = []
# output = []
# out_empty = [0 for _ in range(len(labels))]
#
# for x, doc in enumerate(doc_x):
#   bag = []
#   wrds = [lemmetizer.lemmatize(w) for w in doc]
#
#   for w in words:
#     if w in wrds:
#       bag.append(1)
#     else:
#       bag.append(0)
#
#   output_row = out_empty[:]
#   output_row[labels.index(doc_y[x])] = 1
#
#   training.append(bag)
#   output.append(output_row)
#
# training = numpy.array(training)
# output = numpy.array(output)