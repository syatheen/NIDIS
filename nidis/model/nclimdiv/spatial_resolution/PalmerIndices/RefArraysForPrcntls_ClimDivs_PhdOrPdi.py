import sys
#######BEGIN ANY EDITS REQUIRED#######
PdiOrPhdStr = 'phd' # possible values are 'pdi' and 'phd'
# Begin Beginning year, month, day of month
if PdiOrPhdStr == 'phd':
  BeginDateVec = [2005, 6, 4] 
elif PdiOrPhdStr == 'pdi':
  BeginDateVec = [2005, 1, 1] 
else:
  print('PdiOrPhdStr should be phd or pdi!!')
  sys.exit(0)
# End Beginning year, month, day of month
#EndDateVec = [2019, 12, 28] # Ending year, month, day of month
EndDateVec = [2020, 1, 4] # Ending year, month, day of month
FilesPath = "/att/nobackup/dmocko/Palmer/weekly/"
#FilesPath = "/discover/nobackup/syatheen/NIDIS/Data/Palmer/weekly/"
ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
#ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
PalmerIndex_LowerLimit = -20.0
PalmerIndex_UpperLimit =  20.0
PalmerArrayFileName = PdiOrPhdStr+'RefArray_'+format(BeginDateVec[0],'04')+format(BeginDateVec[1],'02')+format(BeginDateVec[2],'02')+'To'+format(EndDateVec[0],'04')+format(EndDateVec[1],'02')+format(EndDateVec[2],'02')+'.npz'
#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
import geopandas as gp
ClimDivShp = gp.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

#BEGIN CHECK WHETHER THE BEGINNING AND ENDING DATES ARE INDEED SATURDAYS
from datetime import date, datetime, timedelta
BeginDate = date(BeginDateVec[0],BeginDateVec[1], BeginDateVec[2])
EndDate = date(EndDateVec[0],EndDateVec[1], EndDateVec[2])
if BeginDate.weekday() != 5:  # 0 for Monday, 5 for Saturday
  print('Beginning Date Vector needs to be a Saturday!!')
  sys.exit(0)
if EndDate.weekday() != 5:  # 0 for Monday, 5 for Saturday
  print('Ending Date Vector needs to be a Saturday!!')
  sys.exit(0)
#END CHECK WHETHER THE BEGINNING AND ENDING DATES ARE INDEED SATURDAYS

#BEGIN CALCULATING THE NUMBER OF WEEKS ELAPSED FROM THE BEGINNING DATE VECTOR TO THE ENDING ONE
TotalNumDaysDiff = abs(EndDate-BeginDate).days
TotalNumWeeksDiff = TotalNumDaysDiff//7
#END CALCULATING THE NUMBER OF WEEKS ELAPSED FROM THE BEGINNING DATE VECTOR TO THE ENDING ONE

from os import path
import pandas as pd
import numpy as np
#FirstValidFileFound = 0
for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
  IntermediateDate = BeginDate + timedelta(weeks=NumWeeksDiff)
  FileName = FilesPath+'%s-%04d%02d%02d.csv'%(PdiOrPhdStr, IntermediateDate.year, IntermediateDate.month, IntermediateDate.day)
  IntermediateYYYYMMDD = 10000*IntermediateDate.year + 100*IntermediateDate.month + IntermediateDate.day
  IntermediateYYYYMMDD = np.array([IntermediateYYYYMMDD], dtype=np.int32)  
  if path.exists(FileName):
    FileData = pd.read_csv(FileName, skiprows=1, names = ['climdiv','Palmer'], dtype = {'climdiv': np.int32, 'Palmer': np.float64})
    if not FileData.empty:
      FileData.set_index("climdiv",inplace=True)
      FileData_index_list = FileData.index.values.tolist()
      if FileData.isnull().sum().values[0] != 0:
        print("ERROR: Null values in file on day "+str(IntermediateDate.year)+" "+str(IntermediateDate.month)+" "+str(IntermediateDate.day))
        sys.exit(0)
      if CLIMDIV_SortedList_FrmShpFile != FileData_index_list:
        print("ERROR: File CLIMDIV values dont match with those in shapefile!!")
        sys.exit(0)
      IntermediatePalmerArray = FileData['Palmer'].to_numpy(copy=True)
      IntermediatePalmerArray[np.where( (IntermediatePalmerArray < PalmerIndex_LowerLimit) | (IntermediatePalmerArray > PalmerIndex_UpperLimit) )] = np.NaN
    else: # if not FileData.empty:
      print(FileName+' is empty!!')
      IntermediatePalmerArray = np.empty((len(CLIMDIV_SortedList_FrmShpFile),))
      IntermediatePalmerArray[:] = np.NaN
  else:
    print(FileName+' does not exist!!')
    IntermediatePalmerArray = np.empty((len(CLIMDIV_SortedList_FrmShpFile),))
    IntermediatePalmerArray[:] = np.NaN
  #end of "if path.exists(FileName)"
  IntermediatePalmerArray = np.expand_dims(IntermediatePalmerArray, axis=0)
  if NumWeeksDiff == 0:
    YYYYMMDD_Of_RefArrayForPrcntl = np.array(IntermediateYYYYMMDD, copy=True) 
    Palmer_RefArrayForPrcntl = np.array(IntermediatePalmerArray, copy=True)
  else: 
    YYYYMMDD_Of_RefArrayForPrcntl = np.concatenate((YYYYMMDD_Of_RefArrayForPrcntl, IntermediateYYYYMMDD))
    Palmer_RefArrayForPrcntl = np.concatenate((Palmer_RefArrayForPrcntl, IntermediatePalmerArray))
#end of "for NumWeeksDiff in range(0,TotalNumWeeksDiff+1)"

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("Palmer_RefArrayForPrcntl.shape is ",Palmer_RefArrayForPrcntl.shape)
print("Palmer_RefArrayForPrcntl is ",Palmer_RefArrayForPrcntl)
print("np.amin(np.isnan(Palmer_RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(Palmer_RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(Palmer_RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(Palmer_RefArrayForPrcntl).sum(axis=0)))
print('overall min is ',np.nanmin(Palmer_RefArrayForPrcntl),', overall max is ',np.nanmax(Palmer_RefArrayForPrcntl))

np.savez_compressed(PalmerArrayFileName, YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, Palmer_RefArrayForPrcntl = Palmer_RefArrayForPrcntl)



