import TextFileReader

def sort(numList = TextFileReader.readTxt()):    
    for i in range(1,len(numList)):
        currentNumIndex = i        
        for j in range(i+1):
            if numList[currentNumIndex] <= numList[currentNumIndex-j]:
                insertIndex = currentNumIndex-j
            else:
                break
        numList.insert(insertIndex,numList.pop(currentNumIndex))  
    return(numList)

def main():
    print(sort())

if __name__ == "__main__":
    main()
