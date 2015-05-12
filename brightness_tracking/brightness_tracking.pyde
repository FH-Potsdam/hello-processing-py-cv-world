"""
look for the brightest point int the video
"""

# add the needed libs
add_library('video')
add_library('opencv_processing')

# declare the global variables we need
video = None
opencv = None

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
#     set the bg
    background(0, 0, 100, 100)
    ##### CAPTURE #####
#     load the current frame into opencv
    opencv.loadImage(video)
    ##### FILTER #####

    ##### ANALYSE #####
    # look for the brightest point
    brightest_point = opencv.max()

    ##### DISPLAY #####
    image(video, 0, 0, video.width , video.height)
    noFill()
    stroke(60,100,100,100)
    
    ellipse(brightest_point.x, brightest_point.y, 20,20)


def movieEvent(m):
    m.read()

