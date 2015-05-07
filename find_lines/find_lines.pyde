"""
Simple sketch that looks for lines in a video
"""

# add the needed libs
add_library('video')
add_library('opencv_processing')

# declare the global variables we need
video = None
opencv = None
font = None

# setup is run once
def setup():
#     make sure processing knows we are
#     using the global objects
    global video
    global opencv
    global poly
    global font
    font = createFont("Georgia", 12)
    textFont(font)
    textAlign(LEFT)
#     create a new Video object from our video
    video = Movie(this, "dummy.mov")
#     create a new opencv object
#     in the size of the video
    opencv = OpenCV(this, 960, 540)
#     lets try it with opengl
#     can also be P2D
#     setup size of the sketch
    size(960, 540, P2D)
#     now loop and play the video
    video.loop()
    video.play()

    colorMode(HSB, 360, 100, 100, 100)
    background(0,0,100)
    print "End of def setup():"

# now our loop
def draw():
#     set the bg
    fill(0, 0, 100, 1)
    noStroke()
    rect(0, 0, width, height)
    ##### CAPTURE #####
#     load the current frame into opencv
    opencv.loadImage(video)
    ##### FILTER #####
    opencv.gray()  # make it grayscale
# opencv.invert() # invert the colors get it white

    # we raise the contrast
    opencv.contrast(3)
    # set the threshold
    opencv.threshold(200)

    # get a snapshot for displaying the filtered image
    filtered_src = opencv.getSnapshot()
    # find the contours
    ##### ANALYSE #####
    lines = opencv.findLines(10, 1, 10)

    ##### DISPLAY #####
    # now we loop all the lines
    stroke(0,0,0,100)
    for ln in lines:
        # only vertial lines
        if (ln.angle >= radians(0) and ln.angle < radians(1)):
            line(ln.start.x, ln.start.y, ln.end.x, ln.end.y)
    # display the sources
    image(video, 0, 0,video.width/4,video.height/4)
    fill(0,0,100,100)
    text("source video",10,15)
    image(filtered_src, 0, video.height/4,filtered_src.width/4,filtered_src.height/4)
    text("filterd video",10,video.height/4 + 15)


def movieEvent(m):
    m.read()

