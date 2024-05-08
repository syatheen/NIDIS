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

Running the single workflow for indicator 52 for example:

```bash
PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/nclimgrid/SpatialResolution_CLI.py NLDAS2 --indicator 52
```