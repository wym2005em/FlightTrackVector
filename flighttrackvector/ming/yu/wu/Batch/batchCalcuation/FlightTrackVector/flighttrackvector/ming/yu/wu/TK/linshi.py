'''
Created on 2013-12-1

@author: wym
'''

print int('ff', 16)
import binascii
file_object = open('E:/noise/noisemap/Noisemap/NMap/tempbops.grd')
try:
    all_the = file_object.read()
    print all_the
finally:
    file_object.close()