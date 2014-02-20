import FWCore.ParameterSet.Config as cms

import os,sys
sys.path.append('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/H2TauTau/prod/25aug_corrMC/up/mc/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/PAT_CMG_V5_16_0_1377544840/HTT_24Jul_newTES_manzoni_Up_Jobs')
from base_cfg import *
process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/user/cmgtools/CMG/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1548.root', 
        '/store/cmst3/user/cmgtools/CMG/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1549.root', 
        '/store/cmst3/user/cmgtools/CMG/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_155.root', 
        '/store/cmst3/user/cmgtools/CMG/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1550.root', 
        '/store/cmst3/user/cmgtools/CMG/DY2JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1551.root')
)

