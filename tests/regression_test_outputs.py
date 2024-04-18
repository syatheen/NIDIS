import os
import sys
import numpy as np
from glob import glob
from multiprocessing import Pool, cpu_count

# Assert content of filenames - parallel
def check_numpy_content(filename):
    x = np.loadtxt(filename)
    if x.shape[0] != 3:
        return 1
    else:
        return 0

if __name__ == '__main__':

    n_pixels = 469758
    output_path = sys.argv[1]
    output_dir = '/discover/nobackup/projects/fame/jacaraba/NIDIS_Runs/Outputs/Npzs'
    print(output_path)

    # Assert number of filenames
    filenames = glob(os.path.join(output_path, '*.txt'))
    print(len(filenames))

    assert len(filenames) == n_pixels, 'Not done'

    # Assert content of filenames - parallel
    with Pool(cpu_count()) as pool:
        results = pool.map(check_numpy_content, filenames)
    print(f"Failed outputs: {sum(results)}")
    # print(f'The squares of {numbers} are {results}')

    # create single file with values
    # we will create one file per indicator
    print(filenames[0])
    output_filename = os.path.join(output_dir, 'Npzs/NN_U_C_0To' + str(int(round(float(469758-1)))) + '_In113_39_F.npz')
    print(output_filename)

    #ArrayForSingleFile = np.empty((NumElemsInSingleFileArray,))
    #ArrayForSingleFile[:] = np.NaN

    #for WhichElem in range(NumElemsInSingleFileArray): 
    #  ArrayForSingleFile[WhichElem] = np.loadtxt('NN_U_C_' + str(int(round(float(WhichElem))))  + '_In113_39_F.txt')

    #print("ArrayForSingleFile is ",ArrayForSingleFile)
    #print("ArrayForSingleFile.shape is ",ArrayForSingleFile.shape)

    #Idxs = np.where(np.isnan(ArrayForSingleFile))
    #print("Idxs is ",Idxs)
    #print("Idxs[0].shape is ",Idxs[0].shape)

    #np.savez_compressed(SingleFile, ArrayForSingleFile = ArrayForSingleFile)

    # create netcdf

    # delete values
