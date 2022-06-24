#!/usr/bin/env python
# coding: utf-8

# In[7]:



#%matplotlib inline
#%precision %.2f






import pickle
# keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json


# In[4]:

def model_Predict(comment):
    # load json and create model
    json_file = open('model_lstm.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model_lstm.h5")
    print("Loaded model from disk")
    
    
    # In[17]:
    
    
    
    # Set Maximum number of words to be embedded
    NUM_WORDS = 20000
    
    # Define/Load Tokenize text function
    tokenizer = Tokenizer(num_words=NUM_WORDS,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\'',
                          lower=True)
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    
    # In[24]:
    
    
    t=comment
    text =[t]
    sequences_text = tokenizer.texts_to_sequences(text)
    text = pad_sequences(sequences_text,maxlen=50)
    prediction = loaded_model.predict(text)
    return(prediction)
    
#model_Predict("wefg")