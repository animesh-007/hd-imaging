# Camicroscope Code Challenge

## Basics

* Server which return R,G,B channels of an image separately.
* Client which recombines them to original image.

## Prerequisites 

* `Python` version 2.7 or 3.5
* `Flask`
* `Lycon` 
* `NumPy`


## Installation

#### Installing Prerequisites 

`pip install Flask lycon numpy`

#### Cloning the repository

To clone the repository

```
git clone https://github.com/animesh-007/hd-imaging.git
```

#### Building Server

1. `cd` into the newly cloned project folder
2. Run `python app.py`
3. Open `http://localhost:4555/` in a web browser


## Workflow:

* A webpage served at port 4555.Please attach a valid image file and click on `upload`.
* The image file is saved by sever in a directory at `/images`.
* When `Upload` button is clicked image from upload directory gets split into individual channels and are return to client using json.dump(). 
* merge function is used to combine each channels together to form original image.
* merge image can be seen on `http://localhost:4555/merge`
* All the operation are done using Lycon.

* Tried to use NumPy slicing for spliting image as it is faster approach then split function of OpenCV.
