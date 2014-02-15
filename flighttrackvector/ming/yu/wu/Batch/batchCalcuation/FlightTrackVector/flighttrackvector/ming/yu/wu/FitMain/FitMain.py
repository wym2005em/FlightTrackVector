'''
Created on 2013-10-31

@author: wym
'''
from matplotlib.patches import Circle
from flighttrackvector.ming.yu.wu.fitcircle import FitCircle
from flighttrackvector.ming.yu.wu.fitline import FitLine
from flighttrackvector.ming.yu.wu.loaddata import LoadData
from flighttrackvector.ming.yu.wu.fitline import line
from flighttrackvector.ming.yu.wu.point import Point
import flighttrackvector.ming.yu.wu.globe.gl as gl
from flighttrackvector.ming.yu.wu.FitMain import RunOutPut
from flighttrackvector.ming.yu.wu import conf

import sys
sys.stdout = open(str(conf.projectPath)+"log.txt", "a")
class FitMain(object):
    step=5
    sourceResultList=[]
    fitResultList = []

    def __init__(self,pointList):
        self.pointList = pointList
        self.sourceResultList = pointList 
    def mainFit(self,DorA,loadData,paodaoDuankou,flightNum,flightModel,lineError,circleError):    
        startPointIndex = 0
        import matplotlib.pyplot as plt 
#         fig = plt.figure(figsize=(6,6))
#         ax = plt.subplot(111)
        resultList = self.mainFit2(plt,lineError,circleError)#first Iteration
#         plt.plot([point.X for point in self.pointList],[point.Y for point in self.pointList],"black",alpha=0.8) 
        #print resultList
        import types 
        
#         for a in resultList:
#             if(str(a).find("Line")!=-1):
#                 allPoint = a.getAllImagePointListFromXRange()
#                 print "zhixian     "+str(a.point1)+"  fdfds   "+str(a.point2)
# #                 plt.plot([point.X for point in allPoint],[point.Y for point in allPoint],'o',color="green")
#                 
#             else:
#                 allPoint = a.getAllImagePointListFromXRange()
#                 circle = Circle((a.X0,a.Y0),a.radius,alpha=0.25)
# #                 ax.add_patch(circle)
# 
        #print "111   "+str(resultList)



#blue

        #chu li you wen ti de hangxian  difficultPath
        rangeLenResultListM2 =range(0,len(resultList)-2)
        for i in rangeLenResultListM2:
            if str(resultList[i]).find("Line")!=-1: 
                fitCircle = FitCircle.FitCircle([])
                circle,biaoji = fitCircle.fitOneInscribedCircle(resultList[i],resultList[i+2])
                if biaoji.find("difficultPath")!=-1:
                    from flighttrackvector.ming.yu.wu.fitcircle import circle
                    lllLine = line.Line()
                    lllLine.Line(resultList[i].point1,resultList[i+2].point2)
                    resultList[i]=lllLine
                    resultList[i+1]=circle.circle()
                    resultList[i+2]=lllLine
                    del resultList[i+2]
                    del rangeLenResultListM2[-1]
                    del resultList[i+1]
                    del rangeLenResultListM2[-1]
        for i in rangeLenResultListM2:
            if str(resultList[i]).find("Line")!=-1: 
                fitCircle = FitCircle.FitCircle([])
                circle,biaoji = fitCircle.fitOneInscribedCircle(resultList[i],resultList[i+2])
                if biaoji.find("difficultPath")!=-1:
                    from flighttrackvector.ming.yu.wu.fitcircle import circle
                    lllLine = line.Line()
                    lllLine.Line(resultList[i].point1,resultList[i+2].point2)
                    resultList[i]=lllLine
                    resultList[i+1]=circle.circle()
                    resultList[i+2]=lllLine
                    del resultList[i+2]
                    del rangeLenResultListM2[-1]
                    del resultList[i+1]
                    del rangeLenResultListM2[-1]
        for i in rangeLenResultListM2:
            if str(resultList[i]).find("Line")!=-1: 
                fitCircle = FitCircle.FitCircle([])
                circle,biaoji = fitCircle.fitOneInscribedCircle(resultList[i],resultList[i+2])
                if biaoji.find("difficultPath")!=-1:
                    from flighttrackvector.ming.yu.wu.fitcircle import circle
                    lllLine = line.Line()
                    lllLine.Line(resultList[i].point1,resultList[i+2].point2)
                    resultList[i]=lllLine
                    resultList[i+1]=circle.circle()
                    resultList[i+2]=lllLine
                    del resultList[i+2]
                    del rangeLenResultListM2[-1]
                    del resultList[i+1]
                    del rangeLenResultListM2[-1]                    
                 
                 
                    
             
        #waijieCircle change neiqieCircle                            
        for i in rangeLenResultListM2:
            #print "resultList:  "+str(i)+"   "+str(resultList[i])+"shifou   "+str(str(resultList[i]).find("Line"))
            
            if str(resultList[i]).find("Line")!=-1:

                list=[resultList[i],resultList[i+1],resultList[i+2]]#i is firstLine and i+2 is secondLine,i+1 is Circle
                fitCircle = FitCircle.FitCircle([])
                circle,biaoji = fitCircle.fitOneInscribedCircle(resultList[i],resultList[i+2])
                #print "fdsfsdfesfes fsea fesa "+str(biaoji)+str(circle)
