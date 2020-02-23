import os

from flask import Flask, request, render_template, send_from_directory
import jsonify
import numpy as np
import json
from PIL import Image


__author__ = 'animesh'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    
    filename = "rgb01.png"
    target="images/"

    destination = "/".join([target, filename])
    
# #print(image)
    image=Image.open("images/rgb01.png")

    #convert to array
    li_r=list(image.getdata(band=0))
    
    li_g=list(image.getdata(band=1))
    
    li_b=list(image.getdata(band=2))

    return json.dumps({'blue': li_b, 'green': li_g, 'red': li_r}, indent=4, sort_keys=True)


img = json.loads(upload())

blue=img["blue"]
arr_b=np.array(blue,dtype="uint8")

red=img["red"]
arr_r=np.array(red,dtype="uint8")

green=img["green"]
arr_g=np.array(green,dtype="uint8")


reshaper=arr_r.reshape(316,314) #size flipped so it reshapes correctly
reshapeb=arr_b.reshape(316,314)
reshapeg=arr_g.reshape(316,314)

imr=Image.fromarray(reshaper,mode=None) # mode I
imb=Image.fromarray(reshapeb,mode=None)
img=Image.fromarray(reshapeg,mode=None)

merged=Image.merge("RGB",(imr,img,imb))

merged=merged.save("combinedimage.jpg")


if __name__ == "__main__":
    app.run(port=4555, debug=True)
