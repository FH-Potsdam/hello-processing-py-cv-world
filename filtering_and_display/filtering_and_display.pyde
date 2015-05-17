"""
Simple empty sketch
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
    global font
    font = createFont("Arial", 12)
    textFont(font)
    textAlign(LEFT)
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
#     we love hsb
    colorMode(HSB, 360, 100, 100, 100)
    background(0, 0, 100)
    print "End of def setup():"

# now our loop
def draw():

    ##### CAPTURE #####
#     load the current frame into opencv
    opencv.loadImage(video)
    ##### FILTER #####
    # get a snapshot for displaying the filtered images
    opencv.gray()  # make it grayscale
    grey_image = opencv.getSnapshot()
    opencv.contrast(3)  # raise contrast
    contrast_image = opencv.getSnapshot()
    opencv.threshold(240)  # clip all below 240
    threshold_image = opencv.getSnapshot()
    ##### ANALYSE #####
    # do some nasty detection here
    ##### DISPLAY #####

    # display the sources
    image(video, 0, 0, video.width / 2, video.height / 2)
    text("source video", 10, 15)

    image(grey_image, 0, video.height / 2,
          grey_image.width / 2, grey_image.height / 2)
    text("grey video", 10, video.height / 2 + 15)

    image(contrast_image, video.width / 2, 0,
          contrast_image.width / 2, contrast_image.height / 2)
    text("contrast video", video.width / 2 + 10, 15)

    image(threshold_image, video.width / 2, video.height / 2,
          threshold_image.width / 2, threshold_image.height / 2)
    text("threshold video", video.width / 2+ 10, video.height / 2 + 15)


def movieEvent(m):
    m.read()

