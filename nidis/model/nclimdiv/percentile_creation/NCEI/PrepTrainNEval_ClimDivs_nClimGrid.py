# Coded by Soni Yatheendradas
#         on Sep 14, 2021
from __future__ import division

# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

spei_gamma_01_RefFileName = 'RefArrays/ClimDiv_spei_gamma_01_18950205To20210727.npz'
spei_gamma_02_RefFileName = 'RefArrays/ClimDiv_spei_gamma_02_18950305To20210727.npz'
spei_gamma_03_RefFileName = 'RefArrays/ClimDiv_spei_gamma_03_18950402To20210727.npz'
spei_gamma_06_RefFileName = 'RefArrays/ClimDiv_spei_gamma_06_18950702To20210727.npz'
spei_gamma_09_RefFileName = 'RefArrays/ClimDiv_spei_gamma_09_18951001To20210727.npz'
spei_gamma_12_RefFileName = 'RefArrays/ClimDiv_spei_gamma_12_18951231To20210727.npz'
spei_gamma_24_RefFileName = 'RefArrays/ClimDiv_spei_gamma_24_18970105To20210727.npz'
spei_gamma_36_RefFileName = 'RefArrays/ClimDiv_spei_gamma_36_18980104To20210727.npz'
spei_gamma_48_RefFileName = 'RefArrays/ClimDiv_spei_gamma_48_18990103To20210727.npz'
spei_gamma_60_RefFileName = 'RefArrays/ClimDiv_spei_gamma_60_19000102To20210727.npz'
spei_gamma_72_RefFileName = 'RefArrays/ClimDiv_spei_gamma_72_19010101To20210727.npz'

spei_pearson_01_RefFileName = 'RefArrays/ClimDiv_spei_pearson_01_18950205To20210727.npz'
spei_pearson_02_RefFileName = 'RefArrays/ClimDiv_spei_pearson_02_18950305To20210727.npz'
spei_pearson_03_RefFileName = 'RefArrays/ClimDiv_spei_pearson_03_18950402To20210727.npz'
spei_pearson_06_RefFileName = 'RefArrays/ClimDiv_spei_pearson_06_18950702To20210727.npz'
spei_pearson_09_RefFileName = 'RefArrays/ClimDiv_spei_pearson_09_18951001To20210727.npz'
spei_pearson_12_RefFileName = 'RefArrays/ClimDiv_spei_pearson_12_18951231To20210727.npz'
spei_pearson_24_RefFileName = 'RefArrays/ClimDiv_spei_pearson_24_18970105To20210727.npz'
spei_pearson_36_RefFileName = 'RefArrays/ClimDiv_spei_pearson_36_18980104To20210727.npz'
spei_pearson_48_RefFileName = 'RefArrays/ClimDiv_spei_pearson_48_18990103To20210727.npz'
spei_pearson_60_RefFileName = 'RefArrays/ClimDiv_spei_pearson_60_19000102To20210727.npz'
spei_pearson_72_RefFileName = 'RefArrays/ClimDiv_spei_pearson_72_19010101To20210727.npz'

spi_gamma_01_RefFileName = 'RefArrays/ClimDiv_spi_gamma_01_18950205To20210727.npz'
spi_gamma_02_RefFileName = 'RefArrays/ClimDiv_spi_gamma_02_18950305To20210727.npz'
spi_gamma_03_RefFileName = 'RefArrays/ClimDiv_spi_gamma_03_18950402To20210727.npz'
spi_gamma_06_RefFileName = 'RefArrays/ClimDiv_spi_gamma_06_18950702To20210727.npz'
spi_gamma_09_RefFileName = 'RefArrays/ClimDiv_spi_gamma_09_18951001To20210727.npz'
spi_gamma_12_RefFileName = 'RefArrays/ClimDiv_spi_gamma_12_18951231To20210727.npz'
spi_gamma_24_RefFileName = 'RefArrays/ClimDiv_spi_gamma_24_18970105To20210727.npz'
spi_gamma_36_RefFileName = 'RefArrays/ClimDiv_spi_gamma_36_18980104To20210727.npz'
spi_gamma_48_RefFileName = 'RefArrays/ClimDiv_spi_gamma_48_18990103To20210727.npz'
spi_gamma_60_RefFileName = 'RefArrays/ClimDiv_spi_gamma_60_19000102To20210727.npz'
spi_gamma_72_RefFileName = 'RefArrays/ClimDiv_spi_gamma_72_19010101To20210727.npz'

spi_pearson_01_RefFileName = 'RefArrays/ClimDiv_spi_pearson_01_18950205To20210727.npz'
spi_pearson_02_RefFileName = 'RefArrays/ClimDiv_spi_pearson_02_18950305To20210727.npz'
spi_pearson_03_RefFileName = 'RefArrays/ClimDiv_spi_pearson_03_18950402To20210727.npz'
spi_pearson_06_RefFileName = 'RefArrays/ClimDiv_spi_pearson_06_18950702To20210727.npz'
spi_pearson_09_RefFileName = 'RefArrays/ClimDiv_spi_pearson_09_18951001To20210727.npz'
spi_pearson_12_RefFileName = 'RefArrays/ClimDiv_spi_pearson_12_18951231To20210727.npz'
spi_pearson_24_RefFileName = 'RefArrays/ClimDiv_spi_pearson_24_18970105To20210727.npz'
spi_pearson_36_RefFileName = 'RefArrays/ClimDiv_spi_pearson_36_18980104To20210727.npz'
spi_pearson_48_RefFileName = 'RefArrays/ClimDiv_spi_pearson_48_18990103To20210727.npz'
spi_pearson_60_RefFileName = 'RefArrays/ClimDiv_spi_pearson_60_19000102To20210727.npz'
spi_pearson_72_RefFileName = 'RefArrays/ClimDiv_spi_pearson_72_19010101To20210727.npz'

pet_01_RefFileName = 'RefArrays/ClimDiv_pet_01_18950205To20210727.npz'
pet_02_RefFileName = 'RefArrays/ClimDiv_pet_02_18950305To20210727.npz'
pet_03_RefFileName = 'RefArrays/ClimDiv_pet_03_18950402To20210727.npz'
pet_06_RefFileName = 'RefArrays/ClimDiv_pet_06_18950702To20210727.npz'
pet_09_RefFileName = 'RefArrays/ClimDiv_pet_09_18951001To20210727.npz'
pet_12_RefFileName = 'RefArrays/ClimDiv_pet_12_18951231To20210727.npz'
pet_24_RefFileName = 'RefArrays/ClimDiv_pet_24_18970105To20210727.npz'
pet_36_RefFileName = 'RefArrays/ClimDiv_pet_36_18980104To20210727.npz'
pet_48_RefFileName = 'RefArrays/ClimDiv_pet_48_18990103To20210727.npz'
pet_60_RefFileName = 'RefArrays/ClimDiv_pet_60_19000102To20210727.npz'
pet_72_RefFileName = 'RefArrays/ClimDiv_pet_72_19010101To20210727.npz'

prcp_01_RefFileName = 'RefArrays/ClimDiv_prcp_01_18950205To20210727.npz'
prcp_02_RefFileName = 'RefArrays/ClimDiv_prcp_02_18950305To20210727.npz'
prcp_03_RefFileName = 'RefArrays/ClimDiv_prcp_03_18950402To20210727.npz'
prcp_06_RefFileName = 'RefArrays/ClimDiv_prcp_06_18950702To20210727.npz'
prcp_09_RefFileName = 'RefArrays/ClimDiv_prcp_09_18951001To20210727.npz'
prcp_12_RefFileName = 'RefArrays/ClimDiv_prcp_12_18951231To20210727.npz'
prcp_24_RefFileName = 'RefArrays/ClimDiv_prcp_24_18970105To20210727.npz'
prcp_36_RefFileName = 'RefArrays/ClimDiv_prcp_36_18980104To20210727.npz'
prcp_48_RefFileName = 'RefArrays/ClimDiv_prcp_48_18990103To20210727.npz'
prcp_60_RefFileName = 'RefArrays/ClimDiv_prcp_60_19000102To20210727.npz'
prcp_72_RefFileName = 'RefArrays/ClimDiv_prcp_72_19010101To20210727.npz'

tavg_01_RefFileName = 'RefArrays/ClimDiv_tavg_01_18950205To20210727.npz'
tavg_02_RefFileName = 'RefArrays/ClimDiv_tavg_02_18950305To20210727.npz'
tavg_03_RefFileName = 'RefArrays/ClimDiv_tavg_03_18950402To20210727.npz'
tavg_06_RefFileName = 'RefArrays/ClimDiv_tavg_06_18950702To20210727.npz'
tavg_09_RefFileName = 'RefArrays/ClimDiv_tavg_09_18951001To20210727.npz'
tavg_12_RefFileName = 'RefArrays/ClimDiv_tavg_12_18951231To20210727.npz'
tavg_24_RefFileName = 'RefArrays/ClimDiv_tavg_24_18970105To20210727.npz'
tavg_36_RefFileName = 'RefArrays/ClimDiv_tavg_36_18980104To20210727.npz'
tavg_48_RefFileName = 'RefArrays/ClimDiv_tavg_48_18990103To20210727.npz'
tavg_60_RefFileName = 'RefArrays/ClimDiv_tavg_60_19000102To20210727.npz'
tavg_72_RefFileName = 'RefArrays/ClimDiv_tavg_72_19010101To20210727.npz'

tmax_01_RefFileName = 'RefArrays/ClimDiv_tmax_01_18950205To20210727.npz'
tmax_02_RefFileName = 'RefArrays/ClimDiv_tmax_02_18950305To20210727.npz'
tmax_03_RefFileName = 'RefArrays/ClimDiv_tmax_03_18950402To20210727.npz'
tmax_06_RefFileName = 'RefArrays/ClimDiv_tmax_06_18950702To20210727.npz'
tmax_09_RefFileName = 'RefArrays/ClimDiv_tmax_09_18951001To20210727.npz'
tmax_12_RefFileName = 'RefArrays/ClimDiv_tmax_12_18951231To20210727.npz'
tmax_24_RefFileName = 'RefArrays/ClimDiv_tmax_24_18970105To20210727.npz'
tmax_36_RefFileName = 'RefArrays/ClimDiv_tmax_36_18980104To20210727.npz'
tmax_48_RefFileName = 'RefArrays/ClimDiv_tmax_48_18990103To20210727.npz'
tmax_60_RefFileName = 'RefArrays/ClimDiv_tmax_60_19000102To20210727.npz'
tmax_72_RefFileName = 'RefArrays/ClimDiv_tmax_72_19010101To20210727.npz'

TrainDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Train_AllnCG_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_AllnCG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Test_AllnCG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import rankdata

ssstart_Overall = datetime.now()

