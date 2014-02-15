import math
from flighttrackvector.ming.yu.wu.point import Point
from matplotlib.patches import Circle
from flighttrackvector.ming.yu.wu.fitline import FitLine
from flighttrackvector.ming.yu.wu.fitline import line
from scipy import * 
class circle(object):
    def __repr__(self):
        return '[Circle::  radiusAngle:(%s) + radius:(%s)+X0:(%s)+Y0:(%s)+FirstPoint:(%s)+LastPoint(%s)+zuoyou: (%s)]' % (self.radiusAngle, self.radius,self.X0,self.Y0,self.firstPoint,self.lastPoint,self.zuoyou)

    def __init__(self,radiusAngle=0,radius=0,X0=0,Y0=0,firstPoint=Point.Point(0,0),lastPoint=Point.Point(0,0),leftOrRight="zuo"):
        self.radiusAngle = radiusAngle
        self.radius = radius
        self.X0 = X0
        self.Y0 = Y0
        self.firstPoint =firstPoint
        self.lastPoint = lastPoint
        self.zuoyou = leftOrRight
#find     
    def getYfromX(self,X):
        #print "fdsfwea3   3 3"
        #print (self.radius*self.radius)-(X-self.X0)*(X-self.X0)
        return self.Y0+math.sqrt((self.radius*self.radius)-(X-self.X0)*(X-self.X0)),self.Y0-math.sqrt((self.radius*self.radius)-(X-self.X0)*(X-self.X0))   
    
    def getAllImagePointListFromXRange(self):
        pointList=[]
        min =0
        max=0
        if (self.firstPoint.X-self.lastPoint.X)<0:
            min = self.firstPoint.X
            max = self.lastPoint.X
        else:
            max = self.firstPoint.X
            min = self.lastPoint.X  
        for x in arange(min,max+1,1):
            pointList.append(Point.Point(x,self.getYfromX(x)[0]))
        return pointList
    
    def shortestDistanceFromPointToCircle(self,point):
        distance = point.getDistanceToOtherPoint(Point.Point(self.X0,self.Y0))
        if distance>self.radius:
            return distance-self.radius
        if distance<=self.radius:
            return self.radius-distance
    
    def errorSumSquares(self,pointList):
        errorSum=0
        for point in pointList:
            errorSum = errorSum  + self.shortestDistanceFromPointToCircle(point)*self.shortestDistanceFromPointToCircle(point)
        return errorSum/len(pointList)
    
#print    
    
#     def errorSumSquares(self,pointList):
#         errorSum=0
#         for point in pointList:
#             a,b = self.getYfromX(point.X)
#             if(abs(a-point.Y)>abs(b-point.Y)):
#                 errorSum=errorSum + (b-point)*(b-point)
#             else:
#                 errorSum = errorSum+(a-point.Y)*(a-point.Y)
#         return errorSum
                
if __name__=='__main__':
        
    from flighttrackvector.ming.yu.wu.fitcircle import FitCircle
#     y=2*x2
#     pt1 = Point.Point(100)
#     pt1 = Point.Point(100,0)
#     pt2 = Point.Point(150/math.sqrt(2.0),-150/math.sqrt(2.0))
#     pt22=Point.Point(170/math.sqrt(2.0),-160/math.sqrt(2.0))
#     pt3=Point.Point(200/math.sqrt(2.0),-200/math.sqrt(2.0))
#     pt4 = Point.Point(0,-100)
    pointList = []
    
    from scipy import *
    for i in arange(-5,8,1):
        pointList.append(Point.Point(float(i*i),float(i)))
        

    fitCircle = FitCircle.FitCircle(pointList)
    niheyuan = fitCircle.errorSumSquares2()[1]
    fitLine = FitLine.FitLine(pointList)
    nihexian = fitLine.errorSumSquares2()[1]
    lineList = nihexian.getAllImagePointListFromXRange()
    circlePointList = niheyuan.getAllImagePointListFromXRange()
    
    import matplotlib.pyplot as plt 
#     print circlePointList
#     print niheyuan.X0
#     print niheyuan.Y0
    fig = plt.figure(figsize=(6,6))
    ax = plt.subplot(111)
    circle = Circle((niheyuan.X0,niheyuan.Y0),niheyuan.radius)
    ax.add_patch(circle)
    #print niheyuan.radiusAngle
    lll = line.Line()
    lll.Line(pointList[0], pointList[-1])
    lllPointList = lll.getAllImagePointListFromXRange()
    lllperpendicularPointList = lll.returnPerpendicularBisector().getAllImagePointListFromXRange();
    
    plt.plot([point.X for point in lllPointList],[point.Y for point in lllPointList],"green") 
    plt.plot([point.X for point in lllperpendicularPointList],[point.Y for point in lllperpendicularPointList],"black") 
    plt.plot([point.X for point in lineList],[point.Y for point in lineList],"yellow")
    plt.plot([point.X for point in pointList],[point.Y for point in pointList],'or')
    plt.plot(niheyuan.X0,niheyuan.Y0,'oy')
    plt.plot(-1.1,3.42,'ow')
#     plt.plot([point.X for point in circlePointList],[point.Y for point in circlePointList],"black")
#     print circlePointList[-1] 
    #print "line squares:" +str(fitLine.errorSumSquares2()[0])
    #print "circle squares "+str(fitCircle.errorSumSquares2()[0])
    plt.show()     
