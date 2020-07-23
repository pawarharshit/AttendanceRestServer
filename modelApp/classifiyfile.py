from .Crop_face_functions import read_img,find_faces,crop_face,showResult
from .Generate_Embeddings import loadmodel,generate_from_array

import tensorflow as tf

import mtcnn
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image
import numpy as np
import pandas as pd


from django.conf import settings
sixclassPath = os.path.join(settings.BASE_DIR,'modelApp','six_classifier.h5')
classifier = tf.keras.models.load_model(sixclassPath)
classes = ['anurag', 'harshit', 'pankaj', 'rajat', 'shelendra', 'vishnu']

def Classify_image(image_path,classifier = classifier):
    image = read_img(image_path)
    image_face = find_faces(image)
    cut_face = crop_face(image,image_face)
    embeddingPath = os.path.join(settings.BASE_DIR,'modelApp','facenet_keras.h5')
    embeddingModel = loadmodel(embeddingPath)
    embedding = generate_from_array(embeddingModel,cut_face)
    X = embedding.values
    y = classifier.predict(X)
    personidentified = []
    for i in y:
        if(max(i) > 0.80):
            personidentified.append([classes[np.argmax(i)],max(i)])
        else:
            personidentified.append(None)
    result = []
    for x,y in zip(image_face,personidentified):
        result.append([x,y])
    resultingImage = showResult(image,result)
    return  resultingImage,personidentified