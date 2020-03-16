Aim : Creating Server which returns image channels R, G, B separately to client and client combines them to form one image

software used: 
1.Flask as framework
2.opencv-python for image handling

Initialising: 
command 'python app.py' to start the server at PORT 4555.

Workflow:
a web page served at port 4555. pls attach a valid image file and click on channel. the image file saved by sever in a directory at /images.
when Upload button is clicked image from uploads directory turned into individual channels and are stored in directory templates/images/splitedcomponents also combined images are also formed which are stored in directory templates/images/combinedimages.

All the operation are done using opencv-python.

Final result are shown using complete.html page
