'''
Created on 2013-11-12

@author: wym
'''

class RunOutPut(object):
    '''
    classdocs
    '''
    

    def __init__(self,resultList):
        '''
        
        '''
        self.resultList = resultList
    
    def getNoisemapFormat(self,paodaoDuankou,flightNum,flightModel):
        outputResultList = []
        j=0
        DorA=[]
        count=0
        for i in self.resultList:
            count=count+1
            if count>45:
                break
            if j==0:
                j+=1
                if str(i).find("Line")!=-1:
                    DorA="D"
                else:
                    DorA="A"    
            if str(i).find("Line")!=-1:
                outputResultList.append([int(float(str(i.getLineLength())[:8]))])
                #outputResultList.append([(float(str(i.getLineLength())[:8]))])
            if str(i).find("Circle")!=-1:
                #if int(float(str(i.radius)[:8]))!=0:   # yong le nmi ,, so zhu shi
                if (float(str(i.radius)[:8]))!=0.0:   # yong le nmi ,, so zhu shi
                    outputResultList.append([i.zuoyou,float(str(i.radiusAngle)[:5]),int(float(str(i.radius)[:8]))])
                    #outputResultList.append([i.zuoyou,float(str(i.radiusAngle)[:5]),(float(str(i.radius)[:8]))])
        outputResultList.insert(0, "DorA: "+str(DorA))
        outputResultList.insert(0, "flightNum: "+str(flightNum))
        outputResultList.insert(0, "flightModel: " +str(flightModel))
        outputResultList.insert(0, "runway: "+str(paodaoDuankou))
     #   print outputResultList
      #  print str([str(c)+"'," for c in outputResultList]).replace('"', "'");
        
#         outputResultList2=[]
#         for c in outputResultList:
#             if type(c)==list: 
#                 outputResultList2.append(c)
#             else:
#                 outputResultList2.append(c+"',")
#  getLineIntersectionAngle       
                
        outputstr =  str([str(c)+"'," for c in outputResultList[:-1]]).replace('"', "'")
        index = outputstr.index("DorA:")+10
        outputstr = outputstr[:index] + outputstr[index:].replace("'[", "[");
        outputstr = outputstr[:index] + outputstr[index:].replace("]'", "]");
        outputstr = outputstr.replace("],']", "]]");
        outputstr = outputstr.replace(",',","|");
        return outputstr