Training_BeginDate = date(Training_BeginDateVecList[0], Training_BeginDateVecList[1], Training_BeginDateVecList[2])
Training_EndDate = date(Training_EndDateVecList[0], Training_EndDateVecList[1], Training_EndDateVecList[2])
Eval_BeginDate = date(Eval_BeginDateVecList[0], Eval_BeginDateVecList[1], Eval_BeginDateVecList[2])
Eval_EndDate = date(Eval_EndDateVecList[0], Eval_EndDateVecList[1], Eval_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if Training_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for training needs to be a Tuesday!!')
  sys.exit(0)
if Training_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for training needs to be a Tuesday!!')
  sys.exit(0)
if Eval_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for evaluation needs to be a Tuesday!!')
  sys.exit(0)
if Eval_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for evaluation needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if Training_BeginDate > Training_EndDate:
  print('Training_BeginDate should not be later than Training_EndDate!!!')
  sys.exit(0)
if Eval_BeginDate > Eval_EndDate:
  print('Eval_BeginDate should not be later than Eval_EndDate!!!')
  sys.exit(0)

spei_gamma_01_RefObject = np.load(spei_gamma_01_RefFileName)
spei_gamma_02_RefObject = np.load(spei_gamma_02_RefFileName)
spei_gamma_03_RefObject = np.load(spei_gamma_03_RefFileName)
spei_gamma_06_RefObject = np.load(spei_gamma_06_RefFileName)
spei_gamma_09_RefObject = np.load(spei_gamma_09_RefFileName)
spei_gamma_12_RefObject = np.load(spei_gamma_12_RefFileName)
spei_gamma_24_RefObject = np.load(spei_gamma_24_RefFileName)
spei_gamma_36_RefObject = np.load(spei_gamma_36_RefFileName)
spei_gamma_48_RefObject = np.load(spei_gamma_48_RefFileName)
spei_gamma_60_RefObject = np.load(spei_gamma_60_RefFileName)
spei_gamma_72_RefObject = np.load(spei_gamma_72_RefFileName)

spei_pearson_01_RefObject = np.load(spei_pearson_01_RefFileName)
spei_pearson_02_RefObject = np.load(spei_pearson_02_RefFileName)
spei_pearson_03_RefObject = np.load(spei_pearson_03_RefFileName)
spei_pearson_06_RefObject = np.load(spei_pearson_06_RefFileName)
spei_pearson_09_RefObject = np.load(spei_pearson_09_RefFileName)
spei_pearson_12_RefObject = np.load(spei_pearson_12_RefFileName)
spei_pearson_24_RefObject = np.load(spei_pearson_24_RefFileName)
spei_pearson_36_RefObject = np.load(spei_pearson_36_RefFileName)
spei_pearson_48_RefObject = np.load(spei_pearson_48_RefFileName)
spei_pearson_60_RefObject = np.load(spei_pearson_60_RefFileName)
spei_pearson_72_RefObject = np.load(spei_pearson_72_RefFileName)

spi_gamma_01_RefObject = np.load(spi_gamma_01_RefFileName)
spi_gamma_02_RefObject = np.load(spi_gamma_02_RefFileName)
spi_gamma_03_RefObject = np.load(spi_gamma_03_RefFileName)
spi_gamma_06_RefObject = np.load(spi_gamma_06_RefFileName)
spi_gamma_09_RefObject = np.load(spi_gamma_09_RefFileName)
spi_gamma_12_RefObject = np.load(spi_gamma_12_RefFileName)
spi_gamma_24_RefObject = np.load(spi_gamma_24_RefFileName)
spi_gamma_36_RefObject = np.load(spi_gamma_36_RefFileName)
spi_gamma_48_RefObject = np.load(spi_gamma_48_RefFileName)
spi_gamma_60_RefObject = np.load(spi_gamma_60_RefFileName)
spi_gamma_72_RefObject = np.load(spi_gamma_72_RefFileName)

spi_pearson_01_RefObject = np.load(spi_pearson_01_RefFileName)
spi_pearson_02_RefObject = np.load(spi_pearson_02_RefFileName)
spi_pearson_03_RefObject = np.load(spi_pearson_03_RefFileName)
spi_pearson_06_RefObject = np.load(spi_pearson_06_RefFileName)
spi_pearson_09_RefObject = np.load(spi_pearson_09_RefFileName)
spi_pearson_12_RefObject = np.load(spi_pearson_12_RefFileName)
spi_pearson_24_RefObject = np.load(spi_pearson_24_RefFileName)
spi_pearson_36_RefObject = np.load(spi_pearson_36_RefFileName)
spi_pearson_48_RefObject = np.load(spi_pearson_48_RefFileName)
spi_pearson_60_RefObject = np.load(spi_pearson_60_RefFileName)
spi_pearson_72_RefObject = np.load(spi_pearson_72_RefFileName)

pet_01_RefObject = np.load(pet_01_RefFileName)
pet_02_RefObject = np.load(pet_02_RefFileName)
pet_03_RefObject = np.load(pet_03_RefFileName)
pet_06_RefObject = np.load(pet_06_RefFileName)
pet_09_RefObject = np.load(pet_09_RefFileName)
pet_12_RefObject = np.load(pet_12_RefFileName)
pet_24_RefObject = np.load(pet_24_RefFileName)
pet_36_RefObject = np.load(pet_36_RefFileName)
pet_48_RefObject = np.load(pet_48_RefFileName)
pet_60_RefObject = np.load(pet_60_RefFileName)
pet_72_RefObject = np.load(pet_72_RefFileName)

prcp_01_RefObject = np.load(prcp_01_RefFileName)
prcp_02_RefObject = np.load(prcp_02_RefFileName)
prcp_03_RefObject = np.load(prcp_03_RefFileName)
prcp_06_RefObject = np.load(prcp_06_RefFileName)
prcp_09_RefObject = np.load(prcp_09_RefFileName)
prcp_12_RefObject = np.load(prcp_12_RefFileName)
prcp_24_RefObject = np.load(prcp_24_RefFileName)
prcp_36_RefObject = np.load(prcp_36_RefFileName)
prcp_48_RefObject = np.load(prcp_48_RefFileName)
prcp_60_RefObject = np.load(prcp_60_RefFileName)
prcp_72_RefObject = np.load(prcp_72_RefFileName)

tavg_01_RefObject = np.load(tavg_01_RefFileName)
tavg_02_RefObject = np.load(tavg_02_RefFileName)
tavg_03_RefObject = np.load(tavg_03_RefFileName)
tavg_06_RefObject = np.load(tavg_06_RefFileName)
tavg_09_RefObject = np.load(tavg_09_RefFileName)
tavg_12_RefObject = np.load(tavg_12_RefFileName)
tavg_24_RefObject = np.load(tavg_24_RefFileName)
tavg_36_RefObject = np.load(tavg_36_RefFileName)
tavg_48_RefObject = np.load(tavg_48_RefFileName)
tavg_60_RefObject = np.load(tavg_60_RefFileName)
tavg_72_RefObject = np.load(tavg_72_RefFileName)

tmax_01_RefObject = np.load(tmax_01_RefFileName)
tmax_02_RefObject = np.load(tmax_02_RefFileName)
tmax_03_RefObject = np.load(tmax_03_RefFileName)
tmax_06_RefObject = np.load(tmax_06_RefFileName)
tmax_09_RefObject = np.load(tmax_09_RefFileName)
tmax_12_RefObject = np.load(tmax_12_RefFileName)
tmax_24_RefObject = np.load(tmax_24_RefFileName)
tmax_36_RefObject = np.load(tmax_36_RefFileName)
tmax_48_RefObject = np.load(tmax_48_RefFileName)
tmax_60_RefObject = np.load(tmax_60_RefFileName)
tmax_72_RefObject = np.load(tmax_72_RefFileName)

spei_gamma_01_YYYYMMDD_Of_RefArray = spei_gamma_01_RefObject['spei_gamma_01_YYYYMMDD_Of_RefArray']
spei_gamma_02_YYYYMMDD_Of_RefArray = spei_gamma_02_RefObject['spei_gamma_02_YYYYMMDD_Of_RefArray']
spei_gamma_03_YYYYMMDD_Of_RefArray = spei_gamma_03_RefObject['spei_gamma_03_YYYYMMDD_Of_RefArray']
spei_gamma_06_YYYYMMDD_Of_RefArray = spei_gamma_06_RefObject['spei_gamma_06_YYYYMMDD_Of_RefArray']
spei_gamma_09_YYYYMMDD_Of_RefArray = spei_gamma_09_RefObject['spei_gamma_09_YYYYMMDD_Of_RefArray']
spei_gamma_12_YYYYMMDD_Of_RefArray = spei_gamma_12_RefObject['spei_gamma_12_YYYYMMDD_Of_RefArray']
spei_gamma_24_YYYYMMDD_Of_RefArray = spei_gamma_24_RefObject['spei_gamma_24_YYYYMMDD_Of_RefArray']
spei_gamma_36_YYYYMMDD_Of_RefArray = spei_gamma_36_RefObject['spei_gamma_36_YYYYMMDD_Of_RefArray']
spei_gamma_48_YYYYMMDD_Of_RefArray = spei_gamma_48_RefObject['spei_gamma_48_YYYYMMDD_Of_RefArray']
spei_gamma_60_YYYYMMDD_Of_RefArray = spei_gamma_60_RefObject['spei_gamma_60_YYYYMMDD_Of_RefArray']
spei_gamma_72_YYYYMMDD_Of_RefArray = spei_gamma_72_RefObject['spei_gamma_72_YYYYMMDD_Of_RefArray']

spei_pearson_01_YYYYMMDD_Of_RefArray = spei_pearson_01_RefObject['spei_pearson_01_YYYYMMDD_Of_RefArray']
spei_pearson_02_YYYYMMDD_Of_RefArray = spei_pearson_02_RefObject['spei_pearson_02_YYYYMMDD_Of_RefArray']
spei_pearson_03_YYYYMMDD_Of_RefArray = spei_pearson_03_RefObject['spei_pearson_03_YYYYMMDD_Of_RefArray']
spei_pearson_06_YYYYMMDD_Of_RefArray = spei_pearson_06_RefObject['spei_pearson_06_YYYYMMDD_Of_RefArray']
spei_pearson_09_YYYYMMDD_Of_RefArray = spei_pearson_09_RefObject['spei_pearson_09_YYYYMMDD_Of_RefArray']
spei_pearson_12_YYYYMMDD_Of_RefArray = spei_pearson_12_RefObject['spei_pearson_12_YYYYMMDD_Of_RefArray']
spei_pearson_24_YYYYMMDD_Of_RefArray = spei_pearson_24_RefObject['spei_pearson_24_YYYYMMDD_Of_RefArray']
spei_pearson_36_YYYYMMDD_Of_RefArray = spei_pearson_36_RefObject['spei_pearson_36_YYYYMMDD_Of_RefArray']
spei_pearson_48_YYYYMMDD_Of_RefArray = spei_pearson_48_RefObject['spei_pearson_48_YYYYMMDD_Of_RefArray']
spei_pearson_60_YYYYMMDD_Of_RefArray = spei_pearson_60_RefObject['spei_pearson_60_YYYYMMDD_Of_RefArray']
spei_pearson_72_YYYYMMDD_Of_RefArray = spei_pearson_72_RefObject['spei_pearson_72_YYYYMMDD_Of_RefArray']

spi_gamma_01_YYYYMMDD_Of_RefArray = spi_gamma_01_RefObject['spi_gamma_01_YYYYMMDD_Of_RefArray']
spi_gamma_02_YYYYMMDD_Of_RefArray = spi_gamma_02_RefObject['spi_gamma_02_YYYYMMDD_Of_RefArray']
spi_gamma_03_YYYYMMDD_Of_RefArray = spi_gamma_03_RefObject['spi_gamma_03_YYYYMMDD_Of_RefArray']
spi_gamma_06_YYYYMMDD_Of_RefArray = spi_gamma_06_RefObject['spi_gamma_06_YYYYMMDD_Of_RefArray']
spi_gamma_09_YYYYMMDD_Of_RefArray = spi_gamma_09_RefObject['spi_gamma_09_YYYYMMDD_Of_RefArray']
spi_gamma_12_YYYYMMDD_Of_RefArray = spi_gamma_12_RefObject['spi_gamma_12_YYYYMMDD_Of_RefArray']
spi_gamma_24_YYYYMMDD_Of_RefArray = spi_gamma_24_RefObject['spi_gamma_24_YYYYMMDD_Of_RefArray']
spi_gamma_36_YYYYMMDD_Of_RefArray = spi_gamma_36_RefObject['spi_gamma_36_YYYYMMDD_Of_RefArray']
spi_gamma_48_YYYYMMDD_Of_RefArray = spi_gamma_48_RefObject['spi_gamma_48_YYYYMMDD_Of_RefArray']
spi_gamma_60_YYYYMMDD_Of_RefArray = spi_gamma_60_RefObject['spi_gamma_60_YYYYMMDD_Of_RefArray']
spi_gamma_72_YYYYMMDD_Of_RefArray = spi_gamma_72_RefObject['spi_gamma_72_YYYYMMDD_Of_RefArray']

spi_pearson_01_YYYYMMDD_Of_RefArray = spi_pearson_01_RefObject['spi_pearson_01_YYYYMMDD_Of_RefArray']
spi_pearson_02_YYYYMMDD_Of_RefArray = spi_pearson_02_RefObject['spi_pearson_02_YYYYMMDD_Of_RefArray']
spi_pearson_03_YYYYMMDD_Of_RefArray = spi_pearson_03_RefObject['spi_pearson_03_YYYYMMDD_Of_RefArray']
spi_pearson_06_YYYYMMDD_Of_RefArray = spi_pearson_06_RefObject['spi_pearson_06_YYYYMMDD_Of_RefArray']
spi_pearson_09_YYYYMMDD_Of_RefArray = spi_pearson_09_RefObject['spi_pearson_09_YYYYMMDD_Of_RefArray']
spi_pearson_12_YYYYMMDD_Of_RefArray = spi_pearson_12_RefObject['spi_pearson_12_YYYYMMDD_Of_RefArray']
spi_pearson_24_YYYYMMDD_Of_RefArray = spi_pearson_24_RefObject['spi_pearson_24_YYYYMMDD_Of_RefArray']
spi_pearson_36_YYYYMMDD_Of_RefArray = spi_pearson_36_RefObject['spi_pearson_36_YYYYMMDD_Of_RefArray']
spi_pearson_48_YYYYMMDD_Of_RefArray = spi_pearson_48_RefObject['spi_pearson_48_YYYYMMDD_Of_RefArray']
spi_pearson_60_YYYYMMDD_Of_RefArray = spi_pearson_60_RefObject['spi_pearson_60_YYYYMMDD_Of_RefArray']
spi_pearson_72_YYYYMMDD_Of_RefArray = spi_pearson_72_RefObject['spi_pearson_72_YYYYMMDD_Of_RefArray']

pet_01_YYYYMMDD_Of_RefArray = pet_01_RefObject['pet_01_YYYYMMDD_Of_RefArray']
pet_02_YYYYMMDD_Of_RefArray = pet_02_RefObject['pet_02_YYYYMMDD_Of_RefArray']
pet_03_YYYYMMDD_Of_RefArray = pet_03_RefObject['pet_03_YYYYMMDD_Of_RefArray']
pet_06_YYYYMMDD_Of_RefArray = pet_06_RefObject['pet_06_YYYYMMDD_Of_RefArray']
pet_09_YYYYMMDD_Of_RefArray = pet_09_RefObject['pet_09_YYYYMMDD_Of_RefArray']
pet_12_YYYYMMDD_Of_RefArray = pet_12_RefObject['pet_12_YYYYMMDD_Of_RefArray']
pet_24_YYYYMMDD_Of_RefArray = pet_24_RefObject['pet_24_YYYYMMDD_Of_RefArray']
pet_36_YYYYMMDD_Of_RefArray = pet_36_RefObject['pet_36_YYYYMMDD_Of_RefArray']
pet_48_YYYYMMDD_Of_RefArray = pet_48_RefObject['pet_48_YYYYMMDD_Of_RefArray']
pet_60_YYYYMMDD_Of_RefArray = pet_60_RefObject['pet_60_YYYYMMDD_Of_RefArray']
pet_72_YYYYMMDD_Of_RefArray = pet_72_RefObject['pet_72_YYYYMMDD_Of_RefArray']

prcp_01_YYYYMMDD_Of_RefArray = prcp_01_RefObject['prcp_01_YYYYMMDD_Of_RefArray']
prcp_02_YYYYMMDD_Of_RefArray = prcp_02_RefObject['prcp_02_YYYYMMDD_Of_RefArray']
prcp_03_YYYYMMDD_Of_RefArray = prcp_03_RefObject['prcp_03_YYYYMMDD_Of_RefArray']
prcp_06_YYYYMMDD_Of_RefArray = prcp_06_RefObject['prcp_06_YYYYMMDD_Of_RefArray']
prcp_09_YYYYMMDD_Of_RefArray = prcp_09_RefObject['prcp_09_YYYYMMDD_Of_RefArray']
prcp_12_YYYYMMDD_Of_RefArray = prcp_12_RefObject['prcp_12_YYYYMMDD_Of_RefArray']
prcp_24_YYYYMMDD_Of_RefArray = prcp_24_RefObject['prcp_24_YYYYMMDD_Of_RefArray']
prcp_36_YYYYMMDD_Of_RefArray = prcp_36_RefObject['prcp_36_YYYYMMDD_Of_RefArray']
prcp_48_YYYYMMDD_Of_RefArray = prcp_48_RefObject['prcp_48_YYYYMMDD_Of_RefArray']
prcp_60_YYYYMMDD_Of_RefArray = prcp_60_RefObject['prcp_60_YYYYMMDD_Of_RefArray']
prcp_72_YYYYMMDD_Of_RefArray = prcp_72_RefObject['prcp_72_YYYYMMDD_Of_RefArray']

tavg_01_YYYYMMDD_Of_RefArray = tavg_01_RefObject['tavg_01_YYYYMMDD_Of_RefArray']
tavg_02_YYYYMMDD_Of_RefArray = tavg_02_RefObject['tavg_02_YYYYMMDD_Of_RefArray']
tavg_03_YYYYMMDD_Of_RefArray = tavg_03_RefObject['tavg_03_YYYYMMDD_Of_RefArray']
tavg_06_YYYYMMDD_Of_RefArray = tavg_06_RefObject['tavg_06_YYYYMMDD_Of_RefArray']
tavg_09_YYYYMMDD_Of_RefArray = tavg_09_RefObject['tavg_09_YYYYMMDD_Of_RefArray']
tavg_12_YYYYMMDD_Of_RefArray = tavg_12_RefObject['tavg_12_YYYYMMDD_Of_RefArray']
tavg_24_YYYYMMDD_Of_RefArray = tavg_24_RefObject['tavg_24_YYYYMMDD_Of_RefArray']
tavg_36_YYYYMMDD_Of_RefArray = tavg_36_RefObject['tavg_36_YYYYMMDD_Of_RefArray']
tavg_48_YYYYMMDD_Of_RefArray = tavg_48_RefObject['tavg_48_YYYYMMDD_Of_RefArray']
tavg_60_YYYYMMDD_Of_RefArray = tavg_60_RefObject['tavg_60_YYYYMMDD_Of_RefArray']
tavg_72_YYYYMMDD_Of_RefArray = tavg_72_RefObject['tavg_72_YYYYMMDD_Of_RefArray']

tmax_01_YYYYMMDD_Of_RefArray = tmax_01_RefObject['tmax_01_YYYYMMDD_Of_RefArray']
tmax_02_YYYYMMDD_Of_RefArray = tmax_02_RefObject['tmax_02_YYYYMMDD_Of_RefArray']
tmax_03_YYYYMMDD_Of_RefArray = tmax_03_RefObject['tmax_03_YYYYMMDD_Of_RefArray']
tmax_06_YYYYMMDD_Of_RefArray = tmax_06_RefObject['tmax_06_YYYYMMDD_Of_RefArray']
tmax_09_YYYYMMDD_Of_RefArray = tmax_09_RefObject['tmax_09_YYYYMMDD_Of_RefArray']
tmax_12_YYYYMMDD_Of_RefArray = tmax_12_RefObject['tmax_12_YYYYMMDD_Of_RefArray']
tmax_24_YYYYMMDD_Of_RefArray = tmax_24_RefObject['tmax_24_YYYYMMDD_Of_RefArray']
tmax_36_YYYYMMDD_Of_RefArray = tmax_36_RefObject['tmax_36_YYYYMMDD_Of_RefArray']
tmax_48_YYYYMMDD_Of_RefArray = tmax_48_RefObject['tmax_48_YYYYMMDD_Of_RefArray']
tmax_60_YYYYMMDD_Of_RefArray = tmax_60_RefObject['tmax_60_YYYYMMDD_Of_RefArray']
tmax_72_YYYYMMDD_Of_RefArray = tmax_72_RefObject['tmax_72_YYYYMMDD_Of_RefArray']

spei_gamma_01_RefArray = spei_gamma_01_RefObject['spei_gamma_01_RefArray']
spei_gamma_02_RefArray = spei_gamma_02_RefObject['spei_gamma_02_RefArray']
spei_gamma_03_RefArray = spei_gamma_03_RefObject['spei_gamma_03_RefArray']
spei_gamma_06_RefArray = spei_gamma_06_RefObject['spei_gamma_06_RefArray']
spei_gamma_09_RefArray = spei_gamma_09_RefObject['spei_gamma_09_RefArray']
spei_gamma_12_RefArray = spei_gamma_12_RefObject['spei_gamma_12_RefArray']
spei_gamma_24_RefArray = spei_gamma_24_RefObject['spei_gamma_24_RefArray']
spei_gamma_36_RefArray = spei_gamma_36_RefObject['spei_gamma_36_RefArray']
spei_gamma_48_RefArray = spei_gamma_48_RefObject['spei_gamma_48_RefArray']
spei_gamma_60_RefArray = spei_gamma_60_RefObject['spei_gamma_60_RefArray']
spei_gamma_72_RefArray = spei_gamma_72_RefObject['spei_gamma_72_RefArray']

spei_pearson_01_RefArray = spei_pearson_01_RefObject['spei_pearson_01_RefArray']
spei_pearson_02_RefArray = spei_pearson_02_RefObject['spei_pearson_02_RefArray']
spei_pearson_03_RefArray = spei_pearson_03_RefObject['spei_pearson_03_RefArray']
spei_pearson_06_RefArray = spei_pearson_06_RefObject['spei_pearson_06_RefArray']
spei_pearson_09_RefArray = spei_pearson_09_RefObject['spei_pearson_09_RefArray']
spei_pearson_12_RefArray = spei_pearson_12_RefObject['spei_pearson_12_RefArray']
spei_pearson_24_RefArray = spei_pearson_24_RefObject['spei_pearson_24_RefArray']
spei_pearson_36_RefArray = spei_pearson_36_RefObject['spei_pearson_36_RefArray']
spei_pearson_48_RefArray = spei_pearson_48_RefObject['spei_pearson_48_RefArray']
spei_pearson_60_RefArray = spei_pearson_60_RefObject['spei_pearson_60_RefArray']
spei_pearson_72_RefArray = spei_pearson_72_RefObject['spei_pearson_72_RefArray']

spi_gamma_01_RefArray = spi_gamma_01_RefObject['spi_gamma_01_RefArray']
spi_gamma_02_RefArray = spi_gamma_02_RefObject['spi_gamma_02_RefArray']
spi_gamma_03_RefArray = spi_gamma_03_RefObject['spi_gamma_03_RefArray']
spi_gamma_06_RefArray = spi_gamma_06_RefObject['spi_gamma_06_RefArray']
spi_gamma_09_RefArray = spi_gamma_09_RefObject['spi_gamma_09_RefArray']
spi_gamma_12_RefArray = spi_gamma_12_RefObject['spi_gamma_12_RefArray']
spi_gamma_24_RefArray = spi_gamma_24_RefObject['spi_gamma_24_RefArray']
spi_gamma_36_RefArray = spi_gamma_36_RefObject['spi_gamma_36_RefArray']
spi_gamma_48_RefArray = spi_gamma_48_RefObject['spi_gamma_48_RefArray']
spi_gamma_60_RefArray = spi_gamma_60_RefObject['spi_gamma_60_RefArray']
spi_gamma_72_RefArray = spi_gamma_72_RefObject['spi_gamma_72_RefArray']

spi_pearson_01_RefArray = spi_pearson_01_RefObject['spi_pearson_01_RefArray']
spi_pearson_02_RefArray = spi_pearson_02_RefObject['spi_pearson_02_RefArray']
spi_pearson_03_RefArray = spi_pearson_03_RefObject['spi_pearson_03_RefArray']
spi_pearson_06_RefArray = spi_pearson_06_RefObject['spi_pearson_06_RefArray']
spi_pearson_09_RefArray = spi_pearson_09_RefObject['spi_pearson_09_RefArray']
spi_pearson_12_RefArray = spi_pearson_12_RefObject['spi_pearson_12_RefArray']
spi_pearson_24_RefArray = spi_pearson_24_RefObject['spi_pearson_24_RefArray']
spi_pearson_36_RefArray = spi_pearson_36_RefObject['spi_pearson_36_RefArray']
spi_pearson_48_RefArray = spi_pearson_48_RefObject['spi_pearson_48_RefArray']
spi_pearson_60_RefArray = spi_pearson_60_RefObject['spi_pearson_60_RefArray']
spi_pearson_72_RefArray = spi_pearson_72_RefObject['spi_pearson_72_RefArray']

pet_01_RefArray = pet_01_RefObject['pet_01_RefArray']
pet_02_RefArray = pet_02_RefObject['pet_02_RefArray']
pet_03_RefArray = pet_03_RefObject['pet_03_RefArray']
pet_06_RefArray = pet_06_RefObject['pet_06_RefArray']
pet_09_RefArray = pet_09_RefObject['pet_09_RefArray']
pet_12_RefArray = pet_12_RefObject['pet_12_RefArray']
pet_24_RefArray = pet_24_RefObject['pet_24_RefArray']
pet_36_RefArray = pet_36_RefObject['pet_36_RefArray']
pet_48_RefArray = pet_48_RefObject['pet_48_RefArray']
pet_60_RefArray = pet_60_RefObject['pet_60_RefArray']
pet_72_RefArray = pet_72_RefObject['pet_72_RefArray']

prcp_01_RefArray = prcp_01_RefObject['prcp_01_RefArray']
prcp_02_RefArray = prcp_02_RefObject['prcp_02_RefArray']
prcp_03_RefArray = prcp_03_RefObject['prcp_03_RefArray']
prcp_06_RefArray = prcp_06_RefObject['prcp_06_RefArray']
prcp_09_RefArray = prcp_09_RefObject['prcp_09_RefArray']
prcp_12_RefArray = prcp_12_RefObject['prcp_12_RefArray']
prcp_24_RefArray = prcp_24_RefObject['prcp_24_RefArray']
prcp_36_RefArray = prcp_36_RefObject['prcp_36_RefArray']
prcp_48_RefArray = prcp_48_RefObject['prcp_48_RefArray']
prcp_60_RefArray = prcp_60_RefObject['prcp_60_RefArray']
prcp_72_RefArray = prcp_72_RefObject['prcp_72_RefArray']

tavg_01_RefArray = tavg_01_RefObject['tavg_01_RefArray']
tavg_02_RefArray = tavg_02_RefObject['tavg_02_RefArray']
tavg_03_RefArray = tavg_03_RefObject['tavg_03_RefArray']
tavg_06_RefArray = tavg_06_RefObject['tavg_06_RefArray']
tavg_09_RefArray = tavg_09_RefObject['tavg_09_RefArray']
tavg_12_RefArray = tavg_12_RefObject['tavg_12_RefArray']
tavg_24_RefArray = tavg_24_RefObject['tavg_24_RefArray']
tavg_36_RefArray = tavg_36_RefObject['tavg_36_RefArray']
tavg_48_RefArray = tavg_48_RefObject['tavg_48_RefArray']
tavg_60_RefArray = tavg_60_RefObject['tavg_60_RefArray']
tavg_72_RefArray = tavg_72_RefObject['tavg_72_RefArray']

tmax_01_RefArray = tmax_01_RefObject['tmax_01_RefArray']
tmax_02_RefArray = tmax_02_RefObject['tmax_02_RefArray']
tmax_03_RefArray = tmax_03_RefObject['tmax_03_RefArray']
tmax_06_RefArray = tmax_06_RefObject['tmax_06_RefArray']
tmax_09_RefArray = tmax_09_RefObject['tmax_09_RefArray']
tmax_12_RefArray = tmax_12_RefObject['tmax_12_RefArray']
tmax_24_RefArray = tmax_24_RefObject['tmax_24_RefArray']
tmax_36_RefArray = tmax_36_RefObject['tmax_36_RefArray']
tmax_48_RefArray = tmax_48_RefObject['tmax_48_RefArray']
tmax_60_RefArray = tmax_60_RefObject['tmax_60_RefArray']
tmax_72_RefArray = tmax_72_RefObject['tmax_72_RefArray']

def MonthlyList_YYYYMMDDAndArray(YYYYMMDD_Of_Array, ThisArray):
  MM_Of_Array = (YYYYMMDD_Of_Array % 10000) // 100
  MonthlyList_YYYYMMDD_Of_Array = []
  MonthlyList_Array = []
  for WhichMonth in range(1,12+1):
    Idxs = np.where(MM_Of_Array == WhichMonth)
    YYYYMMDD_Of_Array_ThisMonth = YYYYMMDD_Of_Array[Idxs[0]]
    ThisArray_ThisMonth = ThisArray[Idxs[0]]
    MonthlyList_YYYYMMDD_Of_Array.append(YYYYMMDD_Of_Array_ThisMonth)
    MonthlyList_Array.append(ThisArray_ThisMonth)
  #end of for WhichMonth in range(1,12+1):
  return MonthlyList_YYYYMMDD_Of_Array, MonthlyList_Array
#end of def MonthlyList_YYYYMMDDAndArray(YYYYMMDD_Of_Array, ThisArray):

MonthlyList_spei_gamma_01_YYYYMMDD_Of_RefArray, MonthlyList_spei_gamma_01_RefArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_01_YYYYMMDD_Of_RefArray, spei_gamma_01_RefArray)
MonthlyList_spei_gamma_02_YYYYMMDD_Of_RefArray, MonthlyList_spei_gamma_02_RefArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_02_YYYYMMDD_Of_RefArray, spei_gamma_02_RefArray)
MonthlyList_spei_gamma_03_YYYYMMDD_Of_RefArray, MonthlyList_spei_gamma_03_RefArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_03_YYYYMMDD_Of_RefArray, spei_gamma_03_RefArray)
MonthlyList_spei_gamma_06_YYYYMMDD_Of_RefArray, MonthlyList_spei_gamma_06_RefArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_06_YYYYMMDD_Of_RefArray, spei_gamma_06_RefArray)
MonthlyList_spei_gamma_09_YYYYMMDD_Of_RefArray, MonthlyList_spei_gamma_09_RefArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_09_YYYYMMDD_Of_RefArray, spei_gamma_09_RefArray)

MonthlyList_spei_pearson_01_YYYYMMDD_Of_RefArray, MonthlyList_spei_pearson_01_RefArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_01_YYYYMMDD_Of_RefArray, spei_pearson_01_RefArray)
MonthlyList_spei_pearson_02_YYYYMMDD_Of_RefArray, MonthlyList_spei_pearson_02_RefArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_02_YYYYMMDD_Of_RefArray, spei_pearson_02_RefArray)
MonthlyList_spei_pearson_03_YYYYMMDD_Of_RefArray, MonthlyList_spei_pearson_03_RefArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_03_YYYYMMDD_Of_RefArray, spei_pearson_03_RefArray)
MonthlyList_spei_pearson_06_YYYYMMDD_Of_RefArray, MonthlyList_spei_pearson_06_RefArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_06_YYYYMMDD_Of_RefArray, spei_pearson_06_RefArray)
MonthlyList_spei_pearson_09_YYYYMMDD_Of_RefArray, MonthlyList_spei_pearson_09_RefArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_09_YYYYMMDD_Of_RefArray, spei_pearson_09_RefArray)

MonthlyList_spi_gamma_01_YYYYMMDD_Of_RefArray, MonthlyList_spi_gamma_01_RefArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_01_YYYYMMDD_Of_RefArray, spi_gamma_01_RefArray)
MonthlyList_spi_gamma_02_YYYYMMDD_Of_RefArray, MonthlyList_spi_gamma_02_RefArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_02_YYYYMMDD_Of_RefArray, spi_gamma_02_RefArray)
MonthlyList_spi_gamma_03_YYYYMMDD_Of_RefArray, MonthlyList_spi_gamma_03_RefArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_03_YYYYMMDD_Of_RefArray, spi_gamma_03_RefArray)
MonthlyList_spi_gamma_06_YYYYMMDD_Of_RefArray, MonthlyList_spi_gamma_06_RefArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_06_YYYYMMDD_Of_RefArray, spi_gamma_06_RefArray)
MonthlyList_spi_gamma_09_YYYYMMDD_Of_RefArray, MonthlyList_spi_gamma_09_RefArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_09_YYYYMMDD_Of_RefArray, spi_gamma_09_RefArray)

MonthlyList_spi_pearson_01_YYYYMMDD_Of_RefArray, MonthlyList_spi_pearson_01_RefArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_01_YYYYMMDD_Of_RefArray, spi_pearson_01_RefArray)
MonthlyList_spi_pearson_02_YYYYMMDD_Of_RefArray, MonthlyList_spi_pearson_02_RefArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_02_YYYYMMDD_Of_RefArray, spi_pearson_02_RefArray)
MonthlyList_spi_pearson_03_YYYYMMDD_Of_RefArray, MonthlyList_spi_pearson_03_RefArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_03_YYYYMMDD_Of_RefArray, spi_pearson_03_RefArray)
MonthlyList_spi_pearson_06_YYYYMMDD_Of_RefArray, MonthlyList_spi_pearson_06_RefArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_06_YYYYMMDD_Of_RefArray, spi_pearson_06_RefArray)
MonthlyList_spi_pearson_09_YYYYMMDD_Of_RefArray, MonthlyList_spi_pearson_09_RefArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_09_YYYYMMDD_Of_RefArray, spi_pearson_09_RefArray)

MonthlyList_pet_01_YYYYMMDD_Of_RefArray, MonthlyList_pet_01_RefArray = MonthlyList_YYYYMMDDAndArray(pet_01_YYYYMMDD_Of_RefArray, pet_01_RefArray)
MonthlyList_pet_02_YYYYMMDD_Of_RefArray, MonthlyList_pet_02_RefArray = MonthlyList_YYYYMMDDAndArray(pet_02_YYYYMMDD_Of_RefArray, pet_02_RefArray)
MonthlyList_pet_03_YYYYMMDD_Of_RefArray, MonthlyList_pet_03_RefArray = MonthlyList_YYYYMMDDAndArray(pet_03_YYYYMMDD_Of_RefArray, pet_03_RefArray)
MonthlyList_pet_06_YYYYMMDD_Of_RefArray, MonthlyList_pet_06_RefArray = MonthlyList_YYYYMMDDAndArray(pet_06_YYYYMMDD_Of_RefArray, pet_06_RefArray)
MonthlyList_pet_09_YYYYMMDD_Of_RefArray, MonthlyList_pet_09_RefArray = MonthlyList_YYYYMMDDAndArray(pet_09_YYYYMMDD_Of_RefArray, pet_09_RefArray)

MonthlyList_prcp_01_YYYYMMDD_Of_RefArray, MonthlyList_prcp_01_RefArray = MonthlyList_YYYYMMDDAndArray(prcp_01_YYYYMMDD_Of_RefArray, prcp_01_RefArray)
MonthlyList_prcp_02_YYYYMMDD_Of_RefArray, MonthlyList_prcp_02_RefArray = MonthlyList_YYYYMMDDAndArray(prcp_02_YYYYMMDD_Of_RefArray, prcp_02_RefArray)
MonthlyList_prcp_03_YYYYMMDD_Of_RefArray, MonthlyList_prcp_03_RefArray = MonthlyList_YYYYMMDDAndArray(prcp_03_YYYYMMDD_Of_RefArray, prcp_03_RefArray)
MonthlyList_prcp_06_YYYYMMDD_Of_RefArray, MonthlyList_prcp_06_RefArray = MonthlyList_YYYYMMDDAndArray(prcp_06_YYYYMMDD_Of_RefArray, prcp_06_RefArray)
MonthlyList_prcp_09_YYYYMMDD_Of_RefArray, MonthlyList_prcp_09_RefArray = MonthlyList_YYYYMMDDAndArray(prcp_09_YYYYMMDD_Of_RefArray, prcp_09_RefArray)

MonthlyList_tavg_01_YYYYMMDD_Of_RefArray, MonthlyList_tavg_01_RefArray = MonthlyList_YYYYMMDDAndArray(tavg_01_YYYYMMDD_Of_RefArray, tavg_01_RefArray)
MonthlyList_tavg_02_YYYYMMDD_Of_RefArray, MonthlyList_tavg_02_RefArray = MonthlyList_YYYYMMDDAndArray(tavg_02_YYYYMMDD_Of_RefArray, tavg_02_RefArray)
MonthlyList_tavg_03_YYYYMMDD_Of_RefArray, MonthlyList_tavg_03_RefArray = MonthlyList_YYYYMMDDAndArray(tavg_03_YYYYMMDD_Of_RefArray, tavg_03_RefArray)
MonthlyList_tavg_06_YYYYMMDD_Of_RefArray, MonthlyList_tavg_06_RefArray = MonthlyList_YYYYMMDDAndArray(tavg_06_YYYYMMDD_Of_RefArray, tavg_06_RefArray)
MonthlyList_tavg_09_YYYYMMDD_Of_RefArray, MonthlyList_tavg_09_RefArray = MonthlyList_YYYYMMDDAndArray(tavg_09_YYYYMMDD_Of_RefArray, tavg_09_RefArray)

