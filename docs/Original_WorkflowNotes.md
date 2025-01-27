# Processing Notes

## Indicators 52 to 63

The script is executed by:

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh
```

This script is called by PODS through the following script:

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/sbatchpods_InfArrs_ClmDvs_DlyCllToMnthly_5_50AdjustTo0.sh
```

That then calls the following script /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_5_50AdjustTo0 with the contents from below. I need to summarize these contents from the
following files:

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_3_50AdjustTo0
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_4_50AdjustTo0
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_5_50AdjustTo0
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_6_50AdjustTo0
```

Each one

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_3_50AdjustTo0
Mosaic SWE
Mosaic EVAP
Noah SWE
Noah EVAP
SAC SWE
SAC EVAP
```

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_4_50AdjustTo0
VIC SWE
VIC EVAP
```

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_5_50AdjustTo0
Mosaic RUN
Mosaic STRM
Noah RUN
Noah STRM
SAC RUN
SAC STRM
```

```bash
/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_6_50AdjustTo0
VIC RUN
VIC STRM
```

Do we really need to run: Mosaic STRM, Noah STRM, SAC STRM. VIC STRM.


```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 8
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 9
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 10
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 11
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 1980 12
```

and ends with:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic RUN 2021 8
```

But then has SRTM indications as well:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 8
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 9
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 10
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 11
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 1980 12
```

which ends with:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2020 12
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Mosaic STRM 2021 8
```

and then has more from the Noah side:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 8
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 9
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 10
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 11
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 1980 12
```

which finishes with:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah RUN 2021 8
```

And then Noah SRTM:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 8
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 9
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 10
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 11
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 1980 12
```

which ends with:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh Noah STRM 2021 8
```

And then:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 8
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 9
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 10
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 11
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 1980 12
```

which ends with:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC RUN 2021 8
```

which is followed by:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 8
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 9
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 10
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 11
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 1980 12
```

which ends with:

```bash
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 1
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 2
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 3
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 4
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 5
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 6
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 7
./RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh SAC STRM 2021 8
```

- Replace 

[4/29 5:01 PM] Yatheendradas, Soni (GSFC-619.0)[UNIV OF MARYLAND COLLEGE PARK]
Inside /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily :
[4/29 5:01 PM] Yatheendradas, Soni (GSFC-619.0)[UNIV OF MARYLAND COLLEGE PARK]
diff -bw InfoArrays_ClimDivs_DailyCollToMonthly_50AdjustTo0.py InfoArrays_ClimDivs_DailyCollToMonthly.py
[4/29 5:03 PM] Yatheendradas, Soni (GSFC-619.0)[UNIV OF MARYLAND COLLEGE PARK]
InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly.py
[4/29 5:03 PM] Yatheendradas, Soni (GSFC-619.0)[UNIV OF MARYLAND COLLEGE PARK]
After ln 98 of RefArrayForPrcntl
add change to line 99

## Indicators 64 to 67


We need to specify the HUC value differently here
We want the 04 arch
Depending on the extra argument, it will take the filename from that
Test04 is the filename that they start with

The 50’s upper limits needs to be changed
Replicate what climdiv has for this indicator, into the climgrid for this indicator
Checking of the huc filename exists

Does the input data file exist and the huc file exists
Open the extra huc filename
Delete the np.flip(HUCImageInfo, axis=1) line

Extra lines are reading HUCImageInfo
One flip in the image
Uniq_posHUCs line and for loop needs to be included


## Indicators 70 to 71 (ESI Indicators)

NLDAS 2 Daily, NclimDiv are similar

The shape file is different between the NClimdiv and nclimgrid
Things chance under the for loop
Temporary output file is written
Reopen the temporary rasters 


ESI NClimDiv
Add the grid properties
Inside for which dates Star for loop
Gdalwarp for nclimgrid instead of geopandas

We will use NLDAS2 Daily as our base for NClimGrid
We will modify the ESI from NCLIMDIV to MIMIC the NLDAS Daily NCLIMGRID CHANGES
The main thing is the resolution variables and the for loop change that will now use gdalwarp

NLDAS2:
 
nClimDiv: /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/InfoArrays_ClimDivs_DailyCollToMonthly.py
 
nClimGrid: /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/InfoArrays_gdalWarp_ClimGr_DailyCollToMonthly.py
 
Main differences:
1. nClimGrid file specification lines (6 of them)
2. The portion inside and after the 'if IfTifFileExists:' line


———————

Longer duration code

Use the same script from climdiv, and just change the filename difference
1DClimGrid somewhere in the script
Take the script filename from the spreadsheet


——————

Weekly resolution code

Getting the differences of the precip ones
When writing the climgrid code
The heart of the code for climdiv 

4 week ESI array
12 week ESI array

ESI weekly resolution code; /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/PrepRefArraysFromInfoArrays_ESI_Multiweek.py

————————
