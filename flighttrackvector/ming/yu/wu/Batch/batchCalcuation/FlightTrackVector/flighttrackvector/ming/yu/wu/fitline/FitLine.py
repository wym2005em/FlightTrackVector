'''
Created on 2013-10-30

@author: wym
'''
from flighttrackvector.ming.yu.wu.point import Point 
from flighttrackvector.ming.yu.wu.fitline import line
class FitLine(object):
    '''
    classdocs
    '''


    def __init__(self,pointList):
        self.pointList = pointList
    
#     def getYfromX(self,yuceX):
#         return ((yuceX-self.pointList[0].X)*(self.pointList[-1].Y-self.pointList[0].Y))/(self.pointList[-1].X-self.pointList[0].X)+self.pointList[0].Y
#     
#     def errorSumSquares(self):
#         errorSum=0
#         for point in pointList[1:-1]:
#             errorSum=errorSum+(self.getYfromX(point.X)-point.Y)*(self.getYfromX(point.X)-point.Y)
#         return errorSum
    def errorSumSquares2(self):
        l1=line.Line()
        l1.Line(self.pointList[0], self.pointList[-1])
        return l1.errorSumSquares(self.pointList),l1   
             
if __name__=='__main__':
#     pt1 = Point.Point(0,-1)
#     pt2 = Point.Point(1.414/2.0,1.414/2.0)
#     pt3 = Point.Point(13.02,153.04)
#     pt4 = Point.Point(-1.0,0)
    import math
    pt1 = Point.Point(0,0)
    pt2 = Point.Point(0,2)
    pt3 = Point.Point(3,3)
    pt4 = Point.Point(5,5)
#find     
    l1 = line.Line()
    l1.Line(pt1,pt4)
    
    pointList = [pt1,pt2,pt3,pt4]
    
    f = FitLine(pointList)
    
#     print f.errorSumSquares2();    
        