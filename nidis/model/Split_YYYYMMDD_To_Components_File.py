def Split_YYYYMMDD_To_Components(ThisYYYYMMDD):
    ThisYYYY = ThisYYYYMMDD // 10000
    ThisMM = (ThisYYYYMMDD % 10000) // 100
    ThisDD = ThisYYYYMMDD % 100
    return ThisYYYY, ThisMM, ThisDD
