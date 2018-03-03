import TextFileReader

def sort(numList = TextFileReader.readTxt()):        
    for i in range(len(numList)):
        minNumIndex = i
        for j in range(i+1,len(numList)):
            if numList[j]<numList[minNumIndex]:
                minNumIndex = j
        numList[minNumIndex],numList[i] = numList[i],numList[minNumIndex]        
    return(numList)

def main():
    print(sort())

if __name__ == "__main__":
    main()
        
        
        
