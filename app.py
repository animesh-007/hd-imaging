import os

from flask import Flask, request, render_template, send_from_directory
import cv2
import glob
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
    
    # target = os.path.join(APP_ROOT, 'images/')
    # print(target)
    # if not os.path.isdir(target):
    #     os.mkdir(target)
    # print(request.files.getlist("file"))
    # for upload in request.files.getlist("file"):
    #     print(upload)
    #     print("{} is the file name".format(upload.filename))
    #     filename = upload.filename
    #     # This is to verify files are supported
    #     ext = os.path.splitext(filename)[1]
    #     if (ext == ".jpg") or (ext == ".png"):
    #         print("File supported moving on...")
    #     else:
    #         render_template("Error.html", message="Files uploaded are not supported...")
           
            
    
    
    #image = cv2.merge((b,g,r))
    #cv2.imshow('image111',image)
    #cv2.waitKey(0)
    filename = "rgb01.png"
    target="images/"

    destination = "/".join([target, filename])
    
    # print("Accept incoming file:", filename)
    # print("Save it to:", destination)
    # upload.save(destination)


    img=cv2.imread(destination)
    b, g, r = cv2.split(img)
    
    

        
    # print(g.tolist())
    #r = r.tolist()
    #b = b.tolist()
    #g = g.tolist()
    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("complete.html", image_name=filename)
    
    #return json.dumps({'blue': b, 'green': g, 'red': r}, indent=4, sort_keys=True)

    # return '''{
    #     "blue": "{}",
    #     "green": "{}",
    #     "red": "{}",
    # }'''.format(str(b), str(g), str(r))

#blue,green,red=upload()


# #print(image)
    image=Image.open("images/rgb01.png")

    #print(image.size) #size is inverted i.e columns first rows second eg: 500,250

    #convert to array
    li_r=list(image.getdata(band=0))
    #arr_r=np.array(li_r,dtype="uint8")
    li_g=list(image.getdata(band=1))
    #arr_g=np.array(li_g,dtype="uint8")
    li_b=list(image.getdata(band=2))
    #arr_b=np.array(li_b,dtype="uint8")


    return json.dumps({'blue': li_r, 'green': li_g, 'red': li_r}, indent=4, sort_keys=True)


# reshape 
# red,green,blue=upload()
    # reshaper=red.reshape(316,314) #size flipped so it reshapes correctly
    # reshapeb=green.reshape(316,314)
    # reshapeg=blue.reshape(316,314)

    
    # upload.save("/images/merged")

    
    #merged.show()

    # reshape 
#pixelDensity(1)
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

#red and blue colour are not coming properly
merged=merged.save("combinedimage.jpg")







@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)


if __name__ == "__main__":
    app.run(port=4555, debug=True)
