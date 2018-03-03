import TextFileReader,math

def merge(numList):
    mergeList = []
        
    return mergeList

def sort(numList = TextFileReader.readTxt()):    
    for i in range(len(numList)):
        numList[i] = [numList[i]]
    for i in range(math.ceil(math.log2(len(numList)))):
        numList = merge(numList)
    return(numList)

def main():
    print(sort())

if __name__ == "__main__":
    main()
