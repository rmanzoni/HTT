import os
import subprocess

wd     = os.getcwd()
max    = 30
queue  = '1nh'
newfol = 'ggh125_12_5_percent_smear3'
os.system('mkdir {PWD}/{NEW}'.format(PWD=wd,NEW=newfol))

for i in range(max+1) :
  command = '#!/bin/bash\n\
             cd $CMSSW_BASE/src\n\
             eval `scramv1 ru -sh`\n\
             echo \'running\'\n\
             nsvfitStandalone {PWD}/H2TauTauTreeProducerTauTau_ggh125_tree.root H2TauTauTreeProducerTauTau {MAX} {ITER} {PWD}/{NEW}/ggh125_{ITER}.root \n'.format(PWD=wd , NEW=newfol, MAX=str(max) , ITER=str(i) ).replace('  ','')
  
  fname = '/'.join([wd,newfol,'sub_'+str(i)+'.sh'])
  f1    = open(fname, 'w+')
  print >> f1 , command
  os.system('chmod 755 {FILE}'.format(FILE=fname)) 
  f1.close()

for i in range(max+1) :
  fname = '/'.join([wd,newfol,'sub_'+str(i)+'.sh'])
  subprocess.Popen(['bsub -u paoisdapsoid -q {QUEUE} < {FILE}'.format(QUEUE=queue,FILE=fname)], stdout=subprocess.PIPE, shell=True)
 