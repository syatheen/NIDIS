# Multiprocessing version

The challenge of using multi-prog for programs that in many cases last less than 20s
is the addition of overhead from the scheduler. In many cases, this overhead can be
double the time requested. We need to encapsulate this jobs within nodes to make the
overhead be less than the requested time.

Given the limit of 6,000 simultaneous cores per user dedicated to this, the following
processing architecture is suggested.

We will use Python multiprocessing to distribute the jobs across the different tasks.
Given the total number of processes which is 469,908, we will divide and conquer across
nodes to speed up the processing time.

The first phase was to understand how many jobs per node we could fit. Instead of 9 like
you were invoking before, we can actually invoke 100 jobs per Milan node without running
out of memory. Thus the steps to make this process faster are outlined below.

This is by no means the end architecture, but it is a way of getting this process to run
faster in the limited amount of time we have available at this time.

Steps are outlined below:

1. Generate configuration files: We have been generating 513 tasks per task file,
we will increase that to 10000. For now, since I am not sure of the origin of
how the sbatch pixels were split, we will continue using them as 513 pixels per
file, but just reading more of them in parallel.

```bash
bash 1_create_tasks_file.sh NClcFI_ClmGrd1D_V2b_1DFeatSeas_Parameters.conf
```

2. Run bash script that will then call the sbatch command: We have a bash script
that calls the respective sbatch commands that will distribute the processes.
We can have a total of 47 nodes if we max out on the cores we are allowed to use
at the same time.

```bash

```

3. Each slurm job will call a python multiprocessing wrapper, this wrapper will
read a configuration file, will call 100 jobs at the same time, and will
continue to do so iteratively until no processes are left.

Just for reference, the Python script is called as follows:

```bash
python 
```

## Simple Development Script

```bash
python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_V2.py N N 20060103 20191231 USDM CONUS 113 1 37 1 W
```
