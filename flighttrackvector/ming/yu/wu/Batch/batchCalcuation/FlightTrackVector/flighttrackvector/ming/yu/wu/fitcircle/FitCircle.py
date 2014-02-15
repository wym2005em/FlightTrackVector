from flighttrackvector.ming.yu.wu.fitcircle import circle
from flighttrackvector.ming.yu.wu.point import Point
from flighttrackvector.ming.yu.wu.fitline import line
import math
class FitCircle(object):
    pointList=[];
    def __init__(self,pointList=[]):
        self.pointList = pointList
        if len(pointList)!=0:
            self.fitCircle = self.fitCircle3point()
            #print "FitCircle PointList num is 0"
    
    
    #getLineIntersectionAngle
    
    
    #firstLine: startLine
    #secondLine: endLine
    def fitOneInscribedCircle(self,firstLine,secondLine):
        #find the nearest point to the waijieCircle(X0,Y0)
#         print "firstLine:   "+str(firstLine)
        print str(firstLine.getLineLength())+"   shifouxiangdeng   "+str(secondLine.getLineLength())
        firstSecondLineJiaoPoint = firstLine.getLineIntersectPoint(secondLine)
        interestPoint=[]#interestPoint must be on the firstLine
        interestPrePareOnFirstLinePoint=[]
        interestPrePareOnSecondLinePoint=[]
        biaoji =""
        from flighttrackvector.ming.yu.wu.fitcircle import circle

        circlecircle = circle.circle()
        #check if have difficultPath,only if jiaoPoint is near Point2 of firstLine,and is near Point1 of secondLine
        #then make the Point1 of firstLine Link to Point2 of secondLine 
        #print str(firstLine.ifJiaodianPointOnThelineSegment(secondLine))+"  dwfwf3rfwarfaw"
        if str(firstLine.ifJiaodianPointOnThelineSegment(secondLine))=="yes":
            biaoji="difficultPath"
            #print "fdsfsefar3wrwar3war3war3awrawr3war3aw"
            return circlecircle,biaoji 
        
        if firstLine.point1.getDistanceToOtherPoint(firstSecondLineJiaoPoint)>firstLine.point2.getDistanceToOtherPoint(firstSecondLineJiaoPoint) :    
            interestPrePareOnFirstLinePoint = firstLine.point2
        else:
            biaoji="difficultPath"
            return circlecircle,biaoji
        if secondLine.point1.getDistanceToOtherPoint(firstSecondLineJiaoPoint)>secondLine.point2.getDistanceToOtherPoint(firstSecondLineJiaoPoint) :
            biaoji="difficultPath"

            return circlecircle,biaoji
        else:
            interestPrePareOnSecondLinePoint = secondLine.point1
            
        
        
        
        if interestPrePareOnFirstLinePoint.getDistanceToOtherPoint(firstSecondLineJiaoPoint) > interestPrePareOnSecondLinePoint.getDistanceToOtherPoint(firstSecondLineJiaoPoint):
            interestPoint = interestPrePareOnSecondLinePoint
            biaoji = "secondLineNear"
        else:
            interestPoint =  interestPrePareOnFirstLinePoint
            #print interestPoint
            biaoji = "firstLineNear"
        firstVector = firstLine.getUnitVector()
        secondVector = secondLine.getUnitVector()
    
#find     
        vector = [firstVector[0]+secondVector[0],firstVector[1]+secondVector[1]]
            
        k=vector[0]/vector[1]

        b=interestPoint.Y-k*interestPoint.X
        linshiX = 0.1010101#0.1010101 prevent chongfu
        y0=k*linshiX+b#linshi is optional
        

        from flighttrackvector.ming.yu.wu.fitline import line
        lll = line.Line()
        lll.Line(Point.Point(linshiX,y0), interestPoint)
        
        #check yuanxinPoint At Left OR Right
        from flighttrackvector.ming.yu.wu.fitline import line
        lll2 = line.Line()
        lll2.Line(firstLine.point2, secondLine.point1)


        if(biaoji=="firstLineNear"):
            symmetryPoint = secondLine.getLineIntersectPoint(lll)#duichenPoint
            firstVerticalLine = firstLine.getVerticalLineAtPoint(interestPoint)
            secondVerticalLine = secondLine.getVerticalLineAtPoint(symmetryPoint)
            #print "fa3 32 3 23 "
            #print secondVerticalLine
            #print symmetryPoint
            yuanxinPoint = firstVerticalLine.getLineIntersectPoint(secondVerticalLine)
            radius = yuanxinPoint.getDistanceToOtherPoint(symmetryPoint)
            from flighttrackvector.ming.yu.wu.fitcircle import circle
            
            lll3 = line.Line()
            lll3.Line(interestPoint, symmetryPoint)
            leftOrRight = lll3.pointAtVectorLeftOrRight(yuanxinPoint)
            circlecircle = circle.circle(180-firstLine.getLineIntersectionAngle(secondLine),radius,yuanxinPoint.X,yuanxinPoint.Y,interestPoint,symmetryPoint,leftOrRight)
                     
        if(biaoji=="secondLineNear"):
            symmetryPoint = firstLine.getLineIntersectPoint(lll)#duichenPoint
            secondVerticalLine = secondLine.getVerticalLineAtPoint(interestPoint)
            firstVerticalLine = firstLine.getVerticalLineAtPoint(symmetryPoint)
            yuanxinPoint = firstVerticalLine.getLineIntersectPoint(secondVerticalLine)
            radius = yuanxinPoint.getDistanceToOtherPoint(symmetryPoint)
            from flighttrackvector.ming.yu.wu.fitcircle import circle
            
            lll3 = line.Line()
            lll3.Line(symmetryPoint,interestPoint)
            leftOrRight = lll3.pointAtVectorLeftOrRight(yuanxinPoint)
            circlecircle = circle.circle(180-firstLine.getLineIntersectionAngle(secondLine),radius,yuanxinPoint.X,yuanxinPoint.Y,symmetryPoint,interestPoint,leftOrRight)
            
        return circlecircle,biaoji
