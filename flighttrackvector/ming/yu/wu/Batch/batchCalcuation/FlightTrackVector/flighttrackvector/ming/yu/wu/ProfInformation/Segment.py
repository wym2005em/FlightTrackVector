'''
Created on 2013-11-24

@author: wym
'''

class Segment(object):
    '''
    classdocs
    '''
    def __repr__(self):
        return '[profLength: %s,profHeight: %s,profPush: %s,profCode: %s,profSpeed: %s,profNoiseID: %s]' % (self.profLength,self.profHeight,self.profPush,self.profCode,self.profSpeed,self.profNoiseID)

    def __init__(self,profLength,profHeight,profPush,profCode,profSpeed,profNoiseID):
        self.profLength = int(float(profLength))
        self.profHeight = int(float(profHeight))
        self.profPush = float(profPush)
        self.profCode = profCode
        self.profSpeed = int(float(profSpeed))
        self.profNoiseID = profNoiseID
        