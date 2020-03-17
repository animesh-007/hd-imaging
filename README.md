# Camicroscope Code Challenge

## Basics

* Server which return R,G,B channels of an image separately.
* Client which recombines them to original image.

## Prerequisites 

* `Python`
* `Flask`
* `Lycon` 
* `NumPy`


## Installation

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
* When `Upload` button is clicked image from upload directory gets split into individual channels and are stored in directory `templates/images/splitedcomponents` also combined images are also formed which are stored in directory `templates/images/combinedimages`.

* All the operation are done using OpenCV.

* Tried to use NumPy slicing for spliting image as it is faster approach then split function of OpenCV.

* Final results are shown using `http://localhost:4555/complete.html` page
