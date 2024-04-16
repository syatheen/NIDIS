
from __future__ import division

import sys
import logging


def TimeSliceStrict_YYYYMMDDAndRefArrays(
        YYYYMMDD_Of_RefArray,
        RefArray,
        BeginYYYYMMDD,
        EndYYYYMMDD,
        Variable
      ):
    if ((BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray)) and
       (EndYYYYMMDD in list(YYYYMMDD_Of_RefArray))):
        BeginIdx = list(YYYYMMDD_Of_RefArray).index(BeginYYYYMMDD)
        EndIdx = list(YYYYMMDD_Of_RefArray).index(EndYYYYMMDD)
        YYYYMMDD_Of_RefArray = YYYYMMDD_Of_RefArray[BeginIdx: EndIdx+1]
        RefArray = RefArray[BeginIdx: EndIdx+1]
    else:
        logging.info(
            'Begin and end YYYYMMDDs not in YYYYMMDD_Of_RefArray' +
            f'for {Variable} !!!!')
        sys.exit(
            'Begin and end YYYYMMDDs not in YYYYMMDD_Of_RefArray' +
            f'for {Variable} !!!!')
    return YYYYMMDD_Of_RefArray, RefArray
