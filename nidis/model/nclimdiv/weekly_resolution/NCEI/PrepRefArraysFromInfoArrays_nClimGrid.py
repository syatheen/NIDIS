# Coded by Soni Yatheendradas
#         on Sep 13, 2021
from __future__ import division

# BEGIN code arguments / editable section

InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/nClimGrid_Npzs/'

nClimGrid_01_Info_BeginYYYYMM_List = [1895, 1] # monthly mean, taken as valid on last of the month
nClimGrid_02_Info_BeginYYYYMM_List = [1895, 2] # monthly mean, taken as valid on last of the month
nClimGrid_03_Info_BeginYYYYMM_List = [1895, 3] # monthly mean, taken as valid on last of the month
nClimGrid_06_Info_BeginYYYYMM_List = [1895, 6] # monthly mean, taken as valid on last of the month
nClimGrid_09_Info_BeginYYYYMM_List = [1895, 9] # monthly mean, taken as valid on last of the month
nClimGrid_12_Info_BeginYYYYMM_List = [1895, 12] # monthly mean, taken as valid on last of the month
nClimGrid_24_Info_BeginYYYYMM_List = [1896, 12] # monthly mean, taken as valid on last of the month
nClimGrid_36_Info_BeginYYYYMM_List = [1897, 12] # monthly mean, taken as valid on last of the month
nClimGrid_48_Info_BeginYYYYMM_List = [1898, 12] # monthly mean, taken as valid on last of the month
nClimGrid_60_Info_BeginYYYYMM_List = [1899, 12] # monthly mean, taken as valid on last of the month
nClimGrid_72_Info_BeginYYYYMM_List = [1900, 12] # monthly mean, taken as valid on last of the month

nClimGrid_Info_EndYYYYMM_List = [2021, 7] # monthly mean, taken as valid on last of the month

nClimGrid_01_Ref_BeginDateVecList = [1895, 2, 5]  # nClimGrid_01 beginning year, month, day of month, this is also a Tuesday
nClimGrid_02_Ref_BeginDateVecList = [1895, 3, 5]  # nClimGrid_02 beginning year, month, day of month, this is also a Tuesday
nClimGrid_03_Ref_BeginDateVecList = [1895, 4, 2]  # nClimGrid_03 beginning year, month, day of month, this is also a Tuesday
nClimGrid_06_Ref_BeginDateVecList = [1895, 7, 2]  # nClimGrid_06 beginning year, month, day of month, this is also a Tuesday
nClimGrid_09_Ref_BeginDateVecList = [1895, 10, 1]  # nClimGrid_09 beginning year, month, day of month, this is also a Tuesday
nClimGrid_12_Ref_BeginDateVecList = [1895, 12, 31]  # nClimGrid_12 beginning year, month, day of month, this is also a Tuesday
nClimGrid_24_Ref_BeginDateVecList = [1897, 1, 5]  # nClimGrid_24 beginning year, month, day of month, this is also a Tuesday
nClimGrid_36_Ref_BeginDateVecList = [1898, 1, 4]  # nClimGrid_36 beginning year, month, day of month, this is also a Tuesday
nClimGrid_48_Ref_BeginDateVecList = [1899, 1, 3]  # nClimGrid_48 beginning year, month, day of month, this is also a Tuesday
nClimGrid_60_Ref_BeginDateVecList = [1900, 1, 2]  # nClimGrid_60 beginning year, month, day of month, this is also a Tuesday
nClimGrid_72_Ref_BeginDateVecList = [1901, 1, 1]  # nClimGrid_72 beginning year, month, day of month, this is also a Tuesday

nClimGrid_Ref_EndDateVecList = [2021, 7, 27]  # nClimGrid ending year, month, day of month, this is also a Tuesday

spei_gamma_01_RefFileName = 'RefArrays/ClimDiv_spei_gamma_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_02_RefFileName = 'RefArrays/ClimDiv_spei_gamma_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_03_RefFileName = 'RefArrays/ClimDiv_spei_gamma_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_06_RefFileName = 'RefArrays/ClimDiv_spei_gamma_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_09_RefFileName = 'RefArrays/ClimDiv_spei_gamma_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_12_RefFileName = 'RefArrays/ClimDiv_spei_gamma_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_24_RefFileName = 'RefArrays/ClimDiv_spei_gamma_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_36_RefFileName = 'RefArrays/ClimDiv_spei_gamma_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_48_RefFileName = 'RefArrays/ClimDiv_spei_gamma_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_60_RefFileName = 'RefArrays/ClimDiv_spei_gamma_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_gamma_72_RefFileName = 'RefArrays/ClimDiv_spei_gamma_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

spei_pearson_01_RefFileName = 'RefArrays/ClimDiv_spei_pearson_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_02_RefFileName = 'RefArrays/ClimDiv_spei_pearson_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_03_RefFileName = 'RefArrays/ClimDiv_spei_pearson_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_06_RefFileName = 'RefArrays/ClimDiv_spei_pearson_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_09_RefFileName = 'RefArrays/ClimDiv_spei_pearson_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_12_RefFileName = 'RefArrays/ClimDiv_spei_pearson_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_24_RefFileName = 'RefArrays/ClimDiv_spei_pearson_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_36_RefFileName = 'RefArrays/ClimDiv_spei_pearson_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_48_RefFileName = 'RefArrays/ClimDiv_spei_pearson_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_60_RefFileName = 'RefArrays/ClimDiv_spei_pearson_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spei_pearson_72_RefFileName = 'RefArrays/ClimDiv_spei_pearson_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

spi_gamma_01_RefFileName = 'RefArrays/ClimDiv_spi_gamma_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_02_RefFileName = 'RefArrays/ClimDiv_spi_gamma_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_03_RefFileName = 'RefArrays/ClimDiv_spi_gamma_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_06_RefFileName = 'RefArrays/ClimDiv_spi_gamma_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_09_RefFileName = 'RefArrays/ClimDiv_spi_gamma_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_12_RefFileName = 'RefArrays/ClimDiv_spi_gamma_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_24_RefFileName = 'RefArrays/ClimDiv_spi_gamma_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_36_RefFileName = 'RefArrays/ClimDiv_spi_gamma_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_48_RefFileName = 'RefArrays/ClimDiv_spi_gamma_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_60_RefFileName = 'RefArrays/ClimDiv_spi_gamma_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_gamma_72_RefFileName = 'RefArrays/ClimDiv_spi_gamma_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

spi_pearson_01_RefFileName = 'RefArrays/ClimDiv_spi_pearson_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_02_RefFileName = 'RefArrays/ClimDiv_spi_pearson_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_03_RefFileName = 'RefArrays/ClimDiv_spi_pearson_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_06_RefFileName = 'RefArrays/ClimDiv_spi_pearson_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_09_RefFileName = 'RefArrays/ClimDiv_spi_pearson_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_12_RefFileName = 'RefArrays/ClimDiv_spi_pearson_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_24_RefFileName = 'RefArrays/ClimDiv_spi_pearson_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_36_RefFileName = 'RefArrays/ClimDiv_spi_pearson_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_48_RefFileName = 'RefArrays/ClimDiv_spi_pearson_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_60_RefFileName = 'RefArrays/ClimDiv_spi_pearson_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
spi_pearson_72_RefFileName = 'RefArrays/ClimDiv_spi_pearson_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

pet_01_RefFileName = 'RefArrays/ClimDiv_pet_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_02_RefFileName = 'RefArrays/ClimDiv_pet_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_03_RefFileName = 'RefArrays/ClimDiv_pet_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_06_RefFileName = 'RefArrays/ClimDiv_pet_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_09_RefFileName = 'RefArrays/ClimDiv_pet_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_12_RefFileName = 'RefArrays/ClimDiv_pet_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_24_RefFileName = 'RefArrays/ClimDiv_pet_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_36_RefFileName = 'RefArrays/ClimDiv_pet_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_48_RefFileName = 'RefArrays/ClimDiv_pet_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_60_RefFileName = 'RefArrays/ClimDiv_pet_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
pet_72_RefFileName = 'RefArrays/ClimDiv_pet_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

prcp_01_RefFileName = 'RefArrays/ClimDiv_prcp_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_02_RefFileName = 'RefArrays/ClimDiv_prcp_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_03_RefFileName = 'RefArrays/ClimDiv_prcp_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_06_RefFileName = 'RefArrays/ClimDiv_prcp_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_09_RefFileName = 'RefArrays/ClimDiv_prcp_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_12_RefFileName = 'RefArrays/ClimDiv_prcp_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_24_RefFileName = 'RefArrays/ClimDiv_prcp_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_36_RefFileName = 'RefArrays/ClimDiv_prcp_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_48_RefFileName = 'RefArrays/ClimDiv_prcp_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_60_RefFileName = 'RefArrays/ClimDiv_prcp_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
prcp_72_RefFileName = 'RefArrays/ClimDiv_prcp_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

tavg_01_RefFileName = 'RefArrays/ClimDiv_tavg_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_02_RefFileName = 'RefArrays/ClimDiv_tavg_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_03_RefFileName = 'RefArrays/ClimDiv_tavg_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_06_RefFileName = 'RefArrays/ClimDiv_tavg_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_09_RefFileName = 'RefArrays/ClimDiv_tavg_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_12_RefFileName = 'RefArrays/ClimDiv_tavg_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_24_RefFileName = 'RefArrays/ClimDiv_tavg_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_36_RefFileName = 'RefArrays/ClimDiv_tavg_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_48_RefFileName = 'RefArrays/ClimDiv_tavg_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_60_RefFileName = 'RefArrays/ClimDiv_tavg_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tavg_72_RefFileName = 'RefArrays/ClimDiv_tavg_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

