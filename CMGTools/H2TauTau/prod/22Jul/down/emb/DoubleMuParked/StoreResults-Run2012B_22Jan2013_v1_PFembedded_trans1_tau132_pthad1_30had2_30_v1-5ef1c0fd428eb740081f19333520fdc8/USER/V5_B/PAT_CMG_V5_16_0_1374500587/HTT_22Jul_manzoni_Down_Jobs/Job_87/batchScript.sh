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
newFileName=`echo $file | sed -r -e 's/\./_87\./'`
fullFileName=/store/cmst3/user/manzoni/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/HTT_22Jul_manzoni_Down/$newFileName
#this does cmsStage, but with retries
cmsStageWithFailover.py -f $file $fullFileName
#write the files as user readable but not writable
eos chmod 755 /eos/cms/$fullFileName
done
rm *.root
cp -rf * $LS_SUBCWD
