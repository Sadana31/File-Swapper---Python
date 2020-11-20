def swapFiles():
    essay = input("Enter the file which you want to change: ")
    prank = input("Enter the file which you want to take the text from: ")
    data_A = open(essay,"r")
    essayText = data_A.readlines()

    data_B = open(prank, "r")
    prankText = data_B.readlines()

    essayChange = open(essay,"w")
    change = essayChange.writelines(prankText)

    prankChange = open(prank,"w")
    change1 = prankChange.writelines(essayText)
    print("")

    print("Now, this is the text in the original file. Enjoy your prank ;)")
    print(prankText)

swapFiles()

    
