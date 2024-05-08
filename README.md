# National Integrated Drought Information System (NIDIS)

The following software serves as an operational version for the NIDIS map outputs.
Internal progress sheet can be located [here](https://nasa-my.sharepoint.com/:x:/r/personal/jacaraba_ndc_nasa_gov/Documents/WorkDocuments/Projects/ILAB/2024-SONI-Parallel/Indicators_Data_Dictionary_nClimGrid_Resolution_ILAB.xlsx?d=w4d5e4812cb06468d819235dcd8268571&csf=1&web=1&e=cnB6yV).

## RUNS ON DISCOVER

- My current goal is 9 indicators per day completely done so we can finish with the current
outputs in 10 days.

## Background

From Yatheendradas et al. (2023), "Quantifying the Importance of Selected Drought Indicators for the United States Drought Monitor":

Drought maps from the U.S. Drought Monitor and the Objective Short- and Long-Term Drought Indicator Blends and Blend Equivalents are integrated information sources of the different types of drought. Multiple indicators go into creation of these maps, yet it is usually not clear to both public and private stakeholders like local agencies and insurance companies about the importance of any indicator in any region and season to the drought maps. Our study provides such objective information to enable understanding the mechanism and type of drought occurring at a location, season, and possibly event of interest, as well as to potentially aid in better drought monitoring and forecasting using smaller custom sets of indicators.

## Dependencies

Document Python environment creation here:

```bash
```

## Original Workflow

We process the following seasons P U F W A through a series of Python scripts. While we need to add
more background information on this later (we need to ask for the information), here is the summary of
the things that have run:

- Soni Ran: 73 indicators for the A season already done, 20 already done for P U F W
- We need to Run: 113 indicators total for P U F W A
- Right now we can Run: 73 P U F W, where all we need to change is the P U F W

The original script has a single output file per pixel multiplied by 3. Thus we have about
469,908 * 3 small files on discover.

Each single process takes ~10 seconds, 513 tasks per file, each process takes a single CPU.
916 calls to create the task.conf.

Total of 469908 processes to run, 113 indicators and 5 seasons = 113 x 5 seasons. This is for one indicator
season = less than 8 hours is the target, number of pixels = 513. Output directories:

FI1X1_ClmGrd1D_V2b_New
SSiz1X1_ClmGrd1D_V2b_New
WSiz1X1_ClmGrd1D_V2b_New

6 minutes - 50 processes - 1026 pixels
29 min - 90 processes - 10260 pixels
6000 nodes at the same time

Slurm job array, more tasks that can be run at the same time. Only run these many tasks at the same time.
Each task is considered a separate job. It will fit all within a single node.
100 to 200 processes run out of memory.

## Development Workflow

The challenge of using multi-prog for programs that in many cases last less than 20s is the 
addition of overhead from the scheduler. In many cases, this overhead can be double the time 
requested. We need to encapsulate these jobs within nodes to make the overhead be less than 
the requested time. 

 Given the limit of 6,000 simultaneous cores per user dedicated to this, the following processing 
 architecture is suggested. We will use Python multiprocessing to distribute the jobs across the 
 different tasks. Given the total number of processes which is 469,908; we will divide and conquer 
 across nodes to speed up the processing time. 

 The first phase was to understand how many jobs per node we could fit. Instead of 9 like you were 
 invoking before, we can invoke 92 jobs per Milan node without running out of memory (some jobs can 
 fit up to 100). Thus, the steps to make this process faster are outlined below. This is by no means 
 the end architecture, but it is a way of getting this process to run faster in the limited amount 
 of time we have available currently. 

 Steps are outlined below:

1. Generate configuration files: You have been generating 513 tasks per task file, we will increase 
that to 10000. For now, since we are not sure of the origin of how the sbatch pixels were split, we 
will continue using them as 513 pixels per file, but just reading more of them in parallel. This 
allows us to increase the utilization of CPUs per node, increasing the node memory per CPU ratio. 

```bash 
bash 1_create_tasks_file.sh NClcFI_ClmGrd1D_V2b_1DFeatSeas_Parameters.conf 
``` 

At the end of this step, we finish with a total of 916 text files that have the tasks to be distributed 
across nodes. Creating them on the fly like you were doing before creates a big overhead cause by the
 multiple srun calls included in the initial sbatch submission. 

2. Run bash script that will then call the sbatch command: We have a bash script that calls the 
respective sbatch commands that will distribute the processes. We can have a total of 47 nodes if 
we max out on the cores we are allowed to use at the same time. 

```bash 
bash 2_slurm_submission.sh 
``` 

3. Each slurm job will call a python multiprocessing wrapper, this wrapper will read a configuration 
file, will call 100 jobs at the same time, and will continue to do so iteratively until no processes 
are left. Just for reference, the Python script is called as follows: 

```bash 
module load python/GEOSpyD/Min23.5.2-0_py3.11 
source activate /home/jacaraba/.conda/envs/amy-rf 
cd /discover/nobackup/jacaraba/development/benchmark-amy/multiprocessing_version 
python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py 20 40 /discover/nobackup/jacaraba/development/benchmark-amy/multiprocessing_version/tasks 
``` 

## Running the Operational Workflow

To make this workflow operational, we have added the following enhancements:

- Files are merging into a single file per pixel
- Checks for missing files
- Checks for missing data
- Lowers number of inodes
- Multiprocessing implementation (single index, all seasons for a single node)
- Adds postprocessing to the general pipeline

We will use the following directory for intermediate processing:
/discover/nobackup/projects/nca/jacaraba/NIDIS_Runs.

The following are the steps needed to run this workflow operationally. The steps
are outlined in order, and some of them are depedent of the other. These steps
are outlined to run on Discover. Modifications might need to be done if we want to run
this workflow in a different system.

We have two ways of running this workflow now:

- One full node running all 469758 tasks for a single season and a single indicator
  - this option takes about 17 hours for a single indicator, single season
  ```bash
  sbatch sbatch_submission.sh 41 W nca
  ```
- N number of nodes running multiple seasons and a single indicator
  - we will try this option now using 12 nodes at the same time
  ```bash
  bash bash_submission_single_indicator_multi_epoch.sh 43 "P U F W" fame
  ```

### 1. Running Workflow Individually

```bash
PYTHONPATH="/explore/nobackup/people/jacaraba/development/nidis" python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py --indicator 40 --season W --init-task 0 --end-task 5 --output-dir /explore/nobackup/people/jacaraba/projects/NIDIS --step train
```

The default will run all pixels thorugh the same multiprocessing queue:

```bash
PYTHONPATH="/explore/nobackup/people/jacaraba/development/nidis" python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py --indicator 40 --season W --output-dir /explore/nobackup/people/jacaraba/projects/NIDIS --step train
```

Working from discover:

```bash
module load python/GEOSpyD/Min23.5.2-0_py3.11 
source activate /home/jacaraba/.conda/envs/amy-rf 
time PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py --indicator 40 --season W --output-dir /discover/nobackup/projects/nca/jacaraba/NIDIS_Runs --step train --init-task 0 --end-task 10000
```

Or developing locally to avoid output to terminal screen (faster):

```bash
time PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py --indicator 78 --season W --output-dir /discover/nobackup/projects/nca/jacaraba/NIDIS_Runs --step train --init-task 0 --end-task 469758
```

### 2. Running Through Slurm

```bash
bash bash_submission_single_indicator_multi_epoch.sh 9 "A P U F W" fame
bash bash_submission_single_indicator_multi_epoch.sh 10 "A P U F W" fame
```

### 3. Regression Testing

```bash
```

### 4. Postprocessing

```bash
PYTHONPATH="/discover/nobackup/jacaraba/development/nidis" python /discover/nobackup/jacaraba/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py --output-dir /discover/nobackup/projects/fame/jacaraba/NIDIS_Runs --step postprocess --season U F W --indicator 8
```

from Slurm

```bash
sbatch sbatch_submission_single_indicator_multi_epoch_postprocess.sh 43 "P U F W"
```

### 5. Release

```bash
```

## References

- [Quantifying the Importance of Selected Drought Indicators for the United States Drought Monitor](https://journals.ametsoc.org/view/journals/hydr/24/9/JHM-D-22-0180.1.xml)
- [README of Indices](https://portal.nccs.nasa.gov/lisdata_pub/NLDAS/DroughtIndicatorImportanceData/ForSteve/README_Soni.txt)
