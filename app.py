import os
from flask import Flask, request, render_template
import numpy as np
import lycon
import json


__author__ = 'animesh'

app = Flask(__name__,static_url_path='',static_folder='templates/')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    

    target=os.path.join(APP_ROOT,"images/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)


    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename   
        destination = "/".join([target, "image.png"])
        print(destination)
        file.save(destination)

        

    image_path = "images/image.png"

    image = lycon.load(image_path)
    
    # splitting image into 3 channels
    r = image[:,:,0]
    g = image[:,:,1]
    b = image[:,:,2]

    r=r.tolist()
    g=g.tolist()
    b=b.tolist()

    return json.dumps({'blue':b, 'green':g, 'red':r}, sort_keys=True, indent=4) 


@app.route("/merge")
def merge():

    img = json.loads(upload())
    blue=img["blue"]
    arr_b=np.array(blue,dtype="uint8")
    
    red=img["red"]
    arr_r=np.array(red,dtype="uint8")
    
    green=img["green"]
    arr_g=np.array(green,dtype="uint8")

    combinedimaged = np.dstack((arr_r,arr_g,arr_b))

    lycon.save("templates/images/combinedimages/mergeimage.png",combinedimaged)

    return render_template("merge.html")


if __name__ == "__main__":
    app.run(port=4555, debug=True)
    