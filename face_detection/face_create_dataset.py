import cv2
import os

casscade = "haarcascade_frontalface_default.xml"
cap = cv2.VideoCapture(0)
dataset_path= "dataset/"

if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

id = 0
