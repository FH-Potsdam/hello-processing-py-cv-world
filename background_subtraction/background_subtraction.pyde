add_library('video')
add_library('opencv_processing')


video = None
opencv = None
points = []


def setup():
    global video
    global opencv
    size(960, 540, P2D)
    video = Movie(this, "dummy.mov")
    opencv = OpenCV(this, 960, 540)

    opencv.startBackgroundSubtraction(5, 3, 0.5)

    video.loop()
    video.play()


def draw():
    noStroke()
    fill(255,20)
    rect(0,0,width,height)
#     image(video, 0, 0)
    opencv.loadImage(video)

    opencv.updateBackground()

    opencv.dilate()
    opencv.erode()
    noFill()
    stroke(0)
    strokeWeight(1)
    
    contours = opencv.findContours(False,True) 
    if contours.size() > 0:
        r = contours.get(0).getBoundingBox()
        ellipse(r.x, r.y, 10, 10)
        points.append([r.x, r.y])

#     for i in range(0,len(points)):
#         ellipse(points[i][0], points[i][1], 5, 5)   
            
#         contours.get(0).draw()
#     for contour in opencv.findContours(False,True):
#         contour.draw()


def movieEvent(m):
    m.read()

