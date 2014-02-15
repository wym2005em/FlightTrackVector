# -*- coding: UTF-8 -*- 
'''
Created on 2014年2月12日

@author: wu
'''
import sys
temp = sys.stdout
from flighttrackvector.ming.yu.wu.tool import GetOriginRadarData
from flighttrackvector.ming.yu.wu.TK import piliangFitTKexe  
import os
from flighttrackvector.ming.yu.wu.tool import resultSplit 
from flighttrackvector.ming.yu.wu.tool import exeNMap 
from flighttrackvector.ming.yu.wu.Batch import Main
from flighttrackvector.ming.yu.wu import conf
projectPath = conf.projectPath# 'D:\\huijia\\huijia\\workplace\\FlightTrackVector\\flighttrackvector\\ming\\yu\\wu\\'
#originradarDataFileName= conf.originradarDataFileName#'20100503(3)3.txt'
import os
class CMD(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.main = Main.Main()
        log = open(projectPath+'log.txt','w')
        log.truncate()
        
    def flightInformationDataNamePathCheckfunction(self,dataName): 
        #print >>temp,'zhegele???'       
        flightInformationDataNamePathCheck = os.path.exists("Batch\\flightInformation\\"+dataName+"\\")
        if flightInformationDataNamePathCheck ==True:
            print "error:the flightInformationDataNamePathCheck dic is exist ,please create another one,or change the name of the 'radarFile'.txt in the inputFile"
            return False
        return True
    def radarPathCheckfunction(self,dataName): 


        radarPath = os.path.exists(projectPath + "radarTxt\\"+str(dataName))

        if radarPath ==True:
            print >>temp,"error:the +"+ projectPath + "radarTxt\\"+dataName+" dic is exist ,please create another one,改变雷达TXT的文件名"
            print >>temp,"if you want run it ,you can only change the name of "+dataName+".txt .xls file  .ok? (Y/N)"
            r1 = str(sys.stdin.readline()).strip("\n").strip() 
            if r1=="Y":
                print >>temp,"now the dic file are"+str(os.listdir(projectPath + "Batch\\inputFile\\"))
                print >>temp,"please input the new name"
                r2 = str(sys.stdin.readline()).strip("\n").strip() 
                os.rename(projectPath + "Batch\\inputFile\\"+dataName+".txt",projectPath + "Batch\\inputFile\\"+r2+".txt")
                os.rename(projectPath + "Batch\\inputFile\\"+dataName+".xls",projectPath + "Batch\\inputFile\\"+r2+".xls")
                print >>temp,"change OK! now the dic file are"+str(os.listdir(projectPath + "Batch\\inputFile\\"))
                
            return False
        return True
    def roadPathCheckfunction(self,dataName):        
        roadpath = os.path.exists(projectPath + "Batch\\inputFile\\"+dataName+".xls")
        if roadpath ==False:
            print "error:the "+projectPath + "Batch\\inputFile\\"+dataName+".xls"+" file is not exist ,please create another one"
            return False
        return True
    
    def theONEexe(self,dataName,originradarDataFileName):
        if self.radarPathCheckfunction(dataName) and self.roadPathCheckfunction(dataName) ==True:
            self.main.one_formatTheFlight(dataName,originradarDataFileName)
            return True
        return False
    def theTWOexe(self,dataName):
        if self.flightInformationDataNamePathCheckfunction(dataName)==True:
            self.main.two_VectorAndNoiseMapexe(dataName)
            return True
        return False
    def execute(self):
        import sys 
        Description1 ="请输入雷达txt的文件名,从以下列表中选择一个  '注意：不带.txt'"
        print >>temp,Description1
        #print >>temp,os.listdir(projectPath + "Batch\\inputFile\\")
        print >>temp,[file[0:-4] for file in os.listdir(projectPath + "Batch\\inputFile\\") if str(file).find('.txt')!=-1]
        dataName = sys.stdin.readline()
        dataName = str(dataName).strip('/n').strip() 
        print >>temp,"您选择了"+str(dataName)
        Description2="选择运行服务"
        one = "1-从原始雷达信息中提取航迹信息"
        two = "2-航迹矢量化，并且得到计算结果"
        three="3-合并执行"    
        

        print >> temp,Description2
        print >> temp,one
        print >> temp,two
        print >> temp,three
        read1 = sys.stdin.readline()
        if str(read1).strip()=='1':
            self.theONEexe(dataName,str(dataName)+'.txt')
        if str(read1).strip()=='2':
            self.theTWOexe(dataName)
        if str(read1).strip()=='3':
            biaozhi = self.theONEexe(dataName,str(dataName)+'.txt')
            if biaozhi==False:
                print >>temp,"theONEexe is error"
                print "theONEexe is error"
                return 
            self.theTWOexe(dataName) 
         
if __name__ == '__main__':
    cmd = CMD()
    while 1:
        cmd.execute()