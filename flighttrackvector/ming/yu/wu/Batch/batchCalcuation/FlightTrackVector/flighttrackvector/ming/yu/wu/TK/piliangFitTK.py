'''
Created on 2013-11-12

@author: wym
'''
import matplotlib
from xml.dom import minidom
matplotlib.use('TkAgg')
import os
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from flighttrackvector.ming.yu.wu.loaddata import LoadData
from flighttrackvector.ming.yu.wu.FitMain import FitMain

from matplotlib.figure import Figure
from Tkinter import *
import Tkinter as Tk
from matplotlib.patches import Circle
from flighttrackvector.ming.yu.wu.ProfInformation import ProfInfToXML 
from flighttrackvector.ming.yu.wu.loaddata import LoadData  

from flighttrackvector.ming.yu.wu import conf

import sys
sys.stdout = open(str(conf.projectPath)+"log.txt", "a")

class piliangFitTk(object):
    '''
    classdocs
    '''
    sourceResultList=[]
    fitResultList = []
    global tolSentry
    global a
    global can
    l = LoadData.LoadData()

    
        
    def addData(self):
        txtpath = self.tolSentry.get()
        self.addTravelLengthToTxt(txtpath)
        
        
    def outputFile(self):
        filePath = str(self.outputFileSentry.get())
#         print filePath
        fo = open(filePath, "a")
        fo.write(str(self.resultFormat)+"\n")
        fo.close()
        
#         filePath = str(self.outputFileSentry.get())+".xml"
# #         self.tolSentry.get()
#         fo = open(filePath, "w")
#         fo.write(str(self.resultFormat))
#         fo.close()        addData
        
        l = LoadData.LoadData()
        prinf = l.getProfInformation(self.tolSentry.get())
      #  print "fdsfsdjfjejfioa j dsa fa "+str(prinf)
        pitx = ProfInfToXML.ProfInfToXML(prinf)
        
        
        
        import codecs
#         fopen = open(str(self.outputFileSentry.get())+".xml")
        b = minidom.parse(str(self.outputFileSentry.get())+".xml")


        
        b.childNodes[0].appendChild(pitx.getProfInfXml().childNodes[0])
        
      
        f=file(str(self.outputFileSentry.get())+".xml", 'w')
        
#     f = file("book.xml","w")
#         print pitx.getProfInfXml().toprettyxml(indent="  ", newl = '/n/r')
       
        print b.writexml(writer =f, indent="  ", addindent="  ") 
        
        f.close()
        
        
        
    def draw(self,path):
        self.path = path
        l = LoadData.LoadData()
        self.pointList,self.DorA,self.paodaoDuankou,self.flightNum,self.flightModel = l.loadTXTLatLonToXY(path)
#     print pointList[0].Y
        for point in self.pointList:
            point.X = float(point.X)
            point.Y = float(point.Y)
    
            pointList2 = []
        for point in self.pointList:
            if point.X>0:
                pointList2.append(point)
        
        f = FitMain.FitMain(pointList2[::1])
# mainFit       
        self.resultFormat = f.mainFit(self.DorA,self.l,self.paodaoDuankou,self.flightNum,self.flightModel,float(0.002),float(0.01)); 
        #print "fdsfaewajfio3j902ur23qu   "+path 
        self.fitResultList = f.fitResultList
        self.sourceResultList = f.sourceResultList
        
        
        
#         self.a.cla()
#         self.drawFitPicture(self.a)
#         self.drawSourcePicture(self.a)
#         
#         self.can.draw()   

    def addTravelLengthToTxt(self,path):
        l = LoadData.LoadData()
        l.loadTxtAddLength(path)
#       getProfInfXml      
    def exeButtonCommond(self):
        txtpath = self.tolSentry.get()

        self.draw(txtpath)
        #print str(txtpath)
        
        
        
    def drawFitPicture(self,plt):

        for a in self.fitResultList:
            if(str(a).find("Line")!=-1):
                #print "Line     "+str(a.point1)+"  Line   "+str(a.point2)  
                allPoint = a.getAllImagePointListFromXRange()               
                plt.plot([point.X for point in allPoint],[point.Y for point in allPoint],"blue")
                plt.plot(a.point1.X,a.point1.Y,"o",color = "green")   
                plt.plot(a.point2.X,a.point2.Y,"o",color = "green")    
            else:
#                 allPoint = a.getAllImagePointListFromXRange()
                #print "Circle     "+str(a.firstPoint)+"  Circle   "+str(a.lastPoint)
                circle = Circle((a.X0,a.Y0),a.radius,alpha=0.25,color="red")
                plt.add_patch(circle)
      
                
                
    def drawSourcePicture(self,plt):
        plt.plot([point.X for point in self.sourceResultList],[point.Y for point in self.sourceResultList],"black",alpha=0.8) 
    
    def getFileList(self,p):
        p = str(p)
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x  for x in a if os.path.isfile( p + x ) ]
        return b
    
    
if __name__=='__main__':
#FitTK         
    #print "fdsfsdfs"
    import codecs    
    ft = piliangFitTk()
    
    #intputPath
    #path = "E:/piliangWECPLlinshi/linshi/621APP/"
    #outputPath
    #outputPath = "E:/piliangWECPLlinshi/a32132.txt";
    path = "E:/bigNoisemap/Batch/flightInformation/"
    outputPath = "E:/bigNoisemap/Batch/TrackAndProfInformation/track.txt";
    
    
    filenamelist = ft.getFileList(path)
    filelist = [path+filename for filename in filenamelist]
    for txtpath in filelist:
        try:
            l = LoadData.LoadData()
#line shu shi fou > 50  ==>   bu du qu zhe ge wen jian   ,,tiao guo
            if l.getLinesLengthfalseOrtrue(txtpath) == "false":
                continue
#line shu shi fou > 50  ==>   bu du qu zhe ge wen jian   ,,tiao guo
            
#exeButtonCommond
            ft = piliangFitTk()
            ft.draw(txtpath)
    #    print str(txtpath)
        

#addTravelLengthToTxt
        
            l.loadTxtAddLength(txtpath)

#outputFile
            filePath = str(outputPath)
     #   print filePath
            fo = open(filePath, "a")
#         fo.write(str(ft.resultFormat)+"\n")
#         fo.close()
        
#         filePath = str(self.outputFileSentry.get())+".xml"
# #         self.tolSentry.get()
#         fo = open(filePath, "w")
#         fo.write(str(self.resultFormat))
#         fo.close()        addData
#fe e   e e     
            l = LoadData.LoadData()
            prinf = l.getProfInformation(txtpath)
   #     print "fdsfsdjfjejfioa j dsa fa "+str(prinf)
            pitx = ProfInfToXML.ProfInfToXML(prinf)
    
            b = minidom.parse(str(filePath)+".xml")    
            b.childNodes[0].appendChild(pitx.getProfInfXml().childNodes[0])  

        except:
            continue        
#last shi ji write outputFile
        f=file(str(filePath)+".xml", 'w')    
        print b.writexml(writer =f, indent="  ", addindent="  ") 
        f.close()
        
        fo.write(str(ft.resultFormat)+"\n")
        fo.close()
        
        
#         fopen = open(str(self.outputFileSentry.get())+".xml")
    


        
        #621gezhongAPP36R
        
      
        
        
#     f = file("book.xml","w")
#         print pitx.getProfInfXml().toprettyxml(indent="  ", newl = '/n/r')
       
    
        
    







