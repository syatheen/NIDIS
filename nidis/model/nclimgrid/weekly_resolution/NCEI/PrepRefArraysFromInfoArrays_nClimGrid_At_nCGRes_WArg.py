#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Dec 18, 2022
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        WhichVariable
#ArgNum   1

# BEGIN code arguments / editable section

WhichVariable = sys.argv[1] # Choices are
       # 'spei-gamma-01', 'spei-gamma-02', 'spei-gamma-03', 'spei-gamma-06',
       # 'spei-gamma-09', 'spei-gamma-12', 'spei-gamma-24', 'spei-gamma-36',
       # 'spei-gamma-48', 'spei-gamma-60', 'spei-gamma-72',
       # 'spei-pearson-01', 'spei-pearson-02', 'spei-pearson-03', 'spei-pearson-06',
       # 'spei-pearson-09', 'spei-pearson-12', 'spei-pearson-24', 'spei-pearson-36',
       # 'spei-pearson-48', 'spei-pearson-60', 'spei-pearson-72',
       # 'spi-gamma-01', 'spi-gamma-02', 'spi-gamma-03', 'spi-gamma-06',
       # 'spi-gamma-09', 'spi-gamma-12', 'spi-gamma-24', 'spi-gamma-36',
       # 'spi-gamma-48', 'spi-gamma-60', 'spi-gamma-72',
       # 'spi-pearson-01', 'spi-pearson-02', 'spi-pearson-03', 'spi-pearson-06',
       # 'spi-pearson-09', 'spi-pearson-12', 'spi-pearson-24', 'spi-pearson-36',
       # 'spi-pearson-48', 'spi-pearson-60', 'spi-pearson-72',
       # 'pet-01', 'pet-02', 'pet-03', 'pet-06',
       # 'pet-09', 'pet-12', 'pet-24', 'pet-36',
       # 'pet-48', 'pet-60', 'pet-72',
       # 'prcp-01', 'prcp-02', 'prcp-03', 'prcp-06',
       # 'prcp-09', 'prcp-12', 'prcp-24', 'prcp-36',
       # 'prcp-48', 'prcp-60', 'prcp-72',
       # 'tavg-01', 'tavg-02', 'tavg-03', 'tavg-06',
       # 'tavg-09', 'tavg-12', 'tavg-24', 'tavg-36',
       # 'tavg-48', 'tavg-60', 'tavg-72',
       # 'tmax-01', 'tmax-02', 'tmax-03', 'tmax-06',
       # 'tmax-09', 'tmax-12', 'tmax-24', 'tmax-36',
       # 'tmax-48', 'tmax-60', 'tmax-72'

InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/'

if WhichVariable[-2:] == '01':
  nClimGrid_Info_BeginYYYYMM_List = [1895, 1] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '02':
  nClimGrid_Info_BeginYYYYMM_List = [1895, 2] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '03':
  nClimGrid_Info_BeginYYYYMM_List = [1895, 3] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '06':
  nClimGrid_Info_BeginYYYYMM_List = [1895, 6] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '09':
  nClimGrid_Info_BeginYYYYMM_List = [1895, 9] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '12':
  nClimGrid_Info_BeginYYYYMM_List = [1895, 12] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '24':
  nClimGrid_Info_BeginYYYYMM_List = [1896, 12] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '36':
  nClimGrid_Info_BeginYYYYMM_List = [1897, 12] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '48':
  nClimGrid_Info_BeginYYYYMM_List = [1898, 12] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '60':
  nClimGrid_Info_BeginYYYYMM_List = [1899, 12] # monthly mean, taken as valid on last of the month
elif WhichVariable[-2:] == '72':
  nClimGrid_Info_BeginYYYYMM_List = [1900, 12] # monthly mean, taken as valid on last of the month

nClimGrid_Info_EndYYYYMM_List = [2021, 7] # monthly mean, taken as valid on last of the month