MonthlyList_tmax_01_YYYYMMDD_Of_RefArray, MonthlyList_tmax_01_RefArray = MonthlyList_YYYYMMDDAndArray(tmax_01_YYYYMMDD_Of_RefArray, tmax_01_RefArray)
MonthlyList_tmax_02_YYYYMMDD_Of_RefArray, MonthlyList_tmax_02_RefArray = MonthlyList_YYYYMMDDAndArray(tmax_02_YYYYMMDD_Of_RefArray, tmax_02_RefArray)
MonthlyList_tmax_03_YYYYMMDD_Of_RefArray, MonthlyList_tmax_03_RefArray = MonthlyList_YYYYMMDDAndArray(tmax_03_YYYYMMDD_Of_RefArray, tmax_03_RefArray)
MonthlyList_tmax_06_YYYYMMDD_Of_RefArray, MonthlyList_tmax_06_RefArray = MonthlyList_YYYYMMDDAndArray(tmax_06_YYYYMMDD_Of_RefArray, tmax_06_RefArray)
MonthlyList_tmax_09_YYYYMMDD_Of_RefArray, MonthlyList_tmax_09_RefArray = MonthlyList_YYYYMMDDAndArray(tmax_09_YYYYMMDD_Of_RefArray, tmax_09_RefArray)

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

def TimeSlice_YYYYMMDDAndRefArray(YYYYMMDD_Of_RefArray, RefArray, BeginDateVecList, EndDateVecList):
  BeginYYYYMMDD = 10000*BeginDateVecList[0] + 100*BeginDateVecList[1] + BeginDateVecList[2]
  EndYYYYMMDD = 10000*EndDateVecList[0] + 100*EndDateVecList[1] + EndDateVecList[2]
  if ( ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) ) and
       ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) ) ) :
    BeginIdx = list(YYYYMMDD_Of_RefArray).index(10000*BeginDateVecList[0] + 100*BeginDateVecList[1] + BeginDateVecList[2])
    EndIdx = list(YYYYMMDD_Of_RefArray).index(10000*EndDateVecList[0] + 100*EndDateVecList[1] + EndDateVecList[2])
    YYYYMMDD_Of_PrcntlArray = YYYYMMDD_Of_RefArray[ BeginIdx : EndIdx+1 ] 
    PrcntlArray = RefArray[ BeginIdx : EndIdx+1 ] 
  else: # if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
    BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])
    EndDate = date(EndDateVecList[0], EndDateVecList[1], EndDateVecList[2])
    YYYYMMDD_Of_PrcntlArray = CreateYYYYMMDD_Of_Array(BeginDate, EndDate)
    PrcntlArray = np.empty([YYYYMMDD_Of_PrcntlArray.shape[0], RefArray.shape[1]]) 
    PrcntlArray[:] = np.NaN
    if ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) ):
      BeginIdx = list(YYYYMMDD_Of_RefArray).index(10000*BeginDateVecList[0] + 100*BeginDateVecList[1] + BeginDateVecList[2])
      PrcntlArray[ : RefArray.shape[0]-BeginIdx ] = RefArray[ BeginIdx : ] 
    if ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) ):
      EndIdx = list(YYYYMMDD_Of_RefArray).index(10000*EndDateVecList[0] + 100*EndDateVecList[1] + EndDateVecList[2])
      PrcntlArray[ PrcntlArray.shape[0]-(EndIdx+1) : ] = RefArray[ : EndIdx+1 ] 
  #end of if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
  return YYYYMMDD_Of_PrcntlArray, PrcntlArray
#end of def TimeSlice_YYYYMMDDAndRefArray(YYYYMMDD_Of_RefArray, RefArray, BeginDateVecList, EndDateVecList):

def FindPercentilesForValues(RefArray_1d, Values_1d):
  RefArray_1d_NotNaN = RefArray_1d[~np.isnan(RefArray_1d)]
  Values_1d_NotNaN = Values_1d[~np.isnan(Values_1d)]
  if RefArray_1d_NotNaN.size > 0:
    if Values_1d_NotNaN.size > 0:
      SortedRef_1d = np.sort(RefArray_1d_NotNaN)
      SortedRef_1d_size = SortedRef_1d.size
      QuantileInverses_OrdinalTieRanks = (rankdata(SortedRef_1d, method='ordinal') - 1) / \
                                         float(SortedRef_1d_size - 1)
      QuantileInverses_AverageTieRanks = (rankdata(SortedRef_1d, method='average') - 1) / \
                                         float(SortedRef_1d_size - 1)
      Percentiles_1d = np.interp(Values_1d, SortedRef_1d, QuantileInverses_OrdinalTieRanks)
      IfValuesInSortedRef = np.isin(Values_1d, SortedRef_1d)
      ValuesInSortedRef = Values_1d[np.where(IfValuesInSortedRef)]
      Idxs_ValuesInSortedRef_In_SortedRef = np.searchsorted(SortedRef_1d, ValuesInSortedRef)
      Percentiles_AverageTieRanks = QuantileInverses_AverageTieRanks[Idxs_ValuesInSortedRef_In_SortedRef]
      Percentiles_1d[np.where(IfValuesInSortedRef)] = Percentiles_AverageTieRanks
      return Percentiles_1d
    else: # if Values_1d_NotNaN.size > 0
      return Values_1d
    #end of if Values_1d_NotNaN.size > 0
  else: # if RefArray_1d_NotNaN.size > 0
    print('RefArray_1d_NotNaN.size == 0!!!')
    if Values_1d_NotNaN.size > 0:
      print('Values_1d_NotNaN.size > 0 when RefArray_1d_NotNaN.size == 0!!')
      sys.exit(0)
    else: # if Values_1d_NotNaN.size > 0
      return Values_1d
    #end of if Values_1d_NotNaN.size > 0
  #end of if RefArray_1d_NotNaN.size > 0
#end of def FindPercentilesForValues(RefArray_1d, Values_1d):

def LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray):
  for WhichSpatialUnit in range(PrcntlArray.shape[1]):
    RefArray_ThisSpatialUnit = RefArray[:, WhichSpatialUnit]
    PrcntlArray_ThisSpatialUnit = PrcntlArray[:, WhichSpatialUnit]
    PrcntlArray_ThisSpatialUnit = FindPercentilesForValues(RefArray_ThisSpatialUnit, PrcntlArray_ThisSpatialUnit) 
    PrcntlArray[:, WhichSpatialUnit] = PrcntlArray_ThisSpatialUnit
  #end of for WhichSpatialUnit in range(PrcntlArray.shape[1]):
  return PrcntlArray
#end of def LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray):

def LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray):
  for WhichMonth in range(1,12+1):
    RefArray = MonthlyList_RefArray[WhichMonth-1]
    PrcntlArray = MonthlyList_PrcntlArray[WhichMonth-1]
    PrcntlArray = LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray)
    MonthlyList_PrcntlArray[WhichMonth-1] = PrcntlArray
  #end of for WhichMonth in range(1,12+1):
  return MonthlyList_PrcntlArray
#end of def LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray):

def ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray):
  YYYYMMDD_Of_PrcntlArray_1d = np.squeeze(YYYYMMDD_Of_PrcntlArray, axis = 1) 
  for WhichMonth in range(1,12+1):
    YYYYMMDD_Of_PrcntlArray_ThisMonth_1d = np.squeeze(MonthlyList_YYYYMMDD_Of_PrcntlArray[WhichMonth-1], axis = 1) 
    all_sorted = np.argsort(YYYYMMDD_Of_PrcntlArray_1d) 
    ThisMonth_pos = np.searchsorted(YYYYMMDD_Of_PrcntlArray_1d[all_sorted], YYYYMMDD_Of_PrcntlArray_ThisMonth_1d) 
    indices = all_sorted[ThisMonth_pos]
    PrcntlArray[indices, :] = MonthlyList_PrcntlArray[WhichMonth-1] 
  #end of for WhichMonth in range(1,12+1):
  return PrcntlArray
#end of def ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray):

def PrintInfoAboutArray(ThisArray, ThisArray_Str):
  print(ThisArray_Str,".shape is ",ThisArray.shape)
  print(ThisArray_Str,".dtype is ",ThisArray.dtype)
  print(ThisArray_Str," is ",ThisArray)
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
#end of def PrintInfoAboutArray(ThisArray, ThisArray_Str):

#BEGIN section for training

spei_gamma_01_YYYYMMDD_Of_PrcntlArray, spei_gamma_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_01_YYYYMMDD_Of_RefArray, spei_gamma_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_02_YYYYMMDD_Of_PrcntlArray, spei_gamma_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_02_YYYYMMDD_Of_RefArray, spei_gamma_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_03_YYYYMMDD_Of_PrcntlArray, spei_gamma_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_03_YYYYMMDD_Of_RefArray, spei_gamma_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_06_YYYYMMDD_Of_PrcntlArray, spei_gamma_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_06_YYYYMMDD_Of_RefArray, spei_gamma_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_09_YYYYMMDD_Of_PrcntlArray, spei_gamma_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_09_YYYYMMDD_Of_RefArray, spei_gamma_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_12_YYYYMMDD_Of_PrcntlArray, spei_gamma_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_12_YYYYMMDD_Of_RefArray, spei_gamma_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_24_YYYYMMDD_Of_PrcntlArray, spei_gamma_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_24_YYYYMMDD_Of_RefArray, spei_gamma_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_36_YYYYMMDD_Of_PrcntlArray, spei_gamma_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_36_YYYYMMDD_Of_RefArray, spei_gamma_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_48_YYYYMMDD_Of_PrcntlArray, spei_gamma_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_48_YYYYMMDD_Of_RefArray, spei_gamma_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_60_YYYYMMDD_Of_PrcntlArray, spei_gamma_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_60_YYYYMMDD_Of_RefArray, spei_gamma_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_gamma_72_YYYYMMDD_Of_PrcntlArray, spei_gamma_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_72_YYYYMMDD_Of_RefArray, spei_gamma_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

spei_pearson_01_YYYYMMDD_Of_PrcntlArray, spei_pearson_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_01_YYYYMMDD_Of_RefArray, spei_pearson_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_02_YYYYMMDD_Of_PrcntlArray, spei_pearson_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_02_YYYYMMDD_Of_RefArray, spei_pearson_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_03_YYYYMMDD_Of_PrcntlArray, spei_pearson_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_03_YYYYMMDD_Of_RefArray, spei_pearson_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_06_YYYYMMDD_Of_PrcntlArray, spei_pearson_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_06_YYYYMMDD_Of_RefArray, spei_pearson_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_09_YYYYMMDD_Of_PrcntlArray, spei_pearson_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_09_YYYYMMDD_Of_RefArray, spei_pearson_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_12_YYYYMMDD_Of_PrcntlArray, spei_pearson_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_12_YYYYMMDD_Of_RefArray, spei_pearson_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_24_YYYYMMDD_Of_PrcntlArray, spei_pearson_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_24_YYYYMMDD_Of_RefArray, spei_pearson_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_36_YYYYMMDD_Of_PrcntlArray, spei_pearson_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_36_YYYYMMDD_Of_RefArray, spei_pearson_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_48_YYYYMMDD_Of_PrcntlArray, spei_pearson_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_48_YYYYMMDD_Of_RefArray, spei_pearson_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_60_YYYYMMDD_Of_PrcntlArray, spei_pearson_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_60_YYYYMMDD_Of_RefArray, spei_pearson_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spei_pearson_72_YYYYMMDD_Of_PrcntlArray, spei_pearson_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_72_YYYYMMDD_Of_RefArray, spei_pearson_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

spi_gamma_01_YYYYMMDD_Of_PrcntlArray, spi_gamma_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_01_YYYYMMDD_Of_RefArray, spi_gamma_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_02_YYYYMMDD_Of_PrcntlArray, spi_gamma_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_02_YYYYMMDD_Of_RefArray, spi_gamma_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_03_YYYYMMDD_Of_PrcntlArray, spi_gamma_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_03_YYYYMMDD_Of_RefArray, spi_gamma_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_06_YYYYMMDD_Of_PrcntlArray, spi_gamma_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_06_YYYYMMDD_Of_RefArray, spi_gamma_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_09_YYYYMMDD_Of_PrcntlArray, spi_gamma_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_09_YYYYMMDD_Of_RefArray, spi_gamma_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_12_YYYYMMDD_Of_PrcntlArray, spi_gamma_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_12_YYYYMMDD_Of_RefArray, spi_gamma_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_24_YYYYMMDD_Of_PrcntlArray, spi_gamma_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_24_YYYYMMDD_Of_RefArray, spi_gamma_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_36_YYYYMMDD_Of_PrcntlArray, spi_gamma_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_36_YYYYMMDD_Of_RefArray, spi_gamma_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_48_YYYYMMDD_Of_PrcntlArray, spi_gamma_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_48_YYYYMMDD_Of_RefArray, spi_gamma_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_60_YYYYMMDD_Of_PrcntlArray, spi_gamma_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_60_YYYYMMDD_Of_RefArray, spi_gamma_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_gamma_72_YYYYMMDD_Of_PrcntlArray, spi_gamma_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_72_YYYYMMDD_Of_RefArray, spi_gamma_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

spi_pearson_01_YYYYMMDD_Of_PrcntlArray, spi_pearson_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_01_YYYYMMDD_Of_RefArray, spi_pearson_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_02_YYYYMMDD_Of_PrcntlArray, spi_pearson_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_02_YYYYMMDD_Of_RefArray, spi_pearson_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_03_YYYYMMDD_Of_PrcntlArray, spi_pearson_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_03_YYYYMMDD_Of_RefArray, spi_pearson_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_06_YYYYMMDD_Of_PrcntlArray, spi_pearson_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_06_YYYYMMDD_Of_RefArray, spi_pearson_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_09_YYYYMMDD_Of_PrcntlArray, spi_pearson_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_09_YYYYMMDD_Of_RefArray, spi_pearson_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_12_YYYYMMDD_Of_PrcntlArray, spi_pearson_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_12_YYYYMMDD_Of_RefArray, spi_pearson_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_24_YYYYMMDD_Of_PrcntlArray, spi_pearson_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_24_YYYYMMDD_Of_RefArray, spi_pearson_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_36_YYYYMMDD_Of_PrcntlArray, spi_pearson_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_36_YYYYMMDD_Of_RefArray, spi_pearson_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_48_YYYYMMDD_Of_PrcntlArray, spi_pearson_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_48_YYYYMMDD_Of_RefArray, spi_pearson_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_60_YYYYMMDD_Of_PrcntlArray, spi_pearson_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_60_YYYYMMDD_Of_RefArray, spi_pearson_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
spi_pearson_72_YYYYMMDD_Of_PrcntlArray, spi_pearson_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_72_YYYYMMDD_Of_RefArray, spi_pearson_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

pet_01_YYYYMMDD_Of_PrcntlArray, pet_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_01_YYYYMMDD_Of_RefArray, pet_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_02_YYYYMMDD_Of_PrcntlArray, pet_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_02_YYYYMMDD_Of_RefArray, pet_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_03_YYYYMMDD_Of_PrcntlArray, pet_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_03_YYYYMMDD_Of_RefArray, pet_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_06_YYYYMMDD_Of_PrcntlArray, pet_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_06_YYYYMMDD_Of_RefArray, pet_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_09_YYYYMMDD_Of_PrcntlArray, pet_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_09_YYYYMMDD_Of_RefArray, pet_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_12_YYYYMMDD_Of_PrcntlArray, pet_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_12_YYYYMMDD_Of_RefArray, pet_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_24_YYYYMMDD_Of_PrcntlArray, pet_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_24_YYYYMMDD_Of_RefArray, pet_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_36_YYYYMMDD_Of_PrcntlArray, pet_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_36_YYYYMMDD_Of_RefArray, pet_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_48_YYYYMMDD_Of_PrcntlArray, pet_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_48_YYYYMMDD_Of_RefArray, pet_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_60_YYYYMMDD_Of_PrcntlArray, pet_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_60_YYYYMMDD_Of_RefArray, pet_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
pet_72_YYYYMMDD_Of_PrcntlArray, pet_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_72_YYYYMMDD_Of_RefArray, pet_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

prcp_01_YYYYMMDD_Of_PrcntlArray, prcp_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_01_YYYYMMDD_Of_RefArray, prcp_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_02_YYYYMMDD_Of_PrcntlArray, prcp_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_02_YYYYMMDD_Of_RefArray, prcp_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_03_YYYYMMDD_Of_PrcntlArray, prcp_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_03_YYYYMMDD_Of_RefArray, prcp_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_06_YYYYMMDD_Of_PrcntlArray, prcp_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_06_YYYYMMDD_Of_RefArray, prcp_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_09_YYYYMMDD_Of_PrcntlArray, prcp_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_09_YYYYMMDD_Of_RefArray, prcp_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_12_YYYYMMDD_Of_PrcntlArray, prcp_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_12_YYYYMMDD_Of_RefArray, prcp_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_24_YYYYMMDD_Of_PrcntlArray, prcp_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_24_YYYYMMDD_Of_RefArray, prcp_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_36_YYYYMMDD_Of_PrcntlArray, prcp_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_36_YYYYMMDD_Of_RefArray, prcp_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_48_YYYYMMDD_Of_PrcntlArray, prcp_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_48_YYYYMMDD_Of_RefArray, prcp_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_60_YYYYMMDD_Of_PrcntlArray, prcp_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_60_YYYYMMDD_Of_RefArray, prcp_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
prcp_72_YYYYMMDD_Of_PrcntlArray, prcp_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_72_YYYYMMDD_Of_RefArray, prcp_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

tavg_01_YYYYMMDD_Of_PrcntlArray, tavg_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_01_YYYYMMDD_Of_RefArray, tavg_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_02_YYYYMMDD_Of_PrcntlArray, tavg_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_02_YYYYMMDD_Of_RefArray, tavg_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_03_YYYYMMDD_Of_PrcntlArray, tavg_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_03_YYYYMMDD_Of_RefArray, tavg_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_06_YYYYMMDD_Of_PrcntlArray, tavg_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_06_YYYYMMDD_Of_RefArray, tavg_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_09_YYYYMMDD_Of_PrcntlArray, tavg_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_09_YYYYMMDD_Of_RefArray, tavg_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_12_YYYYMMDD_Of_PrcntlArray, tavg_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_12_YYYYMMDD_Of_RefArray, tavg_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_24_YYYYMMDD_Of_PrcntlArray, tavg_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_24_YYYYMMDD_Of_RefArray, tavg_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_36_YYYYMMDD_Of_PrcntlArray, tavg_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_36_YYYYMMDD_Of_RefArray, tavg_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_48_YYYYMMDD_Of_PrcntlArray, tavg_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_48_YYYYMMDD_Of_RefArray, tavg_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_60_YYYYMMDD_Of_PrcntlArray, tavg_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_60_YYYYMMDD_Of_RefArray, tavg_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tavg_72_YYYYMMDD_Of_PrcntlArray, tavg_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_72_YYYYMMDD_Of_RefArray, tavg_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

tmax_01_YYYYMMDD_Of_PrcntlArray, tmax_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_01_YYYYMMDD_Of_RefArray, tmax_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_02_YYYYMMDD_Of_PrcntlArray, tmax_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_02_YYYYMMDD_Of_RefArray, tmax_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_03_YYYYMMDD_Of_PrcntlArray, tmax_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_03_YYYYMMDD_Of_RefArray, tmax_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_06_YYYYMMDD_Of_PrcntlArray, tmax_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_06_YYYYMMDD_Of_RefArray, tmax_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_09_YYYYMMDD_Of_PrcntlArray, tmax_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_09_YYYYMMDD_Of_RefArray, tmax_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_12_YYYYMMDD_Of_PrcntlArray, tmax_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_12_YYYYMMDD_Of_RefArray, tmax_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_24_YYYYMMDD_Of_PrcntlArray, tmax_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_24_YYYYMMDD_Of_RefArray, tmax_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_36_YYYYMMDD_Of_PrcntlArray, tmax_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_36_YYYYMMDD_Of_RefArray, tmax_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_48_YYYYMMDD_Of_PrcntlArray, tmax_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_48_YYYYMMDD_Of_RefArray, tmax_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_60_YYYYMMDD_Of_PrcntlArray, tmax_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_60_YYYYMMDD_Of_RefArray, tmax_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
tmax_72_YYYYMMDD_Of_PrcntlArray, tmax_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_72_YYYYMMDD_Of_RefArray, tmax_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

MonthlyList_spei_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_01_YYYYMMDD_Of_PrcntlArray, spei_gamma_01_PrcntlArray)
MonthlyList_spei_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_02_YYYYMMDD_Of_PrcntlArray, spei_gamma_02_PrcntlArray)
MonthlyList_spei_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_03_YYYYMMDD_Of_PrcntlArray, spei_gamma_03_PrcntlArray)
MonthlyList_spei_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_06_YYYYMMDD_Of_PrcntlArray, spei_gamma_06_PrcntlArray)
MonthlyList_spei_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_09_YYYYMMDD_Of_PrcntlArray, spei_gamma_09_PrcntlArray)

MonthlyList_spei_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_01_YYYYMMDD_Of_PrcntlArray, spei_pearson_01_PrcntlArray)
MonthlyList_spei_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_02_YYYYMMDD_Of_PrcntlArray, spei_pearson_02_PrcntlArray)
MonthlyList_spei_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_03_YYYYMMDD_Of_PrcntlArray, spei_pearson_03_PrcntlArray)
MonthlyList_spei_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_06_YYYYMMDD_Of_PrcntlArray, spei_pearson_06_PrcntlArray)
MonthlyList_spei_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_09_YYYYMMDD_Of_PrcntlArray, spei_pearson_09_PrcntlArray)

MonthlyList_spi_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_01_YYYYMMDD_Of_PrcntlArray, spi_gamma_01_PrcntlArray)
MonthlyList_spi_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_02_YYYYMMDD_Of_PrcntlArray, spi_gamma_02_PrcntlArray)
MonthlyList_spi_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_03_YYYYMMDD_Of_PrcntlArray, spi_gamma_03_PrcntlArray)
MonthlyList_spi_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_06_YYYYMMDD_Of_PrcntlArray, spi_gamma_06_PrcntlArray)
MonthlyList_spi_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_09_YYYYMMDD_Of_PrcntlArray, spi_gamma_09_PrcntlArray)

MonthlyList_spi_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_01_YYYYMMDD_Of_PrcntlArray, spi_pearson_01_PrcntlArray)
MonthlyList_spi_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_02_YYYYMMDD_Of_PrcntlArray, spi_pearson_02_PrcntlArray)
MonthlyList_spi_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_03_YYYYMMDD_Of_PrcntlArray, spi_pearson_03_PrcntlArray)
MonthlyList_spi_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_06_YYYYMMDD_Of_PrcntlArray, spi_pearson_06_PrcntlArray)
MonthlyList_spi_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_09_YYYYMMDD_Of_PrcntlArray, spi_pearson_09_PrcntlArray)

MonthlyList_pet_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_01_YYYYMMDD_Of_PrcntlArray, pet_01_PrcntlArray)
MonthlyList_pet_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_02_YYYYMMDD_Of_PrcntlArray, pet_02_PrcntlArray)
MonthlyList_pet_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_03_YYYYMMDD_Of_PrcntlArray, pet_03_PrcntlArray)
MonthlyList_pet_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_06_YYYYMMDD_Of_PrcntlArray, pet_06_PrcntlArray)
MonthlyList_pet_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_09_YYYYMMDD_Of_PrcntlArray, pet_09_PrcntlArray)

MonthlyList_prcp_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_01_YYYYMMDD_Of_PrcntlArray, prcp_01_PrcntlArray)
MonthlyList_prcp_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_02_YYYYMMDD_Of_PrcntlArray, prcp_02_PrcntlArray)
MonthlyList_prcp_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_03_YYYYMMDD_Of_PrcntlArray, prcp_03_PrcntlArray)
MonthlyList_prcp_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_06_YYYYMMDD_Of_PrcntlArray, prcp_06_PrcntlArray)
MonthlyList_prcp_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_09_YYYYMMDD_Of_PrcntlArray, prcp_09_PrcntlArray)

MonthlyList_tavg_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_01_YYYYMMDD_Of_PrcntlArray, tavg_01_PrcntlArray)
MonthlyList_tavg_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_02_YYYYMMDD_Of_PrcntlArray, tavg_02_PrcntlArray)
MonthlyList_tavg_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_03_YYYYMMDD_Of_PrcntlArray, tavg_03_PrcntlArray)
MonthlyList_tavg_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_06_YYYYMMDD_Of_PrcntlArray, tavg_06_PrcntlArray)
MonthlyList_tavg_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_09_YYYYMMDD_Of_PrcntlArray, tavg_09_PrcntlArray)

MonthlyList_tmax_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_01_YYYYMMDD_Of_PrcntlArray, tmax_01_PrcntlArray)
MonthlyList_tmax_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_02_YYYYMMDD_Of_PrcntlArray, tmax_02_PrcntlArray)
MonthlyList_tmax_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_03_YYYYMMDD_Of_PrcntlArray, tmax_03_PrcntlArray)
MonthlyList_tmax_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_06_YYYYMMDD_Of_PrcntlArray, tmax_06_PrcntlArray)
MonthlyList_tmax_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_09_YYYYMMDD_Of_PrcntlArray, tmax_09_PrcntlArray)