tmax_01_RefFileName = 'RefArrays/ClimDiv_tmax_01_'+format(nClimGrid_01_Ref_BeginDateVecList[0],'04')+format(nClimGrid_01_Ref_BeginDateVecList[1],'02')+format(nClimGrid_01_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_02_RefFileName = 'RefArrays/ClimDiv_tmax_02_'+format(nClimGrid_02_Ref_BeginDateVecList[0],'04')+format(nClimGrid_02_Ref_BeginDateVecList[1],'02')+format(nClimGrid_02_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_03_RefFileName = 'RefArrays/ClimDiv_tmax_03_'+format(nClimGrid_03_Ref_BeginDateVecList[0],'04')+format(nClimGrid_03_Ref_BeginDateVecList[1],'02')+format(nClimGrid_03_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_06_RefFileName = 'RefArrays/ClimDiv_tmax_06_'+format(nClimGrid_06_Ref_BeginDateVecList[0],'04')+format(nClimGrid_06_Ref_BeginDateVecList[1],'02')+format(nClimGrid_06_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_09_RefFileName = 'RefArrays/ClimDiv_tmax_09_'+format(nClimGrid_09_Ref_BeginDateVecList[0],'04')+format(nClimGrid_09_Ref_BeginDateVecList[1],'02')+format(nClimGrid_09_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_12_RefFileName = 'RefArrays/ClimDiv_tmax_12_'+format(nClimGrid_12_Ref_BeginDateVecList[0],'04')+format(nClimGrid_12_Ref_BeginDateVecList[1],'02')+format(nClimGrid_12_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_24_RefFileName = 'RefArrays/ClimDiv_tmax_24_'+format(nClimGrid_24_Ref_BeginDateVecList[0],'04')+format(nClimGrid_24_Ref_BeginDateVecList[1],'02')+format(nClimGrid_24_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_36_RefFileName = 'RefArrays/ClimDiv_tmax_36_'+format(nClimGrid_36_Ref_BeginDateVecList[0],'04')+format(nClimGrid_36_Ref_BeginDateVecList[1],'02')+format(nClimGrid_36_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_48_RefFileName = 'RefArrays/ClimDiv_tmax_48_'+format(nClimGrid_48_Ref_BeginDateVecList[0],'04')+format(nClimGrid_48_Ref_BeginDateVecList[1],'02')+format(nClimGrid_48_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_60_RefFileName = 'RefArrays/ClimDiv_tmax_60_'+format(nClimGrid_60_Ref_BeginDateVecList[0],'04')+format(nClimGrid_60_Ref_BeginDateVecList[1],'02')+format(nClimGrid_60_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'
tmax_72_RefFileName = 'RefArrays/ClimDiv_tmax_72_'+format(nClimGrid_72_Ref_BeginDateVecList[0],'04')+format(nClimGrid_72_Ref_BeginDateVecList[1],'02')+format(nClimGrid_72_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

nClimGrid_01_Ref_BeginDate = date(nClimGrid_01_Ref_BeginDateVecList[0], nClimGrid_01_Ref_BeginDateVecList[1], nClimGrid_01_Ref_BeginDateVecList[2])
nClimGrid_02_Ref_BeginDate = date(nClimGrid_02_Ref_BeginDateVecList[0], nClimGrid_02_Ref_BeginDateVecList[1], nClimGrid_02_Ref_BeginDateVecList[2])
nClimGrid_03_Ref_BeginDate = date(nClimGrid_03_Ref_BeginDateVecList[0], nClimGrid_03_Ref_BeginDateVecList[1], nClimGrid_03_Ref_BeginDateVecList[2])
nClimGrid_06_Ref_BeginDate = date(nClimGrid_06_Ref_BeginDateVecList[0], nClimGrid_06_Ref_BeginDateVecList[1], nClimGrid_06_Ref_BeginDateVecList[2])
nClimGrid_09_Ref_BeginDate = date(nClimGrid_09_Ref_BeginDateVecList[0], nClimGrid_09_Ref_BeginDateVecList[1], nClimGrid_09_Ref_BeginDateVecList[2])
nClimGrid_12_Ref_BeginDate = date(nClimGrid_12_Ref_BeginDateVecList[0], nClimGrid_12_Ref_BeginDateVecList[1], nClimGrid_12_Ref_BeginDateVecList[2])
nClimGrid_24_Ref_BeginDate = date(nClimGrid_24_Ref_BeginDateVecList[0], nClimGrid_24_Ref_BeginDateVecList[1], nClimGrid_24_Ref_BeginDateVecList[2])
nClimGrid_36_Ref_BeginDate = date(nClimGrid_36_Ref_BeginDateVecList[0], nClimGrid_36_Ref_BeginDateVecList[1], nClimGrid_36_Ref_BeginDateVecList[2])
nClimGrid_48_Ref_BeginDate = date(nClimGrid_48_Ref_BeginDateVecList[0], nClimGrid_48_Ref_BeginDateVecList[1], nClimGrid_48_Ref_BeginDateVecList[2])
nClimGrid_60_Ref_BeginDate = date(nClimGrid_60_Ref_BeginDateVecList[0], nClimGrid_60_Ref_BeginDateVecList[1], nClimGrid_60_Ref_BeginDateVecList[2])
nClimGrid_72_Ref_BeginDate = date(nClimGrid_72_Ref_BeginDateVecList[0], nClimGrid_72_Ref_BeginDateVecList[1], nClimGrid_72_Ref_BeginDateVecList[2])

nClimGrid_Ref_EndDate = date(nClimGrid_Ref_EndDateVecList[0], nClimGrid_Ref_EndDateVecList[1], nClimGrid_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays

if nClimGrid_01_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_01_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_02_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_02_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_03_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_03_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_06_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_06_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_09_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_09_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_12_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_12_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_24_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_24_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_36_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_36_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_48_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_48_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_60_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_60_Ref needs to be a Tuesday!!')
  sys.exit(0)
if nClimGrid_72_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for nClimGrid_72_Ref needs to be a Tuesday!!')
  sys.exit(0)

if nClimGrid_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for nClimGrid_Ref needs to be a Tuesday!!')
  sys.exit(0)

#END check whether the beginning and ending days are indeed Tuesdays

if nClimGrid_01_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_01_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_02_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_02_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_03_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_03_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_06_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_06_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_09_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_09_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_12_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_12_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_24_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_24_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_36_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_36_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_48_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_48_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_60_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid_60_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)
if nClimGrid_72_Ref_BeginDate > nClimGrid_Ref_EndDate:
  print('nClimGrid-72_Ref_BeginDate should not be later than nClimGrid_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

def ReadMeanFiles(FileName):
  ThisVariable_Info = np.load(FileName)
  ThisVariable_YYYYMM_Of_InfoArray = ThisVariable_Info['YYYYMM_Of_InfoArrayForPrcntl']
  ThisVariable_InfoArray = ThisVariable_Info['InfoArrayForPrcntl']
  return ThisVariable_YYYYMM_Of_InfoArray, ThisVariable_InfoArray
#end of def ReadMeanFiles(FileName)

nClimGrid_02_YYYYMM_Of_InfoArray, pet_02_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet2MonthsMean_189502To202107.npz')
nClimGrid_03_YYYYMM_Of_InfoArray, pet_03_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet3MonthsMean_189503To202107.npz')
nClimGrid_06_YYYYMM_Of_InfoArray, pet_06_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet6MonthsMean_189506To202107.npz')
nClimGrid_09_YYYYMM_Of_InfoArray, pet_09_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet9MonthsMean_189509To202107.npz')
nClimGrid_12_YYYYMM_Of_InfoArray, pet_12_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet12MonthsMean_189512To202107.npz')
nClimGrid_24_YYYYMM_Of_InfoArray, pet_24_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet24MonthsMean_189612To202107.npz')
nClimGrid_36_YYYYMM_Of_InfoArray, pet_36_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet36MonthsMean_189712To202107.npz')
nClimGrid_48_YYYYMM_Of_InfoArray, pet_48_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet48MonthsMean_189812To202107.npz')
nClimGrid_60_YYYYMM_Of_InfoArray, pet_60_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet60MonthsMean_189912To202107.npz')
nClimGrid_72_YYYYMM_Of_InfoArray, pet_72_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/pet72MonthsMean_190012To202107.npz')

nClimGrid_02_YYYYMM_Of_InfoArray, prcp_02_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp2MonthsMean_189502To202107.npz')
nClimGrid_03_YYYYMM_Of_InfoArray, prcp_03_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp3MonthsMean_189503To202107.npz')
nClimGrid_06_YYYYMM_Of_InfoArray, prcp_06_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp6MonthsMean_189506To202107.npz')
nClimGrid_09_YYYYMM_Of_InfoArray, prcp_09_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp9MonthsMean_189509To202107.npz')
nClimGrid_12_YYYYMM_Of_InfoArray, prcp_12_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp12MonthsMean_189512To202107.npz')
nClimGrid_24_YYYYMM_Of_InfoArray, prcp_24_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp24MonthsMean_189612To202107.npz')
nClimGrid_36_YYYYMM_Of_InfoArray, prcp_36_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp36MonthsMean_189712To202107.npz')
nClimGrid_48_YYYYMM_Of_InfoArray, prcp_48_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp48MonthsMean_189812To202107.npz')
nClimGrid_60_YYYYMM_Of_InfoArray, prcp_60_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp60MonthsMean_189912To202107.npz')
nClimGrid_72_YYYYMM_Of_InfoArray, prcp_72_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/prcp72MonthsMean_190012To202107.npz')

nClimGrid_02_YYYYMM_Of_InfoArray, tavg_02_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg2MonthsMean_189502To202107.npz')
nClimGrid_03_YYYYMM_Of_InfoArray, tavg_03_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg3MonthsMean_189503To202107.npz')
nClimGrid_06_YYYYMM_Of_InfoArray, tavg_06_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg6MonthsMean_189506To202107.npz')
nClimGrid_09_YYYYMM_Of_InfoArray, tavg_09_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg9MonthsMean_189509To202107.npz')
nClimGrid_12_YYYYMM_Of_InfoArray, tavg_12_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg12MonthsMean_189512To202107.npz')
nClimGrid_24_YYYYMM_Of_InfoArray, tavg_24_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg24MonthsMean_189612To202107.npz')
nClimGrid_36_YYYYMM_Of_InfoArray, tavg_36_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg36MonthsMean_189712To202107.npz')
nClimGrid_48_YYYYMM_Of_InfoArray, tavg_48_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg48MonthsMean_189812To202107.npz')
nClimGrid_60_YYYYMM_Of_InfoArray, tavg_60_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg60MonthsMean_189912To202107.npz')
nClimGrid_72_YYYYMM_Of_InfoArray, tavg_72_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tavg72MonthsMean_190012To202107.npz')

nClimGrid_02_YYYYMM_Of_InfoArray, tmax_02_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax2MonthsMean_189502To202107.npz')
nClimGrid_03_YYYYMM_Of_InfoArray, tmax_03_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax3MonthsMean_189503To202107.npz')
nClimGrid_06_YYYYMM_Of_InfoArray, tmax_06_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax6MonthsMean_189506To202107.npz')
nClimGrid_09_YYYYMM_Of_InfoArray, tmax_09_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax9MonthsMean_189509To202107.npz')
nClimGrid_12_YYYYMM_Of_InfoArray, tmax_12_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax12MonthsMean_189512To202107.npz')
nClimGrid_24_YYYYMM_Of_InfoArray, tmax_24_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax24MonthsMean_189612To202107.npz')
nClimGrid_36_YYYYMM_Of_InfoArray, tmax_36_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax36MonthsMean_189712To202107.npz')
nClimGrid_48_YYYYMM_Of_InfoArray, tmax_48_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax48MonthsMean_189812To202107.npz')
nClimGrid_60_YYYYMM_Of_InfoArray, tmax_60_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax60MonthsMean_189912To202107.npz')
nClimGrid_72_YYYYMM_Of_InfoArray, tmax_72_InfoArray = ReadMeanFiles('/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/InfoArrsNMonthsMean/ClimDivs/tmax72MonthsMean_190012To202107.npz')

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
      ThisYearMonth_Variable_Info = np.load(InfoFilesDir+VariableName+'_'+format(ThisYear,'04')+format(ThisMonth,'02')+'ClimDivs.npz')
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

nClimGrid_01_YYYYMM_Of_InfoArray, spei_gamma_01_InfoArray = ConcatFiles('spei-gamma-01', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_02_YYYYMM_Of_InfoArray, spei_gamma_02_InfoArray = ConcatFiles('spei-gamma-02', nClimGrid_02_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_03_YYYYMM_Of_InfoArray, spei_gamma_03_InfoArray = ConcatFiles('spei-gamma-03', nClimGrid_03_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_06_YYYYMM_Of_InfoArray, spei_gamma_06_InfoArray = ConcatFiles('spei-gamma-06', nClimGrid_06_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_09_YYYYMM_Of_InfoArray, spei_gamma_09_InfoArray = ConcatFiles('spei-gamma-09', nClimGrid_09_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_12_YYYYMM_Of_InfoArray, spei_gamma_12_InfoArray = ConcatFiles('spei-gamma-12', nClimGrid_12_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_24_YYYYMM_Of_InfoArray, spei_gamma_24_InfoArray = ConcatFiles('spei-gamma-24', nClimGrid_24_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_36_YYYYMM_Of_InfoArray, spei_gamma_36_InfoArray = ConcatFiles('spei-gamma-36', nClimGrid_36_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_48_YYYYMM_Of_InfoArray, spei_gamma_48_InfoArray = ConcatFiles('spei-gamma-48', nClimGrid_48_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_60_YYYYMM_Of_InfoArray, spei_gamma_60_InfoArray = ConcatFiles('spei-gamma-60', nClimGrid_60_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_72_YYYYMM_Of_InfoArray, spei_gamma_72_InfoArray = ConcatFiles('spei-gamma-72', nClimGrid_72_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, spei_pearson_01_InfoArray = ConcatFiles('spei-pearson-01', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_02_YYYYMM_Of_InfoArray, spei_pearson_02_InfoArray = ConcatFiles('spei-pearson-02', nClimGrid_02_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_03_YYYYMM_Of_InfoArray, spei_pearson_03_InfoArray = ConcatFiles('spei-pearson-03', nClimGrid_03_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_06_YYYYMM_Of_InfoArray, spei_pearson_06_InfoArray = ConcatFiles('spei-pearson-06', nClimGrid_06_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_09_YYYYMM_Of_InfoArray, spei_pearson_09_InfoArray = ConcatFiles('spei-pearson-09', nClimGrid_09_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_12_YYYYMM_Of_InfoArray, spei_pearson_12_InfoArray = ConcatFiles('spei-pearson-12', nClimGrid_12_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_24_YYYYMM_Of_InfoArray, spei_pearson_24_InfoArray = ConcatFiles('spei-pearson-24', nClimGrid_24_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_36_YYYYMM_Of_InfoArray, spei_pearson_36_InfoArray = ConcatFiles('spei-pearson-36', nClimGrid_36_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_48_YYYYMM_Of_InfoArray, spei_pearson_48_InfoArray = ConcatFiles('spei-pearson-48', nClimGrid_48_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_60_YYYYMM_Of_InfoArray, spei_pearson_60_InfoArray = ConcatFiles('spei-pearson-60', nClimGrid_60_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_72_YYYYMM_Of_InfoArray, spei_pearson_72_InfoArray = ConcatFiles('spei-pearson-72', nClimGrid_72_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, spi_gamma_01_InfoArray = ConcatFiles('spi-gamma-01', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_02_YYYYMM_Of_InfoArray, spi_gamma_02_InfoArray = ConcatFiles('spi-gamma-02', nClimGrid_02_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_03_YYYYMM_Of_InfoArray, spi_gamma_03_InfoArray = ConcatFiles('spi-gamma-03', nClimGrid_03_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_06_YYYYMM_Of_InfoArray, spi_gamma_06_InfoArray = ConcatFiles('spi-gamma-06', nClimGrid_06_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_09_YYYYMM_Of_InfoArray, spi_gamma_09_InfoArray = ConcatFiles('spi-gamma-09', nClimGrid_09_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_12_YYYYMM_Of_InfoArray, spi_gamma_12_InfoArray = ConcatFiles('spi-gamma-12', nClimGrid_12_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_24_YYYYMM_Of_InfoArray, spi_gamma_24_InfoArray = ConcatFiles('spi-gamma-24', nClimGrid_24_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_36_YYYYMM_Of_InfoArray, spi_gamma_36_InfoArray = ConcatFiles('spi-gamma-36', nClimGrid_36_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_48_YYYYMM_Of_InfoArray, spi_gamma_48_InfoArray = ConcatFiles('spi-gamma-48', nClimGrid_48_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_60_YYYYMM_Of_InfoArray, spi_gamma_60_InfoArray = ConcatFiles('spi-gamma-60', nClimGrid_60_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_72_YYYYMM_Of_InfoArray, spi_gamma_72_InfoArray = ConcatFiles('spi-gamma-72', nClimGrid_72_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, spi_pearson_01_InfoArray = ConcatFiles('spi-pearson-01', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_02_YYYYMM_Of_InfoArray, spi_pearson_02_InfoArray = ConcatFiles('spi-pearson-02', nClimGrid_02_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_03_YYYYMM_Of_InfoArray, spi_pearson_03_InfoArray = ConcatFiles('spi-pearson-03', nClimGrid_03_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_06_YYYYMM_Of_InfoArray, spi_pearson_06_InfoArray = ConcatFiles('spi-pearson-06', nClimGrid_06_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_09_YYYYMM_Of_InfoArray, spi_pearson_09_InfoArray = ConcatFiles('spi-pearson-09', nClimGrid_09_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_12_YYYYMM_Of_InfoArray, spi_pearson_12_InfoArray = ConcatFiles('spi-pearson-12', nClimGrid_12_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_24_YYYYMM_Of_InfoArray, spi_pearson_24_InfoArray = ConcatFiles('spi-pearson-24', nClimGrid_24_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_36_YYYYMM_Of_InfoArray, spi_pearson_36_InfoArray = ConcatFiles('spi-pearson-36', nClimGrid_36_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_48_YYYYMM_Of_InfoArray, spi_pearson_48_InfoArray = ConcatFiles('spi-pearson-48', nClimGrid_48_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_60_YYYYMM_Of_InfoArray, spi_pearson_60_InfoArray = ConcatFiles('spi-pearson-60', nClimGrid_60_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)
nClimGrid_72_YYYYMM_Of_InfoArray, spi_pearson_72_InfoArray = ConcatFiles('spi-pearson-72', nClimGrid_72_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, prcp_01_InfoArray = ConcatFiles('prcp', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, pet_01_InfoArray = ConcatFiles('pet', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, tavg_01_InfoArray = ConcatFiles('tavg', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

nClimGrid_01_YYYYMM_Of_InfoArray, tmax_01_InfoArray = ConcatFiles('tmax', nClimGrid_01_Info_BeginYYYYMM_List, nClimGrid_Info_EndYYYYMM_List)

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

spei_gamma_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'spei_gamma_01', 'end')
spei_gamma_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'spei_gamma_02', 'end')
spei_gamma_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'spei_gamma_03', 'end')
spei_gamma_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'spei_gamma_06', 'end')
spei_gamma_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'spei_gamma_09', 'end')
spei_gamma_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'spei_gamma_12', 'end')
spei_gamma_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'spei_gamma_24', 'end')
spei_gamma_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'spei_gamma_36', 'end')
spei_gamma_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'spei_gamma_48', 'end')
spei_gamma_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'spei_gamma_60', 'end')
spei_gamma_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'spei_gamma_72', 'end')

spei_pearson_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'spei_pearson_01', 'end')
spei_pearson_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'spei_pearson_02', 'end')
spei_pearson_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'spei_pearson_03', 'end')
spei_pearson_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'spei_pearson_06', 'end')
spei_pearson_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'spei_pearson_09', 'end')
spei_pearson_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'spei_pearson_12', 'end')
spei_pearson_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'spei_pearson_24', 'end')
spei_pearson_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'spei_pearson_36', 'end')
spei_pearson_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'spei_pearson_48', 'end')
spei_pearson_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'spei_pearson_60', 'end')
spei_pearson_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'spei_pearson_72', 'end')

spi_gamma_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'spi_gamma_01', 'end')
spi_gamma_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'spi_gamma_02', 'end')
spi_gamma_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'spi_gamma_03', 'end')
spi_gamma_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'spi_gamma_06', 'end')
spi_gamma_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'spi_gamma_09', 'end')
spi_gamma_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'spi_gamma_12', 'end')
spi_gamma_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'spi_gamma_24', 'end')
spi_gamma_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'spi_gamma_36', 'end')
spi_gamma_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'spi_gamma_48', 'end')
spi_gamma_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'spi_gamma_60', 'end')
spi_gamma_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'spi_gamma_72', 'end')

spi_pearson_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'spi_pearson_01', 'end')
spi_pearson_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'spi_pearson_02', 'end')
spi_pearson_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'spi_pearson_03', 'end')
spi_pearson_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'spi_pearson_06', 'end')
spi_pearson_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'spi_pearson_09', 'end')
spi_pearson_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'spi_pearson_12', 'end')
spi_pearson_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'spi_pearson_24', 'end')
spi_pearson_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'spi_pearson_36', 'end')
spi_pearson_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'spi_pearson_48', 'end')
spi_pearson_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'spi_pearson_60', 'end')
spi_pearson_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'spi_pearson_72', 'end')

pet_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'pet_01', 'end')
pet_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'pet_02', 'end')
pet_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'pet_03', 'end')
pet_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'pet_06', 'end')
pet_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'pet_09', 'end')
pet_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'pet_12', 'end')
pet_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'pet_24', 'end')
pet_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'pet_36', 'end')
pet_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'pet_48', 'end')
pet_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'pet_60', 'end')
pet_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'pet_72', 'end')

prcp_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'prcp_01', 'end')
prcp_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'prcp_02', 'end')
prcp_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'prcp_03', 'end')
prcp_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'prcp_06', 'end')
prcp_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'prcp_09', 'end')
prcp_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'prcp_12', 'end')
prcp_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'prcp_24', 'end')
prcp_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'prcp_36', 'end')
prcp_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'prcp_48', 'end')
prcp_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'prcp_60', 'end')
prcp_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'prcp_72', 'end')