if WhichVariable[-2:] == '01':
  nClimGrid_Ref_BeginDateVecList = [1895, 2, 5]  # nClimGrid_01 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '02':
  nClimGrid_Ref_BeginDateVecList = [1895, 3, 5]  # nClimGrid_02 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '03':
  nClimGrid_Ref_BeginDateVecList = [1895, 4, 2]  # nClimGrid_03 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '06':
  nClimGrid_Ref_BeginDateVecList = [1895, 7, 2]  # nClimGrid_06 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '09':
  nClimGrid_Ref_BeginDateVecList = [1895, 10, 1]  # nClimGrid_09 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '12':
  nClimGrid_Ref_BeginDateVecList = [1895, 12, 31]  # nClimGrid_12 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '24':
  nClimGrid_Ref_BeginDateVecList = [1897, 1, 5]  # nClimGrid_24 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '36':
  nClimGrid_Ref_BeginDateVecList = [1898, 1, 4]  # nClimGrid_36 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '48':
  nClimGrid_Ref_BeginDateVecList = [1899, 1, 3]  # nClimGrid_48 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '60':
  nClimGrid_Ref_BeginDateVecList = [1900, 1, 2]  # nClimGrid_60 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '72':
  nClimGrid_Ref_BeginDateVecList = [1901, 1, 1]  # nClimGrid_72 beginning year, month, day of month, this is also a Tuesday

nClimGrid_Ref_EndDateVecList = [2021, 7, 27]  # nClimGrid ending year, month, day of month, this is also a Tuesday

if WhichVariable == 'spei-gamma-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-gamma-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_gamma_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spei-pearson-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spei_pearson_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-gamma-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_gamma_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'spi-pearson-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_spi_pearson_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'pet-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_pet_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'prcp-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_prcp_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tavg-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tavg_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-01':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_01_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-02':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_02_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-03':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_03_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-06':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_06_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-09':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_09_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-12':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_12_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-24':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_24_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-36':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_36_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-48':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_48_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-60':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_60_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
elif WhichVariable == 'tmax-72':
  Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_tmax_72_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

nClimGrid_Ref_BeginDate = date(nClimGrid_Ref_BeginDateVecList[0], nClimGrid_Ref_BeginDateVecList[1], nClimGrid_Ref_BeginDateVecList[2])

nClimGrid_Ref_EndDate = date(nClimGrid_Ref_EndDateVecList[0], nClimGrid_Ref_EndDateVecList[1], nClimGrid_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays

if nClimGrid_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_Ref needs to be a Tuesday!!')
  sys.exit(0)

if nClimGrid_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for nClimGrid_Ref needs to be a Tuesday!!')
  sys.exit(0)

#END check whether the beginning and ending days are indeed Tuesdays

if nClimGrid_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

def ReadMeanFiles(FileName):
  ThisVariable_Info = np.load(FileName)
  ThisVariable_YYYYMM_Of_InfoArray = ThisVariable_Info['YYYYMM_Of_InfoArrayForPrcntl']
  ThisVariable_InfoArray = ThisVariable_Info['InfoArrayForPrcntl']
  return ThisVariable_YYYYMM_Of_InfoArray, ThisVariable_InfoArray
#end of def ReadMeanFiles(FileName)

if WhichVariable == 'pet-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet2MonthsMean_189502To202107.npz')
elif WhichVariable == 'pet-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet3MonthsMean_189503To202107.npz')
elif WhichVariable == 'pet-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet6MonthsMean_189506To202107.npz')
elif WhichVariable == 'pet-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet9MonthsMean_189509To202107.npz')
elif WhichVariable == 'pet-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet12MonthsMean_189512To202107.npz')
elif WhichVariable == 'pet-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet24MonthsMean_189612To202107.npz')
elif WhichVariable == 'pet-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet36MonthsMean_189712To202107.npz')
elif WhichVariable == 'pet-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet48MonthsMean_189812To202107.npz')
elif WhichVariable == 'pet-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet60MonthsMean_189912To202107.npz')
elif WhichVariable == 'pet-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/pet72MonthsMean_190012To202107.npz')
elif WhichVariable == 'prcp-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp2MonthsMean_189502To202107.npz')
elif WhichVariable == 'prcp-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp3MonthsMean_189503To202107.npz')
elif WhichVariable == 'prcp-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp6MonthsMean_189506To202107.npz')
elif WhichVariable == 'prcp-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp9MonthsMean_189509To202107.npz')
elif WhichVariable == 'prcp-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp12MonthsMean_189512To202107.npz')
elif WhichVariable == 'prcp-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp24MonthsMean_189612To202107.npz')
elif WhichVariable == 'prcp-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp36MonthsMean_189712To202107.npz')
elif WhichVariable == 'prcp-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp48MonthsMean_189812To202107.npz')
elif WhichVariable == 'prcp-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp60MonthsMean_189912To202107.npz')
elif WhichVariable == 'prcp-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/prcp72MonthsMean_190012To202107.npz')
elif WhichVariable == 'tavg-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg2MonthsMean_189502To202107.npz')
elif WhichVariable == 'tavg-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg3MonthsMean_189503To202107.npz')
elif WhichVariable == 'tavg-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg6MonthsMean_189506To202107.npz')
elif WhichVariable == 'tavg-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg9MonthsMean_189509To202107.npz')
elif WhichVariable == 'tavg-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg12MonthsMean_189512To202107.npz')
elif WhichVariable == 'tavg-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg24MonthsMean_189612To202107.npz')
elif WhichVariable == 'tavg-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg36MonthsMean_189712To202107.npz')
elif WhichVariable == 'tavg-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg48MonthsMean_189812To202107.npz')
elif WhichVariable == 'tavg-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg60MonthsMean_189912To202107.npz')
elif WhichVariable == 'tavg-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tavg72MonthsMean_190012To202107.npz')
elif WhichVariable == 'tmax-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax2MonthsMean_189502To202107.npz')
elif WhichVariable == 'tmax-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax3MonthsMean_189503To202107.npz')
elif WhichVariable == 'tmax-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax6MonthsMean_189506To202107.npz')
elif WhichVariable == 'tmax-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax9MonthsMean_189509To202107.npz')
elif WhichVariable == 'tmax-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax12MonthsMean_189512To202107.npz')
elif WhichVariable == 'tmax-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax24MonthsMean_189612To202107.npz')
elif WhichVariable == 'tmax-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax36MonthsMean_189712To202107.npz')
elif WhichVariable == 'tmax-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax48MonthsMean_189812To202107.npz')
elif WhichVariable == 'tmax-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax60MonthsMean_189912To202107.npz')
elif WhichVariable == 'tmax-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimGrid1D/tmax72MonthsMean_190012To202107.npz')

