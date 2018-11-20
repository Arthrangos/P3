#import Collision
import Laser
#import Target
#import Blocker
import cv2
import math
import numpy as np


class Mirror:

    rectangleX1 = 0
    rectangleX2 = 0
    rectangleX3 = 0
    rectangleX4 = 0

    rectangleY1 = 0
    rectangleY2 = 0
    rectangleY3 = 0
    rectangleY4 = 0

    mirrorState = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, img):
        self.rectangleX1 = x1
        self.rectangleX2 = x2
        self.rectangleX3 = x3
        self.rectangleX4 = x4

        self.rectangleY1 = y1
        self.rectangleY2 = y2
        self.rectangleY3 = y3
        self.rectangleY4 = y4

        self.mirrorState = 1
        topLCorner = (x1, y1)
        topRCorner = (x4, y4)
        bottomLCorner = (x2, y2)
        bottomRCorner = (x3, y3)

        cv2.line(img, topLCorner, bottomLCorner, (255, 255, 255), 5)
        cv2.line(img, topRCorner, bottomRCorner, (255, 255, 255), 5)
        cv2.line(img, topLCorner, topRCorner, (255, 255, 255), 5)
        cv2.line(img, bottomLCorner, bottomRCorner, (255, 255, 255), 5)



    def getRectangleX1(self):
        return self.rectangleX1

    def getRectangleX2(self):
        return self.rectangleX2

    def getRectangleX3(self):
        return self.rectangleX3

    def getRectangleX4(self):
        return self.rectangleX4

    def getRectangleY1(self):
        return self.rectangleY1

    def getRectangleY2(self):
        return self.rectangleY2

    def getRectangleY3(self):
        return self.rectangleY3

    def getRectangleY4(self):
        return self.rectangleY4

    def getMirrorState(self):
        return self.mirrorState


def angleDetermine(laserX1, laserY1, laserX2, laserY2, closestCollisionX, closestCollisionY, collisionLineX1,
                   collisionLineY1, collisionLineX2, collisionLineY2, img):

    #The normal for the rectangles line is calulated here
    normalY = collisionLineX2 - collisionLineX1
    normalX = collisionLineY1 - collisionLineY2
    temp = ((collisionLineX2 - collisionLineX1) ** 2) + ((collisionLineY2 - collisionLineY1) ** 2)
    normalLength = math.sqrt(temp)
    normalX = normalX / normalLength
    normalY = normalY / normalLength

    #If the vector is too short, so it can not be properly reflected it will be made longer here
    if laserX2 < collisionLineX1 or laserY1 < collisionLineY1:
        laserVectorX = laserX2-laserX1
        laserVectorY = laserY2-laserY1

        laserX2 = laserVectorX + closestCollisionX
        laserY2 = laserVectorY + closestCollisionY
    else:
        laserX2 = laserX2
        laserY2 = laserY2

    #The vector that goes byound the rectangle side, is found, so it can be reflected in the normal from above.
    rayX = laserX2 - closestCollisionX
    rayY = laserY2 - closestCollisionY

    #The normal is moved to the end of the laser that goes into the rectangle
    dotProduct = (rayX * normalX)+(rayY*normalY)
    dotNormalX = dotProduct*normalX
    dotNormalY = dotProduct*normalY

    #The end of the reflection is found
    reflectionEndX = laserX2 - (dotNormalX * 2)
    reflectionEndY = laserY2 - (dotNormalY * 2)
    #cv2.line(img, (laserX1,laserY1), (closestCollisionX, closestCollisionY), (0, 0, 255), 5)
    return Laser.Laser(closestCollisionX, closestCollisionY, int(reflectionEndX), int(reflectionEndY), img)


