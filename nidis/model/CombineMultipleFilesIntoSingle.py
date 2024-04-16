import numpy as np


def CombineMultipleFilesIntoSingle():

    #####BEGIN ANY EDITS#######
    NumElemsInSingleFileArray = 469758
    SingleFile = 'Npzs/NN_U_C_0To' + str(int(round(float(469758-1)))) + '_In113_39_F.npz'  
    #####END ANY EDITS#######

    ArrayForSingleFile = np.empty((NumElemsInSingleFileArray,))
    ArrayForSingleFile[:] = np.NaN

    for WhichElem in range(NumElemsInSingleFileArray): 
        #  print("#" + str(WhichElem))
        ArrayForSingleFile[WhichElem] = np.loadtxt('NN_U_C_' + str(int(round(float(WhichElem))))  + '_In113_39_F.txt')

    print("ArrayForSingleFile is ",ArrayForSingleFile)
    #print("type(ArrayForSingleFile) is ",type(ArrayForSingleFile))
    print("ArrayForSingleFile.shape is ",ArrayForSingleFile.shape)

    Idxs = np.where(np.isnan(ArrayForSingleFile))
    print("Idxs is ",Idxs)
    # print("type(Idxs) is ",type(Idxs))
    print("Idxs[0].shape is ",Idxs[0].shape)

    np.savez_compressed(SingleFile, ArrayForSingleFile = ArrayForSingleFile)

    return
