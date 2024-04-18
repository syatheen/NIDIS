import os
import numpy as np
from nidis.model.Metadata import DictofNumNamePairs_Channels


def CombineMultipleFilesIntoSingle(indicator, season, output_dir, n_pixels=469758):

    output_filename = os.path.join(
        output_dir,
        f'NN_U_C_0To{str(int(round(float(n_pixels - 1))))}_In113_' +
        f'{DictofNumNamePairs_Channels[indicator]}_{season}.npz'
    )
    print(output_filename)
    #####BEGIN ANY EDITS#######
    #SingleFile = 'Npzs/NN_U_C_0To' + str(int(round(float(469758-1)))) + '_In113_39_F.npz'  
    #####END ANY EDITS#######

    #ArrayForSingleFile = np.empty((n_pixels,))
    #ArrayForSingleFile[:] = np.NaN

    #for WhichElem in range(n_pixels): 
    #    #  print("#" + str(WhichElem))
    #    ArrayForSingleFile[WhichElem] = np.loadtxt('NN_U_C_' + str(int(round(float(WhichElem))))  + '_In113_39_F.txt')

    #print("ArrayForSingleFile is ",ArrayForSingleFile)
    #print("type(ArrayForSingleFile) is ",type(ArrayForSingleFile))
    #print("ArrayForSingleFile.shape is ",ArrayForSingleFile.shape)

    #Idxs = np.where(np.isnan(ArrayForSingleFile))
    #print("Idxs is ",Idxs)
    # print("type(Idxs) is ",type(Idxs))
    #print("Idxs[0].shape is ",Idxs[0].shape)

    #np.savez_compressed(SingleFile, ArrayForSingleFile = ArrayForSingleFile)

    return
