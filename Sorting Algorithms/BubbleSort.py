import TextFileReader

def sort(numList = TextFileReader.readTxt()):
    for i in range(len(numList)):
        for j in range(len(numList)-1):
            if numList[j]>numList[j+1]:
                numList[j],numList[j+1] =  numList[j+1],numList[j]            
    return(numList)

def main():
    print(sort())

if __name__ == "__main__":
    main()
