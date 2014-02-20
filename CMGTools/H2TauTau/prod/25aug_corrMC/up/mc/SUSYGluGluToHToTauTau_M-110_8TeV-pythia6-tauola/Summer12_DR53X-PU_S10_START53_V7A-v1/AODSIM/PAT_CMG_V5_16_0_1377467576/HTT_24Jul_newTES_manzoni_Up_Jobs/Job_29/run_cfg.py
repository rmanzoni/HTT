import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/SUSYGluGluToHToTauTau_M-110_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0_1377467576/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/SUSYGluGluToHToTauTau_M-110_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_85_1_6ti.root', 
        '/store/cmst3/group/cmgtools/CMG/SUSYGluGluToHToTauTau_M-110_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_87_1_q9z.root', 
        '/store/cmst3/group/cmgtools/CMG/SUSYGluGluToHToTauTau_M-110_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_88_1_gc1.root')
)