spei_gamma_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_12_RefArray, spei_gamma_12_PrcntlArray)
spei_gamma_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_24_RefArray, spei_gamma_24_PrcntlArray)
spei_gamma_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_36_RefArray, spei_gamma_36_PrcntlArray)
spei_gamma_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_48_RefArray, spei_gamma_48_PrcntlArray)
spei_gamma_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_60_RefArray, spei_gamma_60_PrcntlArray)
spei_gamma_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_72_RefArray, spei_gamma_72_PrcntlArray)

spei_pearson_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_12_RefArray, spei_pearson_12_PrcntlArray)
spei_pearson_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_24_RefArray, spei_pearson_24_PrcntlArray)
spei_pearson_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_36_RefArray, spei_pearson_36_PrcntlArray)
spei_pearson_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_48_RefArray, spei_pearson_48_PrcntlArray)
spei_pearson_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_60_RefArray, spei_pearson_60_PrcntlArray)
spei_pearson_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_72_RefArray, spei_pearson_72_PrcntlArray)

spi_gamma_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_12_RefArray, spi_gamma_12_PrcntlArray)
spi_gamma_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_24_RefArray, spi_gamma_24_PrcntlArray)
spi_gamma_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_36_RefArray, spi_gamma_36_PrcntlArray)
spi_gamma_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_48_RefArray, spi_gamma_48_PrcntlArray)
spi_gamma_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_60_RefArray, spi_gamma_60_PrcntlArray)
spi_gamma_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_72_RefArray, spi_gamma_72_PrcntlArray)

spi_pearson_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_12_RefArray, spi_pearson_12_PrcntlArray)
spi_pearson_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_24_RefArray, spi_pearson_24_PrcntlArray)
spi_pearson_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_36_RefArray, spi_pearson_36_PrcntlArray)
spi_pearson_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_48_RefArray, spi_pearson_48_PrcntlArray)
spi_pearson_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_60_RefArray, spi_pearson_60_PrcntlArray)
spi_pearson_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_72_RefArray, spi_pearson_72_PrcntlArray)

pet_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_12_RefArray, pet_12_PrcntlArray)
pet_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_24_RefArray, pet_24_PrcntlArray)
pet_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_36_RefArray, pet_36_PrcntlArray)
pet_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_48_RefArray, pet_48_PrcntlArray)
pet_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_60_RefArray, pet_60_PrcntlArray)
pet_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_72_RefArray, pet_72_PrcntlArray)

prcp_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_12_RefArray, prcp_12_PrcntlArray)
prcp_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_24_RefArray, prcp_24_PrcntlArray)
prcp_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_36_RefArray, prcp_36_PrcntlArray)
prcp_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_48_RefArray, prcp_48_PrcntlArray)
prcp_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_60_RefArray, prcp_60_PrcntlArray)
prcp_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_72_RefArray, prcp_72_PrcntlArray)

tavg_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_12_RefArray, tavg_12_PrcntlArray)
tavg_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_24_RefArray, tavg_24_PrcntlArray)
tavg_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_36_RefArray, tavg_36_PrcntlArray)
tavg_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_48_RefArray, tavg_48_PrcntlArray)
tavg_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_60_RefArray, tavg_60_PrcntlArray)
tavg_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_72_RefArray, tavg_72_PrcntlArray)

tmax_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_12_RefArray, tmax_12_PrcntlArray)
tmax_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_24_RefArray, tmax_24_PrcntlArray)
tmax_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_36_RefArray, tmax_36_PrcntlArray)
tmax_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_48_RefArray, tmax_48_PrcntlArray)
tmax_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_60_RefArray, tmax_60_PrcntlArray)
tmax_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_72_RefArray, tmax_72_PrcntlArray)

MonthlyList_spei_gamma_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_01_RefArray, MonthlyList_spei_gamma_01_PrcntlArray)
MonthlyList_spei_gamma_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_02_RefArray, MonthlyList_spei_gamma_02_PrcntlArray)
MonthlyList_spei_gamma_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_03_RefArray, MonthlyList_spei_gamma_03_PrcntlArray)
MonthlyList_spei_gamma_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_06_RefArray, MonthlyList_spei_gamma_06_PrcntlArray)
MonthlyList_spei_gamma_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_09_RefArray, MonthlyList_spei_gamma_09_PrcntlArray)

MonthlyList_spei_pearson_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_01_RefArray, MonthlyList_spei_pearson_01_PrcntlArray)
MonthlyList_spei_pearson_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_02_RefArray, MonthlyList_spei_pearson_02_PrcntlArray)
MonthlyList_spei_pearson_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_03_RefArray, MonthlyList_spei_pearson_03_PrcntlArray)
MonthlyList_spei_pearson_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_06_RefArray, MonthlyList_spei_pearson_06_PrcntlArray)
MonthlyList_spei_pearson_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_09_RefArray, MonthlyList_spei_pearson_09_PrcntlArray)

MonthlyList_spi_gamma_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_01_RefArray, MonthlyList_spi_gamma_01_PrcntlArray)
MonthlyList_spi_gamma_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_02_RefArray, MonthlyList_spi_gamma_02_PrcntlArray)
MonthlyList_spi_gamma_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_03_RefArray, MonthlyList_spi_gamma_03_PrcntlArray)
MonthlyList_spi_gamma_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_06_RefArray, MonthlyList_spi_gamma_06_PrcntlArray)
MonthlyList_spi_gamma_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_09_RefArray, MonthlyList_spi_gamma_09_PrcntlArray)

MonthlyList_spi_pearson_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_01_RefArray, MonthlyList_spi_pearson_01_PrcntlArray)
MonthlyList_spi_pearson_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_02_RefArray, MonthlyList_spi_pearson_02_PrcntlArray)
MonthlyList_spi_pearson_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_03_RefArray, MonthlyList_spi_pearson_03_PrcntlArray)
MonthlyList_spi_pearson_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_06_RefArray, MonthlyList_spi_pearson_06_PrcntlArray)
MonthlyList_spi_pearson_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_09_RefArray, MonthlyList_spi_pearson_09_PrcntlArray)

MonthlyList_pet_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_01_RefArray, MonthlyList_pet_01_PrcntlArray)
MonthlyList_pet_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_02_RefArray, MonthlyList_pet_02_PrcntlArray)
MonthlyList_pet_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_03_RefArray, MonthlyList_pet_03_PrcntlArray)
MonthlyList_pet_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_06_RefArray, MonthlyList_pet_06_PrcntlArray)
MonthlyList_pet_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_09_RefArray, MonthlyList_pet_09_PrcntlArray)

MonthlyList_prcp_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_01_RefArray, MonthlyList_prcp_01_PrcntlArray)
MonthlyList_prcp_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_02_RefArray, MonthlyList_prcp_02_PrcntlArray)
MonthlyList_prcp_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_03_RefArray, MonthlyList_prcp_03_PrcntlArray)
MonthlyList_prcp_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_06_RefArray, MonthlyList_prcp_06_PrcntlArray)
MonthlyList_prcp_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_09_RefArray, MonthlyList_prcp_09_PrcntlArray)

MonthlyList_tavg_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_01_RefArray, MonthlyList_tavg_01_PrcntlArray)
MonthlyList_tavg_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_02_RefArray, MonthlyList_tavg_02_PrcntlArray)
MonthlyList_tavg_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_03_RefArray, MonthlyList_tavg_03_PrcntlArray)
MonthlyList_tavg_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_06_RefArray, MonthlyList_tavg_06_PrcntlArray)
MonthlyList_tavg_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_09_RefArray, MonthlyList_tavg_09_PrcntlArray)

MonthlyList_tmax_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_01_RefArray, MonthlyList_tmax_01_PrcntlArray)
MonthlyList_tmax_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_02_RefArray, MonthlyList_tmax_02_PrcntlArray)
MonthlyList_tmax_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_03_RefArray, MonthlyList_tmax_03_PrcntlArray)
MonthlyList_tmax_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_06_RefArray, MonthlyList_tmax_06_PrcntlArray)
MonthlyList_tmax_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_09_RefArray, MonthlyList_tmax_09_PrcntlArray)

spei_gamma_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_01_YYYYMMDD_Of_PrcntlArray, spei_gamma_01_PrcntlArray, MonthlyList_spei_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_01_PrcntlArray)
spei_gamma_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_02_YYYYMMDD_Of_PrcntlArray, spei_gamma_02_PrcntlArray, MonthlyList_spei_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_02_PrcntlArray)
spei_gamma_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_03_YYYYMMDD_Of_PrcntlArray, spei_gamma_03_PrcntlArray, MonthlyList_spei_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_03_PrcntlArray)
spei_gamma_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_06_YYYYMMDD_Of_PrcntlArray, spei_gamma_06_PrcntlArray, MonthlyList_spei_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_06_PrcntlArray)
spei_gamma_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_09_YYYYMMDD_Of_PrcntlArray, spei_gamma_09_PrcntlArray, MonthlyList_spei_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_09_PrcntlArray)

spei_pearson_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_01_YYYYMMDD_Of_PrcntlArray, spei_pearson_01_PrcntlArray, MonthlyList_spei_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_01_PrcntlArray)
spei_pearson_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_02_YYYYMMDD_Of_PrcntlArray, spei_pearson_02_PrcntlArray, MonthlyList_spei_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_02_PrcntlArray)
spei_pearson_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_03_YYYYMMDD_Of_PrcntlArray, spei_pearson_03_PrcntlArray, MonthlyList_spei_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_03_PrcntlArray)
spei_pearson_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_06_YYYYMMDD_Of_PrcntlArray, spei_pearson_06_PrcntlArray, MonthlyList_spei_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_06_PrcntlArray)
spei_pearson_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_09_YYYYMMDD_Of_PrcntlArray, spei_pearson_09_PrcntlArray, MonthlyList_spei_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_09_PrcntlArray)

spi_gamma_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_01_YYYYMMDD_Of_PrcntlArray, spi_gamma_01_PrcntlArray, MonthlyList_spi_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_01_PrcntlArray)
spi_gamma_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_02_YYYYMMDD_Of_PrcntlArray, spi_gamma_02_PrcntlArray, MonthlyList_spi_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_02_PrcntlArray)
spi_gamma_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_03_YYYYMMDD_Of_PrcntlArray, spi_gamma_03_PrcntlArray, MonthlyList_spi_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_03_PrcntlArray)
spi_gamma_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_06_YYYYMMDD_Of_PrcntlArray, spi_gamma_06_PrcntlArray, MonthlyList_spi_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_06_PrcntlArray)
spi_gamma_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_09_YYYYMMDD_Of_PrcntlArray, spi_gamma_09_PrcntlArray, MonthlyList_spi_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_09_PrcntlArray)

spi_pearson_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_01_YYYYMMDD_Of_PrcntlArray, spi_pearson_01_PrcntlArray, MonthlyList_spi_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_01_PrcntlArray)
spi_pearson_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_02_YYYYMMDD_Of_PrcntlArray, spi_pearson_02_PrcntlArray, MonthlyList_spi_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_02_PrcntlArray)
spi_pearson_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_03_YYYYMMDD_Of_PrcntlArray, spi_pearson_03_PrcntlArray, MonthlyList_spi_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_03_PrcntlArray)
spi_pearson_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_06_YYYYMMDD_Of_PrcntlArray, spi_pearson_06_PrcntlArray, MonthlyList_spi_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_06_PrcntlArray)
spi_pearson_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_09_YYYYMMDD_Of_PrcntlArray, spi_pearson_09_PrcntlArray, MonthlyList_spi_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_09_PrcntlArray)

pet_01_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_01_YYYYMMDD_Of_PrcntlArray, pet_01_PrcntlArray, MonthlyList_pet_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_01_PrcntlArray)
pet_02_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_02_YYYYMMDD_Of_PrcntlArray, pet_02_PrcntlArray, MonthlyList_pet_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_02_PrcntlArray)
pet_03_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_03_YYYYMMDD_Of_PrcntlArray, pet_03_PrcntlArray, MonthlyList_pet_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_03_PrcntlArray)
pet_06_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_06_YYYYMMDD_Of_PrcntlArray, pet_06_PrcntlArray, MonthlyList_pet_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_06_PrcntlArray)
pet_09_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_09_YYYYMMDD_Of_PrcntlArray, pet_09_PrcntlArray, MonthlyList_pet_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_09_PrcntlArray)

prcp_01_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_01_YYYYMMDD_Of_PrcntlArray, prcp_01_PrcntlArray, MonthlyList_prcp_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_01_PrcntlArray)
prcp_02_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_02_YYYYMMDD_Of_PrcntlArray, prcp_02_PrcntlArray, MonthlyList_prcp_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_02_PrcntlArray)
prcp_03_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_03_YYYYMMDD_Of_PrcntlArray, prcp_03_PrcntlArray, MonthlyList_prcp_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_03_PrcntlArray)
prcp_06_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_06_YYYYMMDD_Of_PrcntlArray, prcp_06_PrcntlArray, MonthlyList_prcp_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_06_PrcntlArray)
prcp_09_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_09_YYYYMMDD_Of_PrcntlArray, prcp_09_PrcntlArray, MonthlyList_prcp_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_09_PrcntlArray)

tavg_01_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_01_YYYYMMDD_Of_PrcntlArray, tavg_01_PrcntlArray, MonthlyList_tavg_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_01_PrcntlArray)
tavg_02_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_02_YYYYMMDD_Of_PrcntlArray, tavg_02_PrcntlArray, MonthlyList_tavg_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_02_PrcntlArray)
tavg_03_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_03_YYYYMMDD_Of_PrcntlArray, tavg_03_PrcntlArray, MonthlyList_tavg_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_03_PrcntlArray)
tavg_06_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_06_YYYYMMDD_Of_PrcntlArray, tavg_06_PrcntlArray, MonthlyList_tavg_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_06_PrcntlArray)
tavg_09_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_09_YYYYMMDD_Of_PrcntlArray, tavg_09_PrcntlArray, MonthlyList_tavg_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_09_PrcntlArray)

tmax_01_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_01_YYYYMMDD_Of_PrcntlArray, tmax_01_PrcntlArray, MonthlyList_tmax_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_01_PrcntlArray)
tmax_02_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_02_YYYYMMDD_Of_PrcntlArray, tmax_02_PrcntlArray, MonthlyList_tmax_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_02_PrcntlArray)
tmax_03_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_03_YYYYMMDD_Of_PrcntlArray, tmax_03_PrcntlArray, MonthlyList_tmax_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_03_PrcntlArray)
tmax_06_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_06_YYYYMMDD_Of_PrcntlArray, tmax_06_PrcntlArray, MonthlyList_tmax_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_06_PrcntlArray)
tmax_09_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_09_YYYYMMDD_Of_PrcntlArray, tmax_09_PrcntlArray, MonthlyList_tmax_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_09_PrcntlArray)

print('Training: NumDates = ', spei_gamma_01_PrcntlArray.shape[0], ', NumSpatialUnits = ',spei_gamma_01_PrcntlArray.shape[1])

PrintInfoAboutArray(spei_gamma_01_PrcntlArray, 'spei_gamma_01_PrcntlArray')
PrintInfoAboutArray(spei_gamma_02_PrcntlArray, 'spei_gamma_02_PrcntlArray')
PrintInfoAboutArray(spei_gamma_03_PrcntlArray, 'spei_gamma_03_PrcntlArray')
PrintInfoAboutArray(spei_gamma_06_PrcntlArray, 'spei_gamma_06_PrcntlArray')
PrintInfoAboutArray(spei_gamma_09_PrcntlArray, 'spei_gamma_09_PrcntlArray')
PrintInfoAboutArray(spei_gamma_12_PrcntlArray, 'spei_gamma_12_PrcntlArray')
PrintInfoAboutArray(spei_gamma_24_PrcntlArray, 'spei_gamma_24_PrcntlArray')
PrintInfoAboutArray(spei_gamma_36_PrcntlArray, 'spei_gamma_36_PrcntlArray')
PrintInfoAboutArray(spei_gamma_48_PrcntlArray, 'spei_gamma_48_PrcntlArray')
PrintInfoAboutArray(spei_gamma_60_PrcntlArray, 'spei_gamma_60_PrcntlArray')
PrintInfoAboutArray(spei_gamma_72_PrcntlArray, 'spei_gamma_72_PrcntlArray')

PrintInfoAboutArray(spei_pearson_01_PrcntlArray, 'spei_pearson_01_PrcntlArray')
PrintInfoAboutArray(spei_pearson_02_PrcntlArray, 'spei_pearson_02_PrcntlArray')
PrintInfoAboutArray(spei_pearson_03_PrcntlArray, 'spei_pearson_03_PrcntlArray')
PrintInfoAboutArray(spei_pearson_06_PrcntlArray, 'spei_pearson_06_PrcntlArray')
PrintInfoAboutArray(spei_pearson_09_PrcntlArray, 'spei_pearson_09_PrcntlArray')
PrintInfoAboutArray(spei_pearson_12_PrcntlArray, 'spei_pearson_12_PrcntlArray')
PrintInfoAboutArray(spei_pearson_24_PrcntlArray, 'spei_pearson_24_PrcntlArray')
PrintInfoAboutArray(spei_pearson_36_PrcntlArray, 'spei_pearson_36_PrcntlArray')
PrintInfoAboutArray(spei_pearson_48_PrcntlArray, 'spei_pearson_48_PrcntlArray')
PrintInfoAboutArray(spei_pearson_60_PrcntlArray, 'spei_pearson_60_PrcntlArray')
PrintInfoAboutArray(spei_pearson_72_PrcntlArray, 'spei_pearson_72_PrcntlArray')

PrintInfoAboutArray(spi_gamma_01_PrcntlArray, 'spi_gamma_01_PrcntlArray')
PrintInfoAboutArray(spi_gamma_02_PrcntlArray, 'spi_gamma_02_PrcntlArray')
PrintInfoAboutArray(spi_gamma_03_PrcntlArray, 'spi_gamma_03_PrcntlArray')
PrintInfoAboutArray(spi_gamma_06_PrcntlArray, 'spi_gamma_06_PrcntlArray')
PrintInfoAboutArray(spi_gamma_09_PrcntlArray, 'spi_gamma_09_PrcntlArray')
PrintInfoAboutArray(spi_gamma_12_PrcntlArray, 'spi_gamma_12_PrcntlArray')
PrintInfoAboutArray(spi_gamma_24_PrcntlArray, 'spi_gamma_24_PrcntlArray')
PrintInfoAboutArray(spi_gamma_36_PrcntlArray, 'spi_gamma_36_PrcntlArray')
PrintInfoAboutArray(spi_gamma_48_PrcntlArray, 'spi_gamma_48_PrcntlArray')
PrintInfoAboutArray(spi_gamma_60_PrcntlArray, 'spi_gamma_60_PrcntlArray')
PrintInfoAboutArray(spi_gamma_72_PrcntlArray, 'spi_gamma_72_PrcntlArray')

PrintInfoAboutArray(spi_pearson_01_PrcntlArray, 'spi_pearson_01_PrcntlArray')
PrintInfoAboutArray(spi_pearson_02_PrcntlArray, 'spi_pearson_02_PrcntlArray')
PrintInfoAboutArray(spi_pearson_03_PrcntlArray, 'spi_pearson_03_PrcntlArray')
PrintInfoAboutArray(spi_pearson_06_PrcntlArray, 'spi_pearson_06_PrcntlArray')
PrintInfoAboutArray(spi_pearson_09_PrcntlArray, 'spi_pearson_09_PrcntlArray')
PrintInfoAboutArray(spi_pearson_12_PrcntlArray, 'spi_pearson_12_PrcntlArray')
PrintInfoAboutArray(spi_pearson_24_PrcntlArray, 'spi_pearson_24_PrcntlArray')
PrintInfoAboutArray(spi_pearson_36_PrcntlArray, 'spi_pearson_36_PrcntlArray')
PrintInfoAboutArray(spi_pearson_48_PrcntlArray, 'spi_pearson_48_PrcntlArray')
PrintInfoAboutArray(spi_pearson_60_PrcntlArray, 'spi_pearson_60_PrcntlArray')
PrintInfoAboutArray(spi_pearson_72_PrcntlArray, 'spi_pearson_72_PrcntlArray')

PrintInfoAboutArray(pet_01_PrcntlArray, 'pet_01_PrcntlArray')
PrintInfoAboutArray(pet_02_PrcntlArray, 'pet_02_PrcntlArray')
PrintInfoAboutArray(pet_03_PrcntlArray, 'pet_03_PrcntlArray')
PrintInfoAboutArray(pet_06_PrcntlArray, 'pet_06_PrcntlArray')
PrintInfoAboutArray(pet_09_PrcntlArray, 'pet_09_PrcntlArray')
PrintInfoAboutArray(pet_12_PrcntlArray, 'pet_12_PrcntlArray')
PrintInfoAboutArray(pet_24_PrcntlArray, 'pet_24_PrcntlArray')
PrintInfoAboutArray(pet_36_PrcntlArray, 'pet_36_PrcntlArray')
PrintInfoAboutArray(pet_48_PrcntlArray, 'pet_48_PrcntlArray')
PrintInfoAboutArray(pet_60_PrcntlArray, 'pet_60_PrcntlArray')
PrintInfoAboutArray(pet_72_PrcntlArray, 'pet_72_PrcntlArray')

PrintInfoAboutArray(prcp_01_PrcntlArray, 'prcp_01_PrcntlArray')
PrintInfoAboutArray(prcp_02_PrcntlArray, 'prcp_02_PrcntlArray')
PrintInfoAboutArray(prcp_03_PrcntlArray, 'prcp_03_PrcntlArray')
PrintInfoAboutArray(prcp_06_PrcntlArray, 'prcp_06_PrcntlArray')
PrintInfoAboutArray(prcp_09_PrcntlArray, 'prcp_09_PrcntlArray')
PrintInfoAboutArray(prcp_12_PrcntlArray, 'prcp_12_PrcntlArray')
PrintInfoAboutArray(prcp_24_PrcntlArray, 'prcp_24_PrcntlArray')
PrintInfoAboutArray(prcp_36_PrcntlArray, 'prcp_36_PrcntlArray')
PrintInfoAboutArray(prcp_48_PrcntlArray, 'prcp_48_PrcntlArray')
PrintInfoAboutArray(prcp_60_PrcntlArray, 'prcp_60_PrcntlArray')
PrintInfoAboutArray(prcp_72_PrcntlArray, 'prcp_72_PrcntlArray')

PrintInfoAboutArray(tavg_01_PrcntlArray, 'tavg_01_PrcntlArray')
PrintInfoAboutArray(tavg_02_PrcntlArray, 'tavg_02_PrcntlArray')
PrintInfoAboutArray(tavg_03_PrcntlArray, 'tavg_03_PrcntlArray')
PrintInfoAboutArray(tavg_06_PrcntlArray, 'tavg_06_PrcntlArray')
PrintInfoAboutArray(tavg_09_PrcntlArray, 'tavg_09_PrcntlArray')
PrintInfoAboutArray(tavg_12_PrcntlArray, 'tavg_12_PrcntlArray')
PrintInfoAboutArray(tavg_24_PrcntlArray, 'tavg_24_PrcntlArray')
PrintInfoAboutArray(tavg_36_PrcntlArray, 'tavg_36_PrcntlArray')
PrintInfoAboutArray(tavg_48_PrcntlArray, 'tavg_48_PrcntlArray')
PrintInfoAboutArray(tavg_60_PrcntlArray, 'tavg_60_PrcntlArray')
PrintInfoAboutArray(tavg_72_PrcntlArray, 'tavg_72_PrcntlArray')

PrintInfoAboutArray(tmax_01_PrcntlArray, 'tmax_01_PrcntlArray')
PrintInfoAboutArray(tmax_02_PrcntlArray, 'tmax_02_PrcntlArray')
PrintInfoAboutArray(tmax_03_PrcntlArray, 'tmax_03_PrcntlArray')
PrintInfoAboutArray(tmax_06_PrcntlArray, 'tmax_06_PrcntlArray')
PrintInfoAboutArray(tmax_09_PrcntlArray, 'tmax_09_PrcntlArray')
PrintInfoAboutArray(tmax_12_PrcntlArray, 'tmax_12_PrcntlArray')
PrintInfoAboutArray(tmax_24_PrcntlArray, 'tmax_24_PrcntlArray')
PrintInfoAboutArray(tmax_36_PrcntlArray, 'tmax_36_PrcntlArray')
PrintInfoAboutArray(tmax_48_PrcntlArray, 'tmax_48_PrcntlArray')
PrintInfoAboutArray(tmax_60_PrcntlArray, 'tmax_60_PrcntlArray')
PrintInfoAboutArray(tmax_72_PrcntlArray, 'tmax_72_PrcntlArray')