#     
    def fitCircle3point(self):
        if len(self.pointList)<3:
            print "Error: pointListSize<3"
        firstPoint = self.pointList[0]
        lastPoint = self.pointList[-1]
        l1 = line.Line()
        l1.Line(firstPoint, lastPoint)
        perpendiculaLine = l1.returnPerpendicularBisector()
#         print firstPoint
#         print lastPoint
        #print perpendiculaLine
#         print str(perpendiculaLine)+"    zhuizhipingfen"
        nearestPoint = self.getNearestPointByLine(perpendiculaLine,self.pointList)
        l2 = line.Line()
        l3 = line.Line()
        #print str(firstPoint)+" d "+str(nearestPoint)
        l2.Line(firstPoint, nearestPoint);#nearestPoint must be at the second para
        l3.Line(lastPoint, nearestPoint);#nearestPoint must be at the second para
        intersectionAngle = l2.getLineIntersectionAngle(l3)
        ll = line.Line()
        ll.Line(firstPoint,lastPoint)
        
        radius = ll.getLength()/(2*math.sin(math.radians(intersectionAngle))) 
        
        intersectionAngle = intersectionAngle/2
        radiusAngle = 2*(180-intersectionAngle*2)
  #get X. Y.   #get X. Y.   #get X. Y.   #get X. Y. 
        midPoint = ll.getLineMidPoint() 
        
        
        
#error: midPoint and nearestPoint is same:bigger the midPoint        
        if midPoint.X==nearestPoint.X and midPoint.Y==nearestPoint.Y:
            #print #error: midPoint and nearestPoint is same:bigger the midPoint
            midPoint.X = midPoint.X + midPoint.X*0.01
            midPoint.Y = midPoint.Y + midPoint.Y*0.01
#error: midPoint and nearestPoint is same:bigger the midPoint  


            
        smaDis = midPoint.getDistanceToOtherPoint(nearestPoint)
        
        #print "dff e e e "+str(midPoint)+"  "+str(nearestPoint)
        xxx = nearestPoint.X-midPoint.X
        yyy = nearestPoint.Y-midPoint.Y
        #print "fdsf "+str(smaDis)+"  "+str(radius)
        bili = radius/smaDis
        

        yuanxinX = nearestPoint.X-bili*xxx
        yuanxinY = nearestPoint.Y-bili*yyy
        
        return circle.circle(radiusAngle,radius,yuanxinX,yuanxinY,firstPoint,lastPoint)
        
    nnLine = line.Line()  
    def getNearestPointByLine(self,line,pointList):

        nearestPoint=pointList[0]
        nearerPoint =pointList[1]
        nearestDistance = line.getDistanceWithPoint(pointList[0]);
        for point in pointList[1:]:
            distance = line.getDistanceWithPoint(point)
#             print "distance "+str(distance)
            if distance<nearestDistance:
                nearerPoint = nearestPoint
                nearestDistance=distance
#                 print "nearestDistance "+str(nearestDistance)
                nearestPoint = point
        #print "nearest: "+ str(nearestPoint.X)+"  "+str(nearestPoint.Y)
        #print "nearer: "+str(nearerPoint)
        #print "dfsf  d    d  %s,%s"% (nearestPoint, nearerPoint)
        
        self.nnLine.Line(nearestPoint, nearerPoint)
        intersectPoint = self.nnLine.getLineIntersectPoint(line)
        
#zan shi zhe me zuo ,qianqi 3dian ding yuan wu cha hui mian da 
        return intersectPoint
#         return  Point.Point(nearestPoint.X,line.getYfromX(nearestPoint.X)) 
    
    def errorSumSquares2(self):
        return self.fitCircle.errorSumSquares(self.pointList),self.fitCircle;
    
if __name__=='__main__':
#     pt1 = Point.Point(0,-1)
#     pt2 = Point.Point(1.414/2.0,1.414/2.0)
#     pt3 = Point.Point(13.02,153.04)
#     pt4 = Point.Point(-1.0,0)
    import math
#print     
    pt1 = Point.Point(-1.0,0.0)
    pt2 = Point.Point(-0.5,0.5)
    pt3 = Point.Point(0.25,0.75)
    pt4 = Point.Point(1.0,0.0)
    line1 = line.Line()
    line2 = line.Line()
    line1.Line(pt1, pt2)
    line2.Line(pt3,pt4)
    circle = circle.circle(X0=0.2,Y0=1)
    fitCircle = FitCircle([])
    #print fitCircle.fitOneInscribedCircle(line1,line2,circle)
#     print line1.getVerticalLineAtPoint(Point.Point(0,1.0))
#     pppp = Point.Point(1,1)
#     nnLine = line.Line()
#     nnLine.Line(pt1, pt3)
#     ppppList=[pppp]
#     pointList = [pt1,pt2,pt3,pt4,pt5]
#     fitCircle = FitCircle(pointList)
#     fitCircle.errorSumSquares2()[1]
  
    #print fitCircle.errorSumSquares2();
    #print "fdsfs"