
from __future__ import division

from datetime import date, timedelta
import numpy as np
import copy
import sys
import logging

def CreateYYYYMMDD_Of_Array(BeginDate, EndDate):
    TotalNumDaysDiff = abs(EndDate-BeginDate).days
    TotalNumWeeksDiff = TotalNumDaysDiff//7
    HumanDatesList_Of_Array = []
    for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
        IntermediateDate = BeginDate + timedelta(weeks=NumWeeksDiff)
        HumanDatesList_Of_Array.append(10000*IntermediateDate.year + 100*IntermediateDate.month + IntermediateDate.day)
    YYYYMMDD_Of_Array = np.array(HumanDatesList_Of_Array, dtype = np.int32)
    YYYYMMDD_Of_Array = np.expand_dims(YYYYMMDD_Of_Array, axis=1)
    return YYYYMMDD_Of_Array
#end of def CreateYYYYMMDD_Of_Array(BeginDate, EndDate)

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
    else: # of if ((BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray)) and...
        logging.info(
            'Begin and end YYYYMMDDs not in YYYYMMDD_Of_RefArray ' +
            f'for {Variable} !!!!')
        BeginYYYY = BeginYYYYMMDD // 10000
        EndYYYY = EndYYYYMMDD // 10000
        BeginMM = (BeginYYYYMMDD % 10000) // 100
        EndMM = (EndYYYYMMDD % 10000) // 100
        BeginDD = BeginYYYYMMDD % 100
        EndDD = EndYYYYMMDD % 100
        BeginDate = date(BeginYYYY, BeginMM, BeginDD)
        EndDate = date(EndYYYY, EndMM, EndDD)
        Temp_YYYYMMDD_Of_RefArray = CreateYYYYMMDD_Of_Array(BeginDate, EndDate)
        TempRefArray = np.empty([Temp_YYYYMMDD_Of_RefArray.shape[0], RefArray.shape[1]])
        TempRefArray[:] = np.nan
        if ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) ):
            BeginIdx = list(YYYYMMDD_Of_RefArray).index(BeginYYYYMMDD)
            TempRefArray[ : RefArray.shape[0]-BeginIdx ] = RefArray[ BeginIdx : ]
        #end of if ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) )
        if ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) ):
            EndIdx = list(YYYYMMDD_Of_RefArray).index(EndYYYYMMDD)
            TempRefArray[ TempRefArray.shape[0]-(EndIdx+1) : ] = RefArray[ : EndIdx+1 ]
        #end of if ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) )
        YYYYMMDD_Of_RefArray = copy.deepcopy(Temp_YYYYMMDD_Of_RefArray)
        del Temp_YYYYMMDD_Of_RefArray
        RefArray = copy.deepcopy(TempRefArray)
        del TempRefArray        
    #end of if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
        
    return YYYYMMDD_Of_RefArray, RefArray
#end of def TimeSliceStrict_YYYYMMDDAndRefArrays(..


