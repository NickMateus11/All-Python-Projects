import random

def main():
    txt = open("RawInputs.txt",'w')
    numLen = random.randint(50,100)
    numList = []
    for i in range(numLen):
        numList.append(str(random.randint(0,100)))
    txt.write(" ".join(numList))
    txt.close()
    print('Done')
main()