np.savez_compressed(TrainDataFilename, 
                    YYYYMMDD_Of_Array = spei_gamma_01_YYYYMMDD_Of_PrcntlArray, 
                    spei_gamma_01_PrcntlArray = spei_gamma_01_PrcntlArray, 
                    spei_gamma_02_PrcntlArray = spei_gamma_02_PrcntlArray, 
                    spei_gamma_03_PrcntlArray = spei_gamma_03_PrcntlArray, 
                    spei_gamma_06_PrcntlArray = spei_gamma_06_PrcntlArray, 
                    spei_gamma_09_PrcntlArray = spei_gamma_09_PrcntlArray, 
                    spei_gamma_24_PrcntlArray = spei_gamma_24_PrcntlArray, 
                    spei_gamma_12_PrcntlArray = spei_gamma_12_PrcntlArray, 
                    spei_gamma_36_PrcntlArray = spei_gamma_36_PrcntlArray, 
                    spei_gamma_48_PrcntlArray = spei_gamma_48_PrcntlArray, 
                    spei_gamma_60_PrcntlArray = spei_gamma_60_PrcntlArray, 
                    spei_gamma_72_PrcntlArray = spei_gamma_72_PrcntlArray,
                    spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray, 
                    spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray, 
                    spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray, 
                    spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray, 
                    spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray, 
                    spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray, 
                    spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray, 
                    spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray, 
                    spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray, 
                    spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray, 
                    spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray,
                    spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray, 
                    spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray, 
                    spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray, 
                    spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray, 
                    spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray, 
                    spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray, 
                    spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray, 
                    spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray, 
                    spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray, 
                    spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray, 
                    spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray,
                    spi_pearson_01_PrcntlArray = spi_pearson_01_PrcntlArray, 
                    spi_pearson_02_PrcntlArray = spi_pearson_02_PrcntlArray, 
                    spi_pearson_03_PrcntlArray = spi_pearson_03_PrcntlArray, 
                    spi_pearson_06_PrcntlArray = spi_pearson_06_PrcntlArray, 
                    spi_pearson_09_PrcntlArray = spi_pearson_09_PrcntlArray, 
                    spi_pearson_24_PrcntlArray = spi_pearson_24_PrcntlArray, 
                    spi_pearson_12_PrcntlArray = spi_pearson_12_PrcntlArray, 
                    spi_pearson_36_PrcntlArray = spi_pearson_36_PrcntlArray, 
                    spi_pearson_48_PrcntlArray = spi_pearson_48_PrcntlArray, 
                    spi_pearson_60_PrcntlArray = spi_pearson_60_PrcntlArray, 
                    spi_pearson_72_PrcntlArray = spi_pearson_72_PrcntlArray,
                    pet_01_PrcntlArray = pet_01_PrcntlArray, 
                    pet_02_PrcntlArray = pet_02_PrcntlArray, 
                    pet_03_PrcntlArray = pet_03_PrcntlArray, 
                    pet_06_PrcntlArray = pet_06_PrcntlArray, 
                    pet_09_PrcntlArray = pet_09_PrcntlArray, 
                    pet_24_PrcntlArray = pet_24_PrcntlArray, 
                    pet_12_PrcntlArray = pet_12_PrcntlArray, 
                    pet_36_PrcntlArray = pet_36_PrcntlArray, 
                    pet_48_PrcntlArray = pet_48_PrcntlArray, 
                    pet_60_PrcntlArray = pet_60_PrcntlArray, 
                    pet_72_PrcntlArray = pet_72_PrcntlArray,
                    prcp_01_PrcntlArray = prcp_01_PrcntlArray, 
                    prcp_02_PrcntlArray = prcp_02_PrcntlArray, 
                    prcp_03_PrcntlArray = prcp_03_PrcntlArray, 
                    prcp_06_PrcntlArray = prcp_06_PrcntlArray, 
                    prcp_09_PrcntlArray = prcp_09_PrcntlArray, 
                    prcp_24_PrcntlArray = prcp_24_PrcntlArray, 
                    prcp_12_PrcntlArray = prcp_12_PrcntlArray, 
                    prcp_36_PrcntlArray = prcp_36_PrcntlArray, 
                    prcp_48_PrcntlArray = prcp_48_PrcntlArray, 
                    prcp_60_PrcntlArray = prcp_60_PrcntlArray, 
                    prcp_72_PrcntlArray = prcp_72_PrcntlArray,
                    tavg_01_PrcntlArray = tavg_01_PrcntlArray, 
                    tavg_02_PrcntlArray = tavg_02_PrcntlArray, 
                    tavg_03_PrcntlArray = tavg_03_PrcntlArray, 
                    tavg_06_PrcntlArray = tavg_06_PrcntlArray, 
                    tavg_09_PrcntlArray = tavg_09_PrcntlArray, 
                    tavg_24_PrcntlArray = tavg_24_PrcntlArray, 
                    tavg_12_PrcntlArray = tavg_12_PrcntlArray, 
                    tavg_36_PrcntlArray = tavg_36_PrcntlArray, 
                    tavg_48_PrcntlArray = tavg_48_PrcntlArray, 
                    tavg_60_PrcntlArray = tavg_60_PrcntlArray, 
                    tavg_72_PrcntlArray = tavg_72_PrcntlArray,
                    tmax_01_PrcntlArray = tmax_01_PrcntlArray, 
                    tmax_02_PrcntlArray = tmax_02_PrcntlArray, 
                    tmax_03_PrcntlArray = tmax_03_PrcntlArray, 
                    tmax_06_PrcntlArray = tmax_06_PrcntlArray, 
                    tmax_09_PrcntlArray = tmax_09_PrcntlArray, 
                    tmax_24_PrcntlArray = tmax_24_PrcntlArray, 
                    tmax_12_PrcntlArray = tmax_12_PrcntlArray, 
                    tmax_36_PrcntlArray = tmax_36_PrcntlArray, 
                    tmax_48_PrcntlArray = tmax_48_PrcntlArray, 
                    tmax_60_PrcntlArray = tmax_60_PrcntlArray, 
                    tmax_72_PrcntlArray = tmax_72_PrcntlArray )

#END section for training

#BEGIN section for evaluation

spei_gamma_01_YYYYMMDD_Of_PrcntlArray, spei_gamma_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_01_YYYYMMDD_Of_RefArray, spei_gamma_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_02_YYYYMMDD_Of_PrcntlArray, spei_gamma_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_02_YYYYMMDD_Of_RefArray, spei_gamma_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_03_YYYYMMDD_Of_PrcntlArray, spei_gamma_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_03_YYYYMMDD_Of_RefArray, spei_gamma_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_06_YYYYMMDD_Of_PrcntlArray, spei_gamma_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_06_YYYYMMDD_Of_RefArray, spei_gamma_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_09_YYYYMMDD_Of_PrcntlArray, spei_gamma_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_09_YYYYMMDD_Of_RefArray, spei_gamma_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_12_YYYYMMDD_Of_PrcntlArray, spei_gamma_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_12_YYYYMMDD_Of_RefArray, spei_gamma_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_24_YYYYMMDD_Of_PrcntlArray, spei_gamma_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_24_YYYYMMDD_Of_RefArray, spei_gamma_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_36_YYYYMMDD_Of_PrcntlArray, spei_gamma_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_36_YYYYMMDD_Of_RefArray, spei_gamma_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_48_YYYYMMDD_Of_PrcntlArray, spei_gamma_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_48_YYYYMMDD_Of_RefArray, spei_gamma_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_60_YYYYMMDD_Of_PrcntlArray, spei_gamma_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_60_YYYYMMDD_Of_RefArray, spei_gamma_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_gamma_72_YYYYMMDD_Of_PrcntlArray, spei_gamma_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_gamma_72_YYYYMMDD_Of_RefArray, spei_gamma_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

spei_pearson_01_YYYYMMDD_Of_PrcntlArray, spei_pearson_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_01_YYYYMMDD_Of_RefArray, spei_pearson_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_02_YYYYMMDD_Of_PrcntlArray, spei_pearson_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_02_YYYYMMDD_Of_RefArray, spei_pearson_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_03_YYYYMMDD_Of_PrcntlArray, spei_pearson_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_03_YYYYMMDD_Of_RefArray, spei_pearson_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_06_YYYYMMDD_Of_PrcntlArray, spei_pearson_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_06_YYYYMMDD_Of_RefArray, spei_pearson_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_09_YYYYMMDD_Of_PrcntlArray, spei_pearson_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_09_YYYYMMDD_Of_RefArray, spei_pearson_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_12_YYYYMMDD_Of_PrcntlArray, spei_pearson_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_12_YYYYMMDD_Of_RefArray, spei_pearson_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_24_YYYYMMDD_Of_PrcntlArray, spei_pearson_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_24_YYYYMMDD_Of_RefArray, spei_pearson_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_36_YYYYMMDD_Of_PrcntlArray, spei_pearson_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_36_YYYYMMDD_Of_RefArray, spei_pearson_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_48_YYYYMMDD_Of_PrcntlArray, spei_pearson_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_48_YYYYMMDD_Of_RefArray, spei_pearson_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_60_YYYYMMDD_Of_PrcntlArray, spei_pearson_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_60_YYYYMMDD_Of_RefArray, spei_pearson_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spei_pearson_72_YYYYMMDD_Of_PrcntlArray, spei_pearson_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spei_pearson_72_YYYYMMDD_Of_RefArray, spei_pearson_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

spi_gamma_01_YYYYMMDD_Of_PrcntlArray, spi_gamma_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_01_YYYYMMDD_Of_RefArray, spi_gamma_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_02_YYYYMMDD_Of_PrcntlArray, spi_gamma_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_02_YYYYMMDD_Of_RefArray, spi_gamma_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_03_YYYYMMDD_Of_PrcntlArray, spi_gamma_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_03_YYYYMMDD_Of_RefArray, spi_gamma_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_06_YYYYMMDD_Of_PrcntlArray, spi_gamma_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_06_YYYYMMDD_Of_RefArray, spi_gamma_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_09_YYYYMMDD_Of_PrcntlArray, spi_gamma_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_09_YYYYMMDD_Of_RefArray, spi_gamma_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_12_YYYYMMDD_Of_PrcntlArray, spi_gamma_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_12_YYYYMMDD_Of_RefArray, spi_gamma_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_24_YYYYMMDD_Of_PrcntlArray, spi_gamma_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_24_YYYYMMDD_Of_RefArray, spi_gamma_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_36_YYYYMMDD_Of_PrcntlArray, spi_gamma_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_36_YYYYMMDD_Of_RefArray, spi_gamma_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_48_YYYYMMDD_Of_PrcntlArray, spi_gamma_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_48_YYYYMMDD_Of_RefArray, spi_gamma_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_60_YYYYMMDD_Of_PrcntlArray, spi_gamma_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_60_YYYYMMDD_Of_RefArray, spi_gamma_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_gamma_72_YYYYMMDD_Of_PrcntlArray, spi_gamma_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_gamma_72_YYYYMMDD_Of_RefArray, spi_gamma_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

spi_pearson_01_YYYYMMDD_Of_PrcntlArray, spi_pearson_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_01_YYYYMMDD_Of_RefArray, spi_pearson_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_02_YYYYMMDD_Of_PrcntlArray, spi_pearson_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_02_YYYYMMDD_Of_RefArray, spi_pearson_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_03_YYYYMMDD_Of_PrcntlArray, spi_pearson_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_03_YYYYMMDD_Of_RefArray, spi_pearson_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_06_YYYYMMDD_Of_PrcntlArray, spi_pearson_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_06_YYYYMMDD_Of_RefArray, spi_pearson_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_09_YYYYMMDD_Of_PrcntlArray, spi_pearson_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_09_YYYYMMDD_Of_RefArray, spi_pearson_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_12_YYYYMMDD_Of_PrcntlArray, spi_pearson_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_12_YYYYMMDD_Of_RefArray, spi_pearson_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_24_YYYYMMDD_Of_PrcntlArray, spi_pearson_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_24_YYYYMMDD_Of_RefArray, spi_pearson_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_36_YYYYMMDD_Of_PrcntlArray, spi_pearson_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_36_YYYYMMDD_Of_RefArray, spi_pearson_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_48_YYYYMMDD_Of_PrcntlArray, spi_pearson_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_48_YYYYMMDD_Of_RefArray, spi_pearson_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_60_YYYYMMDD_Of_PrcntlArray, spi_pearson_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_60_YYYYMMDD_Of_RefArray, spi_pearson_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
spi_pearson_72_YYYYMMDD_Of_PrcntlArray, spi_pearson_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(spi_pearson_72_YYYYMMDD_Of_RefArray, spi_pearson_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

pet_01_YYYYMMDD_Of_PrcntlArray, pet_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_01_YYYYMMDD_Of_RefArray, pet_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_02_YYYYMMDD_Of_PrcntlArray, pet_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_02_YYYYMMDD_Of_RefArray, pet_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_03_YYYYMMDD_Of_PrcntlArray, pet_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_03_YYYYMMDD_Of_RefArray, pet_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_06_YYYYMMDD_Of_PrcntlArray, pet_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_06_YYYYMMDD_Of_RefArray, pet_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_09_YYYYMMDD_Of_PrcntlArray, pet_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_09_YYYYMMDD_Of_RefArray, pet_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_12_YYYYMMDD_Of_PrcntlArray, pet_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_12_YYYYMMDD_Of_RefArray, pet_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_24_YYYYMMDD_Of_PrcntlArray, pet_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_24_YYYYMMDD_Of_RefArray, pet_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_36_YYYYMMDD_Of_PrcntlArray, pet_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_36_YYYYMMDD_Of_RefArray, pet_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_48_YYYYMMDD_Of_PrcntlArray, pet_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_48_YYYYMMDD_Of_RefArray, pet_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_60_YYYYMMDD_Of_PrcntlArray, pet_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_60_YYYYMMDD_Of_RefArray, pet_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
pet_72_YYYYMMDD_Of_PrcntlArray, pet_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(pet_72_YYYYMMDD_Of_RefArray, pet_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

prcp_01_YYYYMMDD_Of_PrcntlArray, prcp_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_01_YYYYMMDD_Of_RefArray, prcp_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_02_YYYYMMDD_Of_PrcntlArray, prcp_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_02_YYYYMMDD_Of_RefArray, prcp_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_03_YYYYMMDD_Of_PrcntlArray, prcp_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_03_YYYYMMDD_Of_RefArray, prcp_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_06_YYYYMMDD_Of_PrcntlArray, prcp_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_06_YYYYMMDD_Of_RefArray, prcp_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_09_YYYYMMDD_Of_PrcntlArray, prcp_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_09_YYYYMMDD_Of_RefArray, prcp_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_12_YYYYMMDD_Of_PrcntlArray, prcp_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_12_YYYYMMDD_Of_RefArray, prcp_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_24_YYYYMMDD_Of_PrcntlArray, prcp_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_24_YYYYMMDD_Of_RefArray, prcp_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_36_YYYYMMDD_Of_PrcntlArray, prcp_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_36_YYYYMMDD_Of_RefArray, prcp_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_48_YYYYMMDD_Of_PrcntlArray, prcp_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_48_YYYYMMDD_Of_RefArray, prcp_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_60_YYYYMMDD_Of_PrcntlArray, prcp_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_60_YYYYMMDD_Of_RefArray, prcp_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
prcp_72_YYYYMMDD_Of_PrcntlArray, prcp_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(prcp_72_YYYYMMDD_Of_RefArray, prcp_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

tavg_01_YYYYMMDD_Of_PrcntlArray, tavg_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_01_YYYYMMDD_Of_RefArray, tavg_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_02_YYYYMMDD_Of_PrcntlArray, tavg_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_02_YYYYMMDD_Of_RefArray, tavg_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_03_YYYYMMDD_Of_PrcntlArray, tavg_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_03_YYYYMMDD_Of_RefArray, tavg_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_06_YYYYMMDD_Of_PrcntlArray, tavg_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_06_YYYYMMDD_Of_RefArray, tavg_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_09_YYYYMMDD_Of_PrcntlArray, tavg_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_09_YYYYMMDD_Of_RefArray, tavg_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_12_YYYYMMDD_Of_PrcntlArray, tavg_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_12_YYYYMMDD_Of_RefArray, tavg_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_24_YYYYMMDD_Of_PrcntlArray, tavg_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_24_YYYYMMDD_Of_RefArray, tavg_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_36_YYYYMMDD_Of_PrcntlArray, tavg_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_36_YYYYMMDD_Of_RefArray, tavg_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_48_YYYYMMDD_Of_PrcntlArray, tavg_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_48_YYYYMMDD_Of_RefArray, tavg_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_60_YYYYMMDD_Of_PrcntlArray, tavg_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_60_YYYYMMDD_Of_RefArray, tavg_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tavg_72_YYYYMMDD_Of_PrcntlArray, tavg_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tavg_72_YYYYMMDD_Of_RefArray, tavg_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

tmax_01_YYYYMMDD_Of_PrcntlArray, tmax_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_01_YYYYMMDD_Of_RefArray, tmax_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_02_YYYYMMDD_Of_PrcntlArray, tmax_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_02_YYYYMMDD_Of_RefArray, tmax_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_03_YYYYMMDD_Of_PrcntlArray, tmax_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_03_YYYYMMDD_Of_RefArray, tmax_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_06_YYYYMMDD_Of_PrcntlArray, tmax_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_06_YYYYMMDD_Of_RefArray, tmax_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_09_YYYYMMDD_Of_PrcntlArray, tmax_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_09_YYYYMMDD_Of_RefArray, tmax_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_12_YYYYMMDD_Of_PrcntlArray, tmax_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_12_YYYYMMDD_Of_RefArray, tmax_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_24_YYYYMMDD_Of_PrcntlArray, tmax_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_24_YYYYMMDD_Of_RefArray, tmax_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_36_YYYYMMDD_Of_PrcntlArray, tmax_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_36_YYYYMMDD_Of_RefArray, tmax_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_48_YYYYMMDD_Of_PrcntlArray, tmax_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_48_YYYYMMDD_Of_RefArray, tmax_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_60_YYYYMMDD_Of_PrcntlArray, tmax_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_60_YYYYMMDD_Of_RefArray, tmax_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
tmax_72_YYYYMMDD_Of_PrcntlArray, tmax_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(tmax_72_YYYYMMDD_Of_RefArray, tmax_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

MonthlyList_spei_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_01_YYYYMMDD_Of_PrcntlArray, spei_gamma_01_PrcntlArray)
MonthlyList_spei_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_02_YYYYMMDD_Of_PrcntlArray, spei_gamma_02_PrcntlArray)
MonthlyList_spei_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_03_YYYYMMDD_Of_PrcntlArray, spei_gamma_03_PrcntlArray)
MonthlyList_spei_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_06_YYYYMMDD_Of_PrcntlArray, spei_gamma_06_PrcntlArray)
MonthlyList_spei_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_gamma_09_YYYYMMDD_Of_PrcntlArray, spei_gamma_09_PrcntlArray)

MonthlyList_spei_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_01_YYYYMMDD_Of_PrcntlArray, spei_pearson_01_PrcntlArray)
MonthlyList_spei_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_02_YYYYMMDD_Of_PrcntlArray, spei_pearson_02_PrcntlArray)
MonthlyList_spei_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_03_YYYYMMDD_Of_PrcntlArray, spei_pearson_03_PrcntlArray)
MonthlyList_spei_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_06_YYYYMMDD_Of_PrcntlArray, spei_pearson_06_PrcntlArray)
MonthlyList_spei_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spei_pearson_09_YYYYMMDD_Of_PrcntlArray, spei_pearson_09_PrcntlArray)

MonthlyList_spi_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_01_YYYYMMDD_Of_PrcntlArray, spi_gamma_01_PrcntlArray)
MonthlyList_spi_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_02_YYYYMMDD_Of_PrcntlArray, spi_gamma_02_PrcntlArray)
MonthlyList_spi_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_03_YYYYMMDD_Of_PrcntlArray, spi_gamma_03_PrcntlArray)
MonthlyList_spi_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_06_YYYYMMDD_Of_PrcntlArray, spi_gamma_06_PrcntlArray)
MonthlyList_spi_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_gamma_09_YYYYMMDD_Of_PrcntlArray, spi_gamma_09_PrcntlArray)

MonthlyList_spi_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_01_YYYYMMDD_Of_PrcntlArray, spi_pearson_01_PrcntlArray)
MonthlyList_spi_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_02_YYYYMMDD_Of_PrcntlArray, spi_pearson_02_PrcntlArray)
MonthlyList_spi_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_03_YYYYMMDD_Of_PrcntlArray, spi_pearson_03_PrcntlArray)
MonthlyList_spi_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_06_YYYYMMDD_Of_PrcntlArray, spi_pearson_06_PrcntlArray)
MonthlyList_spi_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(spi_pearson_09_YYYYMMDD_Of_PrcntlArray, spi_pearson_09_PrcntlArray)

MonthlyList_pet_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_01_YYYYMMDD_Of_PrcntlArray, pet_01_PrcntlArray)
MonthlyList_pet_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_02_YYYYMMDD_Of_PrcntlArray, pet_02_PrcntlArray)
MonthlyList_pet_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_03_YYYYMMDD_Of_PrcntlArray, pet_03_PrcntlArray)
MonthlyList_pet_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_06_YYYYMMDD_Of_PrcntlArray, pet_06_PrcntlArray)
MonthlyList_pet_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(pet_09_YYYYMMDD_Of_PrcntlArray, pet_09_PrcntlArray)

MonthlyList_prcp_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_01_YYYYMMDD_Of_PrcntlArray, prcp_01_PrcntlArray)
MonthlyList_prcp_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_02_YYYYMMDD_Of_PrcntlArray, prcp_02_PrcntlArray)
MonthlyList_prcp_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_03_YYYYMMDD_Of_PrcntlArray, prcp_03_PrcntlArray)
MonthlyList_prcp_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_06_YYYYMMDD_Of_PrcntlArray, prcp_06_PrcntlArray)
MonthlyList_prcp_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(prcp_09_YYYYMMDD_Of_PrcntlArray, prcp_09_PrcntlArray)

MonthlyList_tavg_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_01_YYYYMMDD_Of_PrcntlArray, tavg_01_PrcntlArray)
MonthlyList_tavg_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_02_YYYYMMDD_Of_PrcntlArray, tavg_02_PrcntlArray)
MonthlyList_tavg_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_03_YYYYMMDD_Of_PrcntlArray, tavg_03_PrcntlArray)
MonthlyList_tavg_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_06_YYYYMMDD_Of_PrcntlArray, tavg_06_PrcntlArray)
MonthlyList_tavg_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tavg_09_YYYYMMDD_Of_PrcntlArray, tavg_09_PrcntlArray)

MonthlyList_tmax_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_01_YYYYMMDD_Of_PrcntlArray, tmax_01_PrcntlArray)
MonthlyList_tmax_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_02_YYYYMMDD_Of_PrcntlArray, tmax_02_PrcntlArray)
MonthlyList_tmax_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_03_YYYYMMDD_Of_PrcntlArray, tmax_03_PrcntlArray)
MonthlyList_tmax_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_06_YYYYMMDD_Of_PrcntlArray, tmax_06_PrcntlArray)
MonthlyList_tmax_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(tmax_09_YYYYMMDD_Of_PrcntlArray, tmax_09_PrcntlArray)

spei_gamma_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_12_RefArray, spei_gamma_12_PrcntlArray)
spei_gamma_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_24_RefArray, spei_gamma_24_PrcntlArray)
spei_gamma_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_36_RefArray, spei_gamma_36_PrcntlArray)
spei_gamma_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_48_RefArray, spei_gamma_48_PrcntlArray)
spei_gamma_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_60_RefArray, spei_gamma_60_PrcntlArray)
spei_gamma_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_gamma_72_RefArray, spei_gamma_72_PrcntlArray)

spei_pearson_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_12_RefArray, spei_pearson_12_PrcntlArray)
spei_pearson_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_24_RefArray, spei_pearson_24_PrcntlArray)
spei_pearson_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_36_RefArray, spei_pearson_36_PrcntlArray)
spei_pearson_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_48_RefArray, spei_pearson_48_PrcntlArray)
spei_pearson_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_60_RefArray, spei_pearson_60_PrcntlArray)
spei_pearson_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spei_pearson_72_RefArray, spei_pearson_72_PrcntlArray)

