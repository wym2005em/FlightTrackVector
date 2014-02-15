import matplotlib as mpl  
import numpy as np  
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from numpy import *
from flighttrackvector.ming.yu.wu.point import Point 
from matplotlib.patches import Circle
from flighttrackvector.ming.yu.wu.fitcircle import FitCircle
from flighttrackvector.ming.yu.wu.fitline import FitLine
from flighttrackvector.ming.yu.wu.ProfInformation import ProfInf
from flighttrackvector.ming.yu.wu.ProfInformation import Segment
from flighttrackvector.ming.yu.wu.fitline import line
import flighttrackvector.ming.yu.wu.globe.gl as gl
from flighttrackvector.ming.yu.wu.ProfInformation import Segment
from flighttrackvector.ming.yu.wu.ProfInformation import ProfInf
from flighttrackvector.ming.yu.wu.ProfInformation import ProfInfToXML
from flighttrackvector.ming.yu.wu import conf

import sys
sys.stdout = open(str(conf.projectPath)+"log.txt", "a")
class LoadData:
#     runwayDic={"36R":"18L","36R":"18L","36L":"18R","18R":"36L","01":"19","19":"01"}
#     runwayLatLon={"36R":[40.0718,116.5995],"18L":[40.08891,116.5943],"36L":[40.07314,116.5735],"18R":[40.10175,116.569],"01":[40.05856,116.617],"19":[40.09253,116.6117]}
#     ZBAALocation =[40.0736,116.6033]
    

    
    map = Basemap(projection='ortho',lat_0=gl.ZBAALocation[0],lon_0=gl.ZBAALocation[1],resolution='l')
    DorA=[]
    runwayLength={}
    runwayDuankou=[]
    
    def __init__(self,pointList=[]):
        self.setRunWayLength()
#         print self.runwayLength
    
    def getLinesLengthfalseOrtrue(self,path):
        frfr0 = open(path,'r')
        Lines = frfr0.readlines()
        if len(Lines)<50:
            return "false"
        return "true"
        frfr0.close()
    
    def loadTxtAddLength(self,path):
        frfr0 = open(path,'r')
        firstLine = frfr0.readlines()[0]
        frfr0.close()
        
        frfr1 = open(path,"r+")
        
#         newLines = map(lambda x:'string'+x,lines)
        newLines=[]
        lastLine = ""
        thisLine = ""
        for i in frfr1.readlines()[1:]:
            if i[0]!=',':
                return;
            
            lastLine = thisLine
            thisLine = i
            if lastLine=="":
                thisLine = "0.0"+thisLine
            else:
                x1,y1 = self.getXYfromLatLon(thisLine.split(',')[2],thisLine.split(',')[3])
                x2,y2 = self.getXYfromLatLon(lastLine.split(',')[2],lastLine.split(',')[3])
                #print "dfsdfsdfsd"
                #print x1,y1
                pt1 =Point.Point(x1,y1)
                pt2 =Point.Point(x2,y2)
                #===============================================================
                # thisLine = thisLine.replace(thisLine.split(',')[0],'')
                # print thisLine
                # float(lastLine.split(',')[0])
                #===============================================================
                thisLine = str(float(pt1.getDistanceToOtherPoint(pt2))+float(lastLine.split(',')[0]))+thisLine
            newLines.append(thisLine)
        newLines.insert(0, firstLine)
        #print newLines
        frfr1.truncate()
        frfr1.close()
        frfr2 =open(path,'w')
        for i in newLines:
            frfr2.write(i)
        frfr2.close()
        
    #i represent row count
    def getTravelDistance(self,i,path):
        fr = open(path,'r')
        lines = fr.readlines()
        fr.close()
        if lines[0].split(",")[3]=='D':   
            paodaotou = lines[0].strip().split(",")[-1]
            #paodaowei = gl.runwayDic[paodaotou]

            
            x1,y1 = self.getXYfromLatLon(gl.runwayLatLon[paodaotou][0],gl.runwayLatLon[paodaotou][1])
            paodaotouPoint = Point.Point(x1,y1)
            
            x2,y2 = self.getXYfromLatLon(lines[1].strip().split(",")[2],lines[1].strip().split(",")[3])
            guijifirstPoint = Point.Point(x2,y2)
            rL = paodaotouPoint.getDistanceToOtherPoint(guijifirstPoint)
            #rL = self.runwayLength[str(paodaotou)+str(paodaowei)]
            line = lines[i] 
#             print str(rL)+"  dsfs  "+str(paodaotou)+str(paodaowei)
            #print "f8f8f8f888f8888  88f8f"
            #print "float:   "+str(float(rL))
            #print "float:   "+str(line.split(",")[0])
        
            return float(line.split(",")[0])+float(rL)
        else:#if shi ARR
            thisline = lines[-i-1]
            lastline = lines[-1]
            return float(lastline.split(",")[0])-float(thisline.split(",")[0])


    def loadTXTLatLonToXY(self,path):
        pointList=[]
        
        
        frfr = open(path)
        line = frfr.readlines()[0]
        self.DorA = line.strip().split(',')[3]
        self.runwayDuankou = line.strip().split(',')[6]
        self.flightNum = line.strip().split(',')[1]
        self.flightModel = line.strip().split(',')[2]
        fr = open(path)
        for line in fr.readlines()[1:-1]:
            curLine = line.strip().split(',')
