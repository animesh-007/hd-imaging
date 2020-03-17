import os
from flask import Flask, request, render_template, send_from_directory
import numpy as np
import cv2 


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
        destination = "/".join([target, "image.jpg"])
        print(destination)
        file.save(destination)

        

    image_path = "images/image.jpg"
    image = cv2.imread(image_path, 1)
    
    # splitting image into 3 channels
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    cv2.imwrite("templates/images/splitedcomponents/imagered.jpg", r)
    cv2.imwrite("templates/images/splitedcomponents/imagegreen.jpg", g)
    cv2.imwrite("templates/images/splitedcomponents/imageblue.jpg", b)
    

    # combining R,G,B channels into one
    a = np.ones(b.shape, dtype=b.dtype)*50
    bgr_merge = cv2.merge((b,g,r,a))
    
    #setting red channel of combine image 0 for viewing
    bg = bgr_merge.copy()
    bg[:,:,2]=0
    
    #setting blue channel of combine image 0 for viewing
    gr = bgr_merge.copy()
    gr[:,:,0]=0
    

    #setting green channel of combine image 0 for viewing
    rb = bgr_merge.copy()
    rb[:,:,1]=0

    cv2.imwrite("templates/images/combinedimages/imagebgr.jpg", bgr_merge)
    cv2.imwrite("templates/images/combinedimages/imagebg.jpg",bg)
    cv2.imwrite("templates/images/combinedimages/imagegr.jpg",gr)
    cv2.imwrite("templates/images/combinedimages/imagerb.jpg",rb)
    
    

    return render_template("complete.html")





if __name__ == "__main__":
    app.run(port=4555, debug=True)