def ConcatFiles(VariableName, Info_BeginYYYYMM_List, Info_EndYYYYMM_List):
  for ThisYear in range(Info_BeginYYYYMM_List[0], Info_EndYYYYMM_List[0]+1, 1):
    if ThisYear == Info_BeginYYYYMM_List[0]:
      BeginMM = Info_BeginYYYYMM_List[1]
    else:
      BeginMM = 1
    #end of if ThisYear == Info_BeginYYYYMM_List[0]
    if ThisYear == Info_EndYYYYMM_List[0]:
      EndMM = Info_EndYYYYMM_List[1]
    else:
      EndMM = 12
    #end of if ThisYear == Info_EndYYYYMM_List[0]
    for ThisMonth in range(BeginMM, EndMM+1, 1):
      ThisYearMonth_Variable_Info = np.load(InfoFilesDir+VariableName+'_'+format(ThisYear,'04')+format(ThisMonth,'02')+'_1DClimGrid.npz')
      ThisYearMonth_YYYYMM_Of_InfoArray = ThisYearMonth_Variable_Info['YYYYMM_Of_RefArrayForPrcntl']
      ThisYearMonth_InfoArray = ThisYearMonth_Variable_Info['RefArrayForPrcntl']
      if ( (ThisYear == Info_BeginYYYYMM_List[0]) and (ThisMonth == BeginMM) ):
        YYYYMM_Of_InfoArray = np.copy(ThisYearMonth_YYYYMM_Of_InfoArray)
        InfoArray = np.copy(ThisYearMonth_InfoArray)
      else:
        YYYYMM_Of_InfoArray = np.concatenate((YYYYMM_Of_InfoArray, ThisYearMonth_YYYYMM_Of_InfoArray), axis = 0)        
        InfoArray = np.concatenate((InfoArray, ThisYearMonth_InfoArray), axis = 0)
      #end of if ( (ThisYear == Info_BeginYYYYMM_List[0]) and (ThisMonth == BeginMM) )
    #end of for ThisMonth in range(BeginMM, EndMM+1, 1)
  #end of for ThisYear in range(Info_BeginYYYYMM_List[0], Info_EndYYYYMM_List[1]+1, 1)
  return YYYYMM_Of_InfoArray, InfoArray
#end of def ConcatFiles(VariableName, Info_BeginYYYYMM_List, Info_EndYYYYMM_List)

