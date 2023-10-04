from Banknote import *
from firstScript import *

if __name__ == "__main__":
    array = {Banknote('Paper', 'Yellow-gray', 118, 63, 1, 2006, 'АК4589634', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Brown', 118, 70, 2, 2003, 'ВУ2486572', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Blue', 133, 66, 5, 2004, 'ФЯ7319548', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Green', 130, 69, 20, 2018, 'ЛИ1239875', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Violet', 136, 72, 50, 2010, 'ВВ5050505', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Yellow', 142, 75, 100, 2015, 'ЧЦ4563218', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Pink', 148, 75, 200, 2019, 'ШВ7413698', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Yellow-orange', 154, 75, 500, 2020, 'СМ7413695', 'stamp.png', 'FacialPicture.png', 'BackPicture.png'),
             Banknote('Paper', 'Greenish blue', 160, 75, 1000, 2023, 'УВ1837895', 'stamp.png', 'FacialPicture.png', 'BackPicture.png')}
    makeDirOfBanknotes(array)