import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('flaskapp/cardiobot_model.h5') #loading already saved model
import json
import random

data = json.loads(open('flaskapp/intents.json').read())
words = pickle.load(open('flaskapp/words.pkl','rb'))
labels = pickle.load(open('flaskapp/labels.pkl','rb'))

#tokenizing and lemmatizing the sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

#returns a bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # creating a bag of words
    bag = [0]*len(words) #initializing all the values to zero initially
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assigning 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

#uses the trained model to predict the most probable label
def predict_label(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    #sorting by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": labels[r[0]], "probability": str(r[1])})
    return return_list

#once the tag is succesfully predicted, printing a random response associated to that tag
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(text):
    ints = predict_label(text, model)
    res = getResponse(ints, data)
    return res


#Start talking to Cardiobot
# x = None
# print("\nStart talking to Cardiobot!(Type quit to stop)")

# while True:
#     x = input("You: ")
#     if x.lower() == "quit":
#         break

#     else:
#         print("Cardiobot: " + chatbot_response(x))
