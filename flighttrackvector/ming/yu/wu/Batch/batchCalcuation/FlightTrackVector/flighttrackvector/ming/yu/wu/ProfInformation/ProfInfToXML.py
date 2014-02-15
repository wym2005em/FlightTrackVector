'''
Created on 2013-11-24

@author: wym
'''
from xml.dom import minidom
from flighttrackvector.ming.yu.wu.ProfInformation import ProfInf
class ProfInfToXML(object):
    '''
    classdocs
    '''      
    profInfs = []
    
    def __init__(self,profInf):
        self.doc = minidom.Document()
        self.profInf = profInf
     #   print "dfds   s fd  "+str(self.profInf)
        self.profInfs = self.doc.createElement('ProfInfs')
        self.profInfs.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")
        self.doc.appendChild(self.profInfs)
    
    def getProfInfXml(self):
        
        profInfs = self.doc.createElement('ProfInfs')

        profInf = self.doc.createElement('ProfInf')
        
        profID = self.doc.createElement("profID")
        
        profIDText = self.doc.createTextNode(self.profInf.profID)
        profID.appendChild(profIDText)
        
        profPlaneType =  self.doc.createElement("profPlaneType")
        profPlaneTypeText = self.doc.createTextNode(self.profInf.profPlaneType)
        profPlaneType.appendChild(profPlaneTypeText)
        
        profPlaneID =  self.doc.createElement("profPlaneID")
        profPlaneIDText = self.doc.createTextNode(self.profInf.profPlaneID)
        profPlaneID.appendChild(profPlaneIDText)
        
        profPrePlaneID =  self.doc.createElement("profPrePlaneID")
        profPrePlaneIDText = self.doc.createTextNode(self.profInf.profPrePlaneID)
        profPrePlaneID.appendChild(profPrePlaneIDText)
        
        profUnit =  self.doc.createElement("profUnit")
        profUnitTxt = self.doc.createTextNode(self.profInf.profUnit)
        profUnit.appendChild(profUnitTxt)
        
        proHangji =  self.doc.createElement("proHangji")
        proHangjiTxt = self.doc.createTextNode(self.profInf.proHangji)
        proHangji.appendChild(proHangjiTxt)
        
        profDay =  self.doc.createElement("profDay")
        profDayTxt = self.doc.createTextNode(str(self.profInf.profDay))
        profDay.appendChild(profDayTxt)
        
        profBetween =  self.doc.createElement("profBetween")
        profBetweenTxt = self.doc.createTextNode(str(self.profInf.profBetween))
        profBetween.appendChild(profBetweenTxt)
        
        
        profNight =  self.doc.createElement("profNight")
        profNightTxt = self.doc.createTextNode(str(self.profInf.profNight))
        profNight.appendChild(profNightTxt)
        
        self.profInfs.appendChild(profInf)
        profInf.appendChild(profID)
        profInf.appendChild(profPlaneType)
        profInf.appendChild(profPlaneID)
        profInf.appendChild(profPrePlaneID)
        profInf.appendChild(profUnit)
        profInf.appendChild(proHangji)
        profInf.appendChild(profDay)
        profInf.appendChild(profBetween)
        profInf.appendChild(profNight)
        profInf.appendChild(self.addSegmentList())
        
        profInfs.appendChild(profInf)
        return profInfs
        
    def addSegmentList(self):
        profSegment = self.doc.createElement("profSegment")
        for psl in self.profInf.profSegmentList:
            Segment = self.doc.createElement("Segment")
            profLength = self.doc.createElement("profLength")
            profLengthText = self.doc.createTextNode(str(psl.profLength))
            profLength.appendChild(profLengthText)
            profHeight = self.doc.createElement("profHeight")
            profHeightText = self.doc.createTextNode(str(psl.profHeight))
            profHeight.appendChild(profHeightText)            
            profPush = self.doc.createElement("profPush")
            profPushText = self.doc.createTextNode(str(psl.profPush))
            profPush.appendChild(profPushText)   
            profCode = self.doc.createElement("profCode")
            profCodeText = self.doc.createTextNode(str(psl.profCode))
            profCode.appendChild(profCodeText)
            profSpeed = self.doc.createElement("profSpeed")
            profSpeedText = self.doc.createTextNode(str(psl.profSpeed))
            profSpeed.appendChild(profSpeedText)
            profNoiseID = self.doc.createElement("profNoiseID")
            profNoiseIDText = self.doc.createTextNode(str(psl.profNoiseID))
            profNoiseID.appendChild(profNoiseIDText)
            Segment.appendChild(profLength)
            Segment.appendChild(profHeight)
            Segment.appendChild(profPush)
            Segment.appendChild(profCode)
            Segment.appendChild(profSpeed)
            Segment.appendChild(profNoiseID)
            profSegment.appendChild(Segment)
        return profSegment
    
    

    
#     
#     profID,profPlaneType,profPlaneID,profPrePlaneID,profUnit,proHangji,profDay,profBetween,profNight,profSegmentList
#     profLength,profHeight,profPush,profCode,profSpeed,profNoiseID
