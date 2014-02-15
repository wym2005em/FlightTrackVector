'''
Created on 2013-11-11

@author: wym
'''
import os
runwayDic={"36R":"18L","18L":"36R","36L":"18R","18R":"36L","01":"19","19":"01"}
runwayLatLon={"36R":[40.055130,116.5995],"18L":[40.08891,116.5943],"36L":[40.07314,116.5735],"18R":[40.10175,116.569],"01":[40.05856,116.617],"19":[40.09253,116.6117]}
ZBAALocation =[40.0736,116.6033]

def getFileList(p):
        p = str( p )
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x  for x in a if os.path.isfile( p + x ) ]
        return b
    
# path = "E:/piliangWECPLlinshi/linshi/621B737APP18L/"
# filenamelist = getFileList(path)
# filelist = [path+filename for filename in filenamelist]
# print filelist