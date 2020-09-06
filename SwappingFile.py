def swapFileData():

    fileOneData = open("SampleText1.txt",'r+')

    fileTwoData = open("SampleText2.txt",'r+')

    savedData = (fileTwoData)

    for text1 in fileOneData:

        fileOneData.write("fileTwoData")
    
    for text2 in savedData:
        
        savedData.write("fileOneData")


swapFileData()