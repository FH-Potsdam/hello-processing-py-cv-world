"""
look for ta specific color in the video
not working that well right now
"""

# add the needed libs
add_library('video')
add_library('opencv_processing')

# declare the global variables we need
video = None
opencv = None
colorpicker = color(0,0,0,0)

rangeLow = 160
rangeHigh = 180
# setup is run once
def setup():
#     make sure processing knows we are
#     using the global objects
    global video
    global opencv
#     create a new Video object from our video
    video = Movie(this, "dummy.mov")
#     create a new opencv object
#     in the size of the video
    opencv = OpenCV(this, 960, 540)
#     setup size of the sketch
    size(960, 540)
#     now loop and play the video
    video.loop()
    video.play()
    # because we love HSB
    colorMode(HSB, 360, 100, 100, 100)

# now our loop
def draw():



    ##### CAPTURE #####
#     load the current frame into opencv
    opencv.loadImage(video)
    ##### FILTER #####
    opencv.useColor(HSB)
    opencv.setGray(opencv.getH().clone())
    opencv.inRange(rangeLow, rangeHigh)
    filtered_image = opencv.getSnapshot()
    ##### ANALYSE #####

    ##### DISPLAY #####
    #     set the bg
    background(0, 0, 100, 100)
    image(video, 0, 0, video.width, video.height)
    contours = opencv.findContours(True, True)
#     noFill()
    stroke(60, 100, 100, 100)
    if contours.size() > 0:
        biggestContour = contours.get(0)
        r = biggestContour.getBoundingBox()
        noFill()
        strokeWeight(2)
        rect(r.x, r.y, r.width, r.height)
        ##### color picker ####
    fill(colorpicker)
    noStroke()
    rect(0, 0, 10, 10)


def mousePressed():
    
    global colorpicker
    loadPixels()
    h = hue(pixels[mouseX + mouseY * width])
    s = saturation(pixels[mouseX + mouseY * width])
    b = brightness(pixels[mouseX + mouseY * width])

    print "H: ", map(h,0,360,0,255)
    print "S: ", s
    print "B: ", b
    colorpicker = color(h,s,b,100)


def movieEvent(m):
    m.read()

