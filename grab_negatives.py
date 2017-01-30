import requests
import requests.exceptions
import cv2
import numpy as np
import os, shutil

DEST="negativas/"
INFO_FILE="negativas.txt"
W=50
H=50
RESET=True


lista_url ={
    "animal": "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00015388",
    "landscape": "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09287968",
    "flora": "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00017222",
    "food": "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00021265",
    "ingredient": "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07809096"
}

class ResizeError(Exception):
    pass


def save_file_to_disk(url, dest):
    r = requests.get(url, stream=True, timeout=1)
    if r.status_code == 200:
        with open(dest, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f) 

def delete_file_from_disk(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def resize_image(path, w, h):
    try:
        img = cv2.imread(path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
    # should be larger than samples / pos pic (so we can place our image on it)
        resized_image = cv2.resize(img, (w, h))
        cv2.imwrite(path,resized_image)
    except Exception as er:
        raise ResizeError()


def count_current_files(dest):
    return len(os.listdir(dest))    


def get_urls(url):
    return requests.get(url).text

def reset_destination(dest, info_file):
    if os.path.exists(dest):
        shutil.rmtree(dest) 

    os.makedirs(dest)
    with open(info_file, "w") as f:
        f.write("")
        f.close()

def process_files(dest, files, w, h, numeral, info_file, prefijo):
    if numeral == 0:
        return true
    file_name = dest + prefijo + str(numeral) + ".jpg"
    try:
        save_file_to_disk(files[numeral], file_name)
        resize_image(file_name, w, h) 
        append_to_info(file_name, info_file)
    except RuntimeError:
        return True

    except ResizeError as e1:
        delete_file_from_disk(file_name)
    except KeyboardInterrupt:
        raise
    except Exception:
        pass
    return process_files(dest, files, w, h, numeral - 1, info_file, prefijo)

def append_to_info(file_name, info_file):
    with open(info_file, "a") as f:
        f.write(file_name + "\n")
        f.close()

  
def extract_files(origin, dest, w, h, info_file):
    print origin
    prefijo = origin[0]
    url = origin[1]
    print("Trabajamos con el prefijo: %s en la url: %s" % (prefijo, url))
    files = get_urls(url).split('\n')
    process_files(dest, files, w, h, len(files) - 1, info_file, prefijo)
    
def store_raw_images(url, dest, w, h, reset, info_file):
    neg_image_urls = get_urls(url)
    

    if reset: 
        reset_destination(dest, info_file)

    map(lambda origin: extract_files(origin, dest, w, h, info_file), lista_url.iteritems())
 
        

store_raw_images(URL, DEST, W, H, RESET, INFO_FILE)