spi_gamma_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_12_RefArray, spi_gamma_12_PrcntlArray)
spi_gamma_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_24_RefArray, spi_gamma_24_PrcntlArray)
spi_gamma_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_36_RefArray, spi_gamma_36_PrcntlArray)
spi_gamma_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_48_RefArray, spi_gamma_48_PrcntlArray)
spi_gamma_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_60_RefArray, spi_gamma_60_PrcntlArray)
spi_gamma_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_gamma_72_RefArray, spi_gamma_72_PrcntlArray)

spi_pearson_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_12_RefArray, spi_pearson_12_PrcntlArray)
spi_pearson_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_24_RefArray, spi_pearson_24_PrcntlArray)
spi_pearson_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_36_RefArray, spi_pearson_36_PrcntlArray)
spi_pearson_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_48_RefArray, spi_pearson_48_PrcntlArray)
spi_pearson_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_60_RefArray, spi_pearson_60_PrcntlArray)
spi_pearson_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(spi_pearson_72_RefArray, spi_pearson_72_PrcntlArray)

pet_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_12_RefArray, pet_12_PrcntlArray)
pet_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_24_RefArray, pet_24_PrcntlArray)
pet_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_36_RefArray, pet_36_PrcntlArray)
pet_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_48_RefArray, pet_48_PrcntlArray)
pet_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_60_RefArray, pet_60_PrcntlArray)
pet_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(pet_72_RefArray, pet_72_PrcntlArray)

prcp_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_12_RefArray, prcp_12_PrcntlArray)
prcp_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_24_RefArray, prcp_24_PrcntlArray)
prcp_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_36_RefArray, prcp_36_PrcntlArray)
prcp_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_48_RefArray, prcp_48_PrcntlArray)
prcp_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_60_RefArray, prcp_60_PrcntlArray)
prcp_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(prcp_72_RefArray, prcp_72_PrcntlArray)

tavg_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_12_RefArray, tavg_12_PrcntlArray)
tavg_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_24_RefArray, tavg_24_PrcntlArray)
tavg_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_36_RefArray, tavg_36_PrcntlArray)
tavg_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_48_RefArray, tavg_48_PrcntlArray)
tavg_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_60_RefArray, tavg_60_PrcntlArray)
tavg_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tavg_72_RefArray, tavg_72_PrcntlArray)

tmax_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_12_RefArray, tmax_12_PrcntlArray)
tmax_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_24_RefArray, tmax_24_PrcntlArray)
tmax_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_36_RefArray, tmax_36_PrcntlArray)
tmax_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_48_RefArray, tmax_48_PrcntlArray)
tmax_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_60_RefArray, tmax_60_PrcntlArray)
tmax_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(tmax_72_RefArray, tmax_72_PrcntlArray)

MonthlyList_spei_gamma_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_01_RefArray, MonthlyList_spei_gamma_01_PrcntlArray)
MonthlyList_spei_gamma_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_02_RefArray, MonthlyList_spei_gamma_02_PrcntlArray)
MonthlyList_spei_gamma_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_03_RefArray, MonthlyList_spei_gamma_03_PrcntlArray)
MonthlyList_spei_gamma_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_06_RefArray, MonthlyList_spei_gamma_06_PrcntlArray)
MonthlyList_spei_gamma_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_gamma_09_RefArray, MonthlyList_spei_gamma_09_PrcntlArray)

MonthlyList_spei_pearson_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_01_RefArray, MonthlyList_spei_pearson_01_PrcntlArray)
MonthlyList_spei_pearson_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_02_RefArray, MonthlyList_spei_pearson_02_PrcntlArray)
MonthlyList_spei_pearson_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_03_RefArray, MonthlyList_spei_pearson_03_PrcntlArray)
MonthlyList_spei_pearson_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_06_RefArray, MonthlyList_spei_pearson_06_PrcntlArray)
MonthlyList_spei_pearson_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spei_pearson_09_RefArray, MonthlyList_spei_pearson_09_PrcntlArray)

MonthlyList_spi_gamma_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_01_RefArray, MonthlyList_spi_gamma_01_PrcntlArray)
MonthlyList_spi_gamma_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_02_RefArray, MonthlyList_spi_gamma_02_PrcntlArray)
MonthlyList_spi_gamma_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_03_RefArray, MonthlyList_spi_gamma_03_PrcntlArray)
MonthlyList_spi_gamma_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_06_RefArray, MonthlyList_spi_gamma_06_PrcntlArray)
MonthlyList_spi_gamma_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_gamma_09_RefArray, MonthlyList_spi_gamma_09_PrcntlArray)

MonthlyList_spi_pearson_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_01_RefArray, MonthlyList_spi_pearson_01_PrcntlArray)
MonthlyList_spi_pearson_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_02_RefArray, MonthlyList_spi_pearson_02_PrcntlArray)
MonthlyList_spi_pearson_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_03_RefArray, MonthlyList_spi_pearson_03_PrcntlArray)
MonthlyList_spi_pearson_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_06_RefArray, MonthlyList_spi_pearson_06_PrcntlArray)
MonthlyList_spi_pearson_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_spi_pearson_09_RefArray, MonthlyList_spi_pearson_09_PrcntlArray)

MonthlyList_pet_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_01_RefArray, MonthlyList_pet_01_PrcntlArray)
MonthlyList_pet_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_02_RefArray, MonthlyList_pet_02_PrcntlArray)
MonthlyList_pet_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_03_RefArray, MonthlyList_pet_03_PrcntlArray)
MonthlyList_pet_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_06_RefArray, MonthlyList_pet_06_PrcntlArray)
MonthlyList_pet_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_pet_09_RefArray, MonthlyList_pet_09_PrcntlArray)

MonthlyList_prcp_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_01_RefArray, MonthlyList_prcp_01_PrcntlArray)
MonthlyList_prcp_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_02_RefArray, MonthlyList_prcp_02_PrcntlArray)
MonthlyList_prcp_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_03_RefArray, MonthlyList_prcp_03_PrcntlArray)
MonthlyList_prcp_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_06_RefArray, MonthlyList_prcp_06_PrcntlArray)
MonthlyList_prcp_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_prcp_09_RefArray, MonthlyList_prcp_09_PrcntlArray)

MonthlyList_tavg_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_01_RefArray, MonthlyList_tavg_01_PrcntlArray)
MonthlyList_tavg_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_02_RefArray, MonthlyList_tavg_02_PrcntlArray)
MonthlyList_tavg_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_03_RefArray, MonthlyList_tavg_03_PrcntlArray)
MonthlyList_tavg_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_06_RefArray, MonthlyList_tavg_06_PrcntlArray)
MonthlyList_tavg_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tavg_09_RefArray, MonthlyList_tavg_09_PrcntlArray)

MonthlyList_tmax_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_01_RefArray, MonthlyList_tmax_01_PrcntlArray)
MonthlyList_tmax_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_02_RefArray, MonthlyList_tmax_02_PrcntlArray)
MonthlyList_tmax_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_03_RefArray, MonthlyList_tmax_03_PrcntlArray)
MonthlyList_tmax_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_06_RefArray, MonthlyList_tmax_06_PrcntlArray)
MonthlyList_tmax_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_tmax_09_RefArray, MonthlyList_tmax_09_PrcntlArray)

spei_gamma_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_01_YYYYMMDD_Of_PrcntlArray, spei_gamma_01_PrcntlArray, MonthlyList_spei_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_01_PrcntlArray)
spei_gamma_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_02_YYYYMMDD_Of_PrcntlArray, spei_gamma_02_PrcntlArray, MonthlyList_spei_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_02_PrcntlArray)
spei_gamma_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_03_YYYYMMDD_Of_PrcntlArray, spei_gamma_03_PrcntlArray, MonthlyList_spei_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_03_PrcntlArray)
spei_gamma_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_06_YYYYMMDD_Of_PrcntlArray, spei_gamma_06_PrcntlArray, MonthlyList_spei_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_06_PrcntlArray)
spei_gamma_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_gamma_09_YYYYMMDD_Of_PrcntlArray, spei_gamma_09_PrcntlArray, MonthlyList_spei_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_gamma_09_PrcntlArray)

spei_pearson_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_01_YYYYMMDD_Of_PrcntlArray, spei_pearson_01_PrcntlArray, MonthlyList_spei_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_01_PrcntlArray)
spei_pearson_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_02_YYYYMMDD_Of_PrcntlArray, spei_pearson_02_PrcntlArray, MonthlyList_spei_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_02_PrcntlArray)
spei_pearson_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_03_YYYYMMDD_Of_PrcntlArray, spei_pearson_03_PrcntlArray, MonthlyList_spei_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_03_PrcntlArray)
spei_pearson_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_06_YYYYMMDD_Of_PrcntlArray, spei_pearson_06_PrcntlArray, MonthlyList_spei_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_06_PrcntlArray)
spei_pearson_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spei_pearson_09_YYYYMMDD_Of_PrcntlArray, spei_pearson_09_PrcntlArray, MonthlyList_spei_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spei_pearson_09_PrcntlArray)

spi_gamma_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_01_YYYYMMDD_Of_PrcntlArray, spi_gamma_01_PrcntlArray, MonthlyList_spi_gamma_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_01_PrcntlArray)
spi_gamma_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_02_YYYYMMDD_Of_PrcntlArray, spi_gamma_02_PrcntlArray, MonthlyList_spi_gamma_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_02_PrcntlArray)
spi_gamma_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_03_YYYYMMDD_Of_PrcntlArray, spi_gamma_03_PrcntlArray, MonthlyList_spi_gamma_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_03_PrcntlArray)
spi_gamma_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_06_YYYYMMDD_Of_PrcntlArray, spi_gamma_06_PrcntlArray, MonthlyList_spi_gamma_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_06_PrcntlArray)
spi_gamma_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_gamma_09_YYYYMMDD_Of_PrcntlArray, spi_gamma_09_PrcntlArray, MonthlyList_spi_gamma_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_gamma_09_PrcntlArray)

spi_pearson_01_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_01_YYYYMMDD_Of_PrcntlArray, spi_pearson_01_PrcntlArray, MonthlyList_spi_pearson_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_01_PrcntlArray)
spi_pearson_02_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_02_YYYYMMDD_Of_PrcntlArray, spi_pearson_02_PrcntlArray, MonthlyList_spi_pearson_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_02_PrcntlArray)
spi_pearson_03_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_03_YYYYMMDD_Of_PrcntlArray, spi_pearson_03_PrcntlArray, MonthlyList_spi_pearson_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_03_PrcntlArray)
spi_pearson_06_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_06_YYYYMMDD_Of_PrcntlArray, spi_pearson_06_PrcntlArray, MonthlyList_spi_pearson_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_06_PrcntlArray)
spi_pearson_09_PrcntlArray = ReAssembleArraysFromMonthlyList(spi_pearson_09_YYYYMMDD_Of_PrcntlArray, spi_pearson_09_PrcntlArray, MonthlyList_spi_pearson_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_spi_pearson_09_PrcntlArray)

pet_01_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_01_YYYYMMDD_Of_PrcntlArray, pet_01_PrcntlArray, MonthlyList_pet_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_01_PrcntlArray)
pet_02_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_02_YYYYMMDD_Of_PrcntlArray, pet_02_PrcntlArray, MonthlyList_pet_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_02_PrcntlArray)
pet_03_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_03_YYYYMMDD_Of_PrcntlArray, pet_03_PrcntlArray, MonthlyList_pet_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_03_PrcntlArray)
pet_06_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_06_YYYYMMDD_Of_PrcntlArray, pet_06_PrcntlArray, MonthlyList_pet_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_06_PrcntlArray)
pet_09_PrcntlArray = ReAssembleArraysFromMonthlyList(pet_09_YYYYMMDD_Of_PrcntlArray, pet_09_PrcntlArray, MonthlyList_pet_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_pet_09_PrcntlArray)

prcp_01_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_01_YYYYMMDD_Of_PrcntlArray, prcp_01_PrcntlArray, MonthlyList_prcp_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_01_PrcntlArray)
prcp_02_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_02_YYYYMMDD_Of_PrcntlArray, prcp_02_PrcntlArray, MonthlyList_prcp_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_02_PrcntlArray)
prcp_03_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_03_YYYYMMDD_Of_PrcntlArray, prcp_03_PrcntlArray, MonthlyList_prcp_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_03_PrcntlArray)
prcp_06_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_06_YYYYMMDD_Of_PrcntlArray, prcp_06_PrcntlArray, MonthlyList_prcp_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_06_PrcntlArray)
prcp_09_PrcntlArray = ReAssembleArraysFromMonthlyList(prcp_09_YYYYMMDD_Of_PrcntlArray, prcp_09_PrcntlArray, MonthlyList_prcp_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_prcp_09_PrcntlArray)

tavg_01_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_01_YYYYMMDD_Of_PrcntlArray, tavg_01_PrcntlArray, MonthlyList_tavg_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_01_PrcntlArray)
tavg_02_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_02_YYYYMMDD_Of_PrcntlArray, tavg_02_PrcntlArray, MonthlyList_tavg_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_02_PrcntlArray)
tavg_03_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_03_YYYYMMDD_Of_PrcntlArray, tavg_03_PrcntlArray, MonthlyList_tavg_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_03_PrcntlArray)
tavg_06_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_06_YYYYMMDD_Of_PrcntlArray, tavg_06_PrcntlArray, MonthlyList_tavg_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_06_PrcntlArray)
tavg_09_PrcntlArray = ReAssembleArraysFromMonthlyList(tavg_09_YYYYMMDD_Of_PrcntlArray, tavg_09_PrcntlArray, MonthlyList_tavg_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tavg_09_PrcntlArray)

tmax_01_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_01_YYYYMMDD_Of_PrcntlArray, tmax_01_PrcntlArray, MonthlyList_tmax_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_01_PrcntlArray)
tmax_02_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_02_YYYYMMDD_Of_PrcntlArray, tmax_02_PrcntlArray, MonthlyList_tmax_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_02_PrcntlArray)
tmax_03_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_03_YYYYMMDD_Of_PrcntlArray, tmax_03_PrcntlArray, MonthlyList_tmax_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_03_PrcntlArray)
tmax_06_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_06_YYYYMMDD_Of_PrcntlArray, tmax_06_PrcntlArray, MonthlyList_tmax_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_06_PrcntlArray)
tmax_09_PrcntlArray = ReAssembleArraysFromMonthlyList(tmax_09_YYYYMMDD_Of_PrcntlArray, tmax_09_PrcntlArray, MonthlyList_tmax_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_tmax_09_PrcntlArray)

Dev_spei_gamma_01_YYYYMMDD_Of_PrcntlArray = spei_gamma_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_02_YYYYMMDD_Of_PrcntlArray = spei_gamma_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_03_YYYYMMDD_Of_PrcntlArray = spei_gamma_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_06_YYYYMMDD_Of_PrcntlArray = spei_gamma_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_09_YYYYMMDD_Of_PrcntlArray = spei_gamma_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_12_YYYYMMDD_Of_PrcntlArray = spei_gamma_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_24_YYYYMMDD_Of_PrcntlArray = spei_gamma_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_36_YYYYMMDD_Of_PrcntlArray = spei_gamma_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_48_YYYYMMDD_Of_PrcntlArray = spei_gamma_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_60_YYYYMMDD_Of_PrcntlArray = spei_gamma_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_gamma_72_YYYYMMDD_Of_PrcntlArray = spei_gamma_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_spei_pearson_01_YYYYMMDD_Of_PrcntlArray = spei_pearson_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_02_YYYYMMDD_Of_PrcntlArray = spei_pearson_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_03_YYYYMMDD_Of_PrcntlArray = spei_pearson_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_06_YYYYMMDD_Of_PrcntlArray = spei_pearson_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_09_YYYYMMDD_Of_PrcntlArray = spei_pearson_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_12_YYYYMMDD_Of_PrcntlArray = spei_pearson_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_24_YYYYMMDD_Of_PrcntlArray = spei_pearson_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_36_YYYYMMDD_Of_PrcntlArray = spei_pearson_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_48_YYYYMMDD_Of_PrcntlArray = spei_pearson_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_60_YYYYMMDD_Of_PrcntlArray = spei_pearson_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spei_pearson_72_YYYYMMDD_Of_PrcntlArray = spei_pearson_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_spi_gamma_01_YYYYMMDD_Of_PrcntlArray = spi_gamma_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_02_YYYYMMDD_Of_PrcntlArray = spi_gamma_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_03_YYYYMMDD_Of_PrcntlArray = spi_gamma_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_06_YYYYMMDD_Of_PrcntlArray = spi_gamma_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_09_YYYYMMDD_Of_PrcntlArray = spi_gamma_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_12_YYYYMMDD_Of_PrcntlArray = spi_gamma_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_24_YYYYMMDD_Of_PrcntlArray = spi_gamma_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_36_YYYYMMDD_Of_PrcntlArray = spi_gamma_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_48_YYYYMMDD_Of_PrcntlArray = spi_gamma_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_60_YYYYMMDD_Of_PrcntlArray = spi_gamma_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_gamma_72_YYYYMMDD_Of_PrcntlArray = spi_gamma_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_spi_pearson_01_YYYYMMDD_Of_PrcntlArray = spi_pearson_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_02_YYYYMMDD_Of_PrcntlArray = spi_pearson_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_03_YYYYMMDD_Of_PrcntlArray = spi_pearson_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_06_YYYYMMDD_Of_PrcntlArray = spi_pearson_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_09_YYYYMMDD_Of_PrcntlArray = spi_pearson_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_12_YYYYMMDD_Of_PrcntlArray = spi_pearson_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_24_YYYYMMDD_Of_PrcntlArray = spi_pearson_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_36_YYYYMMDD_Of_PrcntlArray = spi_pearson_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_48_YYYYMMDD_Of_PrcntlArray = spi_pearson_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_60_YYYYMMDD_Of_PrcntlArray = spi_pearson_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_spi_pearson_72_YYYYMMDD_Of_PrcntlArray = spi_pearson_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_pet_01_YYYYMMDD_Of_PrcntlArray = pet_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_02_YYYYMMDD_Of_PrcntlArray = pet_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_03_YYYYMMDD_Of_PrcntlArray = pet_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_06_YYYYMMDD_Of_PrcntlArray = pet_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_09_YYYYMMDD_Of_PrcntlArray = pet_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_12_YYYYMMDD_Of_PrcntlArray = pet_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_24_YYYYMMDD_Of_PrcntlArray = pet_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_36_YYYYMMDD_Of_PrcntlArray = pet_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_48_YYYYMMDD_Of_PrcntlArray = pet_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_60_YYYYMMDD_Of_PrcntlArray = pet_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_pet_72_YYYYMMDD_Of_PrcntlArray = pet_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_prcp_01_YYYYMMDD_Of_PrcntlArray = prcp_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_02_YYYYMMDD_Of_PrcntlArray = prcp_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_03_YYYYMMDD_Of_PrcntlArray = prcp_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_06_YYYYMMDD_Of_PrcntlArray = prcp_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_09_YYYYMMDD_Of_PrcntlArray = prcp_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_12_YYYYMMDD_Of_PrcntlArray = prcp_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_24_YYYYMMDD_Of_PrcntlArray = prcp_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_36_YYYYMMDD_Of_PrcntlArray = prcp_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_48_YYYYMMDD_Of_PrcntlArray = prcp_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_60_YYYYMMDD_Of_PrcntlArray = prcp_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_prcp_72_YYYYMMDD_Of_PrcntlArray = prcp_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_tavg_01_YYYYMMDD_Of_PrcntlArray = tavg_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_02_YYYYMMDD_Of_PrcntlArray = tavg_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_03_YYYYMMDD_Of_PrcntlArray = tavg_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_06_YYYYMMDD_Of_PrcntlArray = tavg_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_09_YYYYMMDD_Of_PrcntlArray = tavg_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_12_YYYYMMDD_Of_PrcntlArray = tavg_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_24_YYYYMMDD_Of_PrcntlArray = tavg_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_36_YYYYMMDD_Of_PrcntlArray = tavg_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_48_YYYYMMDD_Of_PrcntlArray = tavg_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_60_YYYYMMDD_Of_PrcntlArray = tavg_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tavg_72_YYYYMMDD_Of_PrcntlArray = tavg_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_tmax_01_YYYYMMDD_Of_PrcntlArray = tmax_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_02_YYYYMMDD_Of_PrcntlArray = tmax_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_03_YYYYMMDD_Of_PrcntlArray = tmax_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_06_YYYYMMDD_Of_PrcntlArray = tmax_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_09_YYYYMMDD_Of_PrcntlArray = tmax_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_12_YYYYMMDD_Of_PrcntlArray = tmax_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_24_YYYYMMDD_Of_PrcntlArray = tmax_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_36_YYYYMMDD_Of_PrcntlArray = tmax_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_48_YYYYMMDD_Of_PrcntlArray = tmax_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_60_YYYYMMDD_Of_PrcntlArray = tmax_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_tmax_72_YYYYMMDD_Of_PrcntlArray = tmax_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_spei_gamma_01_PrcntlArray = spei_gamma_01_PrcntlArray[::2]
Dev_spei_gamma_02_PrcntlArray = spei_gamma_02_PrcntlArray[::2]
Dev_spei_gamma_03_PrcntlArray = spei_gamma_03_PrcntlArray[::2]
Dev_spei_gamma_06_PrcntlArray = spei_gamma_06_PrcntlArray[::2]
Dev_spei_gamma_09_PrcntlArray = spei_gamma_09_PrcntlArray[::2]
Dev_spei_gamma_12_PrcntlArray = spei_gamma_12_PrcntlArray[::2]
Dev_spei_gamma_24_PrcntlArray = spei_gamma_24_PrcntlArray[::2]
Dev_spei_gamma_36_PrcntlArray = spei_gamma_36_PrcntlArray[::2]
Dev_spei_gamma_48_PrcntlArray = spei_gamma_48_PrcntlArray[::2]
Dev_spei_gamma_60_PrcntlArray = spei_gamma_60_PrcntlArray[::2]
Dev_spei_gamma_72_PrcntlArray = spei_gamma_72_PrcntlArray[::2]

Dev_spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray[::2]
Dev_spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray[::2]
Dev_spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray[::2]
Dev_spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray[::2]
Dev_spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray[::2]
Dev_spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray[::2]
Dev_spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray[::2]
Dev_spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray[::2]
Dev_spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray[::2]
Dev_spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray[::2]
Dev_spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray[::2]

Dev_spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray[::2]
Dev_spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray[::2]
Dev_spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray[::2]
Dev_spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray[::2]
Dev_spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray[::2]
Dev_spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray[::2]
Dev_spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray[::2]
Dev_spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray[::2]
Dev_spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray[::2]
Dev_spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray[::2]
Dev_spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray[::2]

Dev_spi_pearson_01_PrcntlArray = spi_pearson_01_PrcntlArray[::2]
Dev_spi_pearson_02_PrcntlArray = spi_pearson_02_PrcntlArray[::2]
Dev_spi_pearson_03_PrcntlArray = spi_pearson_03_PrcntlArray[::2]
Dev_spi_pearson_06_PrcntlArray = spi_pearson_06_PrcntlArray[::2]
Dev_spi_pearson_09_PrcntlArray = spi_pearson_09_PrcntlArray[::2]
Dev_spi_pearson_12_PrcntlArray = spi_pearson_12_PrcntlArray[::2]
Dev_spi_pearson_24_PrcntlArray = spi_pearson_24_PrcntlArray[::2]
Dev_spi_pearson_36_PrcntlArray = spi_pearson_36_PrcntlArray[::2]
Dev_spi_pearson_48_PrcntlArray = spi_pearson_48_PrcntlArray[::2]
Dev_spi_pearson_60_PrcntlArray = spi_pearson_60_PrcntlArray[::2]
Dev_spi_pearson_72_PrcntlArray = spi_pearson_72_PrcntlArray[::2]

Dev_pet_01_PrcntlArray = pet_01_PrcntlArray[::2]
Dev_pet_02_PrcntlArray = pet_02_PrcntlArray[::2]
Dev_pet_03_PrcntlArray = pet_03_PrcntlArray[::2]
Dev_pet_06_PrcntlArray = pet_06_PrcntlArray[::2]
Dev_pet_09_PrcntlArray = pet_09_PrcntlArray[::2]
Dev_pet_12_PrcntlArray = pet_12_PrcntlArray[::2]
Dev_pet_24_PrcntlArray = pet_24_PrcntlArray[::2]
Dev_pet_36_PrcntlArray = pet_36_PrcntlArray[::2]
Dev_pet_48_PrcntlArray = pet_48_PrcntlArray[::2]
Dev_pet_60_PrcntlArray = pet_60_PrcntlArray[::2]
Dev_pet_72_PrcntlArray = pet_72_PrcntlArray[::2]

