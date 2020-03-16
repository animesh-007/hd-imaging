Aim : Creating Server which returns image channels R, G, B separately to client and client combines them to form one image

software used: 
1.Flask as framework
2.<opencv-python> for image handling

initialising: 
command 'python app.py' to start the server at PORT 4555.

workflow:
a web page served at port 4555. pls attach a valid image file and click on channel. the image file saved by sever in a directory at /images.
when Upload button is clicked image from uploads directory turned into individual channels and are also combined which are shown on next page.
it uses opencv-python.

