import numpy as np

def ResetUniquePercentileValuesToMid(ThisPrcntlArray): 

    for iCol in range(ThisPrcntlArray.shape[1]):

        PrcntlsInThisSpatialElement = ThisPrcntlArray[:, iCol]
        validPrcntlsInThisSpatialElement = PrcntlsInThisSpatialElement[~np.isnan(PrcntlsInThisSpatialElement)] 
        if validPrcntlsInThisSpatialElement.size:
            NumValidUniqPrcntlsInSpatialElement = len(np.unique(validPrcntlsInThisSpatialElement)) 
            if NumValidUniqPrcntlsInSpatialElement == 1:
                validPrcntlsInThisSpatialElement[:] = 0.5
                PrcntlsInThisSpatialElement[~np.isnan(PrcntlsInThisSpatialElement)] = validPrcntlsInThisSpatialElement
                ThisPrcntlArray[:, iCol] = PrcntlsInThisSpatialElement 
            #end of if NumValidUniqPrcntlsInSpatialElement == 1
        #end of if validPrcntlsInThisSpatialElement.size

    #end of for iCol in range(ThisPrcntlArray.shape[1])

    return ThisPrcntlArray

#end of def ResetUniquePercentileiValuesToMid(ThisPrcntlArray)

