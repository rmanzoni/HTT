import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0_1377467540/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_16_1_txP.root', 
        '/store/cmst3/group/cmgtools/CMG/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_17_1_Q6V.root', 
        '/store/cmst3/group/cmgtools/CMG/SUSYBBHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_18_1_tw3.root')
)

