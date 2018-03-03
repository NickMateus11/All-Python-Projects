import TextFileReader, BubbleSort , SelectionSort, InsertionSort

def search(num, numList):
    if len(numList) == 1:        
        if numList[0] == num:
            return True
        else:
            return False
    if num < numList[len(numList)//2]:
        return search(num,numList[0:len(numList)//2])
    else:
        return search(num,numList[len(numList)//2:])

def main():
    sortChoice = input("How would you like to sort the data? ").lower()
    if sortChoice == 'bubble sort':
        sortChoice = BubbleSort
    elif sortChoice == 'selection sort':
        sortChoice = SelectionSort
    elif sortChoice == 'insertion sort':
        sortChoice = InsertionSort

    if type(sortChoice) != str:    
        numList = sortChoice.sort(TextFileReader.readTxt())

        searchNum = int(input("What number would you like to find "))

        searchResult = search(searchNum,numList)
        
        if searchResult:
            print("The number was found")
        else:
            print("The number does not exist")
    else:
        print('Invalid input, please try again')
        main()

if __name__ == "__main__":
    main()
