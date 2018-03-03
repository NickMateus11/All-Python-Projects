def readTxt(FileName = "RawInputs.txt"):
    rawTxt = open(FileName)
    numList = [int(i) for i in rawTxt.read().split()]
    rawTxt.close()
    return numList
