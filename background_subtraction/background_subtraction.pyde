"""
How to use background subtraction
"""
# add the needed libs
add_library('video')
add_library('opencv_processing')

# setup global objects
video = None
opencv = None
points = []


def setup():
    # reference global objects
    global video
    global opencv
    # sketh size like video
    size(960, 540)
    # load the video
    video = Movie(this, "dummy.mov")
    # init openCV
    opencv = OpenCV(this, 960, 540)
    # setup background subtraction
    # see 
    # http://atduskgreg.github.io/opencv-processing/reference/
    opencv.startBackgroundSubtraction(5, 3, 0.5)
    # loop and play the video
    video.loop()
    video.play()
    # end of setip


def draw():

    #### CAPTURE ####
    opencv.loadImage(video)
    #### FILTER ####
    opencv.updateBackground()
    opencv.dilate()
    opencv.erode()
    #### ANALYZE ####
    contours = opencv.findContours(False,True) 
    #### DISPLAY ####
    # delete bg
    noStroke()
    fill(255,20)
    rect(0,0,width,height)
    noFill()
    stroke(0)
    strokeWeight(1)
    # if there are contours
    # get the biggest one
    if contours.size() > 0:
        r = contours.get(0).getBoundingBox()
        ellipse(r.x, r.y, 10, 10)
        # save its points in a list
        points.append([r.x, r.y])

    # loop all points
    stroke(255,0,0)
    for i in range(0,len(points)):
        ellipse(points[i][0], points[i][1], 5, 5) 
        contours.get(0).draw()
  
    # simple draw all contours
    stroke(255,255,0)  
    for contour in contours:
        contour.draw()


def movieEvent(m):
    m.read()