tavg_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'tavg_01', 'end')
tavg_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'tavg_02', 'end')
tavg_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'tavg_03', 'end')
tavg_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'tavg_06', 'end')
tavg_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'tavg_09', 'end')
tavg_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'tavg_12', 'end')
tavg_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'tavg_24', 'end')
tavg_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'tavg_36', 'end')
tavg_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'tavg_48', 'end')
tavg_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'tavg_60', 'end')
tavg_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'tavg_72', 'end')

tmax_01_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_01_YYYYMM_Of_InfoArray, 2, 'tmax_01', 'end')
tmax_02_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_02_YYYYMM_Of_InfoArray, 2, 'tmax_02', 'end')
tmax_03_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_03_YYYYMM_Of_InfoArray, 2, 'tmax_03', 'end')
tmax_06_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_06_YYYYMM_Of_InfoArray, 2, 'tmax_06', 'end')
tmax_09_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_09_YYYYMM_Of_InfoArray, 2, 'tmax_09', 'end')
tmax_12_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_12_YYYYMM_Of_InfoArray, 2, 'tmax_12', 'end')
tmax_24_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_24_YYYYMM_Of_InfoArray, 2, 'tmax_24', 'end')
tmax_36_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_36_YYYYMM_Of_InfoArray, 2, 'tmax_36', 'end')
tmax_48_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_48_YYYYMM_Of_InfoArray, 2, 'tmax_48', 'end')
tmax_60_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_60_YYYYMM_Of_InfoArray, 2, 'tmax_60', 'end')
tmax_72_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(nClimGrid_72_YYYYMM_Of_InfoArray, 2, 'tmax_72', 'end')

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

spei_gamma_01_RealDatesList_Of_RefArray, spei_gamma_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_02_RealDatesList_Of_RefArray, spei_gamma_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_03_RealDatesList_Of_RefArray, spei_gamma_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_06_RealDatesList_Of_RefArray, spei_gamma_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_09_RealDatesList_Of_RefArray, spei_gamma_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_12_RealDatesList_Of_RefArray, spei_gamma_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_24_RealDatesList_Of_RefArray, spei_gamma_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_36_RealDatesList_Of_RefArray, spei_gamma_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_48_RealDatesList_Of_RefArray, spei_gamma_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_60_RealDatesList_Of_RefArray, spei_gamma_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_gamma_72_RealDatesList_Of_RefArray, spei_gamma_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

spei_pearson_01_RealDatesList_Of_RefArray, spei_pearson_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_02_RealDatesList_Of_RefArray, spei_pearson_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_03_RealDatesList_Of_RefArray, spei_pearson_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_06_RealDatesList_Of_RefArray, spei_pearson_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_09_RealDatesList_Of_RefArray, spei_pearson_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_12_RealDatesList_Of_RefArray, spei_pearson_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_24_RealDatesList_Of_RefArray, spei_pearson_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_36_RealDatesList_Of_RefArray, spei_pearson_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_48_RealDatesList_Of_RefArray, spei_pearson_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_60_RealDatesList_Of_RefArray, spei_pearson_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
spei_pearson_72_RealDatesList_Of_RefArray, spei_pearson_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

spi_gamma_01_RealDatesList_Of_RefArray, spi_gamma_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_02_RealDatesList_Of_RefArray, spi_gamma_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_03_RealDatesList_Of_RefArray, spi_gamma_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_06_RealDatesList_Of_RefArray, spi_gamma_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_09_RealDatesList_Of_RefArray, spi_gamma_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_12_RealDatesList_Of_RefArray, spi_gamma_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_24_RealDatesList_Of_RefArray, spi_gamma_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_36_RealDatesList_Of_RefArray, spi_gamma_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_48_RealDatesList_Of_RefArray, spi_gamma_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_60_RealDatesList_Of_RefArray, spi_gamma_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_gamma_72_RealDatesList_Of_RefArray, spi_gamma_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

spi_pearson_01_RealDatesList_Of_RefArray, spi_pearson_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_02_RealDatesList_Of_RefArray, spi_pearson_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_03_RealDatesList_Of_RefArray, spi_pearson_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_06_RealDatesList_Of_RefArray, spi_pearson_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_09_RealDatesList_Of_RefArray, spi_pearson_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_12_RealDatesList_Of_RefArray, spi_pearson_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_24_RealDatesList_Of_RefArray, spi_pearson_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_36_RealDatesList_Of_RefArray, spi_pearson_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_48_RealDatesList_Of_RefArray, spi_pearson_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_60_RealDatesList_Of_RefArray, spi_pearson_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
spi_pearson_72_RealDatesList_Of_RefArray, spi_pearson_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

pet_01_RealDatesList_Of_RefArray, pet_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_02_RealDatesList_Of_RefArray, pet_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_03_RealDatesList_Of_RefArray, pet_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_06_RealDatesList_Of_RefArray, pet_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_09_RealDatesList_Of_RefArray, pet_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_12_RealDatesList_Of_RefArray, pet_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_24_RealDatesList_Of_RefArray, pet_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_36_RealDatesList_Of_RefArray, pet_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_48_RealDatesList_Of_RefArray, pet_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_60_RealDatesList_Of_RefArray, pet_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
pet_72_RealDatesList_Of_RefArray, pet_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

prcp_01_RealDatesList_Of_RefArray, prcp_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_02_RealDatesList_Of_RefArray, prcp_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_03_RealDatesList_Of_RefArray, prcp_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_06_RealDatesList_Of_RefArray, prcp_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_09_RealDatesList_Of_RefArray, prcp_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_12_RealDatesList_Of_RefArray, prcp_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_24_RealDatesList_Of_RefArray, prcp_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_36_RealDatesList_Of_RefArray, prcp_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_48_RealDatesList_Of_RefArray, prcp_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_60_RealDatesList_Of_RefArray, prcp_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
prcp_72_RealDatesList_Of_RefArray, prcp_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

tavg_01_RealDatesList_Of_RefArray, tavg_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_02_RealDatesList_Of_RefArray, tavg_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_03_RealDatesList_Of_RefArray, tavg_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_06_RealDatesList_Of_RefArray, tavg_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_09_RealDatesList_Of_RefArray, tavg_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_12_RealDatesList_Of_RefArray, tavg_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_24_RealDatesList_Of_RefArray, tavg_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_36_RealDatesList_Of_RefArray, tavg_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_48_RealDatesList_Of_RefArray, tavg_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_60_RealDatesList_Of_RefArray, tavg_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
tavg_72_RealDatesList_Of_RefArray, tavg_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

tmax_01_RealDatesList_Of_RefArray, tmax_01_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_01_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_02_RealDatesList_Of_RefArray, tmax_02_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_02_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_03_RealDatesList_Of_RefArray, tmax_03_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_03_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_06_RealDatesList_Of_RefArray, tmax_06_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_06_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_09_RealDatesList_Of_RefArray, tmax_09_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_09_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_12_RealDatesList_Of_RefArray, tmax_12_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_12_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_24_RealDatesList_Of_RefArray, tmax_24_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_24_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_36_RealDatesList_Of_RefArray, tmax_36_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_36_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_48_RealDatesList_Of_RefArray, tmax_48_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_48_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_60_RealDatesList_Of_RefArray, tmax_60_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_60_Ref_BeginDate, nClimGrid_Ref_EndDate)
tmax_72_RealDatesList_Of_RefArray, tmax_72_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(nClimGrid_72_Ref_BeginDate, nClimGrid_Ref_EndDate)

#End calculating real dates list for reference arrays

spei_gamma_01_RefArray = np.empty([ spei_gamma_01_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_01_InfoArray.shape[1]])
spei_gamma_01_RefArray[:] = np.NaN
spei_gamma_02_RefArray = np.empty([ spei_gamma_02_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_02_InfoArray.shape[1]])
spei_gamma_02_RefArray[:] = np.NaN
spei_gamma_03_RefArray = np.empty([ spei_gamma_03_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_03_InfoArray.shape[1]])
spei_gamma_03_RefArray[:] = np.NaN
spei_gamma_06_RefArray = np.empty([ spei_gamma_06_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_06_InfoArray.shape[1]])
spei_gamma_06_RefArray[:] = np.NaN
spei_gamma_09_RefArray = np.empty([ spei_gamma_09_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_09_InfoArray.shape[1]])
spei_gamma_09_RefArray[:] = np.NaN
spei_gamma_12_RefArray = np.empty([ spei_gamma_12_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_12_InfoArray.shape[1]])
spei_gamma_12_RefArray[:] = np.NaN
spei_gamma_24_RefArray = np.empty([ spei_gamma_24_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_24_InfoArray.shape[1]])
spei_gamma_24_RefArray[:] = np.NaN
spei_gamma_36_RefArray = np.empty([ spei_gamma_36_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_36_InfoArray.shape[1]])
spei_gamma_36_RefArray[:] = np.NaN
spei_gamma_48_RefArray = np.empty([ spei_gamma_48_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_48_InfoArray.shape[1]])
spei_gamma_48_RefArray[:] = np.NaN
spei_gamma_60_RefArray = np.empty([ spei_gamma_60_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_60_InfoArray.shape[1]])
spei_gamma_60_RefArray[:] = np.NaN
spei_gamma_72_RefArray = np.empty([ spei_gamma_72_YYYYMMDD_Of_RefArray.shape[0], spei_gamma_72_InfoArray.shape[1]])
spei_gamma_72_RefArray[:] = np.NaN

spei_pearson_01_RefArray = np.empty([ spei_pearson_01_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_01_InfoArray.shape[1]])
spei_pearson_01_RefArray[:] = np.NaN
spei_pearson_02_RefArray = np.empty([ spei_pearson_02_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_02_InfoArray.shape[1]])
spei_pearson_02_RefArray[:] = np.NaN
spei_pearson_03_RefArray = np.empty([ spei_pearson_03_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_03_InfoArray.shape[1]])
spei_pearson_03_RefArray[:] = np.NaN
spei_pearson_06_RefArray = np.empty([ spei_pearson_06_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_06_InfoArray.shape[1]])
spei_pearson_06_RefArray[:] = np.NaN
spei_pearson_09_RefArray = np.empty([ spei_pearson_09_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_09_InfoArray.shape[1]])
spei_pearson_09_RefArray[:] = np.NaN
spei_pearson_12_RefArray = np.empty([ spei_pearson_12_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_12_InfoArray.shape[1]])
spei_pearson_12_RefArray[:] = np.NaN
spei_pearson_24_RefArray = np.empty([ spei_pearson_24_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_24_InfoArray.shape[1]])
spei_pearson_24_RefArray[:] = np.NaN
spei_pearson_36_RefArray = np.empty([ spei_pearson_36_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_36_InfoArray.shape[1]])
spei_pearson_36_RefArray[:] = np.NaN
spei_pearson_48_RefArray = np.empty([ spei_pearson_48_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_48_InfoArray.shape[1]])
spei_pearson_48_RefArray[:] = np.NaN
spei_pearson_60_RefArray = np.empty([ spei_pearson_60_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_60_InfoArray.shape[1]])
spei_pearson_60_RefArray[:] = np.NaN
spei_pearson_72_RefArray = np.empty([ spei_pearson_72_YYYYMMDD_Of_RefArray.shape[0], spei_pearson_72_InfoArray.shape[1]])
spei_pearson_72_RefArray[:] = np.NaN

spi_gamma_01_RefArray = np.empty([ spi_gamma_01_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_01_InfoArray.shape[1]])
spi_gamma_01_RefArray[:] = np.NaN
spi_gamma_02_RefArray = np.empty([ spi_gamma_02_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_02_InfoArray.shape[1]])
spi_gamma_02_RefArray[:] = np.NaN
spi_gamma_03_RefArray = np.empty([ spi_gamma_03_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_03_InfoArray.shape[1]])
spi_gamma_03_RefArray[:] = np.NaN
spi_gamma_06_RefArray = np.empty([ spi_gamma_06_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_06_InfoArray.shape[1]])
spi_gamma_06_RefArray[:] = np.NaN
spi_gamma_09_RefArray = np.empty([ spi_gamma_09_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_09_InfoArray.shape[1]])
spi_gamma_09_RefArray[:] = np.NaN
spi_gamma_12_RefArray = np.empty([ spi_gamma_12_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_12_InfoArray.shape[1]])
spi_gamma_12_RefArray[:] = np.NaN
spi_gamma_24_RefArray = np.empty([ spi_gamma_24_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_24_InfoArray.shape[1]])
spi_gamma_24_RefArray[:] = np.NaN
spi_gamma_36_RefArray = np.empty([ spi_gamma_36_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_36_InfoArray.shape[1]])
spi_gamma_36_RefArray[:] = np.NaN
spi_gamma_48_RefArray = np.empty([ spi_gamma_48_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_48_InfoArray.shape[1]])
spi_gamma_48_RefArray[:] = np.NaN
spi_gamma_60_RefArray = np.empty([ spi_gamma_60_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_60_InfoArray.shape[1]])
spi_gamma_60_RefArray[:] = np.NaN
spi_gamma_72_RefArray = np.empty([ spi_gamma_72_YYYYMMDD_Of_RefArray.shape[0], spi_gamma_72_InfoArray.shape[1]])
spi_gamma_72_RefArray[:] = np.NaN

