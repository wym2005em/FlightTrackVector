'''
Created on 2013-11-8

@author: wym
'''
from matplotlib.patches import Circle
from flighttrackvector.ming.yu.wu.fitcircle import FitCircle
from flighttrackvector.ming.yu.wu.fitline import FitLine

from flighttrackvector.ming.yu.wu.fitline import line
from flighttrackvector.ming.yu.wu.point import Point
class MyClass(object):

    def dd(self):
        
        for i in range(10):
            try:   

                if i==3:
                    raise StopIteration()
                print i
            except:
                continue
        
        
        
if __name__=='__main__':
    MyClass = MyClass()
    print MyClass.dd()
    import gl
    