#             print str(float(curLine[1]))+"  "+str(float(curLine[2]))

            x,y=self.getXYfromLatLon(float(curLine[2]),float(curLine[3]))
            point = Point.Point(x,y)
            pointList.append(point)
        
        if self.DorA=='D':
            print 'DDD'
            print len(pointList)
            return pointList,self.DorA,self.runwayDuankou,self.flightNum,self.flightModel
        if self.DorA=='A':
            print 'AAA'
            return pointList[::-1],self.DorA,self.runwayDuankou,self.flightNum,self.flightModel

    def getProfInformation(self,path):
        fr1 = open(path)
        lines = fr1.readlines()
        line = lines[0]

        lineArr = line.strip().split(',')

        DorA = lineArr[3]
        profID = lineArr[1]
        profPlaneType = "CIVILIAN"
        profPlaneID=lineArr[2]
        profPrePlaneID = ""
        profUnit = "LBS"
        profHangji = lineArr[1]
        profDay = 1.0
        profBetween = 0.0
        profNight =0.0
        profsegmentList = []            
        fr2 = open(path)
        profPush= float(5000)
        if DorA =="D":
            lines=lines[1::1]
            profPush= float(5108.901)
            segment = Segment.Segment("0","100","5108.901","VARIABLE","0",lineArr[1])
            segment2 = Segment.Segment("200","100","5108.901","VARIABLE","100",lineArr[1])
            profsegmentList.append(segment)   
            profsegmentList.append(segment2)   
        else:
            lines=lines[-1:0:-1] 
            profPush= float(12081.901)
            segment = Segment.Segment("0","100","12081.901","VARIABLE","0",lineArr[1])
            profsegmentList.append(segment)
        for linecount in range(1,len(lines),5):
            
            curLine = lines[linecount-1].strip().split(',')
            
#             print "curLine  d d d"+str(lines[-linecount])
#             print "curLine  d d d"+str(lines[linecount])
            profLength = float(self.getTravelDistance(linecount,path))
            
            #curLine = lines[linecount].strip().split(',')
            profHeight = float(curLine[4])*float(3.2808)#mi change ft

            if DorA=="A":
                profHeight=profHeight+float(500.0)
#            if DorA=="D":
#                if profHeight>400 and profHeight<1000:
#                    profHeight = profHeight-300
#                if profHeight>1000.0 and profHeight<4000:
#                    profHeight = profHeight*0.5
#                if profHeight>4000.0:
#                    profHeight = profHeight*0.8

#fe e   e e            
            
            
            profCode="VARIABLE"
            profSpeed=float(curLine[5])*float(0.5399)
            profNoiseID=profID
            segment = Segment.Segment(profLength,profHeight,profPush,profCode,profSpeed,profNoiseID)
            profsegmentList.append(segment)
        
        prof = ProfInf.ProfInf(profID,profPlaneType,profPlaneID,profPrePlaneID,profUnit,profHangji,profDay,profBetween,profNight,profsegmentList)
#         print prof
        return prof
#         for a in profsegmentList:
#             print a

    def getXYfromLatLon(self,lats,lons):
        x,y=self.map(lons,lats)
#       m changeTo YingChi()  loadTxtAddLength

#         x = x*3.28083
#         y = y*3.28083
        
    # m changeTo ft
#        x = float(x)*0.00053995
#        y = float(y)*0.00053995
    #  m changeTo HaiLi()
        x = x*3.2808
        y = y*3.2808  
        
        return x,y
    
    def getRunWayLine(self,start,end):
#         print "LoadData  "+ str(gl.runwayLatLon[start][0])
#         print "LoadData  "+str(gl.runwayLatLon[start][1])
        startx,starty = self.getXYfromLatLon(gl.runwayLatLon[start][0],gl.runwayLatLon[start][1])
        startPoint = Point.Point(startx,starty)
        endx,endy = self.getXYfromLatLon(gl.runwayLatLon[end][0],gl.runwayLatLon[end][1])
        endPoint = Point.Point(endx,endy)
        from flighttrackvector.ming.yu.wu.fitline import line
        lline = line.Line()
        lline.Line(startPoint,endPoint)
        return lline
        
            
    def drawXY(self,xMat,yMat):
        import matplotlib.pyplot as plt 
        plt.plot(xMat,yMat) 
        plt.show() 
    
    
    def runLength(self,start,end):
        x,y = self.getXYfromLatLon(gl.runwayLatLon[start][0],gl.runwayLatLon[start][1])
        startP = Point.Point(x,y)
        x,y = self.getXYfromLatLon(gl.runwayLatLon[end][0],gl.runwayLatLon[end][1])
        endP = Point.Point(x,y)
        R18L36RRunway = line.Line()
        R18L36RRunway.Line(startP,endP)

        self.runwayLength[str(start)+str(end)] = R18L36RRunway.getLineLength()
        self.runwayLength[str(end)+str(start)] = R18L36RRunway.getLineLength()
     #   print str(start)+"  dd  "+str(end)+"  dd  "+str(R18L36RRunway.getLineLength())
        
    def setRunWayLength(self):
        self.runLength("36R","18L")
        self.runLength("18L","36R")
        self.runLength("36L","18R")
        self.runLength("18R","36L")
        self.runLength("01","19")
        self.runLength("19","01")
        
        
if __name__=='__main__':
        
    l = LoadData()
    pointList = l.getProfInformation('e:/temp/linshi/a.txt')
    pitx = ProfInfToXML.ProfInfToXML(pointList)
    import codecs
    f=file('e:/test.xml', 'w')
#     f = file("book.xml","w")
  #  print pitx.getProfInfXml().toprettyxml(indent="  ", newl = '/n/r')
   # print pitx.getProfInfXml().writexml(writer =f, indent="  ", addindent="  ") 
    
    
    
    
# print
#     print len([p.X for p in pointList])
#     print pointList[0]
    #=print l1.getLength()
    #print l1.getLineIntersectionAngle(l2) 
      