spi_pearson_01_RefArray = np.empty([ spi_pearson_01_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_01_InfoArray.shape[1]])
spi_pearson_01_RefArray[:] = np.NaN
spi_pearson_02_RefArray = np.empty([ spi_pearson_02_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_02_InfoArray.shape[1]])
spi_pearson_02_RefArray[:] = np.NaN
spi_pearson_03_RefArray = np.empty([ spi_pearson_03_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_03_InfoArray.shape[1]])
spi_pearson_03_RefArray[:] = np.NaN
spi_pearson_06_RefArray = np.empty([ spi_pearson_06_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_06_InfoArray.shape[1]])
spi_pearson_06_RefArray[:] = np.NaN
spi_pearson_09_RefArray = np.empty([ spi_pearson_09_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_09_InfoArray.shape[1]])
spi_pearson_09_RefArray[:] = np.NaN
spi_pearson_12_RefArray = np.empty([ spi_pearson_12_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_12_InfoArray.shape[1]])
spi_pearson_12_RefArray[:] = np.NaN
spi_pearson_24_RefArray = np.empty([ spi_pearson_24_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_24_InfoArray.shape[1]])
spi_pearson_24_RefArray[:] = np.NaN
spi_pearson_36_RefArray = np.empty([ spi_pearson_36_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_36_InfoArray.shape[1]])
spi_pearson_36_RefArray[:] = np.NaN
spi_pearson_48_RefArray = np.empty([ spi_pearson_48_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_48_InfoArray.shape[1]])
spi_pearson_48_RefArray[:] = np.NaN
spi_pearson_60_RefArray = np.empty([ spi_pearson_60_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_60_InfoArray.shape[1]])
spi_pearson_60_RefArray[:] = np.NaN
spi_pearson_72_RefArray = np.empty([ spi_pearson_72_YYYYMMDD_Of_RefArray.shape[0], spi_pearson_72_InfoArray.shape[1]])
spi_pearson_72_RefArray[:] = np.NaN

pet_01_RefArray = np.empty([ pet_01_YYYYMMDD_Of_RefArray.shape[0], pet_01_InfoArray.shape[1]])
pet_01_RefArray[:] = np.NaN
pet_02_RefArray = np.empty([ pet_02_YYYYMMDD_Of_RefArray.shape[0], pet_02_InfoArray.shape[1]])
pet_02_RefArray[:] = np.NaN
pet_03_RefArray = np.empty([ pet_03_YYYYMMDD_Of_RefArray.shape[0], pet_03_InfoArray.shape[1]])
pet_03_RefArray[:] = np.NaN
pet_06_RefArray = np.empty([ pet_06_YYYYMMDD_Of_RefArray.shape[0], pet_06_InfoArray.shape[1]])
pet_06_RefArray[:] = np.NaN
pet_09_RefArray = np.empty([ pet_09_YYYYMMDD_Of_RefArray.shape[0], pet_09_InfoArray.shape[1]])
pet_09_RefArray[:] = np.NaN
pet_12_RefArray = np.empty([ pet_12_YYYYMMDD_Of_RefArray.shape[0], pet_12_InfoArray.shape[1]])
pet_12_RefArray[:] = np.NaN
pet_24_RefArray = np.empty([ pet_24_YYYYMMDD_Of_RefArray.shape[0], pet_24_InfoArray.shape[1]])
pet_24_RefArray[:] = np.NaN
pet_36_RefArray = np.empty([ pet_36_YYYYMMDD_Of_RefArray.shape[0], pet_36_InfoArray.shape[1]])
pet_36_RefArray[:] = np.NaN
pet_48_RefArray = np.empty([ pet_48_YYYYMMDD_Of_RefArray.shape[0], pet_48_InfoArray.shape[1]])
pet_48_RefArray[:] = np.NaN
pet_60_RefArray = np.empty([ pet_60_YYYYMMDD_Of_RefArray.shape[0], pet_60_InfoArray.shape[1]])
pet_60_RefArray[:] = np.NaN
pet_72_RefArray = np.empty([ pet_72_YYYYMMDD_Of_RefArray.shape[0], pet_72_InfoArray.shape[1]])
pet_72_RefArray[:] = np.NaN

prcp_01_RefArray = np.empty([ prcp_01_YYYYMMDD_Of_RefArray.shape[0], prcp_01_InfoArray.shape[1]])
prcp_01_RefArray[:] = np.NaN
prcp_02_RefArray = np.empty([ prcp_02_YYYYMMDD_Of_RefArray.shape[0], prcp_02_InfoArray.shape[1]])
prcp_02_RefArray[:] = np.NaN
prcp_03_RefArray = np.empty([ prcp_03_YYYYMMDD_Of_RefArray.shape[0], prcp_03_InfoArray.shape[1]])
prcp_03_RefArray[:] = np.NaN
prcp_06_RefArray = np.empty([ prcp_06_YYYYMMDD_Of_RefArray.shape[0], prcp_06_InfoArray.shape[1]])
prcp_06_RefArray[:] = np.NaN
prcp_09_RefArray = np.empty([ prcp_09_YYYYMMDD_Of_RefArray.shape[0], prcp_09_InfoArray.shape[1]])
prcp_09_RefArray[:] = np.NaN
prcp_12_RefArray = np.empty([ prcp_12_YYYYMMDD_Of_RefArray.shape[0], prcp_12_InfoArray.shape[1]])
prcp_12_RefArray[:] = np.NaN
prcp_24_RefArray = np.empty([ prcp_24_YYYYMMDD_Of_RefArray.shape[0], prcp_24_InfoArray.shape[1]])
prcp_24_RefArray[:] = np.NaN
prcp_36_RefArray = np.empty([ prcp_36_YYYYMMDD_Of_RefArray.shape[0], prcp_36_InfoArray.shape[1]])
prcp_36_RefArray[:] = np.NaN
prcp_48_RefArray = np.empty([ prcp_48_YYYYMMDD_Of_RefArray.shape[0], prcp_48_InfoArray.shape[1]])
prcp_48_RefArray[:] = np.NaN
prcp_60_RefArray = np.empty([ prcp_60_YYYYMMDD_Of_RefArray.shape[0], prcp_60_InfoArray.shape[1]])
prcp_60_RefArray[:] = np.NaN
prcp_72_RefArray = np.empty([ prcp_72_YYYYMMDD_Of_RefArray.shape[0], prcp_72_InfoArray.shape[1]])
prcp_72_RefArray[:] = np.NaN

tavg_01_RefArray = np.empty([ tavg_01_YYYYMMDD_Of_RefArray.shape[0], tavg_01_InfoArray.shape[1]])
tavg_01_RefArray[:] = np.NaN
tavg_02_RefArray = np.empty([ tavg_02_YYYYMMDD_Of_RefArray.shape[0], tavg_02_InfoArray.shape[1]])
tavg_02_RefArray[:] = np.NaN
tavg_03_RefArray = np.empty([ tavg_03_YYYYMMDD_Of_RefArray.shape[0], tavg_03_InfoArray.shape[1]])
tavg_03_RefArray[:] = np.NaN
tavg_06_RefArray = np.empty([ tavg_06_YYYYMMDD_Of_RefArray.shape[0], tavg_06_InfoArray.shape[1]])
tavg_06_RefArray[:] = np.NaN
tavg_09_RefArray = np.empty([ tavg_09_YYYYMMDD_Of_RefArray.shape[0], tavg_09_InfoArray.shape[1]])
tavg_09_RefArray[:] = np.NaN
tavg_12_RefArray = np.empty([ tavg_12_YYYYMMDD_Of_RefArray.shape[0], tavg_12_InfoArray.shape[1]])
tavg_12_RefArray[:] = np.NaN
tavg_24_RefArray = np.empty([ tavg_24_YYYYMMDD_Of_RefArray.shape[0], tavg_24_InfoArray.shape[1]])
tavg_24_RefArray[:] = np.NaN
tavg_36_RefArray = np.empty([ tavg_36_YYYYMMDD_Of_RefArray.shape[0], tavg_36_InfoArray.shape[1]])
tavg_36_RefArray[:] = np.NaN
tavg_48_RefArray = np.empty([ tavg_48_YYYYMMDD_Of_RefArray.shape[0], tavg_48_InfoArray.shape[1]])
tavg_48_RefArray[:] = np.NaN
tavg_60_RefArray = np.empty([ tavg_60_YYYYMMDD_Of_RefArray.shape[0], tavg_60_InfoArray.shape[1]])
tavg_60_RefArray[:] = np.NaN
tavg_72_RefArray = np.empty([ tavg_72_YYYYMMDD_Of_RefArray.shape[0], tavg_72_InfoArray.shape[1]])
tavg_72_RefArray[:] = np.NaN

tmax_01_RefArray = np.empty([ tmax_01_YYYYMMDD_Of_RefArray.shape[0], tmax_01_InfoArray.shape[1]])
tmax_01_RefArray[:] = np.NaN
tmax_02_RefArray = np.empty([ tmax_02_YYYYMMDD_Of_RefArray.shape[0], tmax_02_InfoArray.shape[1]])
tmax_02_RefArray[:] = np.NaN
tmax_03_RefArray = np.empty([ tmax_03_YYYYMMDD_Of_RefArray.shape[0], tmax_03_InfoArray.shape[1]])
tmax_03_RefArray[:] = np.NaN
tmax_06_RefArray = np.empty([ tmax_06_YYYYMMDD_Of_RefArray.shape[0], tmax_06_InfoArray.shape[1]])
tmax_06_RefArray[:] = np.NaN
tmax_09_RefArray = np.empty([ tmax_09_YYYYMMDD_Of_RefArray.shape[0], tmax_09_InfoArray.shape[1]])
tmax_09_RefArray[:] = np.NaN
tmax_12_RefArray = np.empty([ tmax_12_YYYYMMDD_Of_RefArray.shape[0], tmax_12_InfoArray.shape[1]])
tmax_12_RefArray[:] = np.NaN
tmax_24_RefArray = np.empty([ tmax_24_YYYYMMDD_Of_RefArray.shape[0], tmax_24_InfoArray.shape[1]])
tmax_24_RefArray[:] = np.NaN
tmax_36_RefArray = np.empty([ tmax_36_YYYYMMDD_Of_RefArray.shape[0], tmax_36_InfoArray.shape[1]])
tmax_36_RefArray[:] = np.NaN
tmax_48_RefArray = np.empty([ tmax_48_YYYYMMDD_Of_RefArray.shape[0], tmax_48_InfoArray.shape[1]])
tmax_48_RefArray[:] = np.NaN
tmax_60_RefArray = np.empty([ tmax_60_YYYYMMDD_Of_RefArray.shape[0], tmax_60_InfoArray.shape[1]])
tmax_60_RefArray[:] = np.NaN
tmax_72_RefArray = np.empty([ tmax_72_YYYYMMDD_Of_RefArray.shape[0], tmax_72_InfoArray.shape[1]])
tmax_72_RefArray[:] = np.NaN

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
 
spei_gamma_01_RefArray = TimeInterpolateValues2(spei_gamma_01_RealDatesList_Of_InfoArray, spei_gamma_01_RealDatesList_Of_RefArray, spei_gamma_01_InfoArray, spei_gamma_01_RefArray)
spei_gamma_02_RefArray = TimeInterpolateValues2(spei_gamma_02_RealDatesList_Of_InfoArray, spei_gamma_02_RealDatesList_Of_RefArray, spei_gamma_02_InfoArray, spei_gamma_02_RefArray)
spei_gamma_03_RefArray = TimeInterpolateValues2(spei_gamma_03_RealDatesList_Of_InfoArray, spei_gamma_03_RealDatesList_Of_RefArray, spei_gamma_03_InfoArray, spei_gamma_03_RefArray)
spei_gamma_06_RefArray = TimeInterpolateValues2(spei_gamma_06_RealDatesList_Of_InfoArray, spei_gamma_06_RealDatesList_Of_RefArray, spei_gamma_06_InfoArray, spei_gamma_06_RefArray)
spei_gamma_09_RefArray = TimeInterpolateValues2(spei_gamma_09_RealDatesList_Of_InfoArray, spei_gamma_09_RealDatesList_Of_RefArray, spei_gamma_09_InfoArray, spei_gamma_09_RefArray)
spei_gamma_12_RefArray = TimeInterpolateValues2(spei_gamma_12_RealDatesList_Of_InfoArray, spei_gamma_12_RealDatesList_Of_RefArray, spei_gamma_12_InfoArray, spei_gamma_12_RefArray)
spei_gamma_24_RefArray = TimeInterpolateValues2(spei_gamma_24_RealDatesList_Of_InfoArray, spei_gamma_24_RealDatesList_Of_RefArray, spei_gamma_24_InfoArray, spei_gamma_24_RefArray)
spei_gamma_36_RefArray = TimeInterpolateValues2(spei_gamma_36_RealDatesList_Of_InfoArray, spei_gamma_36_RealDatesList_Of_RefArray, spei_gamma_36_InfoArray, spei_gamma_36_RefArray)
spei_gamma_48_RefArray = TimeInterpolateValues2(spei_gamma_48_RealDatesList_Of_InfoArray, spei_gamma_48_RealDatesList_Of_RefArray, spei_gamma_48_InfoArray, spei_gamma_48_RefArray)
spei_gamma_60_RefArray = TimeInterpolateValues2(spei_gamma_60_RealDatesList_Of_InfoArray, spei_gamma_60_RealDatesList_Of_RefArray, spei_gamma_60_InfoArray, spei_gamma_60_RefArray)
spei_gamma_72_RefArray = TimeInterpolateValues2(spei_gamma_72_RealDatesList_Of_InfoArray, spei_gamma_72_RealDatesList_Of_RefArray, spei_gamma_72_InfoArray, spei_gamma_72_RefArray)

spei_pearson_01_RefArray = TimeInterpolateValues2(spei_pearson_01_RealDatesList_Of_InfoArray, spei_pearson_01_RealDatesList_Of_RefArray, spei_pearson_01_InfoArray, spei_pearson_01_RefArray)
spei_pearson_02_RefArray = TimeInterpolateValues2(spei_pearson_02_RealDatesList_Of_InfoArray, spei_pearson_02_RealDatesList_Of_RefArray, spei_pearson_02_InfoArray, spei_pearson_02_RefArray)
spei_pearson_03_RefArray = TimeInterpolateValues2(spei_pearson_03_RealDatesList_Of_InfoArray, spei_pearson_03_RealDatesList_Of_RefArray, spei_pearson_03_InfoArray, spei_pearson_03_RefArray)
spei_pearson_06_RefArray = TimeInterpolateValues2(spei_pearson_06_RealDatesList_Of_InfoArray, spei_pearson_06_RealDatesList_Of_RefArray, spei_pearson_06_InfoArray, spei_pearson_06_RefArray)
spei_pearson_09_RefArray = TimeInterpolateValues2(spei_pearson_09_RealDatesList_Of_InfoArray, spei_pearson_09_RealDatesList_Of_RefArray, spei_pearson_09_InfoArray, spei_pearson_09_RefArray)
spei_pearson_12_RefArray = TimeInterpolateValues2(spei_pearson_12_RealDatesList_Of_InfoArray, spei_pearson_12_RealDatesList_Of_RefArray, spei_pearson_12_InfoArray, spei_pearson_12_RefArray)
spei_pearson_24_RefArray = TimeInterpolateValues2(spei_pearson_24_RealDatesList_Of_InfoArray, spei_pearson_24_RealDatesList_Of_RefArray, spei_pearson_24_InfoArray, spei_pearson_24_RefArray)
spei_pearson_36_RefArray = TimeInterpolateValues2(spei_pearson_36_RealDatesList_Of_InfoArray, spei_pearson_36_RealDatesList_Of_RefArray, spei_pearson_36_InfoArray, spei_pearson_36_RefArray)
spei_pearson_48_RefArray = TimeInterpolateValues2(spei_pearson_48_RealDatesList_Of_InfoArray, spei_pearson_48_RealDatesList_Of_RefArray, spei_pearson_48_InfoArray, spei_pearson_48_RefArray)
spei_pearson_60_RefArray = TimeInterpolateValues2(spei_pearson_60_RealDatesList_Of_InfoArray, spei_pearson_60_RealDatesList_Of_RefArray, spei_pearson_60_InfoArray, spei_pearson_60_RefArray)
spei_pearson_72_RefArray = TimeInterpolateValues2(spei_pearson_72_RealDatesList_Of_InfoArray, spei_pearson_72_RealDatesList_Of_RefArray, spei_pearson_72_InfoArray, spei_pearson_72_RefArray)

