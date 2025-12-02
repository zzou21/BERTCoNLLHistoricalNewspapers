#!/bin/bash
#SBATCH -J mistralCallTest
#SBATCH --output=output.out
#SBATCH --error=error.err
#SBATCH -p scavenger-gpu        
#SBATCH --gres=gpu:4
#SBATCH --mem=10G
#SBATCH -t 1:00:00

# Initialization
source ~/.bashrc
conda activate mistral
cd $SLURM_SUBMIT_DIR

python mistralAPICall.py