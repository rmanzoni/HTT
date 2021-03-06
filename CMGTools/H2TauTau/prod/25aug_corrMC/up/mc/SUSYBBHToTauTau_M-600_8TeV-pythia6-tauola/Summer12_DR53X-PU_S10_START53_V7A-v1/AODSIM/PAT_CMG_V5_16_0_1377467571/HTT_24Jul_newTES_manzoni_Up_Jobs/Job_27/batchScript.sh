#!/bin/bash
# sets the queue
#BSUB -q 8nm

echo 'environment:'
echo
env
ulimit -v 3000000
echo 'copying job dir to worker'
cd $CMSSW_BASE/src
eval `scramv1 ru -sh`
cd -
cp -rf $LS_SUBCWD .
ls
cd `find . -type d | grep /`
echo 'running'
cmsRun run_cfg.py
if [ $? != 0 ]; then
    echo wrong exit code! removing all root files
    rm *.root
    exit 1 
fi
echo 'sending the job directory back'

for file in *.root; do
newFileName=`echo $file | sed -r -e 's/\./_27\./'`
fullFileName=/store/cmst3/user/manzoni/CMG/SUSYBBHToTauTau_M-600_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_24Jul_newTES_manzoni_Up/$newFileName
#this does cmsStage, but with retries
cmsStageWithFailover.py -f $file $fullFileName
#write the files as user readable but not writable
eos chmod 755 /eos/cms/$fullFileName
done
rm *.root
cp -rf * $LS_SUBCWD
