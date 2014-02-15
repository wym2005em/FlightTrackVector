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
import flighttrackvector.ming.yu.wu.globe.gl as gl
from matplotlib.figure import Figure
from Tkinter import *
import Tkinter as Tk
from matplotlib.patches import Circle
from flighttrackvector.ming.yu.wu.ProfInformation import ProfInfToXML 
from flighttrackvector.ming.yu.wu.loaddata import LoadData  
from flighttrackvector.ming.yu.wu import conf

import sys
sys.stdout = open(str(conf.projectPath)+"log.txt", "a")


class FitTk(object):
    '''
    classdocs
    '''
    sourceResultList=[]
    fitResultList = []
    global tolSentry
    global a
    global can
    l = LoadData.LoadData()
#mainFit
    def __init__(self):
        
#         self.pointList,self.DorA,self.paodaoDuankou,self.flightNum,self.flightModel = self.l.loadTXTLatLonToXY('e:/temp/linshi/a.txt')
# #     print pointList[0].Y
#         for point in self.pointList:
#             point.X = float(point.X)
#             point.Y = float(point.Y)
#      
#             pointList2 = []
#         for point in self.pointList:
#             if point.X>0:
#                 pointList2.append(point)
#         f = FitMain.FitMain(pointList2[::1])
#         f.mainFit(self.DorA,self.l,self.paodaoDuankou,self.flightNum,self.flightModel);  
#         self.fitResultList = f.fitResultList
#         self.sourceResultList = f.sourceResultList
         
        root = Tk.Tk()
        root.wm_title("Embedding in TK")
        f = Figure(figsize=(5,5), dpi=100)
        self.can = FigureCanvasTkAgg(f,master=root)
        self.can.show()
        self.can.get_tk_widget().grid(row=0,columnspan=3)
        self.a = f.add_subplot(111)


        toolbar = NavigationToolbar2TkAgg( self.can, root )
        toolbar.update()
        self.can._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#         self.can._tkcanvas.grid(row=2,columnspan=5,rowspan=5)
        
        
        lineerrorLabel = Label(root,text="1. lineerror")
        lineerrorLabel.pack(anchor="w")
        self.lineErrorSentry = Entry(root)
        self.lineErrorSentry.pack(anchor="w")
        self.lineErrorSentry.insert(0, float(820000.0))#ft danwei
#         self.lineErrorSentry.insert(0, float(220000.0/10020000.0))#hai li danwei
        
        
            
        circleerrorLabel = Label(root,text="2. circleerror")
        circleerrorLabel.pack(anchor="w")
        self.circleErrorSentry = Entry(root)
        self.circleErrorSentry.pack(anchor="w")
        self.circleErrorSentry.insert(0, float(10000))#ft danwei
#         self.circleErrorSentry.insert(0, float(10000/100000.0))#hai li danwei        
        
        inputFileLabel = Label(root,text="3. Please write inputFilePath:")
        inputFileLabel.pack(anchor="w")
        self.tolSentry = Entry(root)
        self.tolSentry.insert(0, "E:/piliangWECPLlinshi/linshi")
        self.tolSentry.pack(anchor="w")
        
        exeButton = Button(root,text="calcuate",command=self.exeButtonCommond)
        exeButton.pack(anchor="w")
        
        outputFileLabel = Label(root,text="4. Please write outputFilePath:")
        outputFileLabel.pack(anchor="w")
        self.outputFileSentry = Entry(root)
        self.outputFileSentry.pack(anchor="w")
        self.outputButton = Button(root,text="outputFile",command= self.outputFile)
     
        self.outputButton.pack(anchor="w")
        
        self.addDataButton = Button(root,text="addData",command= self.addData)
        self.addDataButton.pack(anchor="w")

        Tk.mainloop()
        
    def addData(self):
        txtpath = self.tolSentry.get()
        self.addTravelLengthToTxt(txtpath)
        
        
    def outputFile(self):
        filePath = str(self.outputFileSentry.get())
       # print filePath
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


        #blue
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
        
        self.resultFormat = f.mainFit(self.DorA,self.l,self.paodaoDuankou,self.flightNum,self.flightModel,float(self.lineErrorSentry.get()),float(self.circleErrorSentry.get())); 
      #  print "fdsfaewajfio3j902ur23qu   "+path 
        self.fitResultList = f.fitResultList
        self.sourceResultList = f.sourceResultList
        
        #green
        
        self.a.cla()
        self.drawFitPicture(self.a)
        self.drawSourcePicture(self.a)
        
        self.can.draw()   

    def addTravelLengthToTxt(self,path):
        l = LoadData.LoadData()
        l.loadTxtAddLength(path)
#       getProfInfXml      
    def exeButtonCommond(self):
        txtpath = self.tolSentry.get()

        self.draw(txtpath)
      #  print str(txtpath)
        
        
        
    def drawFitPicture(self,plt):

        for a in self.fitResultList:
            if(str(a).find("Line")!=-1):
          #      print "Line     "+str(a.point1)+"  Line   "+str(a.point2)  
                allPoint = a.getAllImagePointListFromXRange()               
                plt.plot([point.X for point in allPoint],[point.Y for point in allPoint],"blue")
                plt.plot(a.point1.X,a.point1.Y,"o",color = "green")   
                plt.plot(a.point2.X,a.point2.Y,"o",color = "green")    
            else:
#                 allPoint = a.getAllImagePointListFromXRange()
          #      print "Circle     "+str(a.firstPoint)+"  Circle   "+str(a.lastPoint)
                circle = Circle((a.X0,a.Y0),a.radius,alpha=0.25,color="red")
                plt.add_patch(circle)
                
        #plt.plot(20900905.870332837,20895228.973957635,'o',color= 'black')
        
        self.drawRunWay(plt)
        
        
    def drawRunWay(self,plt):
        l = LoadData.LoadData()

        x1,y1 = l.getXYfromLatLon(gl.runwayLatLon["36R"][0],gl.runwayLatLon["36R"][1])
        x2,y2 = l.getXYfromLatLon(gl.runwayLatLon["18L"][0],gl.runwayLatLon["18L"][1])
        x3,y3 = l.getXYfromLatLon(gl.runwayLatLon["36L"][0],gl.runwayLatLon["36L"][1])
        x4,y4 = l.getXYfromLatLon(gl.runwayLatLon["18R"][0],gl.runwayLatLon["18R"][1])
        x5,y5 = l.getXYfromLatLon(gl.runwayLatLon["01"][0],gl.runwayLatLon["01"][1])
        x6,y6 = l.getXYfromLatLon(gl.runwayLatLon["19"][0],gl.runwayLatLon["19"][1])

        
        
        x =[x1,x2,x3,x4,x5,x6]
        y =[y1,y2,y3,y4,y5,y6]
        #print x
        #print y
        plt.plot(x,y,'*',color='blue') 
        
        
                         
                
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
    
import codecs    
ft = FitTk()

        
    







