import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/GluGluToHToTauTau_M-105_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0_1377467478/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-105_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_37_1_k4j.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-105_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_38_1_xKq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-105_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_39_1_Erx.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-105_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_3_1_132.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-105_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_40_1_wWQ.root')
)
