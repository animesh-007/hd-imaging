import os
from flask import Flask, request, render_template
import numpy as np
import lycon


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
    # image = cv2.imread(image_path, 1)
    image = lycon.load(image_path)
    
    # splitting image into 3 channels
    r = image[:,:,0]
    g = image[:,:,1]
    b = image[:,:,2]

    return np.array_str(np.array([r,g,b]))


# combining R,G,B channels into one
combinedimaged = np.dstack((r,g,b))


if __name__ == "__main__":
    app.run(port=4555, debug=True)
