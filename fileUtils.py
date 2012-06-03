#!/usr/bin/env python
'''Various utils for operating with files '''

import os,sys,string

debug = 0
#================================================================================#

def getValuesFromFile(file):
    '''Reads values from txt file - file format has to be one number per line'''
    values = []
    try:
        f = open(file,'r')
    except IOError:
        print 'cannot open ',file 
    else:
        for line in f.readlines():
            values.append(string.atof(line))
#    finally:
    f.close()
    return values

#================================================================================#

def getXYFromFile(file):
    '''Reads X and Y values from txt file - file format has to be X_value \t Y_value per line'''
    values = []
    try:
        f = open(file,'r')
    except IOError:
        print 'cannot open ',file 
    else:
        for line in f.readlines():
            splitLine = line.split('\t')
            values.append([string.atof(splitLine[0]),string.atof(splitLine[1])])
#    finally:
            f.close()
    return values

#================================================================================#

def putXYInFile(file,values):
    '''Writes X and Y values in txt file - file format has to be X_value \t Y_value per line'''
    try:
        f = open(file,'w')
    except IOError:
        print 'cannot open ',file 
    else:
        for x,y in values:
            f.write(str(x) + '\t' + str(y) + '\n')
#    finally:
        f.close()

#================================================================================#

def getXYErrorsFromFile(file):
    '''Reads X, Y, X_error  and Y_error values from txt file - file format has to be X_value \tab Y_value per line \tab Y_error '''
    xVal = []
    yVal = []
    xeVal = []
    yeVal = []
    try:
        f = open(file,'r')
    except IOError:
        print 'cannot open ',file 
    else:
        for line in f.readlines():
            splitLine = line.split('\t')
            xVal.append(string.atof(splitLine[0]))
            yVal.append(string.atof(splitLine[1]))
            xeVal.append(string.atof(splitLine[2]))
            yeVal.append(string.atof(splitLine[3]))
#    finally:
    f.close()
    values = [xVal,yVal,xeVal,yeVal]
    return values

#================================================================================#

def getXYErrorsVectFromFile(file):
    '''Reads X, Y, X_error and Y_error values from txt file - file format has to be X_value \tab Y_value per line \tab Y_error '''
    values = []
    try:
        f = open(file,'r')
    except IOError:
        print 'cannot open ',file 
    else:
        for line in f.readlines():
            splitLine = line.split('\t')
            values.append([string.atof(splitLine[0]),string.atof(splitLine[1]),string.atof(splitLine[2]),string.atof(splitLine[3])])
#    finally:
    f.close()
    return values

#================================================================================#

def mergeXYAxis(xAxisFile,yAxisFile,mergeFile):
    '''Loads X vealues from xAxisFile, Y values from yAxisFile and puts it info mergeFile in format X_Value \t  Y_Value per line'''
    xAxis = getValuesFromFile(xAxisFile)
    yAxis = getValuesFromFile(yAxisFile)
    if(debug):
        print '#x values: ' + str(len(xAxis))
        print '#y values: ' + str(len(yAxis))
    if(len(xAxis) == len(yAxis)):
        try:
            f = open(mergeFile,'w')
        except IOError:
            print 'cannot open ',file 
        else:
            for i in range(len(xAxis)):
                #print str(xAxis[i]) + '\t' + str(yAxis[i])
                f.write(str(xAxis[i]) + '\t' + str(yAxis[i]) + '\n')
        #finally:
        f.close()
        print mergeFile + ' created'
    else:
        print 'Different number of X and Y values, check files! EXIT!'
        sys.exit(1)

#================================================================================#

def mergeXYErrors(xAxisFile,yAxisFile,yErrorFile,mergeFile):
    '''Loads X vealues from xAxisFile, Y values from yAxisFile, Y errors from yErrorFile and puts it info mergeFile in format X_Value \tab  Y_Value \tab Y_error per line'''
    xAxis = getValuesFromFile(xAxisFile)
    yAxis = getValuesFromFile(yAxisFile)
    yErrors = getValuesFromFile(yErrorFile)
    if(debug):
        print '#x values: ' + str(len(xAxis))
        print '#y values: ' + str(len(yAxis))
        print '#y_errors: ' + str(len(yErrors))
    if((len(xAxis) == len(yAxis)) and (len(yAxis) == len(yErrors))):
        try:
            f = open(mergeFile,'w')
        except IOError:
            print 'cannot open ',file 
        else:
            for i in range(len(xAxis)):
                #print str(xAxis[i]) + '\t' + str(yAxis[i])
                f.write(str(xAxis[i]) + '\t' + str(yAxis[i]) + '\t' + str(yErrors[i]) + '\n')
        #finally:
        f.close()
        print mergeFile + ' created'
    else:
        print 'Different number of X, Y and Y_error values, check files! EXIT!'
        sys.exit(1)
       
#================================================================================#            

    

if __name__ == '__main__':
    print 'This module is not designed for stanalone usage!!!'
#    xAxisFile = '../Disociace/data/marta/zeus1_xl.txt'
#    yAxisFile = '../Disociace/data/marta/zeus1_sigma.txt'
#    mergeFile = '../Disociace/data/zeus1.txt'
#    mergeXYAxis(xAxisFile,yAxisFile,mergeFile)
#    vals = getXYFromFile(mergeFile)
#    print vals
