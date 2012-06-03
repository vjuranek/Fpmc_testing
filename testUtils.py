#!/usr/bin/env python

# Test module - various tests of FPMC
# See http://cern.ch/fpmc
# Author: Vojtech.Juranek (Vojtech.Juranek@cern.ch)

import os,sys,time
import string,filecmp
import color

debug = 0

#================================================================================#

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
#    print cs
    return cs

#================================================================================#

def cvsCO(projectName,tagName='',dirName=''):
    #TODO check is there is CVSROOT variable - if no, ask user
    #do cvs check out
    print color.yellow('Checking project from cvs ...')
    command = 'cvs co '
    if(dirName != ''):
        command = command + '-d ' + dirName
    if(tagName != ''):
        command = command + ' -r ' + tagName + ' ' + projectName
    else:
        command = command + ' ' + projectName
    if(debug):
        print color.blue('Command is: ')
        print color.blue(command)
    timeStart = time.time()    
    os.system(command)
    timeEnd = time.time()
    print color.yellow('Check out finished, elapsed time [s]: ' + str(timeEnd - timeStart))
                
    #check if check out was OK - look if the directory is created
    print color.yellow('Now checking consistency...')
    if(dirName != ''):
        coDir = dirName
    else:
        coDir = projectName
    if not(os.path.exists(coDir)):
        print color.red('Directiry ' + coDir + ' does not exist - EXIT!')
        sys.exit(1)
    else:
        print color.green('Check out OK')
        print
        return coDir

#================================================================================#

def build(binary,projectDir=''):
    if(binary == ''):
        print color.red('Build: Name of not specified  - EXIT!')
        sys.exit(1)
    command = 'make'
    origPath = os.path.abspath('./')
    if(projectDir != ''):
        if(os.path.exists(projectDir)):
            os.chdir(projectDir)
        else:
            print color.red('Directiry ' + projectDir + ' does not exist - EXIT!')
            sys.exit(1)
    if not (os.path.exists('Makefile')):
        print color.red('Makefile ' + os.path.abspath('./') + '/Makefile does not exist - EXIT!')
        sys.exit(1)
    print color.yellow('Build start ...')
    if(debug):
        print color.blue('Directory is ')
        print color.blue(os.path.abspath('./'))
    timeStart = time.time()
    os.system(command)
    timeEnd = time.time()
    print color.yellow('Build finished, elapsed time [s]: ' + str(timeEnd - timeStart))
    os.chdir(origPath)

    #check if check out was OK - look if the directory is created
    print color.yellow('Now checking consistency...')
    if not(os.path.exists(projectDir+'/'+binary)):
        print color.red('File ' + os.path.abspath(projectDir) + '/' + binary + ' does not exist - EXIT!')
        sys.exit(1)
    else:
        print color.green('Build OK')
        print
        return os.path.abspath(projectDir) + '/' + binary

#================================================================================#

def runDataCards(binaryPath,dataCardPath,logPath):
    '''binaryPath - absolut path to executelbe file
       dataCardPath - absolut path to datacards directory
       logPath - absolut path to log directory'''
    if not(os.path.isfile(binaryPath)):
        print color.red('Binary file ' + binaryPath + ' does not exist - EXIT!')
        sys.exit(1)
    if not(os.path.isdir(dataCardPath)):
        print color.red('Data card file ' + dataCardPath + ' does not exist - EXIT!')
        sys.exit(1)
    if not(os.path.isdir(logPath)):
        print color.red('Log directory ' + logPath + ' does not exist - EXIT!')
        sys.exit(1)
    binaryDir = (binaryPath.rsplit('/',1))[0]
    if not(os.path.isdir(binaryDir)):
        print color.red('Directory with binary file does not exist - probably not used absoluth path to executeble file - EXIT!')
        sys.exit(1)
    dataCards = os.listdir(dataCardPath)
    origDir = os.path.abspath('./')
    os.chdir(binaryDir)
    for dataCard in dataCards:
        cardFile = dataCardPath+'/'+dataCard
        logFile = logPath+'/'+dataCard+'.log'
        if(os.path.isfile(cardFile)):
            print color.yellow('Now running ' + dataCard)
            command = binaryPath + ' < ' + cardFile + ' > ' + logFile
            if(debug):
                print color.blue('Command is:')
                print color.blue(command)
            timeStart = time.time()
            os.system(command)
            timeEnd = time.time()
            print color.yellow('Test ' + dataCard + ' finisehd, elapsed time [s]: ' + str(timeEnd - timeStart))
            if(os.path.isfile(logFile)):
                print color.green('Log file ' + logFile  + ' created')
            else:
                print color.red('WARNING: log file ' + logFile + ' was not created - something goes wrong!!!' )
        else:
            print color.yellow(dataCard + ' not a file, skipping...')
    os.chdir(origDir)
            
