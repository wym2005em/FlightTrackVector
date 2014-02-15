from flighttrackvector.ming.yu.wu.point import Point 
import math        
from scipy import * 
class Line:
    def __init__(self, a = 0.0, b = 0.0, c = 0.0):
        self.A = a + 0.0
        self.B = b + 0.0
        self.C = c + 0.0
    
    def __repr__(self):
        return '[Line:(%s)x + (%s)y + (%s)=0::::(%s)]' % (self.A, self.B, self.C,self.getLength())
    
     
    #return [Y,X]    
    def getUnitVector(self):
        return [(self.point2.Y-self.point1.Y)/self.getLineLength(),(self.point2.X-self.point1.X)/self.getLineLength()]
    
    #return [X,Y]
    def getVector(self):
        return [(self.point2.X-self.point1.X),(self.point2.Y-self.point1.Y)]

    def pointAtVectorLeftOrRight(self,point):
        l1=Line()
        l2=Line()
        l3=Line()
        l1.Line(self.point1,point)
        l2.Line(point,self.point2)
        l3.Line(self.point2,self.point1)
        l1Vector = l1.getVector()
        l2Vector = l2.getVector()
        l3Vector = l3.getVector()
#         (x1-x3)*(y2-y3) - (y1-y3)(x2-x3)
        S = (l1Vector[0]-l3Vector[0])*(l2Vector[1]-l3Vector[1])-(l1Vector[1]-l3Vector[1])*(l2Vector[0]-l3Vector[0])
        if S==0:
            return "on"
        if S<0:
            return "zuo"
        if S>0:
            return "you"
    
    
    def getLineLength(self):
        import math
        return math.sqrt((self.point2.Y-self.point1.Y)*(self.point2.Y-self.point1.Y)+(self.point2.X-self.point1.X)*(self.point2.X-self.point1.X))
        
    def Line(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
#         print point2
# #         print "((%s)x,  (%s)y)"%(point2.Y,point1.Y) 
#         self.A = point2.Y - point1.Y
#         self.B = -(point2.X - point1.X)
#         self.C = (point2.X - point1.X)*point1.Y - point1.X*(point2.Y - point1.Y)
#        
        #print point2.X
        #print point1.X
        self.k = float(point2.Y-point1.Y)/float(point2.X-point1.X)
        self.b = float(point1.Y)-self.k*float(point1.X)
        self.A=self.k
        self.B=-1
        self.C=self.b
        
        return (self.A, self.B, self.C)
    
    # return 0: point out of the line ***zhixian
    # return 1: point on  the line  ***zhixian
    def getRelationshipBetweenPointAndLine(self,point):
        if str(self.getYfromX(point.X))!=str(point.Y):
            return 0
        else:
            return 1
    
    #hidden danger
    def ifJiaodianPointOnThelineSegment(self,line2):
        jiaodianPoint = self.getLineIntersectPoint(line2)
        line1smallX=self.point1.X
        line1bigX=self.point2.X
        line2smallX=line2.point1.X
        line2bigX=line2.point2.X
        if self.point1.X>self.point2.X:
            line1smallX=self.point2.X
            line1bigX=self.point1.X
        if line2.point1.X>line2.point2.X:
            line2smallX=line2.point2.X
            line2bigX=line2.point1.X
       # print str(jiaodianPoint.X)+"  ddd232323  "+str(line2smallX)+ "  ddd  "+str(line2bigX)
        if (jiaodianPoint.X>=line1smallX) and (jiaodianPoint.X<=line1bigX):
            return "yes"
        if (jiaodianPoint.X>=line2smallX) and (jiaodianPoint.X<=line2bigX):    
            return "yes"
        return "no"
            
#find     
    def getLineIntersectPoint(self,line):
        a1=self.A
        b1=self.B
        c1=self.C
        a2=line.A
        b2=line.B
        c2=line.C
        m = float(self.A)*float(line.B)-float(line.A)*float(self.B)
        if m == 0: 
            print "wrong" 
            return;  
        x = float(c2 * b1 - c1 * b2) / m;
        y = float(c1 * a2 - c2 * a1) / m;   
        p = Point.Point(x, y);
        return p
    
    def getVerticalLineAtPoint(self,point):
        if str(self.getYfromX(point.X))!=str(point.Y):
           # print str(self.getYfromX(point.X))+"ddddd"+str(point.Y)
            print "error: point not On the line"
            return 
        lll = Line()
        k=-1/self.k
        b=point.Y-k*point.X
        y=k*0.10101+b
        lll.Line(point, Point.Point(0.10101,y))
        return lll
            
    
    def getLength(self):
        return math.sqrt((self.point2.X-self.point1.X)*(self.point2.X-self.point1.X)+(self.point2.Y-self.point1.Y)*(self.point2.Y-self.point1.Y))
    
    def errorSumSquares(self,pointList):
        errorSum=0
        for point in pointList:
#             errorSum=errorSum+(self.getYfromX(point.X)-point.Y)*(self.getYfromX(point.X)-point.Y)
            errorSum=errorSum+self.getDistanceWithPoint(point)*self.getDistanceWithPoint(point)
        return errorSum/len(pointList)
    
    def getYfromX(self,yuceX):
#         return ((yuceX-self.point1.X)*(self.point2.Y-self.point1.Y))/(self.point2.X-self.point1.X)+self.point1.Y
        return -self.A/self.B*yuceX-self.C/self.B
 
    
    def returnPerpendicularBisector(self):
#         k= (self.point1.Y-self.point2.Y)/(self.point1.X-self.point2.X)
#         k=-1/k
#         zhongpoint = Point.Point((self.point1.X+self.point2.X)/2,(self.point1.Y+self.point2.Y)/2)
#         b=zhongpoint.Y-k*zhongpoint.X
#         A=1
#         B=-k
#         C=-b
        k=self.B/self.A
        point = Point.Point(float((self.point1.X+self.point2.X)/2.0),float((self.point1.Y+self.point2.Y)/2.0))
        C=(point.Y-point.X*self.B/self.A)*self.A
        A=self.B
        B=-self.A
        #print -self.B/self.A
        #print -B/A
        #print "fdfsdfsdffffffffffffff"
        l=Line(A,B,C)
        
        #print str(self.point1.Y)+" point1Xpoint2X "+str(self.point2.Y)
        #print str((self.point1.Y+self.point2.Y)/2.0)+"  yinggaixiangdeng   "+str(l.getYfromX((self.point1.X+self.point2.X)/2.0))
        l.point1 = Point.Point((float(self.point1.X)+float(self.point2.X))/2,self.getYfromX((float(self.point1.X)+float(self.point2.X))/2))
        l.point2 = Point.Point((float(self.point1.X)+float(self.point2.X))/2-1,l.getYfromX((float(self.point1.X)+float(self.point2.X))/2-1))
        
#         A=self.point2.Y-self.point1.Y
#         B=self.point1.X-self.point2.X
#         C=self.point2.X*self.point1.Y-self.point1.X*self.point2.Y
#         l=Line(A,B,C)
#         l.point1 = Point.Point((float(self.point1.X)+float(self.point2.X))/2,(float(self.point1.Y)+float(self.point2.Y))/2)
#         l.point2 = Point.Point((float(self.point1.X)+float(self.point2.X))/2+5,self.getYfromX((float(self.point1.X)+float(self.point2.X))/2+5))
#         
        return l
    
    def getDistanceWithPoint(self,point):
        return abs(self.A*point.X+self.B*point.Y+self.C)/math.sqrt(self.A*self.A+self.B*self.B)
    
    def getLineMidPoint(self):
        xzhong = (self.point1.X+self.point2.X)/2
        yzhong = (self.point1.Y+self.point2.Y)/2
        p = Point.Point(xzhong,yzhong)
        return p
    
    #cos       
    def getLineIntersectionAngle(self,line2):
        #print '(%s,%s)'%(self.point1.X,self.point2.X)
                 
        ll= Line()
        ll.Line(self.point1, line2.point2)
        #pointToLine = ll.getDistanceWithPointline2(self.point2)
        #print line2.getLength()
        X1 = self.point2.X-self.point1.X
        X1 = -X1
        Y1 = self.point2.Y-self.point1.Y
        Y1 = -Y1
        X2 = line2.point2.X-line2.point1.X
        Y2 = line2.point2.Y-line2.point1.Y
        cos = (X1*X2+Y1*Y2)/(math.sqrt(X1*X1+Y1*Y1)*math.sqrt(X2*X2+Y2*Y2))
        
        #a/math.sin()
       
        print cos
#         return 180-math.degrees(math.acos(cos))
        return math.degrees(math.acos(cos))
        #self.point1  line2.point1
        #self.getLength()*self.getLength()
        
#         k1 = (self.point1.Y-self.point2.Y)/(self.point1.X - self.point2.X)
#         k2 = (line2.point1.Y-line2.point2.Y)/(line2.point1.X - line2.point2.X)
#         angle1 = math.atan(k1)/(math.pi/180)
#         angle2 = math.atan(k2)/(math.pi/180)
#         print angle1
#         print angle2
# #         if k1<0:
# #             angle1 =angle1+180
# #         if k2<0:
# #             angle2 =angle2+180
       #return abs(angle1-angle2)
    
    
    
#     ar k1:Number = (line1.y1-line1.y2)/(line1.x1-line1.x2);
#                 var k2:Number = (line2.y1-line2.y2)/(line2.x1-line2.x2);
#                 var angle1:Number = Math.abs(Math.atan(k1)/(Math.PI/180));
#                 var angle2:Number = Math.abs(Math.atan(k2)/(Math.PI/180));
#         
    def errorSumSquares2(self,pointList):
        l1=Line()
        l1.Line(pointList[0], pointList[-1])
        return l1.errorSumSquares(pointList)


 
    listlist=[]
    def getAllImagePointListFromXRange(self):
        listlist=[]
        pointList=[]
        min =0
        max=0
        fuhao=0
#         if (self.point1.X-self.point2.X)<0:
#             min = self.point1.X
#             max = self.point2.X
#         else:
#             max = self.point1.X
#             min = self.point2.X
        
        if(self.point1.X-self.point2.X)<0:
            fuhao=1
        else:
            fuhao=-1
        #print max
        #print min
        
        listlist = list(arange(float(self.point1.X),float(self.point2.X),fuhao*1.0))

        listlist.append(float(self.point2.X))

        for x in listlist:
            pointList.append(Point.Point(x,self.getYfromX(x)))
        return pointList
    
    
    
                   
if __name__=='__main__':
        
#     pointList = []
#     from scipy import *
#     from scipy import *
#     for i in arange(-10,5,0.1):
#         pointList.append(Point.Point(float(i),float(i*i)))
#    # print pointList
# #     pointList[1]=Point.Point(float(1),float(0))
# #     pointList[2]=Point.Point(float(0),float(1))
#     #print pointList    
#     
#     from flighttrackvector.ming.yu.wu.fitline import FitLine 
# 
#     fitLine = FitLine.FitLine(pointList)
#     linePointList = fitLine.errorSumSquares2()[1].getAllImagePointListFromXRange()
#     
#     import matplotlib.pyplot as plt 
#     
#     lll = Line()
#     lll.Line(pointList[0], pointList[-1])
#     lllPointList = lll.getAllImagePointListFromXRange()
#     lllperpendicularPointList = lll.returnPerpendicularBisector().getAllImagePointListFromXRange();
#     
#     plt.plot([point.X for point in lllperpendicularPointList],[point.Y for point in lllperpendicularPointList],'or') 
#     plt.plot([point.X for point in pointList],[point.Y for point in pointList],'or')
#     plt.plot([point.X for point in linePointList],[point.Y for point in linePointList],"black")
#     plt.show() 
    #print fitLine.errorSumSquares2()[0]
#getLineLength     
    
    p1 = Point.Point(-1,0.0)
    p2 = Point.Point(0,1.0)
    p3 = Point.Point(0.5,1.0)
    p4 = Point.Point(1.0,1.0)  
    l1 = Line()
    l2 = Line()
    l1.Line(p1,p2)
    
    l2.Line(p3,p4)
    #print l1.getLineIntersectionAngle(l2)
    
#     print l1.pointAtVectorLeftOrRight(p4)
   
        
    