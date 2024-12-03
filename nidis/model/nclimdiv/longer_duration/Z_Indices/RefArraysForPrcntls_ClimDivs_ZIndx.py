from __future__ import division
import sys
import numpy as np
#######BEGIN ANY EDITS REQUIRED#######
#BeginYear = 1900 # Beginning year
BeginYear = 1932 # Beginning year
#EndYear = 2019 # Ending year
EndYear = 2020 # Ending year
EndMonth = 1 # Ending year
BeginDateVec = [BeginYear, 1]
#EndDateVec = [EndYear, 12]
EndDateVec = [EndYear, EndMonth]
VariabStr = 'zndx' # possible values are 'pmdi', 'phdi', 'zndx', 'pcpn'
if VariabStr == 'pcpn':
  VariabNum = 1
elif VariabStr == 'phdi':
  VariabNum = 6
elif VariabStr == 'zndx':
  VariabNum = 7
elif VariabStr == 'pmdi':
  VariabNum = 8
else:
  print('VariabStr should be pcpn, phdi, zndx, pmdi!!')
  sys.exit(0)
FilePath = '/att/nobackup/dmocko/Palmer/monthly/'
#FilePath = '/discover/nobackup/syatheen/NIDIS/Data/Palmer/monthly/'
FileName = FilePath+'climdiv-'+VariabStr+'dv-v1.0.0-20200204'
ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
#ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
LowerLimit = -20.0
UpperLimit = 20.0
NumMonthsAccum = 60
IfTransformToMean = 0 # If mean instead of accum
if IfTransformToMean == 1:
  ArrayFileName = 'XRefArr_'+str(NumMonthsAccum)+'MonthMean'+VariabStr+'_'+format(BeginDateVec[0],'04')+format(BeginDateVec[1],'02')+'To'+format(EndDateVec[0],'04')+format(EndDateVec[1],'02')+'.npz'
else:
  ArrayFileName = 'RefArr_'+str(NumMonthsAccum)+'MonthAccum'+VariabStr+'_'+format(BeginDateVec[0],'04')+format(BeginDateVec[1],'02')+'To'+format(EndDateVec[0],'04')+format(EndDateVec[1],'02')+'.npz'
#######END ANY EDITS REQUIRED#########

from datetime import date 
BeginDate = date(BeginDateVec[0],BeginDateVec[1], 1) # day of 1 as placeholder
EndDate = date(EndDateVec[0],EndDateVec[1], 1) # day of 1 as placeholder
if BeginDate > EndDate:
  print('BeginDate should not be later than EndDate!!!')
  sys.exit(0)

from dateutil.relativedelta import relativedelta
BeginDate = BeginDate + relativedelta(months = -(NumMonthsAccum-1)) 
BeginDateVec = [BeginDate.year, BeginDate.month]
BeginYear = BeginDateVec[0]

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
import geopandas as gp
ClimDivShp = gp.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

