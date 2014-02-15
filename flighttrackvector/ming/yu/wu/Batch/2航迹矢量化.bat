@echo off
del TrackAndProfInformation\track.txt
del TrackAndProfInformation\track.txt.xml
xcopy TrackAndProfInformation\copy\track.txt TrackAndProfInformation\
xcopy TrackAndProfInformation\copy\track.txt.xml TrackAndProfInformation\
e:
cd E:\bigNoisemap\Batch\batchCalcuation\FlightTrackVector\flighttrackvector\ming\yu\wu\TK\
start python piliangFitTK.py
exit
