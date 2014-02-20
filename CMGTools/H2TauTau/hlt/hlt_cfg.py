import copy
import os 
import CMGTools.RootTools.fwlite.Config as cfg
import itertools
# from CMGTools.Production.getFiles import getFiles

def myGetFiles(dataset, user, pattern) :
  import subprocess
  command = '/afs/cern.ch/project/eos/installation/0.3.4/bin/eos.select ls /store/cmst3/user/{USR}/{DTS}'.format(USR=user, DTS=dataset)
  cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  return ['root://eoscms//eos/cms/store/cmst3/user/{USR}/{DTS}/%s'.format(USR=user, DTS=dataset) % line.rstrip() for line in cmd.stdout]

eventSelector = cfg.Analyzer(
    'EventSelector',
    toSelect = [
    ]
    )

triggerAna = cfg.Analyzer(
    'hltTauPat' ,
    pt                = 0.,  ### same tau pt cut for both
    eta               = 999, ### same |eta| for both taus
    m_min             = 0,
    m_max             = 99999,
    iso_cut_tau       = 2.0,
    iso_cut_muon      = 2.0,
    filename          = 'myoutput.root',
    diLeptonCutString = '',
    )
    
###################################################
###                PICK UP FILES                ###
###################################################
data = cfg.DataComponent(
  name = 'data',
  files = [],
  intLumi = 7369.,  # pixel lumi 17/9/2013
  triggers = [],
  )

data.files = myGetFiles('/HLTTau_v2', 'manzoni', 'patTuple_final_.*root')
data.nGenEvents  = 1.
data.xSection    = 1.
data.splitFactor = 10

# data = cfg.DataComponent(
#   name = 'data',
#   files = [],
#   intLumi = 7369.,  # pixel lumi 17/9/2013
#   triggers = [],
#   )
# 
# data.files = myGetFiles('/', 'manzoni', 'patTuple.*root')
# data.nGenEvents  = 1.
# data.xSection    = 1.
# data.splitFactor = 10

###################################################
###             SET COMPONENTS BY HAND          ###
###################################################
selectedComponents  = [data]
for c in selectedComponents : c.splitFactor *= 5

###################################################
###                    SEQUENCE                 ###
###################################################
sequence = cfg.Sequence( [
    #eventSelector,
    triggerAna,
    ] )

###################################################
###            SET BATCH OR LOCAL               ###
###################################################
test = 1   # test = 0 run on batch, test = 1 run locally
if test == 1:
  cache = True
  comp = data
  selectedComponents = [comp]
  comp.splitFactor = 1
  comp.files = comp.files[:10]

print [s.name for s in selectedComponents]
    
config = cfg.Config( components = selectedComponents,
                     sequence   = sequence )
