@echo off
del result.txt
xcopy TrackAndProfInformation\copy\result.txt
start TrackAndProfInformation\execute.exe
exit 