#!/usr/bin/env bash
#PrimaryDatasetFraction: 0.031820
#FilesGood: 3
#FilesBad: 0
# 1 jobs found in state Exception
pushd /afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/WH_ZH_TTH_HToTauTau_M-90_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0_1377467471/HTT_24Jul_newTES_manzoni_Up_Jobs/Job_1; bsub -q 8nh -J RESUB -u cmgtoolslsf@gmail.com  < ./batchScript.sh | tee job_id_resub.txt; popd
# 3 jobs found in state VALID