spi_gamma_01_RefArray = TimeInterpolateValues2(spi_gamma_01_RealDatesList_Of_InfoArray, spi_gamma_01_RealDatesList_Of_RefArray, spi_gamma_01_InfoArray, spi_gamma_01_RefArray)
spi_gamma_02_RefArray = TimeInterpolateValues2(spi_gamma_02_RealDatesList_Of_InfoArray, spi_gamma_02_RealDatesList_Of_RefArray, spi_gamma_02_InfoArray, spi_gamma_02_RefArray)
spi_gamma_03_RefArray = TimeInterpolateValues2(spi_gamma_03_RealDatesList_Of_InfoArray, spi_gamma_03_RealDatesList_Of_RefArray, spi_gamma_03_InfoArray, spi_gamma_03_RefArray)
spi_gamma_06_RefArray = TimeInterpolateValues2(spi_gamma_06_RealDatesList_Of_InfoArray, spi_gamma_06_RealDatesList_Of_RefArray, spi_gamma_06_InfoArray, spi_gamma_06_RefArray)
spi_gamma_09_RefArray = TimeInterpolateValues2(spi_gamma_09_RealDatesList_Of_InfoArray, spi_gamma_09_RealDatesList_Of_RefArray, spi_gamma_09_InfoArray, spi_gamma_09_RefArray)
spi_gamma_12_RefArray = TimeInterpolateValues2(spi_gamma_12_RealDatesList_Of_InfoArray, spi_gamma_12_RealDatesList_Of_RefArray, spi_gamma_12_InfoArray, spi_gamma_12_RefArray)
spi_gamma_24_RefArray = TimeInterpolateValues2(spi_gamma_24_RealDatesList_Of_InfoArray, spi_gamma_24_RealDatesList_Of_RefArray, spi_gamma_24_InfoArray, spi_gamma_24_RefArray)
spi_gamma_36_RefArray = TimeInterpolateValues2(spi_gamma_36_RealDatesList_Of_InfoArray, spi_gamma_36_RealDatesList_Of_RefArray, spi_gamma_36_InfoArray, spi_gamma_36_RefArray)
spi_gamma_48_RefArray = TimeInterpolateValues2(spi_gamma_48_RealDatesList_Of_InfoArray, spi_gamma_48_RealDatesList_Of_RefArray, spi_gamma_48_InfoArray, spi_gamma_48_RefArray)
spi_gamma_60_RefArray = TimeInterpolateValues2(spi_gamma_60_RealDatesList_Of_InfoArray, spi_gamma_60_RealDatesList_Of_RefArray, spi_gamma_60_InfoArray, spi_gamma_60_RefArray)
spi_gamma_72_RefArray = TimeInterpolateValues2(spi_gamma_72_RealDatesList_Of_InfoArray, spi_gamma_72_RealDatesList_Of_RefArray, spi_gamma_72_InfoArray, spi_gamma_72_RefArray)

spi_pearson_01_RefArray = TimeInterpolateValues2(spi_pearson_01_RealDatesList_Of_InfoArray, spi_pearson_01_RealDatesList_Of_RefArray, spi_pearson_01_InfoArray, spi_pearson_01_RefArray)
spi_pearson_02_RefArray = TimeInterpolateValues2(spi_pearson_02_RealDatesList_Of_InfoArray, spi_pearson_02_RealDatesList_Of_RefArray, spi_pearson_02_InfoArray, spi_pearson_02_RefArray)
spi_pearson_03_RefArray = TimeInterpolateValues2(spi_pearson_03_RealDatesList_Of_InfoArray, spi_pearson_03_RealDatesList_Of_RefArray, spi_pearson_03_InfoArray, spi_pearson_03_RefArray)
spi_pearson_06_RefArray = TimeInterpolateValues2(spi_pearson_06_RealDatesList_Of_InfoArray, spi_pearson_06_RealDatesList_Of_RefArray, spi_pearson_06_InfoArray, spi_pearson_06_RefArray)
spi_pearson_09_RefArray = TimeInterpolateValues2(spi_pearson_09_RealDatesList_Of_InfoArray, spi_pearson_09_RealDatesList_Of_RefArray, spi_pearson_09_InfoArray, spi_pearson_09_RefArray)
spi_pearson_12_RefArray = TimeInterpolateValues2(spi_pearson_12_RealDatesList_Of_InfoArray, spi_pearson_12_RealDatesList_Of_RefArray, spi_pearson_12_InfoArray, spi_pearson_12_RefArray)
spi_pearson_24_RefArray = TimeInterpolateValues2(spi_pearson_24_RealDatesList_Of_InfoArray, spi_pearson_24_RealDatesList_Of_RefArray, spi_pearson_24_InfoArray, spi_pearson_24_RefArray)
spi_pearson_36_RefArray = TimeInterpolateValues2(spi_pearson_36_RealDatesList_Of_InfoArray, spi_pearson_36_RealDatesList_Of_RefArray, spi_pearson_36_InfoArray, spi_pearson_36_RefArray)
spi_pearson_48_RefArray = TimeInterpolateValues2(spi_pearson_48_RealDatesList_Of_InfoArray, spi_pearson_48_RealDatesList_Of_RefArray, spi_pearson_48_InfoArray, spi_pearson_48_RefArray)
spi_pearson_60_RefArray = TimeInterpolateValues2(spi_pearson_60_RealDatesList_Of_InfoArray, spi_pearson_60_RealDatesList_Of_RefArray, spi_pearson_60_InfoArray, spi_pearson_60_RefArray)
spi_pearson_72_RefArray = TimeInterpolateValues2(spi_pearson_72_RealDatesList_Of_InfoArray, spi_pearson_72_RealDatesList_Of_RefArray, spi_pearson_72_InfoArray, spi_pearson_72_RefArray)

pet_01_RefArray = TimeInterpolateValues2(pet_01_RealDatesList_Of_InfoArray, pet_01_RealDatesList_Of_RefArray, pet_01_InfoArray, pet_01_RefArray)
pet_02_RefArray = TimeInterpolateValues2(pet_02_RealDatesList_Of_InfoArray, pet_02_RealDatesList_Of_RefArray, pet_02_InfoArray, pet_02_RefArray)
pet_03_RefArray = TimeInterpolateValues2(pet_03_RealDatesList_Of_InfoArray, pet_03_RealDatesList_Of_RefArray, pet_03_InfoArray, pet_03_RefArray)
pet_06_RefArray = TimeInterpolateValues2(pet_06_RealDatesList_Of_InfoArray, pet_06_RealDatesList_Of_RefArray, pet_06_InfoArray, pet_06_RefArray)
pet_09_RefArray = TimeInterpolateValues2(pet_09_RealDatesList_Of_InfoArray, pet_09_RealDatesList_Of_RefArray, pet_09_InfoArray, pet_09_RefArray)
pet_12_RefArray = TimeInterpolateValues2(pet_12_RealDatesList_Of_InfoArray, pet_12_RealDatesList_Of_RefArray, pet_12_InfoArray, pet_12_RefArray)
pet_24_RefArray = TimeInterpolateValues2(pet_24_RealDatesList_Of_InfoArray, pet_24_RealDatesList_Of_RefArray, pet_24_InfoArray, pet_24_RefArray)
pet_36_RefArray = TimeInterpolateValues2(pet_36_RealDatesList_Of_InfoArray, pet_36_RealDatesList_Of_RefArray, pet_36_InfoArray, pet_36_RefArray)
pet_48_RefArray = TimeInterpolateValues2(pet_48_RealDatesList_Of_InfoArray, pet_48_RealDatesList_Of_RefArray, pet_48_InfoArray, pet_48_RefArray)
pet_60_RefArray = TimeInterpolateValues2(pet_60_RealDatesList_Of_InfoArray, pet_60_RealDatesList_Of_RefArray, pet_60_InfoArray, pet_60_RefArray)
pet_72_RefArray = TimeInterpolateValues2(pet_72_RealDatesList_Of_InfoArray, pet_72_RealDatesList_Of_RefArray, pet_72_InfoArray, pet_72_RefArray)

prcp_01_RefArray = TimeInterpolateValues2(prcp_01_RealDatesList_Of_InfoArray, prcp_01_RealDatesList_Of_RefArray, prcp_01_InfoArray, prcp_01_RefArray)
prcp_02_RefArray = TimeInterpolateValues2(prcp_02_RealDatesList_Of_InfoArray, prcp_02_RealDatesList_Of_RefArray, prcp_02_InfoArray, prcp_02_RefArray)
prcp_03_RefArray = TimeInterpolateValues2(prcp_03_RealDatesList_Of_InfoArray, prcp_03_RealDatesList_Of_RefArray, prcp_03_InfoArray, prcp_03_RefArray)
prcp_06_RefArray = TimeInterpolateValues2(prcp_06_RealDatesList_Of_InfoArray, prcp_06_RealDatesList_Of_RefArray, prcp_06_InfoArray, prcp_06_RefArray)
prcp_09_RefArray = TimeInterpolateValues2(prcp_09_RealDatesList_Of_InfoArray, prcp_09_RealDatesList_Of_RefArray, prcp_09_InfoArray, prcp_09_RefArray)
prcp_12_RefArray = TimeInterpolateValues2(prcp_12_RealDatesList_Of_InfoArray, prcp_12_RealDatesList_Of_RefArray, prcp_12_InfoArray, prcp_12_RefArray)
prcp_24_RefArray = TimeInterpolateValues2(prcp_24_RealDatesList_Of_InfoArray, prcp_24_RealDatesList_Of_RefArray, prcp_24_InfoArray, prcp_24_RefArray)
prcp_36_RefArray = TimeInterpolateValues2(prcp_36_RealDatesList_Of_InfoArray, prcp_36_RealDatesList_Of_RefArray, prcp_36_InfoArray, prcp_36_RefArray)
prcp_48_RefArray = TimeInterpolateValues2(prcp_48_RealDatesList_Of_InfoArray, prcp_48_RealDatesList_Of_RefArray, prcp_48_InfoArray, prcp_48_RefArray)
prcp_60_RefArray = TimeInterpolateValues2(prcp_60_RealDatesList_Of_InfoArray, prcp_60_RealDatesList_Of_RefArray, prcp_60_InfoArray, prcp_60_RefArray)
prcp_72_RefArray = TimeInterpolateValues2(prcp_72_RealDatesList_Of_InfoArray, prcp_72_RealDatesList_Of_RefArray, prcp_72_InfoArray, prcp_72_RefArray)

tavg_01_RefArray = TimeInterpolateValues2(tavg_01_RealDatesList_Of_InfoArray, tavg_01_RealDatesList_Of_RefArray, tavg_01_InfoArray, tavg_01_RefArray)
tavg_02_RefArray = TimeInterpolateValues2(tavg_02_RealDatesList_Of_InfoArray, tavg_02_RealDatesList_Of_RefArray, tavg_02_InfoArray, tavg_02_RefArray)
tavg_03_RefArray = TimeInterpolateValues2(tavg_03_RealDatesList_Of_InfoArray, tavg_03_RealDatesList_Of_RefArray, tavg_03_InfoArray, tavg_03_RefArray)
tavg_06_RefArray = TimeInterpolateValues2(tavg_06_RealDatesList_Of_InfoArray, tavg_06_RealDatesList_Of_RefArray, tavg_06_InfoArray, tavg_06_RefArray)
tavg_09_RefArray = TimeInterpolateValues2(tavg_09_RealDatesList_Of_InfoArray, tavg_09_RealDatesList_Of_RefArray, tavg_09_InfoArray, tavg_09_RefArray)
tavg_12_RefArray = TimeInterpolateValues2(tavg_12_RealDatesList_Of_InfoArray, tavg_12_RealDatesList_Of_RefArray, tavg_12_InfoArray, tavg_12_RefArray)
tavg_24_RefArray = TimeInterpolateValues2(tavg_24_RealDatesList_Of_InfoArray, tavg_24_RealDatesList_Of_RefArray, tavg_24_InfoArray, tavg_24_RefArray)
tavg_36_RefArray = TimeInterpolateValues2(tavg_36_RealDatesList_Of_InfoArray, tavg_36_RealDatesList_Of_RefArray, tavg_36_InfoArray, tavg_36_RefArray)
tavg_48_RefArray = TimeInterpolateValues2(tavg_48_RealDatesList_Of_InfoArray, tavg_48_RealDatesList_Of_RefArray, tavg_48_InfoArray, tavg_48_RefArray)
tavg_60_RefArray = TimeInterpolateValues2(tavg_60_RealDatesList_Of_InfoArray, tavg_60_RealDatesList_Of_RefArray, tavg_60_InfoArray, tavg_60_RefArray)
tavg_72_RefArray = TimeInterpolateValues2(tavg_72_RealDatesList_Of_InfoArray, tavg_72_RealDatesList_Of_RefArray, tavg_72_InfoArray, tavg_72_RefArray)

