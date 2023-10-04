class Banknote:
    def __init__(self, material, color, xSize, ySize, denomination, year, serialNumber, waterStamp , facialPicture, backPicture):
        self.__material = material
        self.__color = color
        self.__xSize = xSize
        self.__ySize = ySize
        self.__denomination = denomination
        self.__year = year
        self.__serialNumber = serialNumber
        self.__waterStamp = waterStamp
        self.__facialPicture = facialPicture
        self.__backPicture = backPicture

    def getMaterial(self):
        return self.__material

    def getColor(self):
        return self.__color

    def getXSize(self):
        return self.__xSize

    def getYSize(self):
        return self.__ySize

    def getDenomination(self):
        return self.__denomination

    def getYear(self):
        return self.__year

    def getSeriealNumber(self):
        return self.__serialNumber

    def getWaterStamp(self):
        return self.__waterStamp

    def getFacialPicture(self):
        return self.__facialPicture

    def getBackPicture(self):
        return self.__backPicture

    def print(self):
        print("\nМатериал:\t" + str(self.getMaterial()) + "\nЦвет:\t" + str(self.getColor()) +
              "\nРазмер_X:\t" + str(self.getXSize()) + "мм" + "\nРазмер_Y:\t" + str(self.getYSize()) + "мм" +
              "\nНоминал:\t" + str(self.getDenomination()) + "\nГод выпуска:\t" + str(self.getYear()) +
              "\nСерийный номер:\t" + str(self.getSeriealNumber()) + "\nВодная марка:\t" + str(self.getWaterStamp()) +
              "\nЛицевая картинка:\t" + str(self.getFacialPicture()) + "\nЗадняя картинка:\t" + str(self.getBackPicture()))