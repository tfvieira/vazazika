# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 08:24:18 2017

@author: tvieira
"""

"""
Write or load a classification model into a file
"""
from keras.models import model_from_json

def class2json(classifier, filename = "classifier"):
    """Write a classification model into a JSON file"""
    model_json = classifier.to_json()
    with open(filename + ".json", "w") as json_file:
        json_file.write(model_json)
    # Serialize weights to HDF5
    classifier.save_weights(filename + ".h5")
    print("Successfully saved the classifier to file " + filename + ".")

def json2class(filename = "classifier"):
    """Load a classification model from a JSON file"""
    json_file = open(filename + ".json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # Load weights into new model
    loaded_model.load_weights(filename + ".h5")
    print("Loaded model from disk.")
    return loaded_model
