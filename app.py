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
    # image=Image.open("images/image.jpg")
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    cv.imwrite("templates/images/splitedcomponents/imagered.jpg", r)
    cv.imwrite("templates/images/splitedcomponents/imagegreen.jpg", g)
    cv.imwrite("templates/images/splitedcomponents/imageblue.jpg", b)
    # r=r.save("images/r_image.jpg")

    a = np.ones(b.shape, dtype=b.dtype)*50
    bg_merge = cv.merge((b,g,a))
    gr_merge = cv.merge((g,r,a))
    rb_merge = cv.merge((r,b,a))
    bgr_merge = cv.merge((b,g,r,a))
    cv.imwrite("templates/images/combinedimages/imagebg.jpg",bg_merge)
    cv.imwrite("templates/images/combinedimages/imagegr.jpg",gr_merge)
    cv.imwrite("templates/images/combinedimages/imagerb.jpg",rb_merge)
    cv.imwrite("templates/images/combinedimages/imagebgr.jpg", bgr_merge)
    # cv.imwrite("images/bgmerge.jpg", bg_merge)
    

    return render_template("complete.html",image_name="image.jpg")


@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images","image.jpg")

@app.route("/gallery") 
def get_gallery():
    image_names=os.listdir("./images")
    return render_template("gallery.html",image_names=image_names)   




#     #convert to array
#     li_r=list(image.getdata(band=0))
    
#     li_g=list(image.getdata(band=1))
    
#     li_b=list(image.getdata(band=2))


#     return json.dumps({'blue': li_b, 'green': li_g, 'red': li_r}, indent=4, sort_keys=True)

# img = json.loads(upload())

# blue=img["blue"]
# arr_b=np.array(blue,dtype="uint8")

# red=img["red"]
# arr_r=np.array(red,dtype="uint8")

# green=img["green"]
# arr_g=np.array(green,dtype="uint8")


# reshaper=arr_r.reshape(316,314) #size flipped so it reshapes correctly
# reshapeb=arr_b.reshape(316,314)
# reshapeg=arr_g.reshape(316,314)

# imr=Image.fromarray(reshaper,mode=None) # mode I
# imb=Image.fromarray(reshapeb,mode=None)
# img=Image.fromarray(reshapeg,mode=None)

# merged=Image.merge("RGB",(imr,img,imb))

# merged=merged.save("combinedimage.jpg")


if __name__ == "__main__":
    app.run(port=4555, debug=True)