Dev_prcp_01_PrcntlArray = prcp_01_PrcntlArray[::2]
Dev_prcp_02_PrcntlArray = prcp_02_PrcntlArray[::2]
Dev_prcp_03_PrcntlArray = prcp_03_PrcntlArray[::2]
Dev_prcp_06_PrcntlArray = prcp_06_PrcntlArray[::2]
Dev_prcp_09_PrcntlArray = prcp_09_PrcntlArray[::2]
Dev_prcp_12_PrcntlArray = prcp_12_PrcntlArray[::2]
Dev_prcp_24_PrcntlArray = prcp_24_PrcntlArray[::2]
Dev_prcp_36_PrcntlArray = prcp_36_PrcntlArray[::2]
Dev_prcp_48_PrcntlArray = prcp_48_PrcntlArray[::2]
Dev_prcp_60_PrcntlArray = prcp_60_PrcntlArray[::2]
Dev_prcp_72_PrcntlArray = prcp_72_PrcntlArray[::2]

Dev_tavg_01_PrcntlArray = tavg_01_PrcntlArray[::2]
Dev_tavg_02_PrcntlArray = tavg_02_PrcntlArray[::2]
Dev_tavg_03_PrcntlArray = tavg_03_PrcntlArray[::2]
Dev_tavg_06_PrcntlArray = tavg_06_PrcntlArray[::2]
Dev_tavg_09_PrcntlArray = tavg_09_PrcntlArray[::2]
Dev_tavg_12_PrcntlArray = tavg_12_PrcntlArray[::2]
Dev_tavg_24_PrcntlArray = tavg_24_PrcntlArray[::2]
Dev_tavg_36_PrcntlArray = tavg_36_PrcntlArray[::2]
Dev_tavg_48_PrcntlArray = tavg_48_PrcntlArray[::2]
Dev_tavg_60_PrcntlArray = tavg_60_PrcntlArray[::2]
Dev_tavg_72_PrcntlArray = tavg_72_PrcntlArray[::2]

Dev_tmax_01_PrcntlArray = tmax_01_PrcntlArray[::2]
Dev_tmax_02_PrcntlArray = tmax_02_PrcntlArray[::2]
Dev_tmax_03_PrcntlArray = tmax_03_PrcntlArray[::2]
Dev_tmax_06_PrcntlArray = tmax_06_PrcntlArray[::2]
Dev_tmax_09_PrcntlArray = tmax_09_PrcntlArray[::2]
Dev_tmax_12_PrcntlArray = tmax_12_PrcntlArray[::2]
Dev_tmax_24_PrcntlArray = tmax_24_PrcntlArray[::2]
Dev_tmax_36_PrcntlArray = tmax_36_PrcntlArray[::2]
Dev_tmax_48_PrcntlArray = tmax_48_PrcntlArray[::2]
Dev_tmax_60_PrcntlArray = tmax_60_PrcntlArray[::2]
Dev_tmax_72_PrcntlArray = tmax_72_PrcntlArray[::2]

Test_spei_gamma_01_YYYYMMDD_Of_PrcntlArray = spei_gamma_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_02_YYYYMMDD_Of_PrcntlArray = spei_gamma_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_03_YYYYMMDD_Of_PrcntlArray = spei_gamma_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_06_YYYYMMDD_Of_PrcntlArray = spei_gamma_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_09_YYYYMMDD_Of_PrcntlArray = spei_gamma_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_12_YYYYMMDD_Of_PrcntlArray = spei_gamma_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_24_YYYYMMDD_Of_PrcntlArray = spei_gamma_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_36_YYYYMMDD_Of_PrcntlArray = spei_gamma_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_48_YYYYMMDD_Of_PrcntlArray = spei_gamma_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_60_YYYYMMDD_Of_PrcntlArray = spei_gamma_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_gamma_72_YYYYMMDD_Of_PrcntlArray = spei_gamma_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_spei_pearson_01_YYYYMMDD_Of_PrcntlArray = spei_pearson_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_02_YYYYMMDD_Of_PrcntlArray = spei_pearson_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_03_YYYYMMDD_Of_PrcntlArray = spei_pearson_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_06_YYYYMMDD_Of_PrcntlArray = spei_pearson_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_09_YYYYMMDD_Of_PrcntlArray = spei_pearson_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_12_YYYYMMDD_Of_PrcntlArray = spei_pearson_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_24_YYYYMMDD_Of_PrcntlArray = spei_pearson_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_36_YYYYMMDD_Of_PrcntlArray = spei_pearson_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_48_YYYYMMDD_Of_PrcntlArray = spei_pearson_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_60_YYYYMMDD_Of_PrcntlArray = spei_pearson_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spei_pearson_72_YYYYMMDD_Of_PrcntlArray = spei_pearson_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_spi_gamma_01_YYYYMMDD_Of_PrcntlArray = spi_gamma_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_02_YYYYMMDD_Of_PrcntlArray = spi_gamma_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_03_YYYYMMDD_Of_PrcntlArray = spi_gamma_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_06_YYYYMMDD_Of_PrcntlArray = spi_gamma_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_09_YYYYMMDD_Of_PrcntlArray = spi_gamma_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_12_YYYYMMDD_Of_PrcntlArray = spi_gamma_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_24_YYYYMMDD_Of_PrcntlArray = spi_gamma_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_36_YYYYMMDD_Of_PrcntlArray = spi_gamma_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_48_YYYYMMDD_Of_PrcntlArray = spi_gamma_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_60_YYYYMMDD_Of_PrcntlArray = spi_gamma_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_gamma_72_YYYYMMDD_Of_PrcntlArray = spi_gamma_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_spi_pearson_01_YYYYMMDD_Of_PrcntlArray = spi_pearson_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_02_YYYYMMDD_Of_PrcntlArray = spi_pearson_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_03_YYYYMMDD_Of_PrcntlArray = spi_pearson_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_06_YYYYMMDD_Of_PrcntlArray = spi_pearson_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_09_YYYYMMDD_Of_PrcntlArray = spi_pearson_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_12_YYYYMMDD_Of_PrcntlArray = spi_pearson_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_24_YYYYMMDD_Of_PrcntlArray = spi_pearson_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_36_YYYYMMDD_Of_PrcntlArray = spi_pearson_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_48_YYYYMMDD_Of_PrcntlArray = spi_pearson_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_60_YYYYMMDD_Of_PrcntlArray = spi_pearson_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_spi_pearson_72_YYYYMMDD_Of_PrcntlArray = spi_pearson_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_pet_01_YYYYMMDD_Of_PrcntlArray = pet_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_02_YYYYMMDD_Of_PrcntlArray = pet_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_03_YYYYMMDD_Of_PrcntlArray = pet_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_06_YYYYMMDD_Of_PrcntlArray = pet_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_09_YYYYMMDD_Of_PrcntlArray = pet_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_12_YYYYMMDD_Of_PrcntlArray = pet_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_24_YYYYMMDD_Of_PrcntlArray = pet_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_36_YYYYMMDD_Of_PrcntlArray = pet_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_48_YYYYMMDD_Of_PrcntlArray = pet_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_60_YYYYMMDD_Of_PrcntlArray = pet_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_pet_72_YYYYMMDD_Of_PrcntlArray = pet_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_prcp_01_YYYYMMDD_Of_PrcntlArray = prcp_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_02_YYYYMMDD_Of_PrcntlArray = prcp_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_03_YYYYMMDD_Of_PrcntlArray = prcp_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_06_YYYYMMDD_Of_PrcntlArray = prcp_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_09_YYYYMMDD_Of_PrcntlArray = prcp_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_12_YYYYMMDD_Of_PrcntlArray = prcp_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_24_YYYYMMDD_Of_PrcntlArray = prcp_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_36_YYYYMMDD_Of_PrcntlArray = prcp_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_48_YYYYMMDD_Of_PrcntlArray = prcp_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_60_YYYYMMDD_Of_PrcntlArray = prcp_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_prcp_72_YYYYMMDD_Of_PrcntlArray = prcp_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_tavg_01_YYYYMMDD_Of_PrcntlArray = tavg_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_02_YYYYMMDD_Of_PrcntlArray = tavg_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_03_YYYYMMDD_Of_PrcntlArray = tavg_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_06_YYYYMMDD_Of_PrcntlArray = tavg_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_09_YYYYMMDD_Of_PrcntlArray = tavg_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_12_YYYYMMDD_Of_PrcntlArray = tavg_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_24_YYYYMMDD_Of_PrcntlArray = tavg_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_36_YYYYMMDD_Of_PrcntlArray = tavg_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_48_YYYYMMDD_Of_PrcntlArray = tavg_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_60_YYYYMMDD_Of_PrcntlArray = tavg_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tavg_72_YYYYMMDD_Of_PrcntlArray = tavg_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_tmax_01_YYYYMMDD_Of_PrcntlArray = tmax_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_02_YYYYMMDD_Of_PrcntlArray = tmax_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_03_YYYYMMDD_Of_PrcntlArray = tmax_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_06_YYYYMMDD_Of_PrcntlArray = tmax_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_09_YYYYMMDD_Of_PrcntlArray = tmax_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_12_YYYYMMDD_Of_PrcntlArray = tmax_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_24_YYYYMMDD_Of_PrcntlArray = tmax_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_36_YYYYMMDD_Of_PrcntlArray = tmax_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_48_YYYYMMDD_Of_PrcntlArray = tmax_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_60_YYYYMMDD_Of_PrcntlArray = tmax_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_tmax_72_YYYYMMDD_Of_PrcntlArray = tmax_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_spei_gamma_01_PrcntlArray = spei_gamma_01_PrcntlArray[1::2]
Test_spei_gamma_02_PrcntlArray = spei_gamma_02_PrcntlArray[1::2]
Test_spei_gamma_03_PrcntlArray = spei_gamma_03_PrcntlArray[1::2]
Test_spei_gamma_06_PrcntlArray = spei_gamma_06_PrcntlArray[1::2]
Test_spei_gamma_09_PrcntlArray = spei_gamma_09_PrcntlArray[1::2]
Test_spei_gamma_12_PrcntlArray = spei_gamma_12_PrcntlArray[1::2]
Test_spei_gamma_24_PrcntlArray = spei_gamma_24_PrcntlArray[1::2]
Test_spei_gamma_36_PrcntlArray = spei_gamma_36_PrcntlArray[1::2]
Test_spei_gamma_48_PrcntlArray = spei_gamma_48_PrcntlArray[1::2]
Test_spei_gamma_60_PrcntlArray = spei_gamma_60_PrcntlArray[1::2]
Test_spei_gamma_72_PrcntlArray = spei_gamma_72_PrcntlArray[1::2]

Test_spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray[1::2]
Test_spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray[1::2]
Test_spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray[1::2]
Test_spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray[1::2]
Test_spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray[1::2]
Test_spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray[1::2]
Test_spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray[1::2]
Test_spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray[1::2]
Test_spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray[1::2]
Test_spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray[1::2]
Test_spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray[1::2]

Test_spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray[1::2]
Test_spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray[1::2]
Test_spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray[1::2]
Test_spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray[1::2]
Test_spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray[1::2]
Test_spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray[1::2]
Test_spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray[1::2]
Test_spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray[1::2]
Test_spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray[1::2]
Test_spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray[1::2]
Test_spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray[1::2]

Test_spi_pearson_01_PrcntlArray = spi_pearson_01_PrcntlArray[1::2]
Test_spi_pearson_02_PrcntlArray = spi_pearson_02_PrcntlArray[1::2]
Test_spi_pearson_03_PrcntlArray = spi_pearson_03_PrcntlArray[1::2]
Test_spi_pearson_06_PrcntlArray = spi_pearson_06_PrcntlArray[1::2]
Test_spi_pearson_09_PrcntlArray = spi_pearson_09_PrcntlArray[1::2]
Test_spi_pearson_12_PrcntlArray = spi_pearson_12_PrcntlArray[1::2]
Test_spi_pearson_24_PrcntlArray = spi_pearson_24_PrcntlArray[1::2]
Test_spi_pearson_36_PrcntlArray = spi_pearson_36_PrcntlArray[1::2]
Test_spi_pearson_48_PrcntlArray = spi_pearson_48_PrcntlArray[1::2]
Test_spi_pearson_60_PrcntlArray = spi_pearson_60_PrcntlArray[1::2]
Test_spi_pearson_72_PrcntlArray = spi_pearson_72_PrcntlArray[1::2]

Test_pet_01_PrcntlArray = pet_01_PrcntlArray[1::2]
Test_pet_02_PrcntlArray = pet_02_PrcntlArray[1::2]
Test_pet_03_PrcntlArray = pet_03_PrcntlArray[1::2]
Test_pet_06_PrcntlArray = pet_06_PrcntlArray[1::2]
Test_pet_09_PrcntlArray = pet_09_PrcntlArray[1::2]
Test_pet_12_PrcntlArray = pet_12_PrcntlArray[1::2]
Test_pet_24_PrcntlArray = pet_24_PrcntlArray[1::2]
Test_pet_36_PrcntlArray = pet_36_PrcntlArray[1::2]
Test_pet_48_PrcntlArray = pet_48_PrcntlArray[1::2]
Test_pet_60_PrcntlArray = pet_60_PrcntlArray[1::2]
Test_pet_72_PrcntlArray = pet_72_PrcntlArray[1::2]

Test_prcp_01_PrcntlArray = prcp_01_PrcntlArray[1::2]
Test_prcp_02_PrcntlArray = prcp_02_PrcntlArray[1::2]
Test_prcp_03_PrcntlArray = prcp_03_PrcntlArray[1::2]
Test_prcp_06_PrcntlArray = prcp_06_PrcntlArray[1::2]
Test_prcp_09_PrcntlArray = prcp_09_PrcntlArray[1::2]
Test_prcp_12_PrcntlArray = prcp_12_PrcntlArray[1::2]
Test_prcp_24_PrcntlArray = prcp_24_PrcntlArray[1::2]
Test_prcp_36_PrcntlArray = prcp_36_PrcntlArray[1::2]
Test_prcp_48_PrcntlArray = prcp_48_PrcntlArray[1::2]
Test_prcp_60_PrcntlArray = prcp_60_PrcntlArray[1::2]
Test_prcp_72_PrcntlArray = prcp_72_PrcntlArray[1::2]

Test_tavg_01_PrcntlArray = tavg_01_PrcntlArray[1::2]
Test_tavg_02_PrcntlArray = tavg_02_PrcntlArray[1::2]
Test_tavg_03_PrcntlArray = tavg_03_PrcntlArray[1::2]
Test_tavg_06_PrcntlArray = tavg_06_PrcntlArray[1::2]
Test_tavg_09_PrcntlArray = tavg_09_PrcntlArray[1::2]
Test_tavg_12_PrcntlArray = tavg_12_PrcntlArray[1::2]
Test_tavg_24_PrcntlArray = tavg_24_PrcntlArray[1::2]
Test_tavg_36_PrcntlArray = tavg_36_PrcntlArray[1::2]
Test_tavg_48_PrcntlArray = tavg_48_PrcntlArray[1::2]
Test_tavg_60_PrcntlArray = tavg_60_PrcntlArray[1::2]
Test_tavg_72_PrcntlArray = tavg_72_PrcntlArray[1::2]

Test_tmax_01_PrcntlArray = tmax_01_PrcntlArray[1::2]
Test_tmax_02_PrcntlArray = tmax_02_PrcntlArray[1::2]
Test_tmax_03_PrcntlArray = tmax_03_PrcntlArray[1::2]
Test_tmax_06_PrcntlArray = tmax_06_PrcntlArray[1::2]
Test_tmax_09_PrcntlArray = tmax_09_PrcntlArray[1::2]
Test_tmax_12_PrcntlArray = tmax_12_PrcntlArray[1::2]
Test_tmax_24_PrcntlArray = tmax_24_PrcntlArray[1::2]
Test_tmax_36_PrcntlArray = tmax_36_PrcntlArray[1::2]
Test_tmax_48_PrcntlArray = tmax_48_PrcntlArray[1::2]
Test_tmax_60_PrcntlArray = tmax_60_PrcntlArray[1::2]
Test_tmax_72_PrcntlArray = tmax_72_PrcntlArray[1::2]

print('Evaluation: Dev NumDates = ', Dev_spei_gamma_01_PrcntlArray.shape[0], ', NumSpatialUnits = ',Dev_spei_gamma_01_PrcntlArray.shape[1])

