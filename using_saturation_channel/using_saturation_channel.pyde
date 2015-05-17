"""
Simple sketch that uses the saturation channel
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
    video = Movie(this, "slime1.mov")
#     create a new opencv object
#     in the size of the video
    opencv = OpenCV(this, 640, 480)
#     setup size of the sketch
    size(640 * 2, 480)
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
    opencv.useColor(HSB)
    opencv.setGray(opencv.getS().clone())
    
#     opencv.gray()
    opencv.invert()
#     opencv.contrast(4)
    filtered_image = opencv.getSnapshot()
    ##### ANALYSE #####
    contours = opencv.findContours(False, True)

    ##### DISPLAY #####
    image(video, 0, 0, video.width, video.height)
    image(filtered_image, video.width, 0,
          filtered_image.width, filtered_image.height)
    noFill()
    stroke(60, 100, 100, 100)
    strokeWeight(2)
    smooth()
    for contour in contours:
        r = contour.getBoundingBox()
        if r.width < 200:
#         rect(r.x + video.width, r.y,r.width, r.height)
            contour.draw()


def movieEvent(m):
    m.read()