tmax_01_RefArray = TimeInterpolateValues2(tmax_01_RealDatesList_Of_InfoArray, tmax_01_RealDatesList_Of_RefArray, tmax_01_InfoArray, tmax_01_RefArray)
tmax_02_RefArray = TimeInterpolateValues2(tmax_02_RealDatesList_Of_InfoArray, tmax_02_RealDatesList_Of_RefArray, tmax_02_InfoArray, tmax_02_RefArray)
tmax_03_RefArray = TimeInterpolateValues2(tmax_03_RealDatesList_Of_InfoArray, tmax_03_RealDatesList_Of_RefArray, tmax_03_InfoArray, tmax_03_RefArray)
tmax_06_RefArray = TimeInterpolateValues2(tmax_06_RealDatesList_Of_InfoArray, tmax_06_RealDatesList_Of_RefArray, tmax_06_InfoArray, tmax_06_RefArray)
tmax_09_RefArray = TimeInterpolateValues2(tmax_09_RealDatesList_Of_InfoArray, tmax_09_RealDatesList_Of_RefArray, tmax_09_InfoArray, tmax_09_RefArray)
tmax_12_RefArray = TimeInterpolateValues2(tmax_12_RealDatesList_Of_InfoArray, tmax_12_RealDatesList_Of_RefArray, tmax_12_InfoArray, tmax_12_RefArray)
tmax_24_RefArray = TimeInterpolateValues2(tmax_24_RealDatesList_Of_InfoArray, tmax_24_RealDatesList_Of_RefArray, tmax_24_InfoArray, tmax_24_RefArray)
tmax_36_RefArray = TimeInterpolateValues2(tmax_36_RealDatesList_Of_InfoArray, tmax_36_RealDatesList_Of_RefArray, tmax_36_InfoArray, tmax_36_RefArray)
tmax_48_RefArray = TimeInterpolateValues2(tmax_48_RealDatesList_Of_InfoArray, tmax_48_RealDatesList_Of_RefArray, tmax_48_InfoArray, tmax_48_RefArray)
tmax_60_RefArray = TimeInterpolateValues2(tmax_60_RealDatesList_Of_InfoArray, tmax_60_RealDatesList_Of_RefArray, tmax_60_InfoArray, tmax_60_RefArray)
tmax_72_RefArray = TimeInterpolateValues2(tmax_72_RealDatesList_Of_InfoArray, tmax_72_RealDatesList_Of_RefArray, tmax_72_InfoArray, tmax_72_RefArray)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(spei_gamma_01_RefFileName, spei_gamma_01_RefArray = spei_gamma_01_RefArray, spei_gamma_01_YYYYMMDD_Of_RefArray = spei_gamma_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_02_RefFileName, spei_gamma_02_RefArray = spei_gamma_02_RefArray, spei_gamma_02_YYYYMMDD_Of_RefArray = spei_gamma_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_03_RefFileName, spei_gamma_03_RefArray = spei_gamma_03_RefArray, spei_gamma_03_YYYYMMDD_Of_RefArray = spei_gamma_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_06_RefFileName, spei_gamma_06_RefArray = spei_gamma_06_RefArray, spei_gamma_06_YYYYMMDD_Of_RefArray = spei_gamma_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_09_RefFileName, spei_gamma_09_RefArray = spei_gamma_09_RefArray, spei_gamma_09_YYYYMMDD_Of_RefArray = spei_gamma_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_12_RefFileName, spei_gamma_12_RefArray = spei_gamma_12_RefArray, spei_gamma_12_YYYYMMDD_Of_RefArray = spei_gamma_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_24_RefFileName, spei_gamma_24_RefArray = spei_gamma_24_RefArray, spei_gamma_24_YYYYMMDD_Of_RefArray = spei_gamma_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_36_RefFileName, spei_gamma_36_RefArray = spei_gamma_36_RefArray, spei_gamma_36_YYYYMMDD_Of_RefArray = spei_gamma_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_48_RefFileName, spei_gamma_48_RefArray = spei_gamma_48_RefArray, spei_gamma_48_YYYYMMDD_Of_RefArray = spei_gamma_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_60_RefFileName, spei_gamma_60_RefArray = spei_gamma_60_RefArray, spei_gamma_60_YYYYMMDD_Of_RefArray = spei_gamma_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_gamma_72_RefFileName, spei_gamma_72_RefArray = spei_gamma_72_RefArray, spei_gamma_72_YYYYMMDD_Of_RefArray = spei_gamma_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(spei_pearson_01_RefFileName, spei_pearson_01_RefArray = spei_pearson_01_RefArray, spei_pearson_01_YYYYMMDD_Of_RefArray = spei_pearson_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_02_RefFileName, spei_pearson_02_RefArray = spei_pearson_02_RefArray, spei_pearson_02_YYYYMMDD_Of_RefArray = spei_pearson_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_03_RefFileName, spei_pearson_03_RefArray = spei_pearson_03_RefArray, spei_pearson_03_YYYYMMDD_Of_RefArray = spei_pearson_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_06_RefFileName, spei_pearson_06_RefArray = spei_pearson_06_RefArray, spei_pearson_06_YYYYMMDD_Of_RefArray = spei_pearson_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_09_RefFileName, spei_pearson_09_RefArray = spei_pearson_09_RefArray, spei_pearson_09_YYYYMMDD_Of_RefArray = spei_pearson_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_12_RefFileName, spei_pearson_12_RefArray = spei_pearson_12_RefArray, spei_pearson_12_YYYYMMDD_Of_RefArray = spei_pearson_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_24_RefFileName, spei_pearson_24_RefArray = spei_pearson_24_RefArray, spei_pearson_24_YYYYMMDD_Of_RefArray = spei_pearson_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_36_RefFileName, spei_pearson_36_RefArray = spei_pearson_36_RefArray, spei_pearson_36_YYYYMMDD_Of_RefArray = spei_pearson_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_48_RefFileName, spei_pearson_48_RefArray = spei_pearson_48_RefArray, spei_pearson_48_YYYYMMDD_Of_RefArray = spei_pearson_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_60_RefFileName, spei_pearson_60_RefArray = spei_pearson_60_RefArray, spei_pearson_60_YYYYMMDD_Of_RefArray = spei_pearson_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(spei_pearson_72_RefFileName, spei_pearson_72_RefArray = spei_pearson_72_RefArray, spei_pearson_72_YYYYMMDD_Of_RefArray = spei_pearson_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(spi_gamma_01_RefFileName, spi_gamma_01_RefArray = spi_gamma_01_RefArray, spi_gamma_01_YYYYMMDD_Of_RefArray = spi_gamma_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_02_RefFileName, spi_gamma_02_RefArray = spi_gamma_02_RefArray, spi_gamma_02_YYYYMMDD_Of_RefArray = spi_gamma_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_03_RefFileName, spi_gamma_03_RefArray = spi_gamma_03_RefArray, spi_gamma_03_YYYYMMDD_Of_RefArray = spi_gamma_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_06_RefFileName, spi_gamma_06_RefArray = spi_gamma_06_RefArray, spi_gamma_06_YYYYMMDD_Of_RefArray = spi_gamma_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_09_RefFileName, spi_gamma_09_RefArray = spi_gamma_09_RefArray, spi_gamma_09_YYYYMMDD_Of_RefArray = spi_gamma_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_12_RefFileName, spi_gamma_12_RefArray = spi_gamma_12_RefArray, spi_gamma_12_YYYYMMDD_Of_RefArray = spi_gamma_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_24_RefFileName, spi_gamma_24_RefArray = spi_gamma_24_RefArray, spi_gamma_24_YYYYMMDD_Of_RefArray = spi_gamma_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_36_RefFileName, spi_gamma_36_RefArray = spi_gamma_36_RefArray, spi_gamma_36_YYYYMMDD_Of_RefArray = spi_gamma_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_48_RefFileName, spi_gamma_48_RefArray = spi_gamma_48_RefArray, spi_gamma_48_YYYYMMDD_Of_RefArray = spi_gamma_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_60_RefFileName, spi_gamma_60_RefArray = spi_gamma_60_RefArray, spi_gamma_60_YYYYMMDD_Of_RefArray = spi_gamma_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_gamma_72_RefFileName, spi_gamma_72_RefArray = spi_gamma_72_RefArray, spi_gamma_72_YYYYMMDD_Of_RefArray = spi_gamma_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(spi_pearson_01_RefFileName, spi_pearson_01_RefArray = spi_pearson_01_RefArray, spi_pearson_01_YYYYMMDD_Of_RefArray = spi_pearson_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_02_RefFileName, spi_pearson_02_RefArray = spi_pearson_02_RefArray, spi_pearson_02_YYYYMMDD_Of_RefArray = spi_pearson_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_03_RefFileName, spi_pearson_03_RefArray = spi_pearson_03_RefArray, spi_pearson_03_YYYYMMDD_Of_RefArray = spi_pearson_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_06_RefFileName, spi_pearson_06_RefArray = spi_pearson_06_RefArray, spi_pearson_06_YYYYMMDD_Of_RefArray = spi_pearson_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_09_RefFileName, spi_pearson_09_RefArray = spi_pearson_09_RefArray, spi_pearson_09_YYYYMMDD_Of_RefArray = spi_pearson_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_12_RefFileName, spi_pearson_12_RefArray = spi_pearson_12_RefArray, spi_pearson_12_YYYYMMDD_Of_RefArray = spi_pearson_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_24_RefFileName, spi_pearson_24_RefArray = spi_pearson_24_RefArray, spi_pearson_24_YYYYMMDD_Of_RefArray = spi_pearson_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_36_RefFileName, spi_pearson_36_RefArray = spi_pearson_36_RefArray, spi_pearson_36_YYYYMMDD_Of_RefArray = spi_pearson_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_48_RefFileName, spi_pearson_48_RefArray = spi_pearson_48_RefArray, spi_pearson_48_YYYYMMDD_Of_RefArray = spi_pearson_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_60_RefFileName, spi_pearson_60_RefArray = spi_pearson_60_RefArray, spi_pearson_60_YYYYMMDD_Of_RefArray = spi_pearson_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(spi_pearson_72_RefFileName, spi_pearson_72_RefArray = spi_pearson_72_RefArray, spi_pearson_72_YYYYMMDD_Of_RefArray = spi_pearson_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(pet_01_RefFileName, pet_01_RefArray = pet_01_RefArray, pet_01_YYYYMMDD_Of_RefArray = pet_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_02_RefFileName, pet_02_RefArray = pet_02_RefArray, pet_02_YYYYMMDD_Of_RefArray = pet_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_03_RefFileName, pet_03_RefArray = pet_03_RefArray, pet_03_YYYYMMDD_Of_RefArray = pet_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_06_RefFileName, pet_06_RefArray = pet_06_RefArray, pet_06_YYYYMMDD_Of_RefArray = pet_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_09_RefFileName, pet_09_RefArray = pet_09_RefArray, pet_09_YYYYMMDD_Of_RefArray = pet_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_12_RefFileName, pet_12_RefArray = pet_12_RefArray, pet_12_YYYYMMDD_Of_RefArray = pet_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_24_RefFileName, pet_24_RefArray = pet_24_RefArray, pet_24_YYYYMMDD_Of_RefArray = pet_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_36_RefFileName, pet_36_RefArray = pet_36_RefArray, pet_36_YYYYMMDD_Of_RefArray = pet_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_48_RefFileName, pet_48_RefArray = pet_48_RefArray, pet_48_YYYYMMDD_Of_RefArray = pet_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_60_RefFileName, pet_60_RefArray = pet_60_RefArray, pet_60_YYYYMMDD_Of_RefArray = pet_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(pet_72_RefFileName, pet_72_RefArray = pet_72_RefArray, pet_72_YYYYMMDD_Of_RefArray = pet_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(prcp_01_RefFileName, prcp_01_RefArray = prcp_01_RefArray, prcp_01_YYYYMMDD_Of_RefArray = prcp_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_02_RefFileName, prcp_02_RefArray = prcp_02_RefArray, prcp_02_YYYYMMDD_Of_RefArray = prcp_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_03_RefFileName, prcp_03_RefArray = prcp_03_RefArray, prcp_03_YYYYMMDD_Of_RefArray = prcp_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_06_RefFileName, prcp_06_RefArray = prcp_06_RefArray, prcp_06_YYYYMMDD_Of_RefArray = prcp_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_09_RefFileName, prcp_09_RefArray = prcp_09_RefArray, prcp_09_YYYYMMDD_Of_RefArray = prcp_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_12_RefFileName, prcp_12_RefArray = prcp_12_RefArray, prcp_12_YYYYMMDD_Of_RefArray = prcp_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_24_RefFileName, prcp_24_RefArray = prcp_24_RefArray, prcp_24_YYYYMMDD_Of_RefArray = prcp_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_36_RefFileName, prcp_36_RefArray = prcp_36_RefArray, prcp_36_YYYYMMDD_Of_RefArray = prcp_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_48_RefFileName, prcp_48_RefArray = prcp_48_RefArray, prcp_48_YYYYMMDD_Of_RefArray = prcp_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_60_RefFileName, prcp_60_RefArray = prcp_60_RefArray, prcp_60_YYYYMMDD_Of_RefArray = prcp_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(prcp_72_RefFileName, prcp_72_RefArray = prcp_72_RefArray, prcp_72_YYYYMMDD_Of_RefArray = prcp_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(tavg_01_RefFileName, tavg_01_RefArray = tavg_01_RefArray, tavg_01_YYYYMMDD_Of_RefArray = tavg_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_02_RefFileName, tavg_02_RefArray = tavg_02_RefArray, tavg_02_YYYYMMDD_Of_RefArray = tavg_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_03_RefFileName, tavg_03_RefArray = tavg_03_RefArray, tavg_03_YYYYMMDD_Of_RefArray = tavg_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_06_RefFileName, tavg_06_RefArray = tavg_06_RefArray, tavg_06_YYYYMMDD_Of_RefArray = tavg_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_09_RefFileName, tavg_09_RefArray = tavg_09_RefArray, tavg_09_YYYYMMDD_Of_RefArray = tavg_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_12_RefFileName, tavg_12_RefArray = tavg_12_RefArray, tavg_12_YYYYMMDD_Of_RefArray = tavg_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_24_RefFileName, tavg_24_RefArray = tavg_24_RefArray, tavg_24_YYYYMMDD_Of_RefArray = tavg_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_36_RefFileName, tavg_36_RefArray = tavg_36_RefArray, tavg_36_YYYYMMDD_Of_RefArray = tavg_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_48_RefFileName, tavg_48_RefArray = tavg_48_RefArray, tavg_48_YYYYMMDD_Of_RefArray = tavg_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_60_RefFileName, tavg_60_RefArray = tavg_60_RefArray, tavg_60_YYYYMMDD_Of_RefArray = tavg_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(tavg_72_RefFileName, tavg_72_RefArray = tavg_72_RefArray, tavg_72_YYYYMMDD_Of_RefArray = tavg_72_YYYYMMDD_Of_RefArray)

np.savez_compressed(tmax_01_RefFileName, tmax_01_RefArray = tmax_01_RefArray, tmax_01_YYYYMMDD_Of_RefArray = tmax_01_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_02_RefFileName, tmax_02_RefArray = tmax_02_RefArray, tmax_02_YYYYMMDD_Of_RefArray = tmax_02_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_03_RefFileName, tmax_03_RefArray = tmax_03_RefArray, tmax_03_YYYYMMDD_Of_RefArray = tmax_03_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_06_RefFileName, tmax_06_RefArray = tmax_06_RefArray, tmax_06_YYYYMMDD_Of_RefArray = tmax_06_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_09_RefFileName, tmax_09_RefArray = tmax_09_RefArray, tmax_09_YYYYMMDD_Of_RefArray = tmax_09_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_12_RefFileName, tmax_12_RefArray = tmax_12_RefArray, tmax_12_YYYYMMDD_Of_RefArray = tmax_12_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_24_RefFileName, tmax_24_RefArray = tmax_24_RefArray, tmax_24_YYYYMMDD_Of_RefArray = tmax_24_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_36_RefFileName, tmax_36_RefArray = tmax_36_RefArray, tmax_36_YYYYMMDD_Of_RefArray = tmax_36_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_48_RefFileName, tmax_48_RefArray = tmax_48_RefArray, tmax_48_YYYYMMDD_Of_RefArray = tmax_48_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_60_RefFileName, tmax_60_RefArray = tmax_60_RefArray, tmax_60_YYYYMMDD_Of_RefArray = tmax_60_YYYYMMDD_Of_RefArray)
np.savez_compressed(tmax_72_RefFileName, tmax_72_RefArray = tmax_72_RefArray, tmax_72_YYYYMMDD_Of_RefArray = tmax_72_YYYYMMDD_Of_RefArray)

print("spei_gamma_01_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_01_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_01_YYYYMMDD_Of_RefArray is ",spei_gamma_01_YYYYMMDD_Of_RefArray)

print("spei_gamma_01_RefArray.shape is ",spei_gamma_01_RefArray.shape)
print("spei_gamma_01_RefArray is ",spei_gamma_01_RefArray)
print("np.amin(np.isnan(spei_gamma_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_01_RefArray),', overall max is ',np.nanmax(spei_gamma_01_RefArray))

print("spei_pearson_01_RefArray.shape is ",spei_pearson_01_RefArray.shape)
print("spei_pearson_01_RefArray is ",spei_pearson_01_RefArray)
print("np.amin(np.isnan(spei_pearson_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_01_RefArray),', overall max is ',np.nanmax(spei_pearson_01_RefArray))

print("spi_gamma_01_RefArray.shape is ",spi_gamma_01_RefArray.shape)
print("spi_gamma_01_RefArray is ",spi_gamma_01_RefArray)
print("np.amin(np.isnan(spi_gamma_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_01_RefArray),', overall max is ',np.nanmax(spi_gamma_01_RefArray))

print("spi_pearson_01_RefArray.shape is ",spi_pearson_01_RefArray.shape)
print("spi_pearson_01_RefArray is ",spi_pearson_01_RefArray)
print("np.amin(np.isnan(spi_pearson_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_01_RefArray),', overall max is ',np.nanmax(spi_pearson_01_RefArray))

print("pet_01_RefArray.shape is ",pet_01_RefArray.shape)
print("pet_01_RefArray is ",pet_01_RefArray)
print("np.amin(np.isnan(pet_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_01_RefArray),', overall max is ',np.nanmax(pet_01_RefArray))

print("prcp_01_RefArray.shape is ",prcp_01_RefArray.shape)
print("prcp_01_RefArray is ",prcp_01_RefArray)
print("np.amin(np.isnan(prcp_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_01_RefArray),', overall max is ',np.nanmax(prcp_01_RefArray))

print("tavg_01_RefArray.shape is ",tavg_01_RefArray.shape)
print("tavg_01_RefArray is ",tavg_01_RefArray)
print("np.amin(np.isnan(tavg_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_01_RefArray),', overall max is ',np.nanmax(tavg_01_RefArray))

print("tmax_01_RefArray.shape is ",tmax_01_RefArray.shape)
print("tmax_01_RefArray is ",tmax_01_RefArray)
print("np.amin(np.isnan(tmax_01_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_01_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_01_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_01_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_01_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_01_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_01_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_01_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_01_RefArray),', overall max is ',np.nanmax(tmax_01_RefArray))

print("spei_gamma_02_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_02_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_02_YYYYMMDD_Of_RefArray is ",spei_gamma_02_YYYYMMDD_Of_RefArray)

print("spei_gamma_02_RefArray.shape is ",spei_gamma_02_RefArray.shape)
print("spei_gamma_02_RefArray is ",spei_gamma_02_RefArray)
print("np.amin(np.isnan(spei_gamma_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_02_RefArray),', overall max is ',np.nanmax(spei_gamma_02_RefArray))

print("spei_pearson_02_RefArray.shape is ",spei_pearson_02_RefArray.shape)
print("spei_pearson_02_RefArray is ",spei_pearson_02_RefArray)
print("np.amin(np.isnan(spei_pearson_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_02_RefArray),', overall max is ',np.nanmax(spei_pearson_02_RefArray))

print("spi_gamma_02_RefArray.shape is ",spi_gamma_02_RefArray.shape)
print("spi_gamma_02_RefArray is ",spi_gamma_02_RefArray)
print("np.amin(np.isnan(spi_gamma_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_02_RefArray),', overall max is ',np.nanmax(spi_gamma_02_RefArray))

print("spi_pearson_02_RefArray.shape is ",spi_pearson_02_RefArray.shape)
print("spi_pearson_02_RefArray is ",spi_pearson_02_RefArray)
print("np.amin(np.isnan(spi_pearson_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_02_RefArray),', overall max is ',np.nanmax(spi_pearson_02_RefArray))

print("pet_02_RefArray.shape is ",pet_02_RefArray.shape)
print("pet_02_RefArray is ",pet_02_RefArray)
print("np.amin(np.isnan(pet_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_02_RefArray),', overall max is ',np.nanmax(pet_02_RefArray))

print("prcp_02_RefArray.shape is ",prcp_02_RefArray.shape)
print("prcp_02_RefArray is ",prcp_02_RefArray)
print("np.amin(np.isnan(prcp_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_02_RefArray),', overall max is ',np.nanmax(prcp_02_RefArray))

print("tavg_02_RefArray.shape is ",tavg_02_RefArray.shape)
print("tavg_02_RefArray is ",tavg_02_RefArray)
print("np.amin(np.isnan(tavg_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_02_RefArray),', overall max is ',np.nanmax(tavg_02_RefArray))

print("tmax_02_RefArray.shape is ",tmax_02_RefArray.shape)
print("tmax_02_RefArray is ",tmax_02_RefArray)
print("np.amin(np.isnan(tmax_02_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_02_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_02_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_02_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_02_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_02_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_02_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_02_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_02_RefArray),', overall max is ',np.nanmax(tmax_02_RefArray))

print("spei_gamma_03_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_03_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_03_YYYYMMDD_Of_RefArray is ",spei_gamma_03_YYYYMMDD_Of_RefArray)

print("spei_gamma_03_RefArray.shape is ",spei_gamma_03_RefArray.shape)
print("spei_gamma_03_RefArray is ",spei_gamma_03_RefArray)
print("np.amin(np.isnan(spei_gamma_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_03_RefArray),', overall max is ',np.nanmax(spei_gamma_03_RefArray))

print("spei_pearson_03_RefArray.shape is ",spei_pearson_03_RefArray.shape)
print("spei_pearson_03_RefArray is ",spei_pearson_03_RefArray)
print("np.amin(np.isnan(spei_pearson_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_03_RefArray),', overall max is ',np.nanmax(spei_pearson_03_RefArray))

print("spi_gamma_03_RefArray.shape is ",spi_gamma_03_RefArray.shape)
print("spi_gamma_03_RefArray is ",spi_gamma_03_RefArray)
print("np.amin(np.isnan(spi_gamma_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_03_RefArray),', overall max is ',np.nanmax(spi_gamma_03_RefArray))

print("spi_pearson_03_RefArray.shape is ",spi_pearson_03_RefArray.shape)
print("spi_pearson_03_RefArray is ",spi_pearson_03_RefArray)
print("np.amin(np.isnan(spi_pearson_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_03_RefArray),', overall max is ',np.nanmax(spi_pearson_03_RefArray))

print("pet_03_RefArray.shape is ",pet_03_RefArray.shape)
print("pet_03_RefArray is ",pet_03_RefArray)
print("np.amin(np.isnan(pet_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_03_RefArray),', overall max is ',np.nanmax(pet_03_RefArray))

print("prcp_03_RefArray.shape is ",prcp_03_RefArray.shape)
print("prcp_03_RefArray is ",prcp_03_RefArray)
print("np.amin(np.isnan(prcp_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_03_RefArray),', overall max is ',np.nanmax(prcp_03_RefArray))

print("tavg_03_RefArray.shape is ",tavg_03_RefArray.shape)
print("tavg_03_RefArray is ",tavg_03_RefArray)
print("np.amin(np.isnan(tavg_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_03_RefArray),', overall max is ',np.nanmax(tavg_03_RefArray))

print("tmax_03_RefArray.shape is ",tmax_03_RefArray.shape)
print("tmax_03_RefArray is ",tmax_03_RefArray)
print("np.amin(np.isnan(tmax_03_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_03_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_03_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_03_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_03_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_03_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_03_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_03_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_03_RefArray),', overall max is ',np.nanmax(tmax_03_RefArray))

print("spei_gamma_06_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_06_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_06_YYYYMMDD_Of_RefArray is ",spei_gamma_06_YYYYMMDD_Of_RefArray)

print("spei_gamma_06_RefArray.shape is ",spei_gamma_06_RefArray.shape)
print("spei_gamma_06_RefArray is ",spei_gamma_06_RefArray)
print("np.amin(np.isnan(spei_gamma_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_06_RefArray),', overall max is ',np.nanmax(spei_gamma_06_RefArray))

print("spei_pearson_06_RefArray.shape is ",spei_pearson_06_RefArray.shape)
print("spei_pearson_06_RefArray is ",spei_pearson_06_RefArray)
print("np.amin(np.isnan(spei_pearson_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_06_RefArray),', overall max is ',np.nanmax(spei_pearson_06_RefArray))

print("spi_gamma_06_RefArray.shape is ",spi_gamma_06_RefArray.shape)
print("spi_gamma_06_RefArray is ",spi_gamma_06_RefArray)
print("np.amin(np.isnan(spi_gamma_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_06_RefArray),', overall max is ',np.nanmax(spi_gamma_06_RefArray))

print("spi_pearson_06_RefArray.shape is ",spi_pearson_06_RefArray.shape)
print("spi_pearson_06_RefArray is ",spi_pearson_06_RefArray)
print("np.amin(np.isnan(spi_pearson_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_06_RefArray),', overall max is ',np.nanmax(spi_pearson_06_RefArray))

print("pet_06_RefArray.shape is ",pet_06_RefArray.shape)
print("pet_06_RefArray is ",pet_06_RefArray)
print("np.amin(np.isnan(pet_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_06_RefArray),', overall max is ',np.nanmax(pet_06_RefArray))

print("prcp_06_RefArray.shape is ",prcp_06_RefArray.shape)
print("prcp_06_RefArray is ",prcp_06_RefArray)
print("np.amin(np.isnan(prcp_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_06_RefArray),', overall max is ',np.nanmax(prcp_06_RefArray))

print("tavg_06_RefArray.shape is ",tavg_06_RefArray.shape)
print("tavg_06_RefArray is ",tavg_06_RefArray)
print("np.amin(np.isnan(tavg_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_06_RefArray),', overall max is ',np.nanmax(tavg_06_RefArray))

print("tmax_06_RefArray.shape is ",tmax_06_RefArray.shape)
print("tmax_06_RefArray is ",tmax_06_RefArray)
print("np.amin(np.isnan(tmax_06_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_06_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_06_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_06_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_06_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_06_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_06_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_06_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_06_RefArray),', overall max is ',np.nanmax(tmax_06_RefArray))

print("spei_gamma_09_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_09_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_09_YYYYMMDD_Of_RefArray is ",spei_gamma_09_YYYYMMDD_Of_RefArray)

print("spei_gamma_09_RefArray.shape is ",spei_gamma_09_RefArray.shape)
print("spei_gamma_09_RefArray is ",spei_gamma_09_RefArray)
print("np.amin(np.isnan(spei_gamma_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_09_RefArray),', overall max is ',np.nanmax(spei_gamma_09_RefArray))

print("spei_pearson_09_RefArray.shape is ",spei_pearson_09_RefArray.shape)
print("spei_pearson_09_RefArray is ",spei_pearson_09_RefArray)
print("np.amin(np.isnan(spei_pearson_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_09_RefArray),', overall max is ',np.nanmax(spei_pearson_09_RefArray))

print("spi_gamma_09_RefArray.shape is ",spi_gamma_09_RefArray.shape)
print("spi_gamma_09_RefArray is ",spi_gamma_09_RefArray)
print("np.amin(np.isnan(spi_gamma_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_09_RefArray),', overall max is ',np.nanmax(spi_gamma_09_RefArray))

print("spi_pearson_09_RefArray.shape is ",spi_pearson_09_RefArray.shape)
print("spi_pearson_09_RefArray is ",spi_pearson_09_RefArray)
print("np.amin(np.isnan(spi_pearson_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_09_RefArray),', overall max is ',np.nanmax(spi_pearson_09_RefArray))

print("pet_09_RefArray.shape is ",pet_09_RefArray.shape)
print("pet_09_RefArray is ",pet_09_RefArray)
print("np.amin(np.isnan(pet_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_09_RefArray),', overall max is ',np.nanmax(pet_09_RefArray))

print("prcp_09_RefArray.shape is ",prcp_09_RefArray.shape)
print("prcp_09_RefArray is ",prcp_09_RefArray)
print("np.amin(np.isnan(prcp_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_09_RefArray),', overall max is ',np.nanmax(prcp_09_RefArray))

print("tavg_09_RefArray.shape is ",tavg_09_RefArray.shape)
print("tavg_09_RefArray is ",tavg_09_RefArray)
print("np.amin(np.isnan(tavg_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_09_RefArray),', overall max is ',np.nanmax(tavg_09_RefArray))

print("tmax_09_RefArray.shape is ",tmax_09_RefArray.shape)
print("tmax_09_RefArray is ",tmax_09_RefArray)
print("np.amin(np.isnan(tmax_09_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_09_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_09_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_09_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_09_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_09_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_09_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_09_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_09_RefArray),', overall max is ',np.nanmax(tmax_09_RefArray))

print("spei_gamma_12_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_12_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_12_YYYYMMDD_Of_RefArray is ",spei_gamma_12_YYYYMMDD_Of_RefArray)

print("spei_gamma_12_RefArray.shape is ",spei_gamma_12_RefArray.shape)
print("spei_gamma_12_RefArray is ",spei_gamma_12_RefArray)
print("np.amin(np.isnan(spei_gamma_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_12_RefArray),', overall max is ',np.nanmax(spei_gamma_12_RefArray))

print("spei_pearson_12_RefArray.shape is ",spei_pearson_12_RefArray.shape)
print("spei_pearson_12_RefArray is ",spei_pearson_12_RefArray)
print("np.amin(np.isnan(spei_pearson_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_12_RefArray),', overall max is ',np.nanmax(spei_pearson_12_RefArray))

print("spi_gamma_12_RefArray.shape is ",spi_gamma_12_RefArray.shape)
print("spi_gamma_12_RefArray is ",spi_gamma_12_RefArray)
print("np.amin(np.isnan(spi_gamma_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_12_RefArray),', overall max is ',np.nanmax(spi_gamma_12_RefArray))

print("spi_pearson_12_RefArray.shape is ",spi_pearson_12_RefArray.shape)
print("spi_pearson_12_RefArray is ",spi_pearson_12_RefArray)
print("np.amin(np.isnan(spi_pearson_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_12_RefArray),', overall max is ',np.nanmax(spi_pearson_12_RefArray))

print("pet_12_RefArray.shape is ",pet_12_RefArray.shape)
print("pet_12_RefArray is ",pet_12_RefArray)
print("np.amin(np.isnan(pet_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_12_RefArray),', overall max is ',np.nanmax(pet_12_RefArray))

print("prcp_12_RefArray.shape is ",prcp_12_RefArray.shape)
print("prcp_12_RefArray is ",prcp_12_RefArray)
print("np.amin(np.isnan(prcp_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_12_RefArray),', overall max is ',np.nanmax(prcp_12_RefArray))

print("tavg_12_RefArray.shape is ",tavg_12_RefArray.shape)
print("tavg_12_RefArray is ",tavg_12_RefArray)
print("np.amin(np.isnan(tavg_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_12_RefArray),', overall max is ',np.nanmax(tavg_12_RefArray))

print("tmax_12_RefArray.shape is ",tmax_12_RefArray.shape)
print("tmax_12_RefArray is ",tmax_12_RefArray)
print("np.amin(np.isnan(tmax_12_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_12_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_12_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_12_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_12_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_12_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_12_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_12_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_12_RefArray),', overall max is ',np.nanmax(tmax_12_RefArray))

print("spei_gamma_24_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_24_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_24_YYYYMMDD_Of_RefArray is ",spei_gamma_24_YYYYMMDD_Of_RefArray)

print("spei_gamma_24_RefArray.shape is ",spei_gamma_24_RefArray.shape)
print("spei_gamma_24_RefArray is ",spei_gamma_24_RefArray)
print("np.amin(np.isnan(spei_gamma_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_24_RefArray),', overall max is ',np.nanmax(spei_gamma_24_RefArray))

print("spei_pearson_24_RefArray.shape is ",spei_pearson_24_RefArray.shape)
print("spei_pearson_24_RefArray is ",spei_pearson_24_RefArray)
print("np.amin(np.isnan(spei_pearson_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_24_RefArray),', overall max is ',np.nanmax(spei_pearson_24_RefArray))

print("spi_gamma_24_RefArray.shape is ",spi_gamma_24_RefArray.shape)
print("spi_gamma_24_RefArray is ",spi_gamma_24_RefArray)
print("np.amin(np.isnan(spi_gamma_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_24_RefArray),', overall max is ',np.nanmax(spi_gamma_24_RefArray))

print("spi_pearson_24_RefArray.shape is ",spi_pearson_24_RefArray.shape)
print("spi_pearson_24_RefArray is ",spi_pearson_24_RefArray)
print("np.amin(np.isnan(spi_pearson_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_24_RefArray),', overall max is ',np.nanmax(spi_pearson_24_RefArray))

print("pet_24_RefArray.shape is ",pet_24_RefArray.shape)
print("pet_24_RefArray is ",pet_24_RefArray)
print("np.amin(np.isnan(pet_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_24_RefArray),', overall max is ',np.nanmax(pet_24_RefArray))

print("prcp_24_RefArray.shape is ",prcp_24_RefArray.shape)
print("prcp_24_RefArray is ",prcp_24_RefArray)
print("np.amin(np.isnan(prcp_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_24_RefArray),', overall max is ',np.nanmax(prcp_24_RefArray))

print("tavg_24_RefArray.shape is ",tavg_24_RefArray.shape)
print("tavg_24_RefArray is ",tavg_24_RefArray)
print("np.amin(np.isnan(tavg_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_24_RefArray),', overall max is ',np.nanmax(tavg_24_RefArray))

print("tmax_24_RefArray.shape is ",tmax_24_RefArray.shape)
print("tmax_24_RefArray is ",tmax_24_RefArray)
print("np.amin(np.isnan(tmax_24_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_24_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_24_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_24_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_24_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_24_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_24_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_24_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_24_RefArray),', overall max is ',np.nanmax(tmax_24_RefArray))

print("spei_gamma_36_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_36_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_36_YYYYMMDD_Of_RefArray is ",spei_gamma_36_YYYYMMDD_Of_RefArray)

print("spei_gamma_36_RefArray.shape is ",spei_gamma_36_RefArray.shape)
print("spei_gamma_36_RefArray is ",spei_gamma_36_RefArray)
print("np.amin(np.isnan(spei_gamma_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_36_RefArray),', overall max is ',np.nanmax(spei_gamma_36_RefArray))

print("spei_pearson_36_RefArray.shape is ",spei_pearson_36_RefArray.shape)
print("spei_pearson_36_RefArray is ",spei_pearson_36_RefArray)
print("np.amin(np.isnan(spei_pearson_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_36_RefArray),', overall max is ',np.nanmax(spei_pearson_36_RefArray))

print("spi_gamma_36_RefArray.shape is ",spi_gamma_36_RefArray.shape)
print("spi_gamma_36_RefArray is ",spi_gamma_36_RefArray)
print("np.amin(np.isnan(spi_gamma_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_36_RefArray),', overall max is ',np.nanmax(spi_gamma_36_RefArray))

print("spi_pearson_36_RefArray.shape is ",spi_pearson_36_RefArray.shape)
print("spi_pearson_36_RefArray is ",spi_pearson_36_RefArray)
print("np.amin(np.isnan(spi_pearson_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_36_RefArray),', overall max is ',np.nanmax(spi_pearson_36_RefArray))

print("pet_36_RefArray.shape is ",pet_36_RefArray.shape)
print("pet_36_RefArray is ",pet_36_RefArray)
print("np.amin(np.isnan(pet_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_36_RefArray),', overall max is ',np.nanmax(pet_36_RefArray))

print("prcp_36_RefArray.shape is ",prcp_36_RefArray.shape)
print("prcp_36_RefArray is ",prcp_36_RefArray)
print("np.amin(np.isnan(prcp_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_36_RefArray),', overall max is ',np.nanmax(prcp_36_RefArray))

print("tavg_36_RefArray.shape is ",tavg_36_RefArray.shape)
print("tavg_36_RefArray is ",tavg_36_RefArray)
print("np.amin(np.isnan(tavg_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_36_RefArray),', overall max is ',np.nanmax(tavg_36_RefArray))

print("tmax_36_RefArray.shape is ",tmax_36_RefArray.shape)
print("tmax_36_RefArray is ",tmax_36_RefArray)
print("np.amin(np.isnan(tmax_36_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_36_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_36_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_36_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_36_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_36_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_36_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_36_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_36_RefArray),', overall max is ',np.nanmax(tmax_36_RefArray))

print("spei_gamma_48_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_48_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_48_YYYYMMDD_Of_RefArray is ",spei_gamma_48_YYYYMMDD_Of_RefArray)

print("spei_gamma_48_RefArray.shape is ",spei_gamma_48_RefArray.shape)
print("spei_gamma_48_RefArray is ",spei_gamma_48_RefArray)
print("np.amin(np.isnan(spei_gamma_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_48_RefArray),', overall max is ',np.nanmax(spei_gamma_48_RefArray))

print("spei_pearson_48_RefArray.shape is ",spei_pearson_48_RefArray.shape)
print("spei_pearson_48_RefArray is ",spei_pearson_48_RefArray)
print("np.amin(np.isnan(spei_pearson_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_48_RefArray),', overall max is ',np.nanmax(spei_pearson_48_RefArray))

print("spi_gamma_48_RefArray.shape is ",spi_gamma_48_RefArray.shape)
print("spi_gamma_48_RefArray is ",spi_gamma_48_RefArray)
print("np.amin(np.isnan(spi_gamma_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_48_RefArray),', overall max is ',np.nanmax(spi_gamma_48_RefArray))

print("spi_pearson_48_RefArray.shape is ",spi_pearson_48_RefArray.shape)
print("spi_pearson_48_RefArray is ",spi_pearson_48_RefArray)
print("np.amin(np.isnan(spi_pearson_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_48_RefArray),', overall max is ',np.nanmax(spi_pearson_48_RefArray))

print("pet_48_RefArray.shape is ",pet_48_RefArray.shape)
print("pet_48_RefArray is ",pet_48_RefArray)
print("np.amin(np.isnan(pet_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_48_RefArray),', overall max is ',np.nanmax(pet_48_RefArray))

print("prcp_48_RefArray.shape is ",prcp_48_RefArray.shape)
print("prcp_48_RefArray is ",prcp_48_RefArray)
print("np.amin(np.isnan(prcp_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_48_RefArray),', overall max is ',np.nanmax(prcp_48_RefArray))

print("tavg_48_RefArray.shape is ",tavg_48_RefArray.shape)
print("tavg_48_RefArray is ",tavg_48_RefArray)
print("np.amin(np.isnan(tavg_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_48_RefArray),', overall max is ',np.nanmax(tavg_48_RefArray))

print("tmax_48_RefArray.shape is ",tmax_48_RefArray.shape)
print("tmax_48_RefArray is ",tmax_48_RefArray)
print("np.amin(np.isnan(tmax_48_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_48_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_48_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_48_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_48_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_48_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_48_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_48_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_48_RefArray),', overall max is ',np.nanmax(tmax_48_RefArray))

print("spei_gamma_60_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_60_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_60_YYYYMMDD_Of_RefArray is ",spei_gamma_60_YYYYMMDD_Of_RefArray)

print("spei_gamma_60_RefArray.shape is ",spei_gamma_60_RefArray.shape)
print("spei_gamma_60_RefArray is ",spei_gamma_60_RefArray)
print("np.amin(np.isnan(spei_gamma_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_60_RefArray),', overall max is ',np.nanmax(spei_gamma_60_RefArray))

print("spei_pearson_60_RefArray.shape is ",spei_pearson_60_RefArray.shape)
print("spei_pearson_60_RefArray is ",spei_pearson_60_RefArray)
print("np.amin(np.isnan(spei_pearson_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_60_RefArray),', overall max is ',np.nanmax(spei_pearson_60_RefArray))

print("spi_gamma_60_RefArray.shape is ",spi_gamma_60_RefArray.shape)
print("spi_gamma_60_RefArray is ",spi_gamma_60_RefArray)
print("np.amin(np.isnan(spi_gamma_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_60_RefArray),', overall max is ',np.nanmax(spi_gamma_60_RefArray))

print("spi_pearson_60_RefArray.shape is ",spi_pearson_60_RefArray.shape)
print("spi_pearson_60_RefArray is ",spi_pearson_60_RefArray)
print("np.amin(np.isnan(spi_pearson_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_60_RefArray),', overall max is ',np.nanmax(spi_pearson_60_RefArray))

print("pet_60_RefArray.shape is ",pet_60_RefArray.shape)
print("pet_60_RefArray is ",pet_60_RefArray)
print("np.amin(np.isnan(pet_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_60_RefArray),', overall max is ',np.nanmax(pet_60_RefArray))

print("prcp_60_RefArray.shape is ",prcp_60_RefArray.shape)
print("prcp_60_RefArray is ",prcp_60_RefArray)
print("np.amin(np.isnan(prcp_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_60_RefArray),', overall max is ',np.nanmax(prcp_60_RefArray))

print("tavg_60_RefArray.shape is ",tavg_60_RefArray.shape)
print("tavg_60_RefArray is ",tavg_60_RefArray)
print("np.amin(np.isnan(tavg_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_60_RefArray),', overall max is ',np.nanmax(tavg_60_RefArray))

print("tmax_60_RefArray.shape is ",tmax_60_RefArray.shape)
print("tmax_60_RefArray is ",tmax_60_RefArray)
print("np.amin(np.isnan(tmax_60_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_60_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_60_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_60_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_60_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_60_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_60_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_60_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_60_RefArray),', overall max is ',np.nanmax(tmax_60_RefArray))

print("spei_gamma_72_YYYYMMDD_Of_RefArray.shape is ",spei_gamma_72_YYYYMMDD_Of_RefArray.shape)
print("spei_gamma_72_YYYYMMDD_Of_RefArray is ",spei_gamma_72_YYYYMMDD_Of_RefArray)

print("spei_gamma_72_RefArray.shape is ",spei_gamma_72_RefArray.shape)
print("spei_gamma_72_RefArray is ",spei_gamma_72_RefArray)
print("np.amin(np.isnan(spei_gamma_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_gamma_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_gamma_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_gamma_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_gamma_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_gamma_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_gamma_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_gamma_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_gamma_72_RefArray),', overall max is ',np.nanmax(spei_gamma_72_RefArray))

print("spei_pearson_72_RefArray.shape is ",spei_pearson_72_RefArray.shape)
print("spei_pearson_72_RefArray is ",spei_pearson_72_RefArray)
print("np.amin(np.isnan(spei_pearson_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spei_pearson_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spei_pearson_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spei_pearson_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spei_pearson_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spei_pearson_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spei_pearson_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spei_pearson_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spei_pearson_72_RefArray),', overall max is ',np.nanmax(spei_pearson_72_RefArray))

print("spi_gamma_72_RefArray.shape is ",spi_gamma_72_RefArray.shape)
print("spi_gamma_72_RefArray is ",spi_gamma_72_RefArray)
print("np.amin(np.isnan(spi_gamma_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_gamma_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_gamma_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_gamma_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_gamma_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_gamma_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_gamma_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_gamma_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_gamma_72_RefArray),', overall max is ',np.nanmax(spi_gamma_72_RefArray))

print("spi_pearson_72_RefArray.shape is ",spi_pearson_72_RefArray.shape)
print("spi_pearson_72_RefArray is ",spi_pearson_72_RefArray)
print("np.amin(np.isnan(spi_pearson_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(spi_pearson_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(spi_pearson_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(spi_pearson_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(spi_pearson_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(spi_pearson_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(spi_pearson_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(spi_pearson_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(spi_pearson_72_RefArray),', overall max is ',np.nanmax(spi_pearson_72_RefArray))

print("pet_72_RefArray.shape is ",pet_72_RefArray.shape)
print("pet_72_RefArray is ",pet_72_RefArray)
print("np.amin(np.isnan(pet_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(pet_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(pet_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(pet_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(pet_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(pet_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(pet_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(pet_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(pet_72_RefArray),', overall max is ',np.nanmax(pet_72_RefArray))

print("prcp_72_RefArray.shape is ",prcp_72_RefArray.shape)
print("prcp_72_RefArray is ",prcp_72_RefArray)
print("np.amin(np.isnan(prcp_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(prcp_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(prcp_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(prcp_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(prcp_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(prcp_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(prcp_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(prcp_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(prcp_72_RefArray),', overall max is ',np.nanmax(prcp_72_RefArray))

print("tavg_72_RefArray.shape is ",tavg_72_RefArray.shape)
print("tavg_72_RefArray is ",tavg_72_RefArray)
print("np.amin(np.isnan(tavg_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tavg_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tavg_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tavg_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tavg_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tavg_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tavg_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tavg_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tavg_72_RefArray),', overall max is ',np.nanmax(tavg_72_RefArray))

print("tmax_72_RefArray.shape is ",tmax_72_RefArray.shape)
print("tmax_72_RefArray is ",tmax_72_RefArray)
print("np.amin(np.isnan(tmax_72_RefArray).sum(axis=0)) is ",np.amin(np.isnan(tmax_72_RefArray).sum(axis=0)))
print("np.amax(np.isnan(tmax_72_RefArray).sum(axis=0)) is ",np.amax(np.isnan(tmax_72_RefArray).sum(axis=0)))
print("np.amin(np.isnan(tmax_72_RefArray).sum(axis=1)) is ",np.amin(np.isnan(tmax_72_RefArray).sum(axis=1)))
print("np.amax(np.isnan(tmax_72_RefArray).sum(axis=1)) is ",np.amax(np.isnan(tmax_72_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(tmax_72_RefArray),', overall max is ',np.nanmax(tmax_72_RefArray))


