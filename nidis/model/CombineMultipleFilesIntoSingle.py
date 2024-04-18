import os
import logging
import numpy as np
from nidis.model.Metadata import DictofNumNamePairs_Channels

"""

# multithreaded array filling with thread pool and one worker per logical cpu
from time import time
from multiprocessing.pool import ThreadPool
from numpy import empty
 
# fill a portion of a larger array with a value
def fill_subarray(coords, data, value):
    # unpack array indexes
    i1, i2, i3, i4 = coords
    # populate subarray
    data[i1:i2,i3:i4].fill(value)
 
# task function
def task(n=50000):
    # record the start time
    start = time()
    # create an empty array
    data = empty((n,n))
    # create the thread pool
    with ThreadPool(8) as pool:
        # split each dimension (divisor of matrix dimension)
        split = round(n/4)
        # issue tasks
        for x in range(0, n, split):
            for y in range(0, n, split):
                # determine matrix coordinates
                coords = (x, x+split, y, y+split)
                # issue task
                _ = pool.apply_async(fill_subarray, args=(coords, data, 1))
        # close the pool
        pool.close()
        # wait for tasks to complete
        pool.join()
    # calculate and report duration
    duration = time() - start
    # return duration
    return duration
 
# experiment that averages duration of task function
def experiment(repeats=3):
    # repeat the experiment and gather results
    results = [task() for _ in range(repeats)]
    # return the average of the results
    return sum(results) / repeats
 
# run the experiment and report the result
duration = experiment()
print(f'Took {duration:.3f} seconds')
"""


def CombineMultipleFilesIntoSingle(
            indicator,
            season,
            indicator_dir,
            output_dir,
            n_pixels=469758
        ):

    output_filename = os.path.join(
        output_dir,
        f'NN_U_C_0To{str(int(round(float(n_pixels - 1))))}_In113_' +
        f'{DictofNumNamePairs_Channels[indicator]}_{season}.npz'
    )

    FI1X1_ClmGrd1D_V2b_New_Array = np.empty((n_pixels,))
    FI1X1_ClmGrd1D_V2b_New_Array[:] = np.NaN

    SSiz1X1_ClmGrd1D_V2b_New_Array = np.empty((n_pixels,))
    SSiz1X1_ClmGrd1D_V2b_New_Array[:] = np.NaN

    WSiz1X1_ClmGrd1D_V2b_New_Array = np.empty((n_pixels,))
    WSiz1X1_ClmGrd1D_V2b_New_Array[:] = np.NaN

    # currently running in serial, I would like to make it parallel
    for WhichElem in range(n_pixels):
        indicator_result = np.loadtxt(
            os.path.join(
                indicator_dir,
                f'NN_U_C_{WhichElem}_In113_{indicator - 1}_{season}.txt'
            )
        )
        FI1X1_ClmGrd1D_V2b_New_Array[WhichElem] = indicator_result[0]
        SSiz1X1_ClmGrd1D_V2b_New_Array[WhichElem] = indicator_result[1]
        WSiz1X1_ClmGrd1D_V2b_New_Array[WhichElem] = indicator_result[2]

    np.savez_compressed(
        output_filename,
        ArrayForSingleFile=FI1X1_ClmGrd1D_V2b_New_Array,
        FI1X1_ClmGrd1D_V2b_New_Array=FI1X1_ClmGrd1D_V2b_New_Array,
        SSiz1X1_ClmGrd1D_V2b_New_Array=SSiz1X1_ClmGrd1D_V2b_New_Array,
        WSiz1X1_ClmGrd1D_V2b_New_Array=WSiz1X1_ClmGrd1D_V2b_New_Array
    )
    logging.info(f'Saved output to {output_filename}')

    return
