fileName='log.txt'



def writeToLog(text):
    global fileName
    with open(fileName,'a') as f:
            f.write(text+'\n')
