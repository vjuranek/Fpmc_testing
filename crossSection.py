#!/usr/bin/env python
import os

def findLastInFile(file,str):
    css = []
    i = 0
    f = open(file,'r')
    try:
        for line in f:
            if(str in line):
                css.append(line)
                i = i+1
    finally:
        f.close()
    csstr = css[i-1].strip()
    csstr = csstr.split(str)
    cs = csstr[len(csstr)-1].strip()
    print cs
    return cs



def replaceInFile(file,str1,str2):
    import fileinput
    for line in fileinput.FileInput(file,inplace=1):
        if str1 in line:
            print str2,
        else:
            print line,

def writeInFile(file,text):
    f = open(file,'a')
    try:
        f.write(text)
    finally:
        f.close()

cardFile = 'datacard.ffread'
outFile = 'output.log'
dataFile = 'data.txt'
str1 = 'PTMIN       '
str2 = '.\n'
cstr = 'CROSS SECTION (PB) ='
command = './module < ' + cardFile + ' > ' + outFile
print 'commad = ' + command
for ptmin in [15,30,40,50,60,70]:
    print 'Processing ptmin\t=\t' + str(ptmin) 
    ptstr = str1 + str(ptmin) + str2
    replaceInFile(cardFile,str1,ptstr)
    os.system(command)
    cs = findLastInFile(outFile,cstr)
    text = str(ptmin) + '\t' + cs + '\n'
    writeInFile(dataFile,text)
    
