import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/VBF_HToTauTau_M-135_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0_1377467535/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/VBF_HToTauTau_M-135_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_37_1_CVF.root', 
        '/store/cmst3/group/cmgtools/CMG/VBF_HToTauTau_M-135_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_38_1_Ftv.root', 
        '/store/cmst3/group/cmgtools/CMG/VBF_HToTauTau_M-135_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_39_1_pd3.root', 
        '/store/cmst3/group/cmgtools/CMG/VBF_HToTauTau_M-135_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_3_1_PNr.root', 
        '/store/cmst3/group/cmgtools/CMG/VBF_HToTauTau_M-135_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_40_1_gbu.root')
)
