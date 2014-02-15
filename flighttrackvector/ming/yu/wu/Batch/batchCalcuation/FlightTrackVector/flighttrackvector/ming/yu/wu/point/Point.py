class Point:
    def __init__(self, x = 0.0, y = 0.0):

        self.X = x + 0.0
        self.Y = y + 0.0

    def __repr__(self):
        return '[X Y :%s,%s]' % (self.X, self.Y)

    def getDistanceToOtherPoint(self,point):
        import math
        
        return math.sqrt((self.X-point.X)*(self.X-point.X)+(self.Y-point.Y)*(self.Y-point.Y))
    def PointOfIntersection(self, Line1, Line2):
        self.X = (Line1.C*Line2.B - Line2.C*Line1.B)/(Line2.A*Line1.B
- Line1.A*Line2.B)
        self.Y = (Line1.C*Line2.A - Line1.A*Line2.C)/(Line1.A*Line2.B
- Line1.B*Line2.A)
        return (self.X, self.Y)
    
if __name__=='__main__':
        
    pt1 =Point(0.0,0.0)
    pt2 = Point(-1.0,1.0)
   
    
  
    #print l1.getLength()
    #print l1.getLineIntersectionAngle(l2) 
    #print pt1.getDistanceToOtherPoint(pt2)        
        