if WhichVariable == 'spei-gamma-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-01', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-02', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-03', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-06', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-09', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-12', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-24', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-36', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-48', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-60', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-gamma-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-gamma-72', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-01', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-02', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-03', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-06', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-09', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-12', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-24', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-36', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-48', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-60', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spei-pearson-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spei-pearson-72', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-01', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-02', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-03', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-06', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-09', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-12', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-24', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-36', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-48', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-60', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-gamma-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-gamma-72', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-01', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-02':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-02', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-03':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-03', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-06':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-06', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-09':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-09', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-12':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-12', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-24':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-24', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-36':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-36', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-48':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-48', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-60':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-60', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'spi-pearson-72':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('spi-pearson-72', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'prcp-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('prcp', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'pet-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('pet', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'tavg-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('tavg', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
elif WhichVariable == 'tmax-01':
  nClimGrid_YYYYMM_Of_InfoArray, Variable_InfoArray = ConcatFiles('tmax', nClimGrid_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):
  # NumDateElements is 2 if YYYYMMEtc is in YYYYMM format, and 3 if in YYYYMMDD format
  # WhereDayForNumDateElements2 is 'mid' if value representative at mid-month, and 'end' if at end-month (e.g., accumulation)
  if NumDateElements == 3:
    Years_Of_InfoArray = YYYYMMEtc_Of_InfoArray // 10000
    Months_Of_InfoArray = (YYYYMMEtc_Of_InfoArray % 10000) // 100
    DaysOfMonth_Of_InfoArray = YYYYMMEtc_Of_InfoArray % 100 
  elif NumDateElements == 2:
    Years_Of_InfoArray = YYYYMMEtc_Of_InfoArray // 100
    Months_Of_InfoArray = YYYYMMEtc_Of_InfoArray % 100
  else:
    print('NumDateElements should be 3 or 2 in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
    sys.exit(0)
  RealDatesList_Of_InfoArray = []
  for ii in range(len(Years_Of_InfoArray)):
    if NumDateElements == 3:
      RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], DaysOfMonth_Of_InfoArray[ii,0])) 
    elif NumDateElements == 2:
      if WhereDayForNumDateElements2 == 'mid':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 15)) # NOTE 
      elif WhereDayForNumDateElements2 == 'end':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], (monthrange(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0]))[1])) # NOTE 
      elif WhereDayForNumDateElements2 == 'begin':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 1))
      else:
        print('WhereDayForNumDateElements2 should be mid or end in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
        sys.exit(0)
  return RealDatesList_Of_InfoArray
#end of def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):

if WhichVariable == 'spei-gamma-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_01', 'end')
elif WhichVariable == 'spei-gamma-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_02', 'end')
elif WhichVariable == 'spei-gamma-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_03', 'end')
elif WhichVariable == 'spei-gamma-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_06', 'end')
elif WhichVariable == 'spei-gamma-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_09', 'end')
elif WhichVariable == 'spei-gamma-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_12', 'end')
elif WhichVariable == 'spei-gamma-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_24', 'end')
elif WhichVariable == 'spei-gamma-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_36', 'end')
elif WhichVariable == 'spei-gamma-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_48', 'end')
elif WhichVariable == 'spei-gamma-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_60', 'end')
elif WhichVariable == 'spei-gamma-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_gamma_72', 'end')
elif WhichVariable == 'spei-pearson-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_01', 'end')
elif WhichVariable == 'spei-pearson-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_02', 'end')
elif WhichVariable == 'spei-pearson-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_03', 'end')
elif WhichVariable == 'spei-pearson-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_06', 'end')
elif WhichVariable == 'spei-pearson-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_09', 'end')
elif WhichVariable == 'spei-pearson-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_12', 'end')
elif WhichVariable == 'spei-pearson-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_24', 'end')
elif WhichVariable == 'spei-pearson-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_36', 'end')
elif WhichVariable == 'spei-pearson-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_48', 'end')
elif WhichVariable == 'spei-pearson-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_60', 'end')
elif WhichVariable == 'spei-pearson-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spei_pearson_72', 'end')
elif WhichVariable == 'spi-gamma-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_01', 'end')
elif WhichVariable == 'spi-gamma-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_02', 'end')
elif WhichVariable == 'spi-gamma-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_03', 'end')
elif WhichVariable == 'spi-gamma-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_06', 'end')
elif WhichVariable == 'spi-gamma-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_09', 'end')
elif WhichVariable == 'spi-gamma-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_12', 'end')
elif WhichVariable == 'spi-gamma-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_24', 'end')
elif WhichVariable == 'spi-gamma-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_36', 'end')
elif WhichVariable == 'spi-gamma-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_48', 'end')
elif WhichVariable == 'spi-gamma-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_60', 'end')
elif WhichVariable == 'spi-gamma-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_gamma_72', 'end')
elif WhichVariable == 'spi-pearson-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_01', 'end')
elif WhichVariable == 'spi-pearson-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_02', 'end')
elif WhichVariable == 'spi-pearson-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_03', 'end')
elif WhichVariable == 'spi-pearson-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_06', 'end')
elif WhichVariable == 'spi-pearson-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_09', 'end')
elif WhichVariable == 'spi-pearson-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_12', 'end')
elif WhichVariable == 'spi-pearson-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_24', 'end')
elif WhichVariable == 'spi-pearson-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_36', 'end')
elif WhichVariable == 'spi-pearson-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_48', 'end')
elif WhichVariable == 'spi-pearson-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_60', 'end')
elif WhichVariable == 'spi-pearson-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'spi_pearson_72', 'end')
elif WhichVariable == 'pet-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_01', 'end')
elif WhichVariable == 'pet-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_02', 'end')
elif WhichVariable == 'pet-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_03', 'end')
elif WhichVariable == 'pet-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_06', 'end')
elif WhichVariable == 'pet-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_09', 'end')
elif WhichVariable == 'pet-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_12', 'end')
elif WhichVariable == 'pet-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_24', 'end')
elif WhichVariable == 'pet-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_36', 'end')
elif WhichVariable == 'pet-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_48', 'end')
elif WhichVariable == 'pet-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_60', 'end')
elif WhichVariable == 'pet-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'pet_72', 'end')
elif WhichVariable == 'prcp-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_01', 'end')
elif WhichVariable == 'prcp-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_02', 'end')
elif WhichVariable == 'prcp-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_03', 'end')
elif WhichVariable == 'prcp-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_06', 'end')
elif WhichVariable == 'prcp-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_09', 'end')
elif WhichVariable == 'prcp-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_12', 'end')
elif WhichVariable == 'prcp-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_24', 'end')
elif WhichVariable == 'prcp-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_36', 'end')
elif WhichVariable == 'prcp-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_48', 'end')
elif WhichVariable == 'prcp-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_60', 'end')
elif WhichVariable == 'prcp-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'prcp_72', 'end')
elif WhichVariable == 'tavg-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_01', 'end')
elif WhichVariable == 'tavg-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_02', 'end')
elif WhichVariable == 'tavg-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_03', 'end')
elif WhichVariable == 'tavg-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_06', 'end')
elif WhichVariable == 'tavg-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_09', 'end')
elif WhichVariable == 'tavg-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_12', 'end')
elif WhichVariable == 'tavg-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_24', 'end')
elif WhichVariable == 'tavg-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_36', 'end')
elif WhichVariable == 'tavg-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_48', 'end')
elif WhichVariable == 'tavg-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_60', 'end')
elif WhichVariable == 'tavg-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tavg_72', 'end')
elif WhichVariable == 'tmax-01':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_01', 'end')
elif WhichVariable == 'tmax-02':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_02', 'end')
elif WhichVariable == 'tmax-03':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_03', 'end')
elif WhichVariable == 'tmax-06':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_06', 'end')
elif WhichVariable == 'tmax-09':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_09', 'end')
elif WhichVariable == 'tmax-12':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_12', 'end')
elif WhichVariable == 'tmax-24':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_24', 'end')
elif WhichVariable == 'tmax-36':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_36', 'end')
elif WhichVariable == 'tmax-48':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_48', 'end')
elif WhichVariable == 'tmax-60':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_60', 'end')
elif WhichVariable == 'tmax-72':
  Variable_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_YYYYMM_Of_InfoArray, 2, 'tmax_72', 'end')

