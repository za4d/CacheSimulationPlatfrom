#!/bin/bash
#
#SBATCH --job-name=run # Job name for tracking
#SBATCH --partition=cpu-batch  # Partition you wish to use (see above for list)
#SBATCH --cpus-per-task=20     # number of CPU cores used by your job
#SBATCH --mem=1000             # RAM in MB needed in total (also available --mem-per-cpu)
#SBATCH --time=12:00:00        # Job limited to 12 hours (see sinfo for maximums)
#
#SBATCH --mail-type=END,FAIL,TIME_LIMIT_80 # Events to send email on, remove if you don't want this
#SBATCH --output=joboutput_%j.out # Standard out from your job
#SBATCH --error=joboutput_%j.err  # Standard error from your job

## Execute your program(s) ##

srun python3 src/test_Kudu.py
