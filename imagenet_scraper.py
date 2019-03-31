#code part 1
from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import PIL.Image
import urllib

IMAGENET_SYSNETS = {"goldfish, Carassius auratus": "n01443537",
                    "great white shark, white shark, man-eater, man-eating shark, Carcharodon carcharias": "n01484850",
                    "monarch, monarch butterfly, milkweed butterfly, Danaus plexippus": "n02279972"
                   }

def get_imagenet_urls_from_sysnet(sysnet):
    page = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={}".format(sysnet))
    soup = BeautifulSoup(page.content, 'html.parser')#puts the content of the website into the soup variable, each url on a different line
    str_soup=str(soup)#convert soup to string so it can be split
    split_urls=str_soup.split('\r\n')#split so each url is a different possition on a list
    return split_urls

img_rows, img_cols = 32, 32 #number of rows and columns to convert the images to
input_shape = (img_rows, img_cols, 3)#format to store the images (rows, columns,channels) called channels last

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

for category in IMAGENET_SYSNETS:
    urls = get_imagenet_urls_from_sysnet(IMAGENET_SYSNETS[category])

    for i in range(len(urls)):
       if urls[i] != None:
           image = url_to_image(urls[i])
           if (len(image.shape)) == 3:
              save_path = '/content/{}'.format(category) + "/img{}.jpg".format(i)
              cv2.imwrite(save_path, image)
              break
