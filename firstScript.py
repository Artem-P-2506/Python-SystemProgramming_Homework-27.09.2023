import os

def makeDirOfBanknotes(array):
    if not os.path.exists("Banknotes"):
        os.mkdir("Banknotes")
    os.chdir(os.path.join(os.getcwd(), "Banknotes"))
    for item in array:
        serialNumber = item.getSeriealNumber() + ".txt"
        with open(serialNumber, 'w') as file:
            file.write("Material:\t" + str(item.getMaterial()))
            file.write("\nColor:\t" + str(item.getColor()))
            file.write("\nSize_X:\t" + str(item.getXSize()))
            file.write("\nSize_Y:\t" + str(item.getYSize()))
            file.write("\nDenomination:\t" + str(item.getDenomination()))
            file.write("\nYear:\t" + str(item.getYear()))
            file.write("\nWater stamp:\t" + str(item.getWaterStamp()))
            file.write("\nFacial picture:\t" + str(item.getFacialPicture()))
            file.write("\nBack picture:\t" + str(item.getBackPicture()))