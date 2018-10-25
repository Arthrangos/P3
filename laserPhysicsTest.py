import numpy as np
import cv2
import time

img = cv2.imread('test.jpg')

class rectangle:
    def __init__(self, x1, y1, x2, y2, img):
        topLCorner = (x1, y1)
        bottomRCorner = (x2, y2)
        cv2.rectangle(img, topLCorner, bottomRCorner, (0, 255, 0), 2)

    def collisionleft(self, ):


        intersectionY = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - (y1 - y2) * ((x3 * y4) - (y3 * x4))) \
                        / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))




def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 100
    lsY = int(vRow/2)
    leX = int(vCol-50)
    leY = int(vRow/2)+200
    osX = int(vCol/3)
    osY = int(vRow/2)-100
    oeX = vCol-100
    oeY = int(vRow/2)+100
    x1 = lsX
    x2 = leX
    x3 = osX
    x4 = osX
    y1 = lsY
    y2 = leY
    y3 = osY
    y4 = oeY
    intersectionX = ((((lsX * leY) - (lsX * leX)) * (osX - osX)) - ((lsX - leX) * ((osX * oeY) - (osY * osX)))) \
                    / (((lsX - leX) * (osY - oeY)) - ((lsY - leY * (osX - osX))))
    rectangle(osX, osY, oeX, oeY, videoFeed)
    drawLaser = cv2.line(videoFeed, (lsX, lsY), (leX, leY), (0, 0, 255), 5)
    drawLaser = cv2.line(videoFeed, (int(intersectionX), int(intersectionY)), (int(intersectionX), int(intersectionY)), (255, 0, 0), 5)


cap = cv2.VideoCapture(0)

ret, last_frame = cap.read()

if last_frame is None:
    exit()

while(cap.isOpened()):
    ret, frame = cap.read()

    if frame is None:
        exit()

    laserFire(frame,20,0.2) #Call to laser function
    cv2.imshow('frame', frame)

    if cv2.waitKey(33) >= 0:
        break

    last_frame = frame

cap.release()
cv2.destroyAllWindows()