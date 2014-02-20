import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/WH_ZH_TTH_HToTauTau_M-135_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0_1377467456/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/WH_ZH_TTH_HToTauTau_M-135_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_1_2_rlM.root', 
        '/store/cmst3/group/cmgtools/CMG/WH_ZH_TTH_HToTauTau_M-135_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_20_1_1Kw.root', 
        '/store/cmst3/group/cmgtools/CMG/WH_ZH_TTH_HToTauTau_M-135_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_21_1_F9B.root', 
        '/store/cmst3/group/cmgtools/CMG/WH_ZH_TTH_HToTauTau_M-135_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_2_1_5Ch.root', 
        '/store/cmst3/group/cmgtools/CMG/WH_ZH_TTH_HToTauTau_M-135_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/PAT_CMG_V5_16_0/cmgTuple_3_1_F6K.root')
)

