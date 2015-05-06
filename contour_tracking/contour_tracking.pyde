"""
Simple sketch that tracks some spots in a video
"""

# add the needed libs
add_library('video')
add_library('opencv_processing')

# we need also the polygon
# the polygon has a nice method to see
# if a point is within it
from java.awt import Polygon
# declare the global variables we need
video = None
opencv = None
poly = None

# setup is run once
def setup():
#     make sure processing knows we are
#     using the global objects
    global video
    global opencv
    global poly
#     create a new Video object from our video
    video = Movie(this, "flock.mov")
#     create a new opencv object
#     in the size of the video
    opencv = OpenCV(this, 960, 540)
#     lets try it with opengl
#     can also be P2D
#     setup size of the sketch
    size(960, 540)
#     now loop and play the video
    video.loop()
    video.play()
#     we want our rectangles drawn from the center
    rectMode(CENTER)
#     now. We create our poly where we need it
#     we need to create it in the right global
#     coordinates. We cant use push and pop matrix
#     if we want to move it later on
    poly = Polygon()
#     now add some points to the poly
    for i in range(0,360,30):
#         calc x,y in a circle
        x = int(sin(radians(i))*100 + width/2)
        y = int(cos(radians(i))*100 + height/2)
#         and add those points to the poly
        poly.addPoint(x,y)
        
#     we could also do that by hand
#     but wo wants that
#     poly.addPoint(width/2 - 50,height/2 - 50)
#     poly.addPoint(width/2,height/4)
#     poly.addPoint(width/2 + 50,height/2 - 50)
#     poly.addPoint(width/2 + 50,height/2 + 50)
#     poly.addPoint(width/2 - 50,height/2 + 50)
    print "End of def setup():"

# now our loop
def draw():
#     set the bg
    background(255)
    ##### CAPTURE #####
#     load the current frame into opencv
    opencv.loadImage(video)
    ##### FILTER #####
    opencv.gray() # make it grayscale
    opencv.invert() # invert the colors get it white
    # set the threshold
    # everything below RGB 200,200,200 will be black
    opencv.threshold(200)
    # we could raise the contrast
#     opencv.contrast(1.2)
    # get a snapshot for displaying the filtered image
    filtered_src = opencv.getSnapshot()
    # find the contours
    ##### ANALYSE #####
    contours = opencv.findContours(True, True)
    # styling
    fill(255)
    # now we draw our polygon
    # not needed for the check
    beginShape()
    for i in range(poly.npoints):
        vertex(poly.xpoints[i], poly.ypoints[i])    
    endShape(CLOSE)
    ##### DISPLAY #####
    # now we loop all the contours 
    for c in contours:
        # for each contour we get its bounding box
        r = c.getBoundingBox()
        # this is the check if the center of the 
        # bounding box is within the poly
        if poly.contains(r.x, r.y):
            # make it one color
            fill(255,0,0)
        else:
            # if not make it the other
            fill(0,255,0)
        # now draw the bounding box
        # but a bit bigger
        rect(r.x, r.y, r.width*3, r.height*3)
      # we also could draw all the countours directly
    #
#     for contour in opencv.findContours():
#         contour.draw()
    image(video, 0, 0,video.width/4,video.height/4)
    image(filtered_src, 0, video.height/4,filtered_src.width/4,filtered_src.height/4)


def movieEvent(m):
    m.read()

