from __future__ import division
from datetime import date, datetime, timedelta
import numpy as np
import sys

def TimeSliceStrict_YYYYMMDDAndRefArrays(YYYYMMDD_Of_RefArray, RefArray, BeginYYYYMMDD, EndYYYYMMDD, Variable):
  if ( ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) ) and
       ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) ) ) :
    BeginIdx = list(YYYYMMDD_Of_RefArray).index(BeginYYYYMMDD)
    EndIdx = list(YYYYMMDD_Of_RefArray).index(EndYYYYMMDD)
    YYYYMMDD_Of_RefArray = YYYYMMDD_Of_RefArray[ BeginIdx : EndIdx+1 ]
    RefArray = RefArray[ BeginIdx : EndIdx+1 ]
  else: # if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
    print('Begin and end YYYYMMDDs not in YYYYMMDD_Of_RefArray for ' + Variable + '!!!!')
    sys.exit('Begin and end YYYYMMDDs not in YYYYMMDD_Of_RefArray for ' + Variable + '!!!!')
  #end of if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
  return YYYYMMDD_Of_RefArray, RefArray
#end of def TimeSliceStrict_YYYYMMDDAndRefArrays(YYYYMMDD_Of_RefArray, RefArray, BeginYYYYMMDD, EndYYYYMMDD, Variable)

