import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import random
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

#reading the intents file
x = open('flaskapp/intents.json').read()
data = json.loads(x)


words=[]
labels = []
docs = []
ignore_words = ['?', '!','.']

#tokenizing the words and appening into the list
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append((wrds, intent['tag']))

    if intent["tag"] not in labels:
        labels.append(intent["tag"])


#lemmaztizing, converting into lowercase words and removing duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

labels = sorted(list(set(labels)))

pickle.dump(words,open('flaskapp/words.pkl','wb'))
pickle.dump(labels,open('flaskapp/labels.pkl','wb'))

#creating our training data

training = []
output_empty = [0] * len(labels) # creating an empty list and initializing to 0 for our output

#training set, bag of words for each sentence
for doc in docs:
    #initializing our bag of words
    bag = []
    pattern_words = doc[0]
    #lemmatizing each word (create base or similar word) in order to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    #print(pattern_words)

    #creating our bag of words list with value 1 if word match found in current pattern else 0
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    #output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[labels.index(doc[1])] = 1
    training.append([bag, output_row])

#shuffling our features and turning into numpy array
random.shuffle(training)
training = np.array(training)

#creating train and test lists. x is the patterns and y is intents
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Training data created")

#Building the model
#It consists of 3 layers. First layer has 128 neurons, second layer has 64 neurons and
#3rd which is the output layer contains number of neurons equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

#Compiling model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#fitting and saving the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('flaskapp/cardiobot_model.h5', hist)
print("model created")