#                 if biaoji.find("difficultPath")!=-1:
#                     from flighttrackvector.ming.yu.wu.fitcircle import circle
#                     lllLine = line.Line()
#                     lllLine.Line(resultList[i].point1,resultList[i+2].point2)
#                     resultList[i]=lllLine
#                     resultList[i+1]=circle.circle()
#                     resultList[i+2]=lllLine
#                     del resultList[i+2]
#                     del rangeLenResultListM2[-1]
#                     del resultList[i+1]
#                     del rangeLenResultListM2[-1]
#                     print "ddddddfffffffdd"+ str(lllLine.point1)+str(lllLine.point2)
#                     continue
                #discuss the position of circle.lastPoint with the secondLine
                resultList[i+1]=circle
                #print str(biaoji)+"   ddd   "+str(biaoji.find("firstLineNear"))+ "  dfdf33333333333333333333333d "
                if biaoji.find("firstLineNear")!=-1:
                    
                    lllLine=line.Line()
                    
                    lllLine.Line(resultList[i+1].lastPoint,resultList[i+2].point2)
                    
                    lllLine2 = line.Line()
                    lllLine2.Line(resultList[i+2].point1,resultList[i+2].point2)

                    #print str(resultList[i+1].lastPoint)+"   fdffdfdsdfsfdsafda   "+str(resultList[i+2].point1)
                    #print str(lllLine) +" ffffffffff  "+str(lllLine2)
                    #print str(resultList[i+1].lastPoint)+"    fssssssssssssss     " + str(resultList[i+2].point2)
                    #print str(resultList[i+2].point1)+"    fssssssssssssss     " + str(resultList[i+2].point2)
                    #print str(resultList[i+2])+"    fsdddddddddddddd     " + str(lllLine)
                    resultList[i+2]=lllLine
            
                if biaoji.find("secondLineNear")!=-1:
                    lll=line.Line()
                    #print "sssssssssdd     "+str(i)+"    "+str(resultList[i].point1)+"  "+str(resultList[i+1].firstPoint)
                    lll.Line(resultList[i].point1,resultList[i+1].firstPoint)
                    resultList[i]=lll
        #print "222   "+str(resultList)
              #111  
                
        self.becauseDorAresultListChange(resultList,DorA,loadData,paodaoDuankou)        
#find                 
        #View the neijieCircle         
        for a in resultList:
            if(str(a).find("Line")!=-1):
                print "Line"
               # print "Line     "+str(a.point1)+"  Line   "+str(a.point2)  
                allPoint = a.getAllImagePointListFromXRange()               
#                 plt.plot([point.X for point in allPoint],[point.Y for point in allPoint],"blue")
#                 plt.plot(a.point1.X,a.point1.Y,"o",color = "green")   
#                 plt.plot(a.point2.X,a.point2.Y,"o",color = "green")    
            else:
#                 allPoint = a.getAllImagePointListFromXRange()
               # print "Circle     "+str(a.firstPoint)+"  Circle   "+str(a.lastPoint)
                circle = Circle((a.X0,a.Y0),a.radius,alpha=0.25,color="red")
#                 ax.add_patch(circle)
        #runway bian de hang ji  chu li
      #  print "s s s  s" +str((resultList))
        #print "fdfe 34 34 "
        #print resultList
        self.runwayNextGuiji(DorA,paodaoDuankou,resultList,loadData);
        #print resultList
        self.fitResultList = resultList
        
        
        runoutput = RunOutPut.RunOutPut(resultList)
        #print runoutput.getNoisemapFormat(paodaoDuankou,flightNum,flightModel)
        
        
        return runoutput.getNoisemapFormat(paodaoDuankou,flightNum,flightModel)
