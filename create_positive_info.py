import requests
import cv2
import numpy as np
import os, shutil

DEST="positivas/"
W=50
H=50
INFO_FILE="positivas.txt"

def get_files(path):
    return os.listdir(path)


def show(str):
    print str


def resize_file(path, file, w, h):
    
    file_name = path + file
    img = cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)
    # should be larger than samples / pos pic (so we can place our image on it)
    resized_image = cv2.resize(img, (w, h))
    cv2.imwrite(file_name,resized_image)
    return file_name


def append_to_info(file_name, info_file):
    with open(info_file, "a") as f:
        f.write(file_name + " 1 0 0 50 50\n")
        f.close()

def delete_info_file(info_file):
    os.unlink(info_file)


def create_positive_info(info_file, path, w, h):
    try:
        delete_info_file(info_file)
    except:
        pass
    files = get_files(path)
    map(lambda file: append_to_info(resize_file(path, file, w, h), info_file), files)

create_positive_info(INFO_FILE, DEST, W, H)