del nClimGrid_YYYYMM_Of_InfoArray

#Begin calculating real dates list for reference arrays

def GetTimeInfoOfRefArray(Ref_BeginDate, Ref_EndDate):
  TotalNumDaysDiff = abs(Ref_EndDate-Ref_BeginDate).days
  TotalNumWeeksDiff = TotalNumDaysDiff//7
  RealDatesList_Of_RefArray = []
  HumanDatesList_Of_RefArray = []
  for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
    Ref_IntermediateDate = Ref_BeginDate + timedelta(weeks=NumWeeksDiff)
    RealDatesList_Of_RefArray.append(Ref_IntermediateDate)
    HumanDatesList_Of_RefArray.append(10000*Ref_IntermediateDate.year + 100*Ref_IntermediateDate.month + Ref_IntermediateDate.day)
  YYYYMMDD_Of_RefArray = np.array(HumanDatesList_Of_RefArray, dtype = np.int32)
  YYYYMMDD_Of_RefArray = np.expand_dims(YYYYMMDD_Of_RefArray, axis=1)
  return RealDatesList_Of_RefArray, YYYYMMDD_Of_RefArray
#end of def GetTimeInfoOfRefArray(Ref_BeginDate, Ref_EndDate):

Variable_RealDatesList_Of_RefArray, Variable_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_Ref_BeginDate, nClimGrid_Ref_EndDate)

