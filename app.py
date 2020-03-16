import os

from flask import Flask, request, render_template, send_from_directory
import jsonify
import numpy as np
import json
from PIL import Image
import cv2 as cv


__author__ = 'animesh'

app = Flask(__name__,static_url_path='',static_folder='templates/')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    
    # filename = "rgb01.png"
    # target="images/"
    target=os.path.join(APP_ROOT,"images/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)


    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename   
        destination = "/".join([target, "image.jpg"])
        print(destination)
        file.save(destination)

        
# # #print(image)
    image_path = "images/image.jpg"
    image = cv.imread(image_path, 1)
    
    # splitting image into 3 channels
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    cv.imwrite("templates/images/splitedcomponents/imagered.jpg", r)
    cv.imwrite("templates/images/splitedcomponents/imagegreen.jpg", g)
    cv.imwrite("templates/images/splitedcomponents/imageblue.jpg", b)
    

    # combining R,G,B channels into one
    a = np.ones(b.shape, dtype=b.dtype)*50
    bgr_merge = cv.merge((b,g,r,a))
    
    bg = bgr_merge.copy()
    bg[:,:,2]=0
    
    gr = bgr_merge.copy()
    gr[:,:,0]=0
    
    rb = bgr_merge.copy()
    rb[:,:,1]=0

    cv.imwrite("templates/images/combinedimages/imagebgr.jpg", bgr_merge)
    cv.imwrite("templates/images/combinedimages/imagebg.jpg",bg)
    cv.imwrite("templates/images/combinedimages/imagegr.jpg",gr)
    cv.imwrite("templates/images/combinedimages/imagerb.jpg",rb)
    
    

    return render_template("complete.html")





if __name__ == "__main__":
    app.run(port=4555, debug=True)