#         plt.show() 



    def runwayNextGuiji(self,DorA,paodaoDuankou,resultList,loadData): 
        if DorA=="A":
            ranges = range(0,len(resultList))
            for obj in ranges:
                if str(resultList[obj]).find("Line")!=-1:
                    
                    x,y = loadData.getXYfromLatLon(gl.runwayLatLon[paodaoDuankou][0],gl.runwayLatLon[paodaoDuankou][1])
                    pp = Point.Point(x,y)
                    
                    lll=line.Line()
                    #print "sssssssssdd     "+str(i)+"    "+str(resultList[i].point1)+"  "+str(resultList[i+1].firstPoint)
                    lll.Line(pp,resultList[obj].point2)
                    resultList[obj] = lll
                    break;   
        
            
    def mainFit2(self,plt,lineError,circleError):
        resultList=[]
        lines=[]
        linesErrorSum=[]
        circles=[]
        circlesErrorSum=[]
        switchLine = 1
        startPointIndex=0
        step=5
        for i in range(10,len(self.pointList),step):
         #   print str(startPointIndex)+ "sss  " +str(i)
          #  print str(self.pointList[i].X)+"  XYXY "+str(self.pointList[i].Y)
            if(switchLine==1):
                fitline = FitLine.FitLine(self.pointList[startPointIndex:i+1])
                errorSum,line = fitline.errorSumSquares2()
                lines.append(line)
                linesErrorSum.append(errorSum)
                print "lineError "+str(errorSum)
                if len(lines)==1:
                    continue
#                 if errorSum/(linesErrorSum[-2])>5:#error is so big
#                 if errorSum>220000.0/10020000.0:
              #  print errorSum,lineError
                if errorSum>lineError:                
#                     plt.plot(self.pointList[startPointIndex].X,self.pointList[startPointIndex].Y,'o',color='red',alpha=0.55)
#                     plt.plot(self.pointList[i-step].X,self.pointList[i-step].Y,'o',color='black',alpha=0.55)
                 #   print str(startPointIndex) +": "+str(i-step)
                    fitline = FitLine.FitLine(self.pointList[startPointIndex:i-step+1])
                    #print "Line  startPointIndex:   "+str(startPointIndex)+"Line  endPointIndex    "+str(i-step+1)
                    lineline = fitline.errorSumSquares2()[1]
                    plt.plot(self.pointList[startPointIndex].X,self.pointList[startPointIndex].Y,'o',color='red',alpha=0.55)
                    plt.plot(self.pointList[i-step].X,self.pointList[i-step].Y,'o',color='black',alpha=0.55)
                    
                     #green
                    switchLine=0
                    startPointIndex = i-step
                    resultList.append(lineline)
                    
#                     linePointList = line.getAllImagePointListFromXRange()
#                     plt.plot([point.X for point in linePointList],[point.Y for point in linePointList],"green")
                    continue
            if(switchLine==0):
                
               # print "fdsfsd   "+str(startPointIndex)+"  " +str(i) 
                fitCircle = FitCircle.FitCircle(self.pointList[startPointIndex:i+1])
                errorSum,circle = fitCircle.errorSumSquares2()
                circles.append(circle)
                circlesErrorSum.append(errorSum)
                print "circleError "+str(errorSum)
                if len(circles)==1:
                    continue
#                 if errorSum/circlesErrorSum[-2]>5:
#                 if errorSum>10000/100000.0 and (circle.radiusAngle>10):
                if errorSum>circleError and (circle.radiusAngle>10):    
                 #   print str(startPointIndex) +": "+str(i-step)
#getLineIntersectionAngle                    
                    fitCircle = FitCircle.FitCircle(self.pointList[startPointIndex:i-step+1])
                  #  print "Circle  startPointIndex:   "+str(startPointIndex)+"Circle  endPointIndex    "+str(i-step+1)                    
                    criclecircle = fitCircle.errorSumSquares2()[1]
                    plt.plot(self.pointList[startPointIndex].X,self.pointList[startPointIndex].Y,'o',color='black',alpha=0.85)
                    plt.plot(self.pointList[i-step].X,self.pointList[i-step].Y,'o',color='black',alpha=0.85)
                    
                    switchLine=1
                    startPointIndex = i-step
        
                    resultList.append(criclecircle)

#                     circlePointList = circle.getAllImagePointListFromXRange()
#                     plt.plot([point.X for point in circlePointList],[point.Y for point in circlePointList],"black")
                    continue
                
                
                
                
