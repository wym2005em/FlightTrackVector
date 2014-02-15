'''
Created on 2013-11-24

@author: wym
'''

class ProfInf(object):
    '''
    classdocs
    '''
    
    def __repr__(self):
        return '[profID: %s profPlaneType: %s profPlaneID: %s profPrePlaneID: %s profUnit: %s proHangji: %s profDay: %s profBetween: %s profNight: %s profSegmentList: %s]' % (self.profID,self.profPlaneType,self.profPlaneID,self.profPrePlaneID,self.profUnit,self.proHangji,self.profDay,self.profBetween,self.profNight,self.profSegmentList)
    
    def __init__(self,profID,profPlaneType,profPlaneID,profPrePlaneID,profUnit,proHangji,profDay,profBetween,profNight,profSegmentList):
        self.profID = profID
        self.profPlaneType = profPlaneType
        self.profPlaneID = profPlaneID
        self.profPrePlaneID = profPrePlaneID
        self.profUnit = profUnit
        self.proHangji = proHangji
        self.profDay = profDay
        self.profBetween = profBetween
        self.profNight = profNight
        self.profSegmentList = profSegmentList
        
    
     