#End calculating real dates list for reference arrays

Variable_RefArray = np.empty([ Variable_YYYYMMDD_Of_RefArray.shape[0], Variable_InfoArray.shape[1]])
Variable_RefArray[:] = np.NaN

def TimeInterpolateValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
  for DestinationDateIdx in range(len(DestinationDatesList)):
    ThisDestinationDate = DestinationDatesList[DestinationDateIdx] 
    if ThisDestinationDate in SourceDatesList:
      SourceIdxForThisDest = SourceDatesList.index(ThisDestinationDate) 
      DestinationArray[DestinationDateIdx,:] = SourceArray[SourceIdxForThisDest,:] 
    else:
      DaysDiffList = []
      for ThisSourceDate in SourceDatesList:
        DaysDiffList.append((ThisDestinationDate - ThisSourceDate).days)
      DaysDiffArray = np.array(DaysDiffList)
      SourceLowerIdxForThisDest = np.amax(np.where(DaysDiffArray > 0)) 
      SrcSlice = SourceArray[SourceLowerIdxForThisDest:SourceLowerIdxForThisDest+2,:]
      SrcSlice_isnan = np.isnan(SrcSlice)  
      SrcSlice_isnan_int = SrcSlice_isnan.astype(np.int32)
      SrcSlice_isnan_sum = np.sum(SrcSlice_isnan_int, axis = 0)
      Idxs_NotAllRowsNan = np.where(SrcSlice_isnan_sum < SrcSlice.shape[0])
      if Idxs_NotAllRowsNan[0].size > 0:
        SrcSlice_notnan = ~SrcSlice_isnan 
        SrcSlice_notnan_int = SrcSlice_notnan.astype(np.int32)
        Wt1 = float(-DaysDiffList[SourceLowerIdxForThisDest+1])
        Wt2 = float(DaysDiffList[SourceLowerIdxForThisDest])
        WtsMat = np.repeat(np.array([[Wt1],[Wt2]], dtype = SrcSlice.dtype), repeats = SrcSlice.shape[1], axis = 1) 
        Wtd_SrcSlice = np.multiply(SrcSlice, WtsMat)
        BooledWtsMat = np.multiply(WtsMat, SrcSlice_notnan_int)     
        Wtd_SrcSlice_NotAllRowsNan = Wtd_SrcSlice[:, Idxs_NotAllRowsNan[0]]
        BooledWtsMat_NotAllRowsNan = BooledWtsMat[:, Idxs_NotAllRowsNan[0]]
        Sum_Wtd_SrcSlice_NotAllRowsNan = np.nansum(Wtd_SrcSlice_NotAllRowsNan, axis = 0)
        Sum_Wts_NotAllRowsNan = np.nansum(BooledWtsMat_NotAllRowsNan, axis = 0)
        DestinationArray[DestinationDateIdx,Idxs_NotAllRowsNan[0]] = np.divide(Sum_Wtd_SrcSlice_NotAllRowsNan, 
                                                           Sum_Wts_NotAllRowsNan)
      #end of if Idxs_NotAllRowsNan[0].size > 0:
    #end of if ThisDestinationDate in SourceDatesList:
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeInterpolateValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):

