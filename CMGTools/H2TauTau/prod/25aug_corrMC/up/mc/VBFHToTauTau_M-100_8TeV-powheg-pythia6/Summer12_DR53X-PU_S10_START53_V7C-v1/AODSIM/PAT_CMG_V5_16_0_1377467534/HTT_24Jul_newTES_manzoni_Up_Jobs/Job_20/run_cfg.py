import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/VBFHToTauTau_M-100_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0_1377467534/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/VBFHToTauTau_M-100_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_96_1_XP0.root', 
        '/store/cmst3/group/cmgtools/CMG/VBFHToTauTau_M-100_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_97_1_ePG.root', 
        '/store/cmst3/group/cmgtools/CMG/VBFHToTauTau_M-100_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_98_1_DRQ.root', 
        '/store/cmst3/group/cmgtools/CMG/VBFHToTauTau_M-100_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_99_1_LjB.root', 
        '/store/cmst3/group/cmgtools/CMG/VBFHToTauTau_M-100_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_9_1_K9a.root')
)