# def angleDetermineStillBad(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, img):
#     vectorAx = ax2 - ax1
#     vectorAy = ay2 - ay1
#     vectorBx = bx2 - bx1
#     vectorBy = by2 - by1
#     vectorCx = vectorAx
#     vectorCy = vectorAy
#
#     vectorA = [vectorAx, vectorAy]
#     vectorB = [vectorBx, vectorBy]
#     vectorB90deg = [-vectorBy, vectorBx]
#     normalVectorToBx1= ax2
#     normalVectorToBx2= ax2+vectorB90deg[0]
#     normalVectorToBy1= ay2
#     normalVectorToBy2= ay2+vectorB90deg[1]
#     normalVectorToBx = normalVectorToBx2-normalVectorToBx1
#     normalVectorToBy= normalVectorToBy2-normalVectorToBy1
#     cv2.line(img, (ax2, ay2), (ax2+vectorCx, ay2+vectorCy), (255, 255, 0), 5)
#     magnitudeOfA = int(math.sqrt(math.pow(vectorAx, 2) + math.pow(vectorAy, 2))) #POP POP!!! #https://www.youtube.com/watch?v=dyp9Qw12boI&ab_channel=Jalkie
#     magnitudeOfB = int(math.sqrt(math.pow(vectorBx, 2) + math.pow(vectorBy, 2)))
#     #magnitudeOfnormalB = int(math.sqrt(math.pow(normalVectorToBx, 2) + math.pow(normalVectorToBy, 2)))
#     #normOfnormalVectorToBx = normalVectorToBx/magnitudeOfnormalB
#     #normOfnormalVectorToBy = normalVectorToBy/magnitudeOfnormalB
#
#     #dotProductOfStuff = (ax2*normalVectorToBx)+(ay2*normalVectorToBy)
#
#     #rLx = vectorAx-2*(dotProductOfStuff)*normOfnormalVectorToBx
#     #rLy = vectorAy - 2 * (dotProductOfStuff) * normOfnormalVectorToBy
#
#
#
#     vectorProduct = (vectorAx*vectorBx) + (vectorAy*vectorBy)
#     magnitudeProduct = (magnitudeOfA * magnitudeOfB)
#
#
#
# def angleDetermineBad(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, img):
#     vectorAx = ax2 - ax1
#     vectorAy = ay2 - ay1
#     vectorBx = bx2 - bx1
#     vectorBy = by2 - by1
#
#     vectorA = [vectorAx, vectorAy]
#     vectorB = [vectorBx, vectorBy]
#     magnitudeOfA = int(math.sqrt(math.pow(vectorAx, 2) + math.pow(vectorAy, 2))) #POP POP!!! #https://www.youtube.com/watch?v=dyp9Qw12boI&ab_channel=Jalkie
#     magnitudeOfB = int(math.sqrt(math.pow(vectorBx, 2) + math.pow(vectorBy, 2)))
#
#     print(vectorAx, vectorAy, vectorBx, vectorBy, magnitudeOfA, magnitudeOfB)
#
#     vectorProduct = (vectorAx*vectorBx) + (vectorAy*vectorBy)
#     magnitudeProduct = (magnitudeOfA * magnitudeOfB)
#     print(vectorProduct, magnitudeProduct)
#
#     cosAngle = vectorProduct/magnitudeProduct
#     print("cos",cosAngle)
#     Angle = math.degrees(math.acos(cosAngle))
#     print("A",Angle)
#
#     print(vectorA, vectorB)
#     cross = np.cross(vectorA, vectorB)
#     print("cross", cross)
#
#     x1 = ax2
#     y1 = ay2
#     rLx2 = x1 + (magnitudeOfA * math.cos(Angle))
#     rLy2 = y1 + (magnitudeOfA * math.sin(Angle))
#     print("rLx2", rLx2)
#     print("rLy2", rLy2)
#
#     print("final shit",ax2, ay2, rLx2, rLy2)
#     cv2.line(img, (-vectorBy, vectorBx), (vectorBy, -vectorBx), (0, 255, 0), 5)
#     cv2.line(img, (int(ax2), int(ay2)), (int(rLx2), int(rLy2)), (0, 255, 0), 5)
#     #Laser.Laser
