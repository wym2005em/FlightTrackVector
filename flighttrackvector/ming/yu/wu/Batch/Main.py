'''
Created on 2014 1 28

@author: wu
'''
from flighttrackvector.ming.yu.wu.tool import GetOriginRadarData
from flighttrackvector.ming.yu.wu.TK import piliangFitTKexe  
import os
from flighttrackvector.ming.yu.wu.tool import resultSplit 
from flighttrackvector.ming.yu.wu.tool import exeNMap 
from flighttrackvector.ming.yu.wu import conf

import sys
sys.stdout = open(str(conf.projectPath)+"log.txt", "a")

projectPath =conf.projectPath# 'D:\\huijia\\huijia\\workplace\\FlightTrackVector\\flighttrackvector\\ming\\yu\\wu\\'
####!!!   originradarDataFileName must be same as the arg of exucute(arg)  exclude the .txt  

class Main(object):
    '''
    run with all the project 
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        print 'init'
        
        
    #dataName is link to the roadInformation .xls File  the JAR file input output:
    #String inputPath = args[0]+"Batch//inputFlightNumAndDate.txt";
    #String outputPath = args[0]+"Batch//flightInformation//args[1]//";
    #String radarpath = args[0]+"Batch//radarTxt//"+args[1];
    #String roadpath = args[0]+"Batch//inputFile//"+args[1]+".xls";
    #args[0]=projectPath
    #args[1]=dataName
    #create the file in the inputFile dictor...
    def execute(self,dataName,originradarDataFileName):
        print "check"
        import os
        formatTrackCheck = os.path.exists(projectPath+"Batch\\FormatTrack.jar")
        if formatTrackCheck == False:
            print "error:FormatTrack is not exist"
            return
        flightInformationDataNamePathCheck = os.path.exists("Batch\\flightInformation\\"+dataName+"\\")
        if flightInformationDataNamePathCheck ==True:
            print "error:the flightInformationDataNamePathCheck dic is exist ,please create another one"
            return
          #radarPath = projectPath + "Batch//radarTxt//"+dataName
        radarPath = os.path.exists(projectPath + "\\radarTxt\\"+dataName)
        if radarPath ==True:
            print "error:the radarPath dic is exist ,please create another one"
            return
        roadpath = os.path.exists(projectPath + "Batch\\inputFile\\"+dataName+".xls")
        if roadpath ==False:
            print "error:the .xls file is not exist ,please create another one"
            return
        self.one_formatTheFlight(dataName,originradarDataFileName)
        self.two_VectorAndNoiseMapexe(dataName)
       
       
       
    def one_formatTheFlight(self,dataName,originradarDataFileName):
                #delete all the resultSplit
        import os
        for filename in os.listdir(projectPath+"Batch"):
            if str(filename).find('resultSplit')!=-1:
                os.remove(projectPath+"Batch//"+filename)
    #delete all the resultSplit        
        print "1"
        os.mkdir(projectPath + "\\radarTxt\\"+dataName)
        os.mkdir(projectPath+"Batch\\flightInformation\\"+dataName)
        gor = GetOriginRadarData.GetOriginRadarData()
        gor.get(projectPath+'Batch\\inputFile\\'+originradarDataFileName,projectPath+"radarTxt\\"+dataName+"\\")
        import jpype 
        print "2"
        os.popen("java -jar "+projectPath+"Batch\\FormatTrack.jar "+projectPath +" "+dataName)#execute FormatTack.jar
        
    def two_VectorAndNoiseMapexe(self,dataName):
        print "3"
        os.popen("del "+projectPath+"Batch\\TrackAndProfInformation\\track.txt")
        os.popen("del "+projectPath+"Batch\\TrackAndProfInformation\\track.txt.xml")
        os.popen("xcopy "+projectPath+"Batch\\TrackAndProfInformation\\copy\\track.txt "+projectPath+ "Batch\\TrackAndProfInformation\\")
        os.popen("xcopy "+projectPath+"Batch\\TrackAndProfInformation\\copy\\track.txt.xml " +projectPath+"Batch\\TrackAndProfInformation\\")
        piliangFitTKexe.execute(projectPath+"Batch\\flightInformation\\"+dataName+"\\",projectPath+"\\Batch\\TrackAndProfInformation\\track.txt")
        os.popen("del "+projectPath+"Batch\\result.txt")
        os.popen("copy "+projectPath+"Batch\\TrackAndProfInformation\\copy\\result.txt "+projectPath+"Batch\\")
        os.popen("start "+projectPath+"Batch\\TrackAndProfInformation\\execute.exe")
        
        import time
        time.sleep(2)
        print "4"
        #split("D:\\huijia\\huijia\\workplace\\FlightTrackVector\\flighttrackvector\\ming\\yu\\wu\\Batch\\","D:\\huijia\\huijia\\workplace\\FlightTrackVector\\flighttrackvector\\ming\\yu\\wu\\Batch\\flightDat\\")
        resultSplit.split(projectPath+"Batch\\",projectPath +"Batch\\flightDat\\")
        print "5"
        beijingopxPath = projectPath+'NMap\\beijing.opx'
        splitFilePath=projectPath+"Batch\\"
        fileOutPath=projectPath+'NMap\\tempbopsresult.txt'
        beijingopxfilePath = projectPath+'NMap\\beijing.opx'
        runBeijingNMapPath = projectPath+'NMap\\runBeijingNMap.bat'
        tempbopsPoiPath = projectPath+'NMap\\tempbops.poi'
        #tempbopsresultPath = projectPath+'NMap\\tempbopsresult.txt'
        tempbopsresultPath = conf.tempbopsresultPath
        resultfilePath = projectPath+'NMap\\tempbopsresult.txt'
        exenMap = exeNMap.exeMap()
        exenMap.execute(beijingopxPath, splitFilePath, fileOutPath, beijingopxfilePath, runBeijingNMapPath, tempbopsPoiPath, tempbopsresultPath, resultfilePath)
        
        print "end"
           
         

        
if __name__ == '__main__':
    main = Main()
    main.execute("20100503(2)",'20100503(3)3.txt')