def TimeInterpolateValues2(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
  for DestinationDateIdx in range(len(DestinationDatesList)):
    ThisDestinationDate = DestinationDatesList[DestinationDateIdx]
    if ThisDestinationDate in SourceDatesList:
      SourceIdxForThisDest = SourceDatesList.index(ThisDestinationDate)
      DestinationArray[DestinationDateIdx,:] = SourceArray[SourceIdxForThisDest,:]
    else:
      DaysDiffList = []
      for ThisSourceDate in SourceDatesList:
        DaysDiffList.append((ThisDestinationDate - ThisSourceDate).days)
      DaysDiffArray = np.array(DaysDiffList)
      SourceLowerIdxForThisDest = np.amax(np.where(DaysDiffArray > 0))
      SrcSlice = SourceArray[SourceLowerIdxForThisDest:SourceLowerIdxForThisDest+2,:]
      SrcSlice_isnan = np.isnan(SrcSlice)
      SrcSlice_isnan_int = SrcSlice_isnan.astype(np.int32)
      SrcSlice_isnan_sum = np.sum(SrcSlice_isnan_int, axis = 0)
      Idxs_AllRowsValid = np.where(SrcSlice_isnan_sum == 0)
      if Idxs_AllRowsValid[0].size > 0:
        SrcSlice_notnan = ~SrcSlice_isnan
        SrcSlice_notnan_int = SrcSlice_notnan.astype(np.int32)
        Wt1 = float(-DaysDiffList[SourceLowerIdxForThisDest+1])
        Wt2 = float(DaysDiffList[SourceLowerIdxForThisDest])
        WtsMat = np.repeat(np.array([[Wt1],[Wt2]], dtype = SrcSlice.dtype), repeats = SrcSlice.shape[1], axis = 1)
        Wtd_SrcSlice = np.multiply(SrcSlice, WtsMat)
        BooledWtsMat = np.multiply(WtsMat, SrcSlice_notnan_int)
        Wtd_SrcSlice_AllRowsValid = Wtd_SrcSlice[:, Idxs_AllRowsValid[0]]
        BooledWtsMat_AllRowsValid = BooledWtsMat[:, Idxs_AllRowsValid[0]]
        Sum_Wtd_SrcSlice_AllRowsValid = np.nansum(Wtd_SrcSlice_AllRowsValid, axis = 0)
        Sum_Wts_AllRowsValid = np.nansum(BooledWtsMat_AllRowsValid, axis = 0)
        DestinationArray[DestinationDateIdx,Idxs_AllRowsValid[0]] = np.divide(Sum_Wtd_SrcSlice_AllRowsValid,
                                                           Sum_Wts_AllRowsValid)
      #end of if Idxs_AllRowsValid[0].size > 0:
    #end of if ThisDestinationDate in SourceDatesList:
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeInterpolateValues2(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
 
Variable_RefArray = TimeInterpolateValues2(Variable_RealDatesList_Of_InfoArray, Variable_RealDatesList_Of_RefArray, Variable_InfoArray, Variable_RefArray)

del Variable_InfoArray
del Variable_RealDatesList_Of_InfoArray
del Variable_RealDatesList_Of_RefArray

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(Variable_RefFileName, Variable_RefArray = Variable_RefArray, Variable_YYYYMMDD_Of_RefArray = Variable_YYYYMMDD_Of_RefArray)

print(WhichVariable+"_YYYYMMDD_Of_RefArray.shape is ",Variable_YYYYMMDD_Of_RefArray.shape)
print(WhichVariable+"_YYYYMMDD_Of_RefArray is ",Variable_YYYYMMDD_Of_RefArray)
 
del Variable_YYYYMMDD_Of_RefArray
 
print(WhichVariable+"_RefArray.shape is ",Variable_RefArray.shape)
print(WhichVariable+"_RefArray is ",Variable_RefArray)
print("np.amin(np.isnan("+WhichVariable+"_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Variable_RefArray).sum(axis=0)))
print("np.amax(np.isnan("+WhichVariable+"_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Variable_RefArray).sum(axis=0)))
print("np.amin(np.isnan("+WhichVariable+"_RefArray).sum(axis=1)) is ",np.amin(np.isnan(Variable_RefArray).sum(axis=1)))
print("np.amax(np.isnan("+WhichVariable+"_RefArray).sum(axis=1)) is ",np.amax(np.isnan(Variable_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(Variable_RefArray),', overall max is ',np.nanmax(Variable_RefArray))

del Variable_RefArray

