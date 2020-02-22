import os

from flask import Flask, request, render_template, send_from_directory
import cv2
import glob
import jsonify
import numpy as np
import json


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
    r = r.tolist()
    
    b = b.tolist()
    g = g.tolist()
    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("complete.html", image_name=filename)
    
    return json.dumps({'blue': b, 'green': g, 'red': r}, indent=4, sort_keys=True)

    # return '''{
    #     "blue": "{}",
    #     "green": "{}",
    #     "red": "{}",
    # }'''.format(str(b), str(g), str(r))

#blue,green,red=upload()


# #print(image)


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
