import tensorflow as tf
import numpy as np
import cv2

# load AI model
model = tf.keras.models.load_model("skin_model.h5")

labels = ["Dry Skin", "Normal Skin", "Oily Skin"]


def predict_skin(image_path):

    img = cv2.imread(image_path)

    img = cv2.resize(img, (224,224))
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    class_id = np.argmax(prediction)

    confidence = prediction[0][class_id]

    skin_type = labels[class_id]

    return skin_type, confidence