PrintInfoAboutArray(Dev_spei_gamma_01_PrcntlArray, 'Dev_spei_gamma_01_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_02_PrcntlArray, 'Dev_spei_gamma_02_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_03_PrcntlArray, 'Dev_spei_gamma_03_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_06_PrcntlArray, 'Dev_spei_gamma_06_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_09_PrcntlArray, 'Dev_spei_gamma_09_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_12_PrcntlArray, 'Dev_spei_gamma_12_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_24_PrcntlArray, 'Dev_spei_gamma_24_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_36_PrcntlArray, 'Dev_spei_gamma_36_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_48_PrcntlArray, 'Dev_spei_gamma_48_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_60_PrcntlArray, 'Dev_spei_gamma_60_PrcntlArray')
PrintInfoAboutArray(Dev_spei_gamma_72_PrcntlArray, 'Dev_spei_gamma_72_PrcntlArray')

PrintInfoAboutArray(Dev_spei_pearson_01_PrcntlArray, 'Dev_spei_pearson_01_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_02_PrcntlArray, 'Dev_spei_pearson_02_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_03_PrcntlArray, 'Dev_spei_pearson_03_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_06_PrcntlArray, 'Dev_spei_pearson_06_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_09_PrcntlArray, 'Dev_spei_pearson_09_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_12_PrcntlArray, 'Dev_spei_pearson_12_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_24_PrcntlArray, 'Dev_spei_pearson_24_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_36_PrcntlArray, 'Dev_spei_pearson_36_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_48_PrcntlArray, 'Dev_spei_pearson_48_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_60_PrcntlArray, 'Dev_spei_pearson_60_PrcntlArray')
PrintInfoAboutArray(Dev_spei_pearson_72_PrcntlArray, 'Dev_spei_pearson_72_PrcntlArray')

PrintInfoAboutArray(Dev_spi_gamma_01_PrcntlArray, 'Dev_spi_gamma_01_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_02_PrcntlArray, 'Dev_spi_gamma_02_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_03_PrcntlArray, 'Dev_spi_gamma_03_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_06_PrcntlArray, 'Dev_spi_gamma_06_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_09_PrcntlArray, 'Dev_spi_gamma_09_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_12_PrcntlArray, 'Dev_spi_gamma_12_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_24_PrcntlArray, 'Dev_spi_gamma_24_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_36_PrcntlArray, 'Dev_spi_gamma_36_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_48_PrcntlArray, 'Dev_spi_gamma_48_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_60_PrcntlArray, 'Dev_spi_gamma_60_PrcntlArray')
PrintInfoAboutArray(Dev_spi_gamma_72_PrcntlArray, 'Dev_spi_gamma_72_PrcntlArray')

PrintInfoAboutArray(Dev_spi_pearson_01_PrcntlArray, 'Dev_spi_pearson_01_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_02_PrcntlArray, 'Dev_spi_pearson_02_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_03_PrcntlArray, 'Dev_spi_pearson_03_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_06_PrcntlArray, 'Dev_spi_pearson_06_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_09_PrcntlArray, 'Dev_spi_pearson_09_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_12_PrcntlArray, 'Dev_spi_pearson_12_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_24_PrcntlArray, 'Dev_spi_pearson_24_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_36_PrcntlArray, 'Dev_spi_pearson_36_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_48_PrcntlArray, 'Dev_spi_pearson_48_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_60_PrcntlArray, 'Dev_spi_pearson_60_PrcntlArray')
PrintInfoAboutArray(Dev_spi_pearson_72_PrcntlArray, 'Dev_spi_pearson_72_PrcntlArray')

PrintInfoAboutArray(Dev_pet_01_PrcntlArray, 'Dev_pet_01_PrcntlArray')
PrintInfoAboutArray(Dev_pet_02_PrcntlArray, 'Dev_pet_02_PrcntlArray')
PrintInfoAboutArray(Dev_pet_03_PrcntlArray, 'Dev_pet_03_PrcntlArray')
PrintInfoAboutArray(Dev_pet_06_PrcntlArray, 'Dev_pet_06_PrcntlArray')
PrintInfoAboutArray(Dev_pet_09_PrcntlArray, 'Dev_pet_09_PrcntlArray')
PrintInfoAboutArray(Dev_pet_12_PrcntlArray, 'Dev_pet_12_PrcntlArray')
PrintInfoAboutArray(Dev_pet_24_PrcntlArray, 'Dev_pet_24_PrcntlArray')
PrintInfoAboutArray(Dev_pet_36_PrcntlArray, 'Dev_pet_36_PrcntlArray')
PrintInfoAboutArray(Dev_pet_48_PrcntlArray, 'Dev_pet_48_PrcntlArray')
PrintInfoAboutArray(Dev_pet_60_PrcntlArray, 'Dev_pet_60_PrcntlArray')
PrintInfoAboutArray(Dev_pet_72_PrcntlArray, 'Dev_pet_72_PrcntlArray')

PrintInfoAboutArray(Dev_prcp_01_PrcntlArray, 'Dev_prcp_01_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_02_PrcntlArray, 'Dev_prcp_02_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_03_PrcntlArray, 'Dev_prcp_03_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_06_PrcntlArray, 'Dev_prcp_06_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_09_PrcntlArray, 'Dev_prcp_09_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_12_PrcntlArray, 'Dev_prcp_12_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_24_PrcntlArray, 'Dev_prcp_24_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_36_PrcntlArray, 'Dev_prcp_36_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_48_PrcntlArray, 'Dev_prcp_48_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_60_PrcntlArray, 'Dev_prcp_60_PrcntlArray')
PrintInfoAboutArray(Dev_prcp_72_PrcntlArray, 'Dev_prcp_72_PrcntlArray')

PrintInfoAboutArray(Dev_tavg_01_PrcntlArray, 'Dev_tavg_01_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_02_PrcntlArray, 'Dev_tavg_02_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_03_PrcntlArray, 'Dev_tavg_03_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_06_PrcntlArray, 'Dev_tavg_06_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_09_PrcntlArray, 'Dev_tavg_09_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_12_PrcntlArray, 'Dev_tavg_12_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_24_PrcntlArray, 'Dev_tavg_24_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_36_PrcntlArray, 'Dev_tavg_36_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_48_PrcntlArray, 'Dev_tavg_48_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_60_PrcntlArray, 'Dev_tavg_60_PrcntlArray')
PrintInfoAboutArray(Dev_tavg_72_PrcntlArray, 'Dev_tavg_72_PrcntlArray')

PrintInfoAboutArray(Dev_tmax_01_PrcntlArray, 'Dev_tmax_01_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_02_PrcntlArray, 'Dev_tmax_02_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_03_PrcntlArray, 'Dev_tmax_03_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_06_PrcntlArray, 'Dev_tmax_06_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_09_PrcntlArray, 'Dev_tmax_09_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_12_PrcntlArray, 'Dev_tmax_12_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_24_PrcntlArray, 'Dev_tmax_24_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_36_PrcntlArray, 'Dev_tmax_36_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_48_PrcntlArray, 'Dev_tmax_48_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_60_PrcntlArray, 'Dev_tmax_60_PrcntlArray')
PrintInfoAboutArray(Dev_tmax_72_PrcntlArray, 'Dev_tmax_72_PrcntlArray')

print('Evaluation: Test NumDates = ', Test_spei_gamma_01_PrcntlArray.shape[0], ', NumSpatialUnits = ',Test_spei_gamma_01_PrcntlArray.shape[1])

PrintInfoAboutArray(Test_spei_gamma_01_PrcntlArray, 'Test_spei_gamma_01_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_02_PrcntlArray, 'Test_spei_gamma_02_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_03_PrcntlArray, 'Test_spei_gamma_03_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_06_PrcntlArray, 'Test_spei_gamma_06_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_09_PrcntlArray, 'Test_spei_gamma_09_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_12_PrcntlArray, 'Test_spei_gamma_12_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_24_PrcntlArray, 'Test_spei_gamma_24_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_36_PrcntlArray, 'Test_spei_gamma_36_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_48_PrcntlArray, 'Test_spei_gamma_48_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_60_PrcntlArray, 'Test_spei_gamma_60_PrcntlArray')
PrintInfoAboutArray(Test_spei_gamma_72_PrcntlArray, 'Test_spei_gamma_72_PrcntlArray')

PrintInfoAboutArray(Test_spei_pearson_01_PrcntlArray, 'Test_spei_pearson_01_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_02_PrcntlArray, 'Test_spei_pearson_02_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_03_PrcntlArray, 'Test_spei_pearson_03_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_06_PrcntlArray, 'Test_spei_pearson_06_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_09_PrcntlArray, 'Test_spei_pearson_09_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_12_PrcntlArray, 'Test_spei_pearson_12_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_24_PrcntlArray, 'Test_spei_pearson_24_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_36_PrcntlArray, 'Test_spei_pearson_36_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_48_PrcntlArray, 'Test_spei_pearson_48_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_60_PrcntlArray, 'Test_spei_pearson_60_PrcntlArray')
PrintInfoAboutArray(Test_spei_pearson_72_PrcntlArray, 'Test_spei_pearson_72_PrcntlArray')

PrintInfoAboutArray(Test_spi_gamma_01_PrcntlArray, 'Test_spi_gamma_01_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_02_PrcntlArray, 'Test_spi_gamma_02_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_03_PrcntlArray, 'Test_spi_gamma_03_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_06_PrcntlArray, 'Test_spi_gamma_06_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_09_PrcntlArray, 'Test_spi_gamma_09_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_12_PrcntlArray, 'Test_spi_gamma_12_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_24_PrcntlArray, 'Test_spi_gamma_24_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_36_PrcntlArray, 'Test_spi_gamma_36_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_48_PrcntlArray, 'Test_spi_gamma_48_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_60_PrcntlArray, 'Test_spi_gamma_60_PrcntlArray')
PrintInfoAboutArray(Test_spi_gamma_72_PrcntlArray, 'Test_spi_gamma_72_PrcntlArray')

PrintInfoAboutArray(Test_spi_pearson_01_PrcntlArray, 'Test_spi_pearson_01_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_02_PrcntlArray, 'Test_spi_pearson_02_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_03_PrcntlArray, 'Test_spi_pearson_03_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_06_PrcntlArray, 'Test_spi_pearson_06_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_09_PrcntlArray, 'Test_spi_pearson_09_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_12_PrcntlArray, 'Test_spi_pearson_12_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_24_PrcntlArray, 'Test_spi_pearson_24_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_36_PrcntlArray, 'Test_spi_pearson_36_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_48_PrcntlArray, 'Test_spi_pearson_48_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_60_PrcntlArray, 'Test_spi_pearson_60_PrcntlArray')
PrintInfoAboutArray(Test_spi_pearson_72_PrcntlArray, 'Test_spi_pearson_72_PrcntlArray')

PrintInfoAboutArray(Test_pet_01_PrcntlArray, 'Test_pet_01_PrcntlArray')
PrintInfoAboutArray(Test_pet_02_PrcntlArray, 'Test_pet_02_PrcntlArray')
PrintInfoAboutArray(Test_pet_03_PrcntlArray, 'Test_pet_03_PrcntlArray')
PrintInfoAboutArray(Test_pet_06_PrcntlArray, 'Test_pet_06_PrcntlArray')
PrintInfoAboutArray(Test_pet_09_PrcntlArray, 'Test_pet_09_PrcntlArray')
PrintInfoAboutArray(Test_pet_12_PrcntlArray, 'Test_pet_12_PrcntlArray')
PrintInfoAboutArray(Test_pet_24_PrcntlArray, 'Test_pet_24_PrcntlArray')
PrintInfoAboutArray(Test_pet_36_PrcntlArray, 'Test_pet_36_PrcntlArray')
PrintInfoAboutArray(Test_pet_48_PrcntlArray, 'Test_pet_48_PrcntlArray')
PrintInfoAboutArray(Test_pet_60_PrcntlArray, 'Test_pet_60_PrcntlArray')
PrintInfoAboutArray(Test_pet_72_PrcntlArray, 'Test_pet_72_PrcntlArray')

PrintInfoAboutArray(Test_prcp_01_PrcntlArray, 'Test_prcp_01_PrcntlArray')
PrintInfoAboutArray(Test_prcp_02_PrcntlArray, 'Test_prcp_02_PrcntlArray')
PrintInfoAboutArray(Test_prcp_03_PrcntlArray, 'Test_prcp_03_PrcntlArray')
PrintInfoAboutArray(Test_prcp_06_PrcntlArray, 'Test_prcp_06_PrcntlArray')
PrintInfoAboutArray(Test_prcp_09_PrcntlArray, 'Test_prcp_09_PrcntlArray')
PrintInfoAboutArray(Test_prcp_12_PrcntlArray, 'Test_prcp_12_PrcntlArray')
PrintInfoAboutArray(Test_prcp_24_PrcntlArray, 'Test_prcp_24_PrcntlArray')
PrintInfoAboutArray(Test_prcp_36_PrcntlArray, 'Test_prcp_36_PrcntlArray')
PrintInfoAboutArray(Test_prcp_48_PrcntlArray, 'Test_prcp_48_PrcntlArray')
PrintInfoAboutArray(Test_prcp_60_PrcntlArray, 'Test_prcp_60_PrcntlArray')
PrintInfoAboutArray(Test_prcp_72_PrcntlArray, 'Test_prcp_72_PrcntlArray')

PrintInfoAboutArray(Test_tavg_01_PrcntlArray, 'Test_tavg_01_PrcntlArray')
PrintInfoAboutArray(Test_tavg_02_PrcntlArray, 'Test_tavg_02_PrcntlArray')
PrintInfoAboutArray(Test_tavg_03_PrcntlArray, 'Test_tavg_03_PrcntlArray')
PrintInfoAboutArray(Test_tavg_06_PrcntlArray, 'Test_tavg_06_PrcntlArray')
PrintInfoAboutArray(Test_tavg_09_PrcntlArray, 'Test_tavg_09_PrcntlArray')
PrintInfoAboutArray(Test_tavg_12_PrcntlArray, 'Test_tavg_12_PrcntlArray')
PrintInfoAboutArray(Test_tavg_24_PrcntlArray, 'Test_tavg_24_PrcntlArray')
PrintInfoAboutArray(Test_tavg_36_PrcntlArray, 'Test_tavg_36_PrcntlArray')
PrintInfoAboutArray(Test_tavg_48_PrcntlArray, 'Test_tavg_48_PrcntlArray')
PrintInfoAboutArray(Test_tavg_60_PrcntlArray, 'Test_tavg_60_PrcntlArray')
PrintInfoAboutArray(Test_tavg_72_PrcntlArray, 'Test_tavg_72_PrcntlArray')

PrintInfoAboutArray(Test_tmax_01_PrcntlArray, 'Test_tmax_01_PrcntlArray')
PrintInfoAboutArray(Test_tmax_02_PrcntlArray, 'Test_tmax_02_PrcntlArray')
PrintInfoAboutArray(Test_tmax_03_PrcntlArray, 'Test_tmax_03_PrcntlArray')
PrintInfoAboutArray(Test_tmax_06_PrcntlArray, 'Test_tmax_06_PrcntlArray')
PrintInfoAboutArray(Test_tmax_09_PrcntlArray, 'Test_tmax_09_PrcntlArray')
PrintInfoAboutArray(Test_tmax_12_PrcntlArray, 'Test_tmax_12_PrcntlArray')
PrintInfoAboutArray(Test_tmax_24_PrcntlArray, 'Test_tmax_24_PrcntlArray')
PrintInfoAboutArray(Test_tmax_36_PrcntlArray, 'Test_tmax_36_PrcntlArray')
PrintInfoAboutArray(Test_tmax_48_PrcntlArray, 'Test_tmax_48_PrcntlArray')
PrintInfoAboutArray(Test_tmax_60_PrcntlArray, 'Test_tmax_60_PrcntlArray')
PrintInfoAboutArray(Test_tmax_72_PrcntlArray, 'Test_tmax_72_PrcntlArray')

np.savez_compressed(DevDataFilename, 
                    YYYYMMDD_Of_Array = Dev_spei_gamma_01_YYYYMMDD_Of_PrcntlArray, 
                    spei_gamma_01_PrcntlArray = Dev_spei_gamma_01_PrcntlArray, 
                    spei_gamma_02_PrcntlArray = Dev_spei_gamma_02_PrcntlArray, 
                    spei_gamma_03_PrcntlArray = Dev_spei_gamma_03_PrcntlArray, 
                    spei_gamma_06_PrcntlArray = Dev_spei_gamma_06_PrcntlArray, 
                    spei_gamma_09_PrcntlArray = Dev_spei_gamma_09_PrcntlArray, 
                    spei_gamma_24_PrcntlArray = Dev_spei_gamma_24_PrcntlArray, 
                    spei_gamma_12_PrcntlArray = Dev_spei_gamma_12_PrcntlArray, 
                    spei_gamma_36_PrcntlArray = Dev_spei_gamma_36_PrcntlArray, 
                    spei_gamma_48_PrcntlArray = Dev_spei_gamma_48_PrcntlArray, 
                    spei_gamma_60_PrcntlArray = Dev_spei_gamma_60_PrcntlArray, 
                    spei_gamma_72_PrcntlArray = Dev_spei_gamma_72_PrcntlArray,
                    spei_pearson_01_PrcntlArray = Dev_spei_pearson_01_PrcntlArray, 
                    spei_pearson_02_PrcntlArray = Dev_spei_pearson_02_PrcntlArray, 
                    spei_pearson_03_PrcntlArray = Dev_spei_pearson_03_PrcntlArray, 
                    spei_pearson_06_PrcntlArray = Dev_spei_pearson_06_PrcntlArray, 
                    spei_pearson_09_PrcntlArray = Dev_spei_pearson_09_PrcntlArray, 
                    spei_pearson_24_PrcntlArray = Dev_spei_pearson_24_PrcntlArray, 
                    spei_pearson_12_PrcntlArray = Dev_spei_pearson_12_PrcntlArray, 
                    spei_pearson_36_PrcntlArray = Dev_spei_pearson_36_PrcntlArray, 
                    spei_pearson_48_PrcntlArray = Dev_spei_pearson_48_PrcntlArray, 
                    spei_pearson_60_PrcntlArray = Dev_spei_pearson_60_PrcntlArray, 
                    spei_pearson_72_PrcntlArray = Dev_spei_pearson_72_PrcntlArray,
                    spi_gamma_01_PrcntlArray = Dev_spi_gamma_01_PrcntlArray, 
                    spi_gamma_02_PrcntlArray = Dev_spi_gamma_02_PrcntlArray, 
                    spi_gamma_03_PrcntlArray = Dev_spi_gamma_03_PrcntlArray, 
                    spi_gamma_06_PrcntlArray = Dev_spi_gamma_06_PrcntlArray, 
                    spi_gamma_09_PrcntlArray = Dev_spi_gamma_09_PrcntlArray, 
                    spi_gamma_24_PrcntlArray = Dev_spi_gamma_24_PrcntlArray, 
                    spi_gamma_12_PrcntlArray = Dev_spi_gamma_12_PrcntlArray, 
                    spi_gamma_36_PrcntlArray = Dev_spi_gamma_36_PrcntlArray, 
                    spi_gamma_48_PrcntlArray = Dev_spi_gamma_48_PrcntlArray, 
                    spi_gamma_60_PrcntlArray = Dev_spi_gamma_60_PrcntlArray, 
                    spi_gamma_72_PrcntlArray = Dev_spi_gamma_72_PrcntlArray,
                    spi_pearson_01_PrcntlArray = Dev_spi_pearson_01_PrcntlArray, 
                    spi_pearson_02_PrcntlArray = Dev_spi_pearson_02_PrcntlArray, 
                    spi_pearson_03_PrcntlArray = Dev_spi_pearson_03_PrcntlArray, 
                    spi_pearson_06_PrcntlArray = Dev_spi_pearson_06_PrcntlArray, 
                    spi_pearson_09_PrcntlArray = Dev_spi_pearson_09_PrcntlArray, 
                    spi_pearson_24_PrcntlArray = Dev_spi_pearson_24_PrcntlArray, 
                    spi_pearson_12_PrcntlArray = Dev_spi_pearson_12_PrcntlArray, 
                    spi_pearson_36_PrcntlArray = Dev_spi_pearson_36_PrcntlArray, 
                    spi_pearson_48_PrcntlArray = Dev_spi_pearson_48_PrcntlArray, 
                    spi_pearson_60_PrcntlArray = Dev_spi_pearson_60_PrcntlArray, 
                    spi_pearson_72_PrcntlArray = Dev_spi_pearson_72_PrcntlArray,
                    pet_01_PrcntlArray = Dev_pet_01_PrcntlArray, 
                    pet_02_PrcntlArray = Dev_pet_02_PrcntlArray, 
                    pet_03_PrcntlArray = Dev_pet_03_PrcntlArray, 
                    pet_06_PrcntlArray = Dev_pet_06_PrcntlArray, 
                    pet_09_PrcntlArray = Dev_pet_09_PrcntlArray, 
                    pet_24_PrcntlArray = Dev_pet_24_PrcntlArray, 
                    pet_12_PrcntlArray = Dev_pet_12_PrcntlArray, 
                    pet_36_PrcntlArray = Dev_pet_36_PrcntlArray, 
                    pet_48_PrcntlArray = Dev_pet_48_PrcntlArray, 
                    pet_60_PrcntlArray = Dev_pet_60_PrcntlArray, 
                    pet_72_PrcntlArray = Dev_pet_72_PrcntlArray,
                    prcp_01_PrcntlArray = Dev_prcp_01_PrcntlArray, 
                    prcp_02_PrcntlArray = Dev_prcp_02_PrcntlArray, 
                    prcp_03_PrcntlArray = Dev_prcp_03_PrcntlArray, 
                    prcp_06_PrcntlArray = Dev_prcp_06_PrcntlArray, 
                    prcp_09_PrcntlArray = Dev_prcp_09_PrcntlArray, 
                    prcp_24_PrcntlArray = Dev_prcp_24_PrcntlArray, 
                    prcp_12_PrcntlArray = Dev_prcp_12_PrcntlArray, 
                    prcp_36_PrcntlArray = Dev_prcp_36_PrcntlArray, 
                    prcp_48_PrcntlArray = Dev_prcp_48_PrcntlArray, 
                    prcp_60_PrcntlArray = Dev_prcp_60_PrcntlArray, 
                    prcp_72_PrcntlArray = Dev_prcp_72_PrcntlArray,
                    tavg_01_PrcntlArray = Dev_tavg_01_PrcntlArray, 
                    tavg_02_PrcntlArray = Dev_tavg_02_PrcntlArray, 
                    tavg_03_PrcntlArray = Dev_tavg_03_PrcntlArray, 
                    tavg_06_PrcntlArray = Dev_tavg_06_PrcntlArray, 
                    tavg_09_PrcntlArray = Dev_tavg_09_PrcntlArray, 
                    tavg_24_PrcntlArray = Dev_tavg_24_PrcntlArray, 
                    tavg_12_PrcntlArray = Dev_tavg_12_PrcntlArray, 
                    tavg_36_PrcntlArray = Dev_tavg_36_PrcntlArray, 
                    tavg_48_PrcntlArray = Dev_tavg_48_PrcntlArray, 
                    tavg_60_PrcntlArray = Dev_tavg_60_PrcntlArray, 
                    tavg_72_PrcntlArray = Dev_tavg_72_PrcntlArray,
                    tmax_01_PrcntlArray = Dev_tmax_01_PrcntlArray, 
                    tmax_02_PrcntlArray = Dev_tmax_02_PrcntlArray, 
                    tmax_03_PrcntlArray = Dev_tmax_03_PrcntlArray, 
                    tmax_06_PrcntlArray = Dev_tmax_06_PrcntlArray, 
                    tmax_09_PrcntlArray = Dev_tmax_09_PrcntlArray, 
                    tmax_24_PrcntlArray = Dev_tmax_24_PrcntlArray, 
                    tmax_12_PrcntlArray = Dev_tmax_12_PrcntlArray, 
                    tmax_36_PrcntlArray = Dev_tmax_36_PrcntlArray, 
                    tmax_48_PrcntlArray = Dev_tmax_48_PrcntlArray, 
                    tmax_60_PrcntlArray = Dev_tmax_60_PrcntlArray, 
                    tmax_72_PrcntlArray = Dev_tmax_72_PrcntlArray )

np.savez_compressed(TestDataFilename, 
                    YYYYMMDD_Of_Array = Test_spei_gamma_01_YYYYMMDD_Of_PrcntlArray, 
                    spei_gamma_01_PrcntlArray = Test_spei_gamma_01_PrcntlArray, 
                    spei_gamma_02_PrcntlArray = Test_spei_gamma_02_PrcntlArray, 
                    spei_gamma_03_PrcntlArray = Test_spei_gamma_03_PrcntlArray, 
                    spei_gamma_06_PrcntlArray = Test_spei_gamma_06_PrcntlArray, 
                    spei_gamma_09_PrcntlArray = Test_spei_gamma_09_PrcntlArray, 
                    spei_gamma_24_PrcntlArray = Test_spei_gamma_24_PrcntlArray, 
                    spei_gamma_12_PrcntlArray = Test_spei_gamma_12_PrcntlArray, 
                    spei_gamma_36_PrcntlArray = Test_spei_gamma_36_PrcntlArray, 
                    spei_gamma_48_PrcntlArray = Test_spei_gamma_48_PrcntlArray, 
                    spei_gamma_60_PrcntlArray = Test_spei_gamma_60_PrcntlArray, 
                    spei_gamma_72_PrcntlArray = Test_spei_gamma_72_PrcntlArray,
                    spei_pearson_01_PrcntlArray = Test_spei_pearson_01_PrcntlArray, 
                    spei_pearson_02_PrcntlArray = Test_spei_pearson_02_PrcntlArray, 
                    spei_pearson_03_PrcntlArray = Test_spei_pearson_03_PrcntlArray, 
                    spei_pearson_06_PrcntlArray = Test_spei_pearson_06_PrcntlArray, 
                    spei_pearson_09_PrcntlArray = Test_spei_pearson_09_PrcntlArray, 
                    spei_pearson_24_PrcntlArray = Test_spei_pearson_24_PrcntlArray, 
                    spei_pearson_12_PrcntlArray = Test_spei_pearson_12_PrcntlArray, 
                    spei_pearson_36_PrcntlArray = Test_spei_pearson_36_PrcntlArray, 
                    spei_pearson_48_PrcntlArray = Test_spei_pearson_48_PrcntlArray, 
                    spei_pearson_60_PrcntlArray = Test_spei_pearson_60_PrcntlArray, 
                    spei_pearson_72_PrcntlArray = Test_spei_pearson_72_PrcntlArray,
                    spi_gamma_01_PrcntlArray = Test_spi_gamma_01_PrcntlArray, 
                    spi_gamma_02_PrcntlArray = Test_spi_gamma_02_PrcntlArray, 
                    spi_gamma_03_PrcntlArray = Test_spi_gamma_03_PrcntlArray, 
                    spi_gamma_06_PrcntlArray = Test_spi_gamma_06_PrcntlArray, 
                    spi_gamma_09_PrcntlArray = Test_spi_gamma_09_PrcntlArray, 
                    spi_gamma_24_PrcntlArray = Test_spi_gamma_24_PrcntlArray, 
                    spi_gamma_12_PrcntlArray = Test_spi_gamma_12_PrcntlArray, 
                    spi_gamma_36_PrcntlArray = Test_spi_gamma_36_PrcntlArray, 
                    spi_gamma_48_PrcntlArray = Test_spi_gamma_48_PrcntlArray, 
                    spi_gamma_60_PrcntlArray = Test_spi_gamma_60_PrcntlArray, 
                    spi_gamma_72_PrcntlArray = Test_spi_gamma_72_PrcntlArray,
                    spi_pearson_01_PrcntlArray = Test_spi_pearson_01_PrcntlArray, 
                    spi_pearson_02_PrcntlArray = Test_spi_pearson_02_PrcntlArray, 
                    spi_pearson_03_PrcntlArray = Test_spi_pearson_03_PrcntlArray, 
                    spi_pearson_06_PrcntlArray = Test_spi_pearson_06_PrcntlArray, 
                    spi_pearson_09_PrcntlArray = Test_spi_pearson_09_PrcntlArray, 
                    spi_pearson_24_PrcntlArray = Test_spi_pearson_24_PrcntlArray, 
                    spi_pearson_12_PrcntlArray = Test_spi_pearson_12_PrcntlArray, 
                    spi_pearson_36_PrcntlArray = Test_spi_pearson_36_PrcntlArray, 
                    spi_pearson_48_PrcntlArray = Test_spi_pearson_48_PrcntlArray, 
                    spi_pearson_60_PrcntlArray = Test_spi_pearson_60_PrcntlArray, 
                    spi_pearson_72_PrcntlArray = Test_spi_pearson_72_PrcntlArray,
                    pet_01_PrcntlArray = Test_pet_01_PrcntlArray, 
                    pet_02_PrcntlArray = Test_pet_02_PrcntlArray, 
                    pet_03_PrcntlArray = Test_pet_03_PrcntlArray, 
                    pet_06_PrcntlArray = Test_pet_06_PrcntlArray, 
                    pet_09_PrcntlArray = Test_pet_09_PrcntlArray, 
                    pet_24_PrcntlArray = Test_pet_24_PrcntlArray, 
                    pet_12_PrcntlArray = Test_pet_12_PrcntlArray, 
                    pet_36_PrcntlArray = Test_pet_36_PrcntlArray, 
                    pet_48_PrcntlArray = Test_pet_48_PrcntlArray, 
                    pet_60_PrcntlArray = Test_pet_60_PrcntlArray, 
                    pet_72_PrcntlArray = Test_pet_72_PrcntlArray,
                    prcp_01_PrcntlArray = Test_prcp_01_PrcntlArray, 
                    prcp_02_PrcntlArray = Test_prcp_02_PrcntlArray, 
                    prcp_03_PrcntlArray = Test_prcp_03_PrcntlArray, 
                    prcp_06_PrcntlArray = Test_prcp_06_PrcntlArray, 
                    prcp_09_PrcntlArray = Test_prcp_09_PrcntlArray, 
                    prcp_24_PrcntlArray = Test_prcp_24_PrcntlArray, 
                    prcp_12_PrcntlArray = Test_prcp_12_PrcntlArray, 
                    prcp_36_PrcntlArray = Test_prcp_36_PrcntlArray, 
                    prcp_48_PrcntlArray = Test_prcp_48_PrcntlArray, 
                    prcp_60_PrcntlArray = Test_prcp_60_PrcntlArray, 
                    prcp_72_PrcntlArray = Test_prcp_72_PrcntlArray,
                    tavg_01_PrcntlArray = Test_tavg_01_PrcntlArray, 
                    tavg_02_PrcntlArray = Test_tavg_02_PrcntlArray, 
                    tavg_03_PrcntlArray = Test_tavg_03_PrcntlArray, 
                    tavg_06_PrcntlArray = Test_tavg_06_PrcntlArray, 
                    tavg_09_PrcntlArray = Test_tavg_09_PrcntlArray, 
                    tavg_24_PrcntlArray = Test_tavg_24_PrcntlArray, 
                    tavg_12_PrcntlArray = Test_tavg_12_PrcntlArray, 
                    tavg_36_PrcntlArray = Test_tavg_36_PrcntlArray, 
                    tavg_48_PrcntlArray = Test_tavg_48_PrcntlArray, 
                    tavg_60_PrcntlArray = Test_tavg_60_PrcntlArray, 
                    tavg_72_PrcntlArray = Test_tavg_72_PrcntlArray,
                    tmax_01_PrcntlArray = Test_tmax_01_PrcntlArray, 
                    tmax_02_PrcntlArray = Test_tmax_02_PrcntlArray, 
                    tmax_03_PrcntlArray = Test_tmax_03_PrcntlArray, 
                    tmax_06_PrcntlArray = Test_tmax_06_PrcntlArray, 
                    tmax_09_PrcntlArray = Test_tmax_09_PrcntlArray, 
                    tmax_24_PrcntlArray = Test_tmax_24_PrcntlArray, 
                    tmax_12_PrcntlArray = Test_tmax_12_PrcntlArray, 
                    tmax_36_PrcntlArray = Test_tmax_36_PrcntlArray, 
                    tmax_48_PrcntlArray = Test_tmax_48_PrcntlArray, 
                    tmax_60_PrcntlArray = Test_tmax_60_PrcntlArray, 
                    tmax_72_PrcntlArray = Test_tmax_72_PrcntlArray )

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