#resultList ==0  is    error set too big  OR   the   HangJi is so short        
        if len(resultList)==0:
            resultList.append(lines[-1])
#resultList ==0  is    error set too big  OR   the   HangJi is so short             
            
            
            
        return resultList
    
        #self.fit        
    def fit(self):
        fitline = FitLine.FitLine(self.pointList)
        fitCircle = FitCircle.FitCircle(self.pointList)
        linePointList = fitline.errorSumSquares2()[1].getAllImagePointListFromXRange()
        niheyuan = fitCircle.errorSumSquares2()[1]
        #circlePointList = niheyuan.getAllImagePointListFromXRange()
        import matplotlib.pyplot as plt 
        
        fig = plt.figure(figsize=(6,6))
        ax = plt.subplot(111)
        circle = Circle((niheyuan.X0,niheyuan.Y0),niheyuan.radius)
        ax = plt.subplot(111)
        circle = Circle((niheyuan.X0,niheyuan.Y0),niheyuan.radius,fc ="black")
        ax.add_patch(circle)
        #plt.plot([point.X for point in circlePointList],[point.Y for point in circlePointList],"black") 
        plt.plot([point.X for point in pointList],[point.Y for point in pointList],"blue") 
        plt.plot([point.X for point in linePointList],[point.Y for point in linePointList],"red") 
     #   print "line squares:" +str(fitline.errorSumSquares2()[0])
     #   print "circle squares "+str(fitCircle.errorSumSquares2()[0])
        plt.show() 
    
    def becauseDorAresultListChange(self,resultList,DorA,loadData,paodaoDuankou):
        linyiduanNameDuankou = gl.runwayDic[paodaoDuankou]
        gl.runwayLatLon[linyiduanNameDuankou]
        if DorA=="A":
            runwayVector = loadData.getRunWayLine(linyiduanNameDuankou,paodaoDuankou)
            fitCircle = FitCircle.FitCircle([])

            circle,biaoji = fitCircle.fitOneInscribedCircle(runwayVector,resultList[0])
            resultList.insert(0,circle)
            resultList.insert(0,runwayVector)
            self.changeLineWithCircleBiaoJi(resultList,0,biaoji)
            del resultList[0]
       #     print "aaaaaaaaaaaaaaa  aa"+str(biaoji)
        if DorA=='D':
            runwayVector = loadData.getRunWayLine(paodaoDuankou,linyiduanNameDuankou)
            fitCircle = FitCircle.FitCircle([])
#             print "  d d d d    "+str(resultList[0])+"   " +str(line)
        #    print "sdsdfsdfsdaf dsa fds fdsa  "+str(resultList[0].point1)
        #    print "sdsdfsdfsdaf dsa fds fdsa222  "+str(runwayVector.point2)
            circle,biaoji = fitCircle.fitOneInscribedCircle(runwayVector,resultList[0])
        #    print "biaoji biaoji biaoji "+biaoji
         #   print "sdsdfsdfsdaf dsa fds fdsa  "+str(resultList[0].point1)
         #   print "sdsdfsdfsdaf dsa fds fdsa222  "+str(runwayVector.point2)
            resultList.insert(0,circle)
            resultList.insert(0,runwayVector)
            self.changeLineWithCircleBiaoJi(resultList,0,biaoji)
          #  print "aaaaaaaaaaaaaaa  aa2"+str(biaoji)
            
            
            
    def changeLineWithCircleBiaoJi(self,resultList,i,biaoji):
        if biaoji.find("firstLineNear")!=-1:
            lllLine=line.Line()
            lllLine.Line(resultList[i+1].lastPoint,resultList[i+2].point2)
            lllLine2 = line.Line()
            lllLine2.Line(resultList[i+2].point1,resultList[i+2].point2)
            resultList[i+2]=lllLine
            
        if biaoji.find("secondLineNear")!=-1:
            lll=line.Line()
            lll.Line(resultList[i].point1,resultList[i+1].firstPoint)
            resultList[i]=lll
            
            
     


        
if __name__=='__main__':

    
    
    l = LoadData.LoadData()
    pointList,DorA,paodaoDuankou,flightNum,flightModel = l.loadTXTLatLonToXY('e:/temp/linshi/a.txt')
#     print pointList[0].Y
    for point in pointList:
        point.X = float(point.X)
        point.Y = float(point.Y)
    
    pointList2 = []
    for point in pointList:
        if point.X>0:
            pointList2.append(point)
    f = FitMain(pointList2[::1])
    
    print f.mainFit(DorA,l,paodaoDuankou,flightNum,flightModel);    
                