#================================================================================#

def getDataCardNames(dataCardPath):
    if not(os.path.isdir(dataCardPath)):
        print color.red('Data card file ' + dataCardPath + ' does not exist - EXIT!')
        sys.exit(1)
    dataCardNames = []
    dataCards = os.listdir(dataCardPath)
    for card in dataCards:
        if(os.path.isfile(dataCardPath+'/'+card)):
            dataCardNames.append(card)
    return dataCardNames
    

#================================================================================#

def getCSFromLog(dataCards,logPath):
    '''dataCardPath - absolut path to datacards directory
       logPath - absolut path to log directory'''
    if not(os.path.isdir(logPath)):
        print color.red('Log directory ' + logPath + ' does not exist - EXIT!')
        sys.exit(1)
    CSs = []
    cstr = 'CROSS SECTION (PB) ='
    for dataCard in dataCards:
        logFile = logPath+'/'+dataCard+'.log'
        if(os.path.isfile(logFile)):  
            cs = findLastInFile(logFile,cstr)
            csf = string.atof(cs)
            CSs.append(csf)
        else:
            print color.red('WARNING: log file ' + logFile + ' does not exist - SKIPPED!!!' )
    return CSs

#================================================================================#

def cmpTwoLogDir(logPath1,logPath2,dataCardNames):
    if not(os.path.isdir(logPath1)):
        print color.red('Log directory ' + logPath1 + ' does not exist - EXIT!')
        sys.exit(1)
    if not(os.path.isdir(logPath2)):
        print color.red('Log directory ' + logPath2 + ' does not exist - EXIT!')
        sys.exit(1)
    logFiles = []
    for card in dataCardNames:
        logFiles.append(card+'.log')
    cmps = filecmp.cmpfiles(logPath1,logPath2,logFiles)
    print color.green('=====================================================')
    print color.green('Files which are the same:')
    for file in cmps[0]:
        print color.green(file)
    print color.green('=====================================================')
    print
    print color.red('=====================================================')
    print color.red('Files which are NOT the same:')
    for file in cmps[1]:
        print color.red(file)
    print color.red('=====================================================')
    print
    print color.yellow('=====================================================')
    print color.yellow('Files which script was not able to compare:')
    for file in cmps[2]:
        print color.yellow(file)
    print color.yellow('=====================================================')
    print

#================================================================================#

def runTests(settings):

    #load user setting
    projectName = settings['projectName']
    binary = settings['binary']
    cardName = settings['cardName']
    cardDir = settings['cardDir']
    tagName1 = settings['tagName1']
    dirName1 = settings['dirName1']
    tagName2 = settings['tagName2']
    dirName2 = settings['dirName2']
    debug = settings['debug']

    #check out datacards
    dataCardsDir = cvsCO(cardName,dirName=cardDir)

    #check out versions
    coDir1 = cvsCO(projectName,tagName1,dirName1)
    coDir2 = cvsCO(projectName,tagName2,dirName2)

    #build versions
    bin1 = build(binary,coDir1)
    bin2 = build(binary,coDir2)

    #setup paths etc.
    absDir = os.path.abspath('./')
    dataCardsDir = absDir + '/' + dataCardsDir
    logDir1 = absDir + '/' + 'logs1'
    logDir2 = absDir + '/' + 'logs2'
    cardNames = getDataCardNames(dataCardsDir)

    #run tests
    #runDataCards(bin1,dataCardsDir,logDir1)
    #runDataCards(bin2,dataCardsDir,logDir2)

    #compare results (log files)
    #compare log files
    cmpTwoLogDir(logDir1,logDir2,cardNames)
    #copare cross sections
    cs1 = getCSFromLog(cardNames,logDir1)
    cs2 = getCSFromLog(cardNames,logDir2)
    i = 0
    diffs = []
    for card in cardNames:
        diffs.append(cs1[i] - cs2[i])
        i = i + 1
    print color.green('Differences in cross sections:')
    for diff in diffs:
        print diff
    print

#================================================================================#


