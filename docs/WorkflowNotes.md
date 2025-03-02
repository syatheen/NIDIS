# Indicators Data Processing

We document here the data preprocessing steps for each indicator.
This document only includes the steps needed for processing,
while the document with name Original_WorkflowNotes.md includes
the documentation from the original workflow.

## Indicators 52 to 63

The following combinations are needed for each indicator between
52 to 63. Each combination is given to the necessary scripts. The
time range starts on 1980-1 and ends on 2021-8, with a month value
for each year interval.

Make sure the original GeoTIFF files have been unpacked.

| Indicator #  | ArgLSM         | ArgVariable   |
| :---:        |     :---:      |        :---:  |
| 52   | Mosaic     | EVAP      |
| 53   | Noah       | EVAP      |
| 54   | SAC        | EVAP      |
| 55   | VIC        | EVAP      |
| 56   | Mosaic     | SWE       |
| 57   | Noah       | SWE       |
| 58   | SAC        | SWE       |
| 59   | VIC        | SWE       |
| 60   | Mosaic     | RUN       |
| 61   | Noah       | RUN       |
| 62   | SAC        | RUN       |
| 63   | VIC        | RUN       |

### Spatial Resolution

Running the single workflow for indicator 52 for example:

```bash
PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/nclimgrid/SpatialResolution_CLI.py NLDAS2 --indicator 52 --lsm Mosaic --variable EVAP
```

We use this same arguments to go over each one of the other indicators.

### Weekly Resolution

The next step belongs to weekly resolution. To run this on the current workflow we run the following command:

```bash
PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/nclimgrid/WeeklyResolution_CLI.py -i 53
```

This can be submitted via slurm with:

```bash
sbatch sbatch_weekly_resolution.sh 53
```

### Percentile Creation

The next step belong to the percentile creation code. To run this on the current workflow we run the following command:

```bash
PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/nclimgrid/PercentileCreation_CLI.py --indicator 53
```

This can be submitted via slurm with:

```bash
sbatch sbatch_percentile_creation.sh 53
```

## Indicators 64 to 67

The following combinations are needed for each indicator between
64 to 67. Each combination is given to the necessary scripts. The
time range starts on 1980-1 and ends on 2021-8, with a month value
for each year interval.

Make sure the original GeoTIFF files have been unpacked and that you
have access to the test04.tif HUC filename.

| Indicator #  | ArgLSM         | ArgVariable   | HUC  |
| :---:        |     :---:      |        :---:  |:---: |
| 64           | Mosaic         | STRM          | H04  |
| 65           | Noah           | STRM          | H04  |
| 66           | SAC            | STRM          | H04  |
| 67           | VIC            | STRM          | H04  |

Each one of those entries is ran with H04 as the HUC parameter. An example
if this run is listed below:

```bash
PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/nclimgrid/SpatialResolution_CLI.py NLDAS2HUC --indicator 64 --lsm Mosaic --variable STRM --huc-value H04
```