from os import path
import pandas as pd
if path.exists(FileName):
  FileData = pd.read_table(FileName, header=None, sep="\s+", names = ['st_dv_variab_year','monthlyValue01','monthlyValue02','monthlyValue03','monthlyValue04','monthlyValue05','monthlyValue06','monthlyValue07','monthlyValue08','monthlyValue09','monthlyValue10','monthlyValue11','monthlyValue12'], dtype = {'st_dv_variab_year': np.dtype('U',10), 'monthlyValue01': np.float64, 'monthlyValue02': np.float64, 'monthlyValue03': np.float64, 'monthlyValue04': np.float64, 'monthlyValue05': np.float64, 'monthlyValue06': np.float64, 'monthlyValue07': np.float64, 'monthlyValue08': np.float64, 'monthlyValue09': np.float64, 'monthlyValue10': np.float64, 'monthlyValue11': np.float64, 'monthlyValue12': np.float64})
  if not FileData.empty:
    FileData["st"] = FileData["st_dv_variab_year"].apply(lambda d: d[:2])
    FileData["variab"] = FileData["st_dv_variab_year"].apply(lambda d: d[4:6])
    FileData["year"] = FileData["st_dv_variab_year"].apply(lambda d: d[6:])
    FileData["st_dv"] = FileData["st_dv_variab_year"].apply(lambda d: d[:4])
    FileData["st"] = FileData["st"].astype(str).astype(np.int32)
    FileData["variab"] = FileData["variab"].astype(str).astype(np.int32)
    FileData["year"] = FileData["year"].astype(str).astype(np.int32)
    FileData["st_dv"] = FileData["st_dv"].astype(str).astype(np.int32)
    NewData = FileData.loc[(FileData['st'] >= 1) &
                           (FileData['st'] <= 48) &
                           (FileData['variab'] == VariabNum) &
                           (FileData['year'] >= BeginYear) &
                           (FileData['year'] <= EndYear) ]     
    NewData = NewData[["st_dv","year",'monthlyValue01','monthlyValue02','monthlyValue03','monthlyValue04','monthlyValue05','monthlyValue06','monthlyValue07','monthlyValue08','monthlyValue09','monthlyValue10','monthlyValue11','monthlyValue12']]
    NewData = pd.wide_to_long(NewData, stubnames='monthlyValue', 
                              i=['st_dv','year'],
                              j='month')
    NewData = pd.DataFrame(NewData.to_records())
    NewData["month"] = NewData["month"].astype(str).str.zfill(2)
    NewData["year"] = NewData["year"].astype(str)
    NewData["yearmonth"] = NewData["year"]+NewData["month"]
    NewData["yearmonth"] = NewData["yearmonth"].astype(str).astype(np.int32)
    NewData = NewData.drop(["year", "month"], axis=1)
    NewData = NewData.pivot(index='yearmonth', columns='st_dv', values='monthlyValue')
    NewData_columns_list = NewData.columns.values.tolist()
    if CLIMDIV_SortedList_FrmShpFile != NewData_columns_list:
      print("ERROR: File CLIMDIV values dont match with those in shapefile!!")
      sys.exit(0)

    NewData = NewData.loc[100*BeginDateVec[0]+BeginDateVec[1]:100*EndDateVec[0]+EndDateVec[1]:1]

    NewData_index_list = NewData.index.values.tolist()

    TotalNumMonthsDiff = (EndDate.year - BeginDate.year) * 12 + (EndDate.month - BeginDate.month) # Calculating the number of months elapsed from the beginning date to the ending one
 
    DesiredYearMonthsList = [] 
    for NumMonthsDiff in range(0,TotalNumMonthsDiff+1):
      IntermediateDate = BeginDate + relativedelta(months=NumMonthsDiff) 
      DesiredYearMonthsList.append(100*IntermediateDate.year+IntermediateDate.month)
    if DesiredYearMonthsList != NewData_index_list:
      print("ERROR: YearMonths dont match those desired!!")
      print("DesiredYearMonthsList is ",DesiredYearMonthsList)
      print("len(DesiredYearMonthsList) is ",len(DesiredYearMonthsList))
      print("NewData_index_list is ",NewData_index_list)
      print("len(NewData_index_list) is ",len(NewData_index_list))
      sys.exit(0)

    print("NewData.isnull().sum().values[0] is ",NewData.isnull().sum().values[0])

    print('overall min is ',NewData.values.min(),', overall max is ',NewData.values.max())
    if (NewData.isnull().sum().values[0] != 0):
      print("ERROR: Null/NaN values means we cannot use current cumsum technique!!!")
      sys.exit(0)

    if ~np.isnan(LowerLimit):
      if (NewData.values.min() < LowerLimit):
        print("ERROR: values < LowerLimit means we cannot use current cumsum technique!!!")
        sys.exit(0)
    if ~np.isnan(UpperLimit):
      if (NewData.values.max() > UpperLimit):
        print("ERROR: values > UpperLimit means we cannot use current cumsum technique!!!")
        sys.exit(0)
    
    RefArrayForPrcntl = NewData.to_numpy(copy=True) 

#      if np.isnan(UpperLimit):
#        RefArrayForPrcntl[np.where( RefArrayForPrcntl < LowerLimit )] = np.NaN
#      else:
#        RefArrayForPrcntl[np.where( (RefArrayForPrcntl < LowerLimit) | (RefArrayForPrcntl > UpperLimit) )] = np.NaN
  
    print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
    print("RefArrayForPrcntl is ",RefArrayForPrcntl)
#      print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
#      print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))

    YYYYMM_Of_RefArrayForPrcntl = np.array(NewData_index_list, dtype = np.int32)
    YYYYMM_Of_RefArrayForPrcntl = np.expand_dims(YYYYMM_Of_RefArrayForPrcntl, axis=1)
    print("YYYYMM_Of_RefArrayForPrcntl.shape is ",YYYYMM_Of_RefArrayForPrcntl.shape)
    print("YYYYMM_Of_RefArrayForPrcntl is ",YYYYMM_Of_RefArrayForPrcntl)

    #Begin for n-month accumulation
    RefArrayForPrcntl = RefArrayForPrcntl.cumsum(axis=0)
    RefArrayForPrcntl[NumMonthsAccum:] = RefArrayForPrcntl[NumMonthsAccum:] - RefArrayForPrcntl[:-NumMonthsAccum]
#      print("RefArrayForPrcntl is ",RefArrayForPrcntl)
    YYYYMM_Of_RefArrayForPrcntl = YYYYMM_Of_RefArrayForPrcntl[NumMonthsAccum-1:]
    RefArrayForPrcntl = RefArrayForPrcntl[NumMonthsAccum-1:]
    #End for n-month accumulation

    print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
    print("RefArrayForPrcntl is ",RefArrayForPrcntl)
    print("YYYYMM_Of_RefArrayForPrcntl.shape is ",YYYYMM_Of_RefArrayForPrcntl.shape)
    print("YYYYMM_Of_RefArrayForPrcntl is ",YYYYMM_Of_RefArrayForPrcntl)

    if IfTransformToMean == 1:
      RefArrayForPrcntl = RefArrayForPrcntl / NumMonthsAccum 

    np.savez_compressed(ArrayFileName, YYYYMM_Of_RefArrayForPrcntl = YYYYMM_Of_RefArrayForPrcntl, RefArrayForPrcntl = RefArrayForPrcntl)

  else: # if not FileData.empty:
    print(FileName+' is empty!!')
else:
  print(FileName+' does not exist!!')



