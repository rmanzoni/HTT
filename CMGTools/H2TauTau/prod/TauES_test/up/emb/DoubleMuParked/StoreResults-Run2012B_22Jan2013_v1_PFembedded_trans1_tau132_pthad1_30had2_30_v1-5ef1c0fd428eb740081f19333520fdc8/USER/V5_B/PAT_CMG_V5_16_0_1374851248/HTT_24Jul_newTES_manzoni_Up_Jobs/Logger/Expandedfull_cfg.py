import FWCore.ParameterSet.Config as cms

process = cms.Process("H2TAUTAU")

process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring( ('/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_1.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_10.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_100.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_101.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_102.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_103.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_104.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_105.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_106.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_107.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_108.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_109.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_11.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_110.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_111.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_112.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_113.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_114.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_115.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_116.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_117.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_118.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_119.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_12.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_120.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_121.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_122.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_123.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_124.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_125.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_126.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_127.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_128.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_129.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_13.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_130.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_131.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_132.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_133.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_134.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_135.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_136.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_137.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_138.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_139.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_14.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_140.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_141.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_142.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_143.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_144.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_145.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_146.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_147.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_148.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_149.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_15.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_150.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_151.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_152.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_153.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_154.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_155.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_156.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_157.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_158.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_159.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_16.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_160.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_161.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_162.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_163.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_164.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_165.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_166.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_167.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_168.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_169.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_17.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_170.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_171.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_172.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_173.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_174.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_175.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_176.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_177.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_178.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_179.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_18.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_180.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_181.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_182.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_183.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_184.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_185.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_186.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_187.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_188.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_189.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_19.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_190.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_191.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_192.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_193.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_194.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_195.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_196.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_197.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_198.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_199.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_2.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_20.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_200.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_201.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_202.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_203.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_204.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_205.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_206.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_207.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_208.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_209.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_21.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_210.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_211.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_212.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_213.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_214.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_215.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_216.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_217.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_218.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_219.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_22.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_220.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_221.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_222.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_223.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_224.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_225.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_226.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_227.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_228.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_229.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_23.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_230.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_231.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_232.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_233.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_234.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_235.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_236.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_237.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_238.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_239.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_24.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_240.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_241.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_242.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_243.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_244.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_245.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_246.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_247.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_248.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_249.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_25.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_250.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_251.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_252.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_253.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_254.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_255.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_256.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_257.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_258.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_259.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_26.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_260.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_261.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_262.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_263.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_264.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_265.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_266.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_267.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_268.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_269.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_27.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_270.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_271.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_272.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_273.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_274.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_275.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_276.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_277.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_278.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_279.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_28.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_280.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_281.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_282.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_283.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_284.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_285.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_286.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_287.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_288.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_289.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_29.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_290.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_291.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_292.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_293.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_294.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_295.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_296.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_297.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_298.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_299.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_3.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_30.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_300.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_301.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_302.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_303.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_304.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_305.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_306.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_307.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_308.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_309.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_31.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_310.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_311.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_312.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_313.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_314.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_315.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_316.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_317.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_318.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_319.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_32.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_320.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_321.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_322.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_323.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_324.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_325.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_326.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_327.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_328.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_329.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_33.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_330.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_331.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_332.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_333.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_334.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_335.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_336.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_337.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_338.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_339.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_34.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_340.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_341.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_342.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_343.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_344.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_345.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_346.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_347.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_348.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_349.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_35.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_350.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_351.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_352.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_353.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_354.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_355.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_356.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_357.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_358.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_359.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_36.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_360.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_361.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_362.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_363.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_364.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_365.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_366.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_367.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_368.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_369.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_37.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_370.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_371.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_372.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_373.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_374.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_375.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_376.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_377.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_378.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_379.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_38.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_380.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_381.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_39.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_4.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_40.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_41.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_42.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_43.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_44.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_45.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_46.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_47.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_48.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_49.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_5.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_50.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_51.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_52.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_53.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_54.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_55.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_56.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_57.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_58.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_59.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_6.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_60.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_61.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_62.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_63.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_64.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_65.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_66.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_67.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_68.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_69.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_7.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_70.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_71.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_72.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_73.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_74.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_75.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_76.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_77.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_78.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_79.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_8.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_80.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_81.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_82.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_83.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_84.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_85.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_86.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_87.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_88.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_89.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_9.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_90.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_91.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_92.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_93.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_94.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_95.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_96.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_97.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_98.root', 
        '/store/cmst3/user/cmgtools/CMG/DoubleMuParked/StoreResults-Run2012B_22Jan2013_v1_PFembedded_trans1_tau132_pthad1_30had2_30_v1-5ef1c0fd428eb740081f19333520fdc8/USER/V5_B/PAT_CMG_V5_16_0/cmgTuple_99.root' ) ),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange( ("190645:10-190645:110", "190646:1-190646:111", "190659:33-190659:167", "190679:1-190679:55", "190688:69-190688:249", 
        "190702:51-190702:53", "190702:55-190702:122", "190702:124-190702:169", "190703:1-190703:252", "190704:1-190704:3", 
        "190705:1-190705:5", "190705:7-190705:65", "190705:81-190705:336", "190705:338-190705:350", "190705:353-190705:383", 
        "190706:1-190706:126", "190707:1-190707:237", "190707:239-190707:257", "190708:1-190708:189", "190733:71-190733:96", 
        "190733:99-190733:389", "190733:392-190733:460", "190736:1-190736:80", "190736:83-190736:185", "190738:1-190738:130", 
        "190738:133-190738:226", "190738:229-190738:349", "190782:55-190782:181", "190782:184-190782:233", "190782:236-190782:399", 
        "190782:401-190782:409", "190895:64-190895:202", "190895:210-190895:302", "190895:305-190895:584", "190895:587-190895:948", 
        "190906:73-190906:256", "190906:259-190906:354", "190906:356-190906:496", "190945:124-190945:207", "190949:1-190949:81", 
        "191043:45-191043:46", "191046:1-191046:21", "191046:24-191046:82", "191046:84-191046:88", "191046:92-191046:116", 
        "191046:119-191046:180", "191046:183", "191046:185-191046:239", "191056:1", "191056:4-191056:9", 
        "191056:16-191056:17", "191056:19", "191057:1", "191057:4-191057:40", "191062:1", 
        "191062:3", "191062:5-191062:214", "191062:216-191062:541", "191090:1-191090:55", "191201:38-191201:49", 
        "191201:52-191201:79", "191202:1-191202:64", "191202:66-191202:68", "191202:87-191202:105", "191202:108-191202:118", 
        "191226:77-191226:78", "191226:81-191226:831", "191226:833-191226:1454", "191226:1456-191226:1466", "191226:1469-191226:1507", 
        "191226:1510-191226:1686", "191247:1-191247:153", "191247:156-191247:280", "191247:283-191247:606", "191247:608-191247:620", 
        "191247:622-191247:818", "191247:821-191247:834", "191247:837-191247:1031", "191247:1034-191247:1046", "191247:1049-191247:1140", 
        "191247:1143-191247:1187", "191247:1190-191247:1214", "191247:1217-191247:1224", "191248:1-191248:103", "191264:59-191264:79", 
        "191264:82-191264:152", "191264:155-191264:189", "191271:56-191271:223", "191271:225-191271:363", "191276:1-191276:16", 
        "191277:1-191277:28", "191277:30-191277:164", "191277:167-191277:253", "191277:255-191277:457", "191277:460-191277:535", 
        "191277:537-191277:576", "191277:579-191277:775", "191277:778-191277:811", "191277:813-191277:849", "191367:1-191367:2", 
        "191411:1-191411:23", "191695:1", "191718:43-191718:95", "191718:98-191718:207", "191720:1", 
        "191720:3-191720:15", "191720:17-191720:181", "191721:1", "191721:3-191721:34", "191721:36-191721:183", 
        "191721:186-191721:189", "191726:1-191726:13", "191810:15", "191810:22-191810:49", "191810:52-191810:92", 
        "191830:54-191830:242", "191830:245-191830:301", "191830:304-191830:393", "191833:1", "191833:3-191833:103", 
        "191834:1-191834:30", "191834:33-191834:74", "191834:77-191834:299", "191834:302-191834:352", "191837:1-191837:44", 
        "191837:47-191837:53", "191837:56-191837:65", "191856:1-191856:133", "191859:1-191859:28", "191859:31-191859:126", 
        "193093:1-193093:33", "193123:1-193123:27", "193124:1-193124:52", "193192:58-193192:86", "193193:1-193193:6", 
        "193193:8", "193193:11-193193:83", "193193:86-193193:120", "193193:122-193193:160", "193193:162-193193:274", 
        "193193:276-193193:495", "193193:497-193193:506", "193207:54-193207:182", "193334:29-193334:172", "193336:1-193336:264", 
        "193336:267-193336:492", "193336:495-193336:684", "193336:687-193336:729", "193336:732-193336:951", "193541:77-193541:101", 
        "193541:103-193541:413", "193541:416-193541:575", "193541:578-193541:619", "193556:41-193556:83", "193557:1-193557:84", 
        "193575:48-193575:173", "193575:176-193575:349", "193575:351-193575:394", "193575:397-193575:415", "193575:417-193575:658", 
        "193575:660-193575:752", "193621:60-193621:570", "193621:573-193621:769", "193621:772-193621:976", "193621:979-193621:1053", 
        "193621:1056-193621:1137", "193621:1139-193621:1193", "193621:1195-193621:1371", "193621:1373-193621:1654", "193834:1-193834:35", 
        "193835:1-193835:20", "193835:22-193835:26", "193836:1-193836:2", "193998:66-193998:113", "193998:115-193998:278", 
        "193999:1-193999:45", "194027:57-194027:113", "194050:53-194050:113", "194050:116-194050:273", "194050:275-194050:355", 
        "194050:357-194050:369", "194050:372-194050:391", "194050:394-194050:490", "194050:492-194050:814", "194050:816-194050:1435", 
        "194050:1437-194050:1735", "194050:1760-194050:1888", "194051:1-194051:12", "194052:1-194052:99", "194052:102-194052:166", 
        "194075:48-194075:101", "194075:103", "194075:105-194075:107", "194075:109", "194075:111", 
        "194076:1-194076:9", "194076:11-194076:55", "194076:58-194076:163", "194076:165-194076:228", "194076:230-194076:264", 
        "194076:267-194076:507", "194076:509-194076:527", "194076:530-194076:538", "194076:541-194076:562", "194076:565-194076:748", 
        "194108:81-194108:161", "194108:164-194108:264", "194108:266-194108:373", "194108:376-194108:396", "194108:398-194108:433", 
        "194108:436-194108:452", "194108:454-194108:577", "194108:579-194108:590", "194108:593-194108:668", "194108:671-194108:872", 
        "194115:66-194115:184", "194115:186-194115:338", "194115:340-194115:346", "194115:348-194115:493", "194115:496-194115:731", 
        "194115:819-194115:857", "194117:1-194117:38", "194119:1-194119:229", "194119:232-194119:261", "194120:1-194120:162", 
        "194120:165-194120:406", "194150:42-194150:127", "194150:129-194150:261", "194150:264-194150:311", "194151:47-194151:72", 
        "194151:75-194151:191", "194151:193-194151:238", "194151:240-194151:617", "194151:619", "194151:621", 
        "194151:623", "194153:1-194153:115", "194199:96-194199:227", "194199:229-194199:336", "194199:339-194199:402", 
        "194210:3-194210:195", "194210:198-194210:217", "194210:220-194210:359", "194210:361-194210:555", "194223:61-194223:112", 
        "194224:1-194224:126", "194224:129-194224:206", "194224:208-194224:250", "194224:253-194224:309", "194224:312-194224:386", 
        "194224:389-194224:412", "194225:1-194225:23", "194225:26-194225:47", "194225:49-194225:85", "194225:88-194225:149", 
        "194270:56-194270:68", "194303:56-194303:66", "194303:69-194303:102", "194304:1-194304:43", "194304:46", 
        "194305:1-194305:84", "194314:52-194314:130", "194314:133-194314:300", "194315:1-194315:10", "194315:13-194315:314", 
        "194315:317-194315:428", "194315:431-194315:452", "194315:455-194315:467", "194317:1-194317:20", "194424:63-194424:141", 
        "194424:144-194424:195", "194424:198-194424:266", "194424:268-194424:421", "194424:424-194424:478", "194424:481-194424:531", 
        "194424:534-194424:553", "194424:556-194424:706", "194424:708", "194428:1-194428:85", "194428:87-194428:122", 
        "194428:125-194428:294", "194428:296-194428:465", "194429:1-194429:4", "194429:7-194429:54", "194429:57-194429:147", 
        "194429:150-194429:411", "194429:413-194429:742", "194429:745-194429:986", "194429:988-194429:1019", "194439:46-194439:77", 
        "194439:79-194439:106", "194455:45-194455:64", "194455:67-194455:140", "194455:142-194455:255", "194455:293-194455:303", 
        "194464:1-194464:127", "194464:130-194464:142", "194464:145-194464:210", "194479:1-194479:44", "194479:165-194479:232", 
        "194479:235-194479:262", "194479:265-194479:374", "194479:377-194479:431", "194479:434-194479:489", "194479:492-194479:529", 
        "194479:531-194479:566", "194480:1-194480:32", "194480:34-194480:205", "194480:207-194480:375", "194480:377-194480:387", 
        "194480:389-194480:759", "194480:762-194480:956", "194480:959-194480:1402", "194533:46-194533:379", "194533:382-194533:415", 
        "194533:417-194533:618", "194533:620-194533:872", "194619:31-194619:110", "194631:1-194631:42", "194631:44-194631:100", 
        "194631:102-194631:169", "194631:171-194631:222", "194643:1-194643:287", "194644:1-194644:168", "194644:171-194644:181", 
        "194644:184-194644:185", "194644:187-194644:319", "194644:321-194644:421", "194691:61-194691:104", "194691:107-194691:155", 
        "194691:158-194691:251", "194691:254-194691:268", "194691:271-194691:272", "194691:275-194691:289", "194691:292-194691:313", 
        "194699:1-194699:30", "194699:32-194699:52", "194699:55-194699:64", "194699:67-194699:71", "194699:73-194699:154", 
        "194699:157-194699:215", "194699:218-194699:238", "194699:241-194699:259", "194702:1-194702:138", "194702:141-194702:191", 
        "194704:1-194704:41", "194704:44-194704:545", "194704:548-194704:592", "194711:1-194711:7", "194711:9-194711:619", 
        "194712:1-194712:56", "194712:61-194712:418", "194712:420-194712:625", "194712:627-194712:759", "194735:44-194735:71", 
        "194735:74-194735:101", "194735:104-194735:130", "194778:60-194778:118", "194778:120-194778:219", "194789:1-194789:18", 
        "194789:21-194789:32", "194789:34-194789:80", "194789:82-194789:166", "194789:168-194789:269", "194789:272-194789:405", 
        "194789:409-194789:414", "194789:417-194789:427", "194789:430-194789:566", "194790:1-194790:45", "194825:72-194825:117", 
        "194825:120-194825:221", "194896:34-194896:55", "194896:58-194896:79", "194896:82-194896:103", "194897:1-194897:6", 
        "194897:8-194897:78", "194897:80-194897:96", "194897:98-194897:102", "194912:53-194912:70", "194912:72-194912:96", 
        "194912:98-194912:444", "194912:446-194912:450", "194912:453-194912:467", "194912:470-194912:561", "194912:564-194912:660", 
        "194912:663-194912:813", "194912:815-194912:840", "194912:843-194912:864", "194912:866-194912:1004", "194912:1007-194912:1025", 
        "194912:1027-194912:1067", "194912:1069-194912:1137", "194912:1140-194912:1166", "194912:1168-194912:1249", "194912:1251-194912:1304", 
        "194912:1307-194912:1444", "194912:1447-194912:1487", "194912:1489-194912:1503", "194912:1506-194912:1662", "194914:1-194914:38", 
        "194915:1-194915:74", "195013:94-195013:144", "195013:146-195013:185", "195013:187-195013:206", "195013:208-195013:299", 
        "195013:302-195013:324", "195013:326-195013:366", "195013:369-195013:447", "195013:450-195013:526", "195013:528-195013:541", 
        "195014:1-195014:6", "195014:9-195014:119", "195014:121-195014:148", "195015:1-195015:13", "195016:1-195016:21", 
        "195016:23-195016:55", "195016:58-195016:63", "195016:65-195016:174", "195016:177-195016:184", "195016:186-195016:241", 
        "195016:243-195016:246", "195016:248-195016:251", "195016:254-195016:367", "195016:370-195016:422", "195016:425-195016:560", 
        "195016:563-195016:569", "195099:70-195099:144", "195099:147-195099:186", "195099:189-195099:208", "195099:211-195099:224", 
        "195099:227-195099:248", "195109:98-195109:241", "195112:1-195112:12", "195112:15-195112:26", "195113:1-195113:209", 
        "195113:212-195113:388", "195113:391-195113:403", "195113:406-195113:419", "195113:422-195113:492", "195113:495-195113:579", 
        "195114:1-195114:69", "195114:72-195114:103", "195115:1-195115:7", "195115:10-195115:22", "195147:132-195147:282", 
        "195147:285-195147:294", "195147:297-195147:331", "195147:334-195147:363", "195147:366-195147:442", "195147:445-195147:536", 
        "195147:539-195147:559", "195163:72-195163:138", "195163:140-195163:224", "195163:227-195163:240", "195163:243", 
        "195163:246-195163:347", "195164:1-195164:64", "195165:1-195165:4", "195165:7-195165:41", "195165:44-195165:54", 
        "195165:56-195165:153", "195165:156-195165:260", "195165:263-195165:266", "195251:1-195251:131", "195251:134-195251:137", 
        "195251:140-195251:152", "195251:154-195251:165", "195251:167-195251:242", "195303:109-195303:191", "195303:194-195303:277", 
        "195303:280-195303:310", "195303:312-195303:316", "195303:318-195303:409", "195304:1-195304:3", "195304:6-195304:22", 
        "195304:27-195304:80", "195304:83-195304:100", "195304:103-195304:154", "195304:157-195304:341", "195304:344-195304:588", 
        "195304:590-195304:727", "195304:729-195304:1003", "195304:1006-195304:1079", "195304:1083-195304:1140", "195304:1143-195304:1229", 
        "195378:90-195378:117", "195378:120-195378:127", "195378:130-195378:185", "195378:187-195378:204", "195378:206-195378:302", 
        "195378:305-195378:542", "195378:544-195378:565", "195378:567-195378:645", "195378:647-195378:701", "195378:703-195378:734", 
        "195378:737-195378:1120", "195378:1122-195378:1133", "195390:1", "195390:4-195390:27", "195390:30-195390:145", 
        "195390:147-195390:183", "195390:186-195390:187", "195390:190-195390:208", "195390:210-195390:213", "195390:215-195390:400", 
        "195396:49-195396:55", "195396:58-195396:63", "195396:66-195396:131", "195397:1-195397:10", "195397:12-195397:89", 
        "195397:92-195397:120", "195397:123-195397:141", "195397:143-195397:251", "195397:253", "195397:256-195397:475", 
        "195397:478-195397:525", "195397:527-195397:608", "195397:611-195397:776", "195397:779-195397:970", "195397:972-195397:1121", 
        "195397:1123-195397:1181", "195397:1184-195397:1198", "195397:1200-195397:1209", "195398:3-195398:137", "195398:139-195398:494", 
        "195398:497-195398:585", "195398:587-195398:817", "195398:820-195398:824", "195398:827-195398:1225", "195398:1228-195398:1307", 
        "195398:1309-195398:1712", "195398:1721-195398:1736", "195398:1741-195398:1752", "195398:1767-195398:1795", "195399:1-195399:192", 
        "195399:194-195399:382", "195530:1-195530:80", "195530:82-195530:104", "195530:107-195530:156", "195530:159-195530:300", 
        "195530:302-195530:405", "195540:68-195540:123", "195540:126-195540:137", "195540:140-195540:283", "195540:286-195540:319", 
        "195551:91-195551:106", "195552:1-195552:21", "195552:23-195552:27", "195552:30-195552:147", "195552:149-195552:155", 
        "195552:158-195552:182", "195552:185-195552:287", "195552:290-195552:349", "195552:352-195552:469", "195552:472-195552:815", 
        "195552:818-195552:823", "195552:825-195552:883", "195552:885-195552:1152", "195552:1154-195552:1300", "195552:1303-195552:1789", 
        "195633:40-195633:42", "195647:1-195647:41", "195649:1-195649:69", "195649:72-195649:151", "195649:154-195649:181", 
        "195649:183-195649:247", "195655:1-195655:129", "195655:131-195655:184", "195655:186-195655:260", "195655:263-195655:350", 
        "195655:353-195655:446", "195655:448-195655:483", "195655:485-195655:498", "195656:1-195656:362", "195658:1-195658:37", 
        "195658:40-195658:362", "195658:364-195658:382", "195658:384-195658:386", "195749:1-195749:8", "195749:10-195749:33", 
        "195749:36-195749:131", "195757:1-195757:82", "195757:85-195757:115", "195757:118-195757:161", "195757:163-195757:206", 
        "195758:1-195758:18", "195774:1-195774:13", "195774:16-195774:137", "195774:139-195774:151", "195774:154-195774:162", 
        "195774:164-195774:256", "195774:258-195774:276", "195774:279-195774:362", "195774:365-195774:466", "195774:469-195774:618", 
        "195774:620-195774:649", "195774:651-195774:830", "195775:1-195775:57", "195775:60-195775:100", "195775:103-195775:170", 
        "195776:1-195776:63", "195776:66-195776:283", "195776:286-195776:337", "195776:340-195776:399", "195776:401-195776:409", 
        "195776:411-195776:477", "195841:74-195841:85", "195868:1-195868:88", "195868:90-195868:107", "195868:110-195868:205", 
        "195915:1-195915:109", "195915:111-195915:275", "195915:278-195915:390", "195915:393-195915:417", "195915:419-195915:429", 
        "195915:432-195915:505", "195915:507-195915:747", "195915:749-195915:785", "195915:787-195915:828", "195915:830-195915:850", 
        "195916:1-195916:16", "195916:19-195916:68", "195916:71-195916:212", "195917:1-195917:4", "195918:1-195918:44", 
        "195918:46", "195918:49-195918:64", "195919:1-195919:15", "195923:1-195923:14", "195925:1-195925:12", 
        "195926:1", "195926:3-195926:19", "195926:21-195926:34", "195929:1-195929:29", "195930:1-195930:77", 
        "195930:80-195930:176", "195930:179-195930:526", "195930:529-195930:596", "195937:1-195937:28", "195937:31-195937:186", 
        "195937:188-195937:396", "195947:23-195947:62", "195947:64-195947:88", "195948:51-195948:116", "195948:119-195948:144", 
        "195948:147", "195948:150-195948:352", "195948:355-195948:369", "195948:372-195948:402", "195948:404-195948:500", 
        "195948:503-195948:540", "195948:543-195948:565", "195948:567-195948:602", "195948:605-195948:615", "195950:1-195950:71", 
        "195950:73-195950:138", "195950:141-195950:169", "195950:172-195950:332", "195950:335-195950:350", "195950:353-195950:382", 
        "195950:385-195950:421", "195950:424-195950:450", "195950:453-195950:483", "195950:485-195950:616", "195950:619-195950:715", 
        "195950:718-195950:787", "195950:789-195950:800", "195950:803-195950:829", "195950:831", "195950:833-195950:1587", 
        "195963:54-195963:58", "195970:44-195970:49", "195970:51-195970:85", "196019:54-196019:68", "196027:1-196027:55", 
        "196027:58-196027:119", "196027:121-196027:155", "196027:158-196027:186", "196046:12-196046:40", "196047:1-196047:64", 
        "196047:70-196047:75", "196048:1-196048:44", "196048:46-196048:48", "196197:58-196197:122", "196197:125-196197:179", 
        "196197:181-196197:311", "196197:313-196197:516", "196197:519-196197:562", "196199:1-196199:33", "196199:36-196199:83", 
        "196199:86-196199:118", "196199:121-196199:147", "196199:150-196199:237", "196199:239-196199:285", "196199:287-196199:534", 
        "196200:1-196200:68", "196202:3-196202:61", "196202:64-196202:108", "196203:1-196203:102", "196203:107-196203:117", 
        "196218:55-196218:199", "196218:201-196218:224", "196218:226-196218:393", "196218:396-196218:494", "196218:496-196218:741", 
        "196218:744-196218:752", "196218:754-196218:757", "196218:759-196218:820", "196239:1-196239:59", "196239:62-196239:154", 
        "196239:157-196239:272", "196239:274-196239:373", "196239:375-196239:432", "196239:435-196239:465", "196239:468-196239:647", 
        "196239:650-196239:706", "196239:709-196239:1025", "196249:63-196249:77", "196249:80-196249:99", "196250:1-196250:2", 
        "196250:5-196250:265", "196250:267-196250:426", "196252:1-196252:35", "196334:59-196334:111", "196334:113-196334:123", 
        "196334:126-196334:132", "196334:135-196334:167", "196334:170-196334:193", "196334:196-196334:257", "196334:259-196334:267", 
        "196334:270-196334:289", "196334:292-196334:342", "196349:65-196349:84", "196349:86-196349:154", "196349:157-196349:244", 
        "196349:246-196349:258", "196357:1-196357:4", "196359:1-196359:2", "196362:1-196362:88", "196363:1-196363:8", 
        "196363:11-196363:34", "196364:1-196364:93", "196364:96-196364:136", "196364:139-196364:365", "196364:368-196364:380", 
        "196364:382-196364:601", "196364:603-196364:795", "196364:798-196364:884", "196364:887-196364:1196", "196364:1199-196364:1200", 
        "196364:1203-196364:1299", "196437:1", "196437:3-196437:74", "196437:77-196437:169", "196438:1-196438:181", 
        "196438:184-196438:699", "196438:701-196438:1269", "196452:82-196452:112", "196452:114-196452:490", "196452:493-196452:586", 
        "196452:589-196452:618", "196452:622-196452:668", "196452:671-196452:716", "196452:718-196452:726", "196452:728-196452:956", 
        "196452:958-196452:1004", "196452:1007-196452:1091", "196453:1-196453:74", "196453:77-196453:145", "196453:147-196453:669", 
        "196453:673-196453:714", "196453:717-196453:799", "196453:802-196453:988", "196453:991-196453:1178", "196453:1180", 
        "196453:1182-196453:1248", "196453:1250-196453:1528", "196453:1531-196453:1647", "196495:114-196495:180", "196495:182-196495:272", 
        "196509:1-196509:68", "196531:62-196531:150", "196531:152-196531:253", "196531:256-196531:285", "196531:288-196531:302", 
        "196531:305-196531:422", "196531:425-196531:440", "198049:1-198049:11", "198049:14-198049:57", "198050:2-198050:155", 
        "198063:1-198063:37", "198063:40-198063:72", "198063:74-198063:124", "198063:127-198063:294", "198116:36-198116:52", 
        "198116:54-198116:55", "198116:58-198116:96", "198116:98-198116:112", "198207:1-198207:97", "198208:1-198208:92", 
        "198208:94-198208:134", "198208:137-198208:147", "198208:150-198208:209", "198210:1-198210:221", "198212:1-198212:574", 
        "198213:1-198213:107", "198215:1-198215:12", "198230:1-198230:33", "198230:36-198230:57", "198230:60-198230:235", 
        "198230:237-198230:324", "198230:326-198230:388", "198230:390-198230:459", "198230:462-198230:625", "198230:627-198230:651", 
        "198230:653-198230:805", "198230:808-198230:811", "198230:814-198230:948", "198230:950-198230:1090", "198230:1093-198230:1103", 
        "198230:1106-198230:1332", "198230:1335-198230:1380", "198249:1-198249:7", "198269:3-198269:198", "198271:1-198271:91", 
        "198271:93-198271:170", "198271:173-198271:299", "198271:301-198271:450", "198271:453-198271:513", "198271:516-198271:616", 
        "198271:619-198271:628", "198271:631-198271:791", "198271:793-198271:797", "198272:1-198272:185", "198272:188-198272:245", 
        "198272:248-198272:314", "198272:317-198272:433", "198272:436-198272:444", "198272:454-198272:620", "198346:44-198346:47", 
        "198372:57-198372:110", "198485:68-198485:109", "198485:112-198485:134", "198485:136-198485:181", "198485:184-198485:239", 
        "198487:1-198487:145", "198487:147-198487:514", "198487:517-198487:668", "198487:671-198487:733", "198487:736-198487:757", 
        "198487:760-198487:852", "198487:854-198487:994", "198487:997-198487:1434", "198487:1437-198487:1610", "198522:65-198522:144", 
        "198522:147-198522:208", "198941:102-198941:189", "198941:191-198941:220", "198941:222-198941:241", "198941:243-198941:249", 
        "198941:252-198941:284", "198954:108-198954:156", "198954:159-198954:277", "198955:1-198955:45", "198955:47-198955:50", 
        "198955:53-198955:220", "198955:223-198955:269", "198955:271-198955:284", "198955:286-198955:338", "198955:340-198955:580", 
        "198955:583-198955:742", "198955:744-198955:910", "198955:913-198955:946", "198955:949-198955:1162", "198955:1165-198955:1169", 
        "198955:1172-198955:1182", "198955:1185-198955:1188", "198955:1190-198955:1246", "198955:1249-198955:1304", "198955:1306-198955:1467", 
        "198955:1470-198955:1485", "198955:1487-198955:1552", "198969:58-198969:81", "198969:84-198969:247", "198969:249-198969:323", 
        "198969:325-198969:365", "198969:367-198969:413", "198969:416-198969:466", "198969:468-198969:643", "198969:646-198969:918", 
        "198969:920-198969:1011", "198969:1013-198969:1175", "198969:1178-198969:1236", "198969:1239-198969:1253", "199008:75-199008:93", 
        "199008:95-199008:121", "199008:124-199008:208", "199008:211-199008:331", "199008:333-199008:373", "199008:376-199008:482", 
        "199008:485-199008:605", "199008:608-199008:644", "199011:1-199011:11", "199011:13-199011:24", "199021:59-199021:88", 
        "199021:91-199021:128", "199021:130-199021:133", "199021:136-199021:309", "199021:311-199021:333", "199021:335-199021:410", 
        "199021:414-199021:469", "199021:471-199021:533", "199021:535-199021:563", "199021:565-199021:1223", "199021:1226-199021:1479", 
        "199021:1481-199021:1494", "199318:65-199318:138", "199319:1-199319:7", "199319:9-199319:223", "199319:226-199319:277", 
        "199319:280-199319:348", "199319:351-199319:358", "199319:360-199319:422", "199319:424-199319:490", "199319:492-199319:493", 
        "199319:496-199319:612", "199319:615-199319:642", "199319:645-199319:720", "199319:723-199319:728", "199319:730-199319:731", 
        "199319:734-199319:741", "199319:744-199319:752", "199319:754-199319:943", "199319:945-199319:997", "199336:1-199336:33", 
        "199336:36-199336:122", "199336:125-199336:231", "199336:234-199336:614", "199336:617-199336:789", "199336:791-199336:977", 
        "199356:95-199356:121", "199356:123-199356:168", "199356:171-199356:205", "199356:208-199356:231", "199409:25-199409:54", 
        "199409:56-199409:89", "199409:91-199409:204", "199409:206-199409:290", "199409:293-199409:583", "199409:586-199409:602", 
        "199409:604-199409:1014", "199409:1016-199409:1300", "199428:61-199428:197", "199428:200-199428:210", "199428:212-199428:382", 
        "199428:387-199428:414", "199428:417-199428:436", "199428:439-199428:530", "199428:533-199428:648", "199429:1-199429:28", 
        "199429:30-199429:36", "199429:39-199429:55", "199429:58-199429:101", "199429:103-199429:148", "199429:151-199429:154", 
        "199435:63-199435:106", "199435:109-199435:261", "199435:263-199435:579", "199435:582-199435:654", "199435:656-199435:696", 
        "199435:699-199435:1034", "199435:1037-199435:1144", "199435:1147-199435:1327", "199435:1330-199435:1411", "199435:1414-199435:1431", 
        "199435:1434-199435:1441", "199435:1444-199435:1487", "199435:1489-199435:1610", "199436:1-199436:113", "199436:116-199436:254", 
        "199436:257-199436:675", "199436:678-199436:748", "199564:1-199564:3", "199569:1-199569:2", "199569:5-199569:136", 
        "199569:139-199569:367", "199570:1-199570:17", "199571:1-199571:184", "199571:186-199571:360", "199571:363-199571:561", 
        "199572:1-199572:317", "199573:1-199573:22", "199574:1-199574:53", "199574:56-199574:153", "199574:156-199574:246", 
        "199608:60-199608:157", "199608:159-199608:209", "199608:211-199608:341", "199608:344-199608:390", "199608:392-199608:461", 
        "199608:464-199608:800", "199608:802-199608:1064", "199608:1067-199608:1392", "199608:1395-199608:1630", "199608:1633-199608:1904", 
        "199608:1907-199608:1962", "199608:1965-199608:2252", "199608:2255-199608:2422", "199698:72-199698:94", "199698:96-199698:127", 
        "199699:1-199699:154", "199699:157-199699:169", "199699:172-199699:410", "199699:412-199699:756", "199703:1-199703:94", 
        "199703:97-199703:482", "199703:485-199703:529", "199739:66-199739:133", "199751:103-199751:119", "199751:121-199751:127", 
        "199752:1-199752:141", "199752:144-199752:180", "199752:182-199752:186", "199752:188-199752:211", "199752:214-199752:322", 
        "199753:1-199753:59", "199754:1-199754:203", "199754:205-199754:325", "199754:328-199754:457", "199754:459-199754:607", 
        "199754:610-199754:613", "199754:615-199754:806", "199754:808-199754:998", "199804:78-199804:88", "199804:90-199804:181", 
        "199804:183-199804:235", "199804:238-199804:278", "199804:281-199804:290", "199804:292-199804:519", "199804:522-199804:575", 
        "199804:577-199804:628", "199804:631-199804:632", "199812:70-199812:141", "199812:144-199812:163", "199812:182-199812:211", 
        "199812:214-199812:471", "199812:474-199812:505", "199812:508-199812:557", "199812:560-199812:571", "199812:574-199812:623", 
        "199812:626-199812:751", "199812:754-199812:796", "199832:58-199832:62", "199832:65-199832:118", "199832:121-199832:139", 
        "199832:142-199832:286", "199833:1-199833:13", "199833:16-199833:103", "199833:105-199833:250", "199833:253-199833:493", 
        "199833:496-199833:794", "199833:797-199833:1032", "199833:1034-199833:1185", "199833:1188-199833:1239", "199834:1-199834:9", 
        "199834:11", "199834:14-199834:18", "199834:21-199834:54", "199834:56-199834:57", "199834:62-199834:65", 
        "199834:69-199834:284", "199834:286-199834:503", "199834:505-199834:942", "199862:59-199862:141", "199864:1-199864:87", 
        "199864:89", "199864:92-199864:103", "199864:106-199864:372", "199864:374-199864:385", "199864:388-199864:486", 
        "199867:1-199867:134", "199867:136-199867:172", "199867:174-199867:218", "199867:221-199867:320", "199868:1-199868:21", 
        "199875:70-199875:150", "199875:152-199875:334", "199876:1-199876:19", "199876:22-199876:95", "199876:97-199876:249", 
        "199876:252-199876:272", "199876:274-199876:340", "199876:343-199876:362", "199876:365-199876:376", "199877:1-199877:173", 
        "199877:175-199877:605", "199877:607-199877:701", "199877:703-199877:871", "199960:72-199960:139", "199960:141-199960:197", 
        "199960:204-199960:232", "199960:235-199960:363", "199960:365-199960:367", "199960:370-199960:380", "199960:383-199960:459", 
        "199960:461-199960:466", "199960:469-199960:485", "199961:1-199961:211", "199961:213-199961:287", "199967:60-199967:120", 
        "199967:122-199967:170", "199967:172-199967:198", "199973:73-199973:89", "200041:62-200041:83", "200041:85-200041:157", 
        "200041:162-200041:274", "200041:277-200041:318", "200041:321-200041:335", "200041:337-200041:386", "200041:388-200041:389", 
        "200041:392-200041:400", "200041:402-200041:568", "200041:571-200041:593", "200041:595-200041:646", "200041:649-200041:728", 
        "200041:731-200041:860", "200041:862-200041:930", "200041:932-200041:1096", "200042:1-200042:110", "200042:112-200042:536", 
        "200049:1-200049:177", "200075:76-200075:139", "200075:142-200075:232", "200075:256-200075:326", "200075:329-200075:422", 
        "200075:425-200075:431", "200075:434-200075:500", "200075:502-200075:605", "200091:67", "200091:70-200091:151", 
        "200091:154-200091:172", "200091:174-200091:187", "200091:190-200091:196", "200091:199-200091:201", "200091:204-200091:425", 
        "200091:428-200091:535", "200091:537-200091:607", "200091:610-200091:879", "200091:881-200091:943", "200091:946-200091:999", 
        "200091:1001-200091:1025", "200091:1027-200091:1132", "200091:1135-200091:1339", "200091:1341-200091:1433", "200091:1435-200091:1450", 
        "200091:1453-200091:1523", "200091:1526-200091:1664", "200091:1667-200091:1680", "200091:1683-200091:1710", "200152:74-200152:116", 
        "200160:52-200160:68", "200161:1-200161:97", "200161:100-200161:112", "200174:81-200174:84", "200177:1-200177:56", 
        "200178:1-200178:38", "200180:1-200180:18", "200186:1-200186:3", "200186:6-200186:24", "200188:1-200188:24", 
        "200188:27-200188:28", "200188:31-200188:76", "200188:79-200188:271", "200188:274-200188:352", "200190:1-200190:4", 
        "200190:6-200190:76", "200190:79-200190:143", "200190:146-200190:159", "200190:162-200190:256", "200190:258-200190:321", 
        "200190:324-200190:401", "200190:403-200190:453", "200190:456-200190:457", "200190:460-200190:565", "200190:567-200190:588", 
        "200190:591", "200190:593-200190:595", "200190:597-200190:646", "200190:649-200190:878", "200229:1-200229:33", 
        "200229:41-200229:219", "200229:222-200229:244", "200229:247-200229:290", "200229:293-200229:624", "200229:627-200229:629", 
        "200243:69-200243:103", "200243:106-200243:139", "200244:3-200244:304", "200244:307-200244:442", "200244:445-200244:507", 
        "200244:510-200244:619", "200245:1-200245:103", "200245:105-200245:128", "200245:131-200245:248", "200245:251-200245:357", 
        "200368:72-200368:180", "200369:1-200369:5", "200369:8-200369:61", "200369:64-200369:360", "200369:363-200369:439", 
        "200369:441-200369:578", "200369:580-200369:603", "200369:606-200369:684", "200369:686", "200381:8-200381:15", 
        "200381:18-200381:36", "200381:38-200381:89", "200381:91-200381:195", "200466:134-200466:274", "200473:96-200473:157", 
        "200473:159-200473:224", "200473:226-200473:304", "200473:306-200473:469", "200473:472-200473:524", "200473:527-200473:542", 
        "200473:545-200473:619", "200473:622-200473:688", "200473:691-200473:730", "200473:733-200473:738", "200473:740-200473:1324", 
        "200491:87-200491:107", "200491:110-200491:149", "200491:152-200491:157", "200491:160-200491:197", "200491:199-200491:237", 
        "200491:240-200491:270", "200491:273", "200491:276-200491:334", "200491:336-200491:360", "200491:363-200491:419", 
        "200515:97-200515:183", "200519:1-200519:111", "200519:114-200519:126", "200519:129-200519:136", "200519:138-200519:224", 
        "200519:227-200519:258", "200519:261-200519:350", "200519:353-200519:611", "200519:613-200519:747", "200525:77-200525:149", 
        "200525:151-200525:164", "200525:166-200525:190", "200525:193-200525:276", "200525:278-200525:311", "200525:314-200525:464", 
        "200525:467-200525:488", "200525:491-200525:674", "200525:676-200525:704", "200525:707-200525:755", "200525:757-200525:895", 
        "200525:898-200525:937", "200525:939-200525:990", "200532:1-200532:37", "200599:75-200599:129", "200599:132-200599:137", 
        "200600:1-200600:183", "200600:186-200600:299", "200600:302-200600:313", "200600:316-200600:324", "200600:327-200600:334", 
        "200600:336-200600:397", "200600:399-200600:417", "200600:420-200600:526", "200600:529-200600:591", "200600:594-200600:596", 
        "200600:598-200600:609", "200600:611-200600:660", "200600:663-200600:823", "200600:826-200600:900", "200600:902-200600:943", 
        "200600:945-200600:1139", "200961:1-200961:115", "200976:94-200976:164", "200990:75-200990:143", "200991:1-200991:42", 
        "200991:44", "200991:47-200991:80", "200991:83-200991:175", "200991:178-200991:181", "200991:184-200991:252", 
        "200991:255-200991:632", "200991:635-200991:916", "200991:918-200991:1017", "200991:1019-200991:1048", "200992:1-200992:405", 
        "200992:408-200992:434", "200992:436-200992:581", "201062:78-201062:268", "201097:83-201097:136", "201097:138-201097:245", 
        "201097:248-201097:300", "201097:303-201097:370", "201097:372-201097:429", "201097:432-201097:497", "201114:1-201114:14", 
        "201115:1-201115:73", "201159:70-201159:211", "201164:1-201164:8", "201164:10-201164:94", "201164:96-201164:125", 
        "201164:128-201164:178", "201164:180-201164:198", "201164:200-201164:271", "201164:274-201164:416", "201164:418", 
        "201168:1-201168:37", "201168:39-201168:275", "201168:278-201168:481", "201168:483-201168:558", "201168:560-201168:730", 
        "201173:1-201173:194", "201173:197-201173:586", "201174:1-201174:214", "201174:216-201174:263", "201174:265-201174:339", 
        "201174:342-201174:451", "201191:75-201191:98", "201191:100-201191:216", "201191:218-201191:389", "201191:392-201191:492", 
        "201191:494-201191:506", "201191:509-201191:585", "201191:587-201191:594", "201191:597-201191:607", "201191:609-201191:794", 
        "201191:796-201191:838", "201191:841-201191:974", "201191:977-201191:1105", "201191:1108-201191:1117", "201191:1120-201191:1382", 
        "201191:1385-201191:1386", "201193:1-201193:19", "201196:1-201196:238", "201196:241-201196:278", "201196:286-201196:299", 
        "201196:302-201196:338", "201196:341-201196:515", "201196:518-201196:720", "201196:723-201196:789", "201196:803-201196:841", 
        "201197:1-201197:23", "201202:1-201202:437", "201229:1-201229:5", "201229:8-201229:26", "201229:29-201229:73", 
        "201278:62-201278:163", "201278:166-201278:229", "201278:232-201278:256", "201278:259-201278:316", "201278:318-201278:595", 
        "201278:598-201278:938", "201278:942-201278:974", "201278:976-201278:1160", "201278:1163-201278:1304", "201278:1306-201278:1793", 
        "201278:1796-201278:1802", "201278:1805-201278:1906", "201278:1909-201278:1929", "201278:1932-201278:2174", "201554:70-201554:86", 
        "201554:88-201554:114", "201554:116-201554:126", "201602:76-201602:81", "201602:83-201602:194", "201602:196-201602:494", 
        "201602:496-201602:614", "201602:617-201602:635", "201611:87-201611:145", "201611:149-201611:182", "201611:184-201611:186", 
        "201613:1-201613:42", "201613:44-201613:49", "201613:53-201613:210", "201613:213-201613:215", "201613:218-201613:225", 
        "201613:228-201613:646", "201624:83-201624:92", "201624:95-201624:240", "201624:270", "201625:211-201625:312", 
        "201625:315-201625:348", "201625:351-201625:416", "201625:418-201625:588", "201625:591-201625:671", "201625:673-201625:758", 
        "201625:760-201625:791", "201625:793-201625:944", "201657:77-201657:93", "201657:95-201657:108", "201657:110-201657:118", 
        "201658:1-201658:19", "201658:21-201658:118", "201658:121-201658:136", "201658:139-201658:288", "201668:78-201668:157", 
        "201669:1-201669:9", "201669:12-201669:136", "201669:139-201669:141", "201669:143-201669:165", "201671:1-201671:120", 
        "201671:122-201671:174", "201671:177-201671:462", "201671:464-201671:482", "201671:485-201671:499", "201671:501-201671:545", 
        "201671:547-201671:571", "201671:574-201671:614", "201671:617-201671:766", "201671:768-201671:896", "201671:899-201671:911", 
        "201671:914-201671:1007", "201678:1-201678:120", "201679:1-201679:110", "201679:112-201679:241", "201679:244-201679:298", 
        "201679:302-201679:321", "201679:324-201679:461", "201679:463-201679:483", "201692:78-201692:81", "201692:83-201692:179", 
        "201705:65-201705:73", "201705:75-201705:109", "201705:111-201705:187", "201706:1-201706:62", "201707:1-201707:23", 
        "201707:26-201707:42", "201707:45-201707:115", "201707:118-201707:130", "201707:133-201707:160", "201707:163-201707:276", 
        "201707:279-201707:471", "201707:473-201707:511", "201707:514-201707:545", "201707:547-201707:570", "201707:572-201707:622", 
        "201707:625-201707:735", "201707:738-201707:806", "201707:809-201707:876", "201707:879-201707:964", "201708:1-201708:79", 
        "201718:58-201718:108", "201727:67-201727:185", "201729:6-201729:20", "201729:22-201729:75", "201729:77-201729:126", 
        "201729:129-201729:154", "201729:156-201729:216", "201729:219-201729:244", "201794:58-201794:94", "201802:68-201802:209", 
        "201802:211-201802:214", "201802:216-201802:220", "201802:223-201802:288", "201802:290-201802:296", "201816:1-201816:72", 
        "201816:74-201816:105", "201816:107-201816:157", "201817:1-201817:274", "201818:1", "201819:1-201819:94", 
        "201819:96-201819:241", "201824:1-201824:139", "201824:141-201824:176", "201824:179-201824:286", "201824:289-201824:492", 
        "202012:98-202012:121", "202012:126-202012:131", "202013:1-202013:2", "202013:5-202013:35", "202013:38-202013:57", 
        "202014:1-202014:5", "202014:8-202014:14", "202014:16-202014:18", "202014:20-202014:77", "202014:79-202014:102", 
        "202014:104-202014:174", "202014:177-202014:190", "202014:192-202014:196", "202016:1-202016:48", "202016:51-202016:134", 
        "202016:137-202016:177", "202016:179-202016:743", "202016:745-202016:831", "202016:834-202016:890", "202016:893-202016:896", 
        "202016:898-202016:932", "202016:934-202016:1010", "202044:84-202044:101", "202044:104-202044:266", "202044:268-202044:461", 
        "202044:463-202044:466", "202045:1-202045:30", "202045:33-202045:72", "202045:75-202045:528", "202045:531-202045:601", 
        "202045:603-202045:785", "202045:788-202045:809", "202045:822-202045:823", "202054:6-202054:266", "202054:268-202054:489", 
        "202054:492-202054:605", "202054:608-202054:631", "202060:76-202060:142", "202060:144-202060:154", "202060:156-202060:244", 
        "202060:246-202060:497", "202060:499-202060:642", "202060:644-202060:682", "202060:684-202060:743", "202060:746-202060:936", 
        "202074:66-202074:174", "202075:1-202075:18", "202075:21-202075:187", "202075:189-202075:214", "202075:217-202075:247", 
        "202075:250-202075:342", "202075:345-202075:406", "202075:409-202075:497", "202075:500-202075:537", "202075:539", 
        "202075:542-202075:560", "202075:562-202075:615", "202075:618-202075:628", "202084:83-202084:156", "202084:159-202084:177", 
        "202084:179-202084:180", "202084:182-202084:239", "202087:1-202087:25", "202087:28-202087:208", "202087:210-202087:357", 
        "202087:359-202087:652", "202087:655-202087:853", "202087:856-202087:1093", "202088:1-202088:286", "202093:1-202093:104", 
        "202093:107-202093:320", "202093:322-202093:360", "202116:59-202116:60", "202178:67-202178:78", "202178:80-202178:88", 
        "202178:91-202178:177", "202178:180-202178:186", "202178:188-202178:337", "202178:340-202178:377", "202178:379-202178:425", 
        "202178:428-202178:475", "202178:478-202178:548", "202178:551-202178:717", "202178:720-202178:965", "202178:967-202178:1444", 
        "202178:1447-202178:1505", "202178:1508-202178:1519", "202178:1522-202178:1555", "202205:94-202205:114", "202209:1-202209:48", 
        "202209:51-202209:142", "202237:39-202237:128", "202237:131", "202237:134-202237:219", "202237:222-202237:235", 
        "202237:238-202237:275", "202237:277-202237:289", "202237:291-202237:316", "202237:319-202237:419", "202237:422-202237:538", 
        "202237:540-202237:936", "202237:939-202237:950", "202237:952-202237:976", "202237:979-202237:1079", "202272:76-202272:112", 
        "202272:115-202272:141", "202272:144-202272:185", "202272:188-202272:205", "202272:208-202272:305", "202272:307-202272:313", 
        "202272:315-202272:371", "202272:436-202272:480", "202272:483-202272:555", "202272:558-202272:577", "202272:579-202272:683", 
        "202272:686-202272:705", "202272:707-202272:740", "202272:742-202272:890", "202272:937-202272:1295", "202272:1299-202272:1481", 
        "202299:68-202299:84", "202299:87-202299:141", "202299:143-202299:193", "202299:196-202299:358", "202299:361-202299:379", 
        "202299:382-202299:414", "202299:416-202299:452", "202299:455-202299:555", "202305:1-202305:89", "202305:92-202305:130", 
        "202305:133-202305:323", "202314:67-202314:104", "202314:107-202314:265", "202314:268-202314:278", "202328:46-202328:89", 
        "202328:92-202328:156", "202328:158-202328:276", "202328:278-202328:291", "202328:294-202328:434", "202328:437-202328:460", 
        "202328:463-202328:586", "202328:588-202328:610", "202328:612-202328:614", "202333:1-202333:235", "202389:81-202389:182", 
        "202389:185-202389:190", "202389:192-202389:199", "202469:87-202469:158", "202469:160-202469:174", "202469:177-202469:352", 
        "202472:1-202472:96", "202472:99-202472:112", "202477:1-202477:129", "202477:131-202477:150", "202478:1-202478:177", 
        "202478:180-202478:183", "202478:186-202478:219", "202478:222-202478:360", "202478:362-202478:506", "202478:509-202478:531", 
        "202478:534-202478:718", "202478:720-202478:927", "202478:929-202478:973", "202478:975-202478:1029", "202478:1031-202478:1186", 
        "202478:1189-202478:1212", "202478:1215-202478:1248", "202504:77-202504:96", "202504:99-202504:133", "202504:135-202504:182", 
        "202504:184-202504:211", "202504:213-202504:241", "202504:243-202504:392", "202504:395-202504:527", "202504:529-202504:617", 
        "202504:620-202504:715", "202504:718-202504:763", "202504:766-202504:1172", "202504:1174-202504:1247", "202504:1250-202504:1471", 
        "202504:1474-202504:1679", "202504:1682-202504:1704", "202972:1-202972:30", "202972:33-202972:184", "202972:186-202972:290", 
        "202972:292-202972:295", "202972:298-202972:371", "202972:374-202972:429", "202972:431-202972:544", "202973:1-202973:234", 
        "202973:237-202973:305", "202973:308-202973:437", "202973:439-202973:530", "202973:532-202973:541", "202973:544-202973:552", 
        "202973:555-202973:851", "202973:853-202973:1408", "203002:77-203002:128", "203002:130-203002:141", "203002:144-203002:207", 
        "203002:209-203002:267", "203002:270-203002:360", "203002:362-203002:501", "203002:504-203002:641", "203002:643-203002:669", 
        "203002:671", "203002:674-203002:717", "203002:720-203002:1034", "203002:1037-203002:1070", "203002:1073-203002:1370", 
        "203002:1372-203002:1392", "203002:1395-203002:1410", "203002:1413-203002:1596", "203709:1-203709:121", "203742:1-203742:29", 
        "203777:103-203777:113", "203830:82-203830:182", "203832:1-203832:11", "203833:1-203833:70", "203833:73-203833:128", 
        "203834:1-203834:40", "203835:1-203835:70", "203835:73-203835:358", "203853:122-203853:222", "203894:82-203894:272", 
        "203894:275-203894:477", "203894:480-203894:902", "203894:905-203894:1319", "203909:79-203909:113", "203909:116-203909:117", 
        "203909:120-203909:140", "203909:143-203909:382", "203912:1-203912:306", "203912:308-203912:566", "203912:569-203912:609", 
        "203912:611-203912:698", "203912:701-203912:820", "203912:823-203912:865", "203912:867-203912:1033", "203912:1035-203912:1321", 
        "203987:1-203987:9", "203987:12-203987:241", "203987:243-203987:339", "203987:342-203987:781", "203987:784-203987:1014", 
        "203992:1-203992:15", "203994:1-203994:56", "203994:59-203994:136", "203994:139-203994:304", "203994:306-203994:342", 
        "203994:344-203994:425", "204100:117-204100:139", "204101:1-204101:74", "204113:82-204113:96", "204113:98-204113:102", 
        "204113:105-204113:127", "204113:129-204113:191", "204113:194-204113:258", "204113:261-204113:327", "204113:329-204113:388", 
        "204113:390-204113:400", "204113:402-204113:583", "204113:585-204113:690", "204114:1-204114:358", "204238:23-204238:52", 
        "204238:55", "204250:92-204250:118", "204250:121-204250:177", "204250:179-204250:285", "204250:287-204250:336", 
        "204250:339-204250:400", "204250:403-204250:521", "204250:524-204250:543", "204250:546-204250:682", "204250:684-204250:801", 
        "204511:1-204511:56", "204541:5-204541:39", "204541:42", "204541:44-204541:139", "204541:142-204541:149", 
        "204541:151-204541:204", "204544:1-204544:11", "204544:13-204544:93", "204544:96-204544:195", "204544:197-204544:224", 
        "204544:226-204544:334", "204544:337-204544:426", "204552:1-204552:9", "204553:1-204553:51", "204553:53-204553:60", 
        "204553:63-204553:101", "204554:1-204554:5", "204554:7-204554:221", "204554:224-204554:455", "204554:458-204554:470", 
        "204554:472-204554:481", "204554:483-204554:514", "204555:1-204555:329", "204555:331-204555:334", "204563:91-204563:99", 
        "204563:102-204563:178", "204563:180-204563:219", "204563:222-204563:229", "204563:231-204563:364", "204563:366", 
        "204563:369-204563:470", "204563:473-204563:524", "204563:527-204563:571", "204564:1-204564:84", "204564:87-204564:89", 
        "204564:92-204564:159", "204564:161-204564:187", "204564:190-204564:191", "204564:193-204564:293", "204564:296-204564:315", 
        "204564:317-204564:340", "204564:343-204564:427", "204564:429-204564:434", "204564:437-204564:735", "204564:737-204564:855", 
        "204564:858-204564:1206", "204564:1209-204564:1248", "204564:1251-204564:1284", "204565:1-204565:48", "204566:1-204566:12", 
        "204567:1-204567:38", "204576:49-204576:192", "204576:195-204576:301", "204577:1-204577:46", "204577:49-204577:64", 
        "204577:67-204577:105", "204577:107-204577:170", "204577:173-204577:181", "204577:183-204577:193", "204577:196-204577:653", 
        "204577:656-204577:669", "204577:671-204577:740", "204577:742-204577:913", "204577:915-204577:1057", "204577:1059-204577:1115", 
        "204577:1117-204577:1282", "204599:73-204599:83", "204599:85-204599:94", "204599:97-204599:121", "204599:124-204599:125", 
        "204599:128-204599:173", "204599:175-204599:240", "204599:243-204599:245", "204599:248-204599:264", "204599:266-204599:292", 
        "204599:294-204599:334", "204601:1-204601:25", "204601:28-204601:62", "204601:65-204601:80", "204601:83-204601:89", 
        "204601:92-204601:290", "204601:292-204601:563", "204601:565-204601:591", "204601:593-204601:652", "204601:655-204601:780", 
        "204601:783-204601:812", "204601:814-204601:892", "204601:894-204601:984", "204601:986-204601:1003", "204601:1006-204601:1038", 
        "204601:1040-204601:1088", "204601:1091-204601:1102", "204601:1105-204601:1161", "204601:1164-204601:1250", "205086:95-205086:149", 
        "205111:88-205111:390", "205111:392-205111:441", "205111:444-205111:446", "205158:81-205158:289", "205158:292-205158:313", 
        "205158:315-205158:473", "205158:476-205158:591", "205158:594-205158:595", "205158:597-205158:612", "205158:615-205158:663", 
        "205158:665-205158:667", "205158:672-205158:685", "205158:687-205158:733", "205193:80-205193:109", "205193:111-205193:349", 
        "205193:352-205193:486", "205193:488-205193:650", "205193:652-205193:712", "205193:714-205193:902", "205217:1-205217:12", 
        "205217:16-205217:111", "205217:113-205217:171", "205217:174-205217:250", "205217:253-205217:318", "205233:94-205233:153", 
        "205236:1-205236:190", "205236:193-205236:207", "205236:209-205236:260", "205236:263-205236:331", "205236:334-205236:352", 
        "205238:1-205238:6", "205238:9-205238:199", "205238:202-205238:254", "205238:256-205238:304", "205238:306-205238:355", 
        "205238:358-205238:381", "205238:384-205238:596", "205238:598-205238:617", "205303:35-205303:54", "205303:90-205303:132", 
        "205303:135-205303:144", "205310:76-205310:306", "205310:309-205310:313", "205310:316", "205310:319-205310:321", 
        "205310:324-205310:457", "205310:460-205310:559", "205311:1-205311:85", "205311:88-205311:92", "205311:95-205311:183", 
        "205311:186-205311:395", "205311:397-205311:592", "205311:595-205311:910", "205311:913-205311:1260", "205339:71-205339:175", 
        "205339:178-205339:213", "205339:216-205339:230", "205339:233-205339:262", "205339:265-205339:404", "205344:1-205344:83", 
        "205344:86-205344:104", "205344:106-205344:359", "205344:362-205344:431", "205344:433-205344:949", "205344:951-205344:967", 
        "205344:969-205344:1127", "205344:1129-205344:1346", "205344:1348-205344:1586", "205515:82-205515:201", "205515:203-205515:216", 
        "205519:1-205519:47", "205519:50-205519:172", "205519:175-205519:367", "205519:370-205519:386", "205519:389-205519:472", 
        "205526:1-205526:269", "205526:272-205526:277", "205526:280-205526:332", "205614:1-205614:4", "205614:7-205614:40", 
        "205617:1-205617:29", "205617:32-205617:102", "205617:105-205617:123", "205617:125-205617:140", "205617:143-205617:264", 
        "205617:266-205617:448", "205617:451-205617:532", "205617:534-205617:547", "205618:1-205618:12", "205620:1-205620:175", 
        "205666:60-205666:119", "205666:122-205666:165", "205666:168-205666:259", "205666:261-205666:322", "205666:325-205666:578", 
        "205666:580-205666:594", "205666:597-205666:721", "205666:724-205666:739", "205667:1-205667:165", "205667:168-205667:282", 
        "205667:285-205667:318", "205667:321-205667:412", "205667:415-205667:689", "205667:692-205667:751", "205667:754-205667:774", 
        "205667:777-205667:1109", "205683:76-205683:82", "205683:85-205683:178", "205683:181-205683:198", "205683:201-205683:305", 
        "205690:1-205690:40", "205694:1-205694:205", "205694:208-205694:230", "205694:233-205694:347", "205694:350-205694:452", 
        "205694:455-205694:593", "205694:595-205694:890", "205718:49-205718:75", "205718:78-205718:97", "205718:100-205718:103", 
        "205718:105-205718:176", "205718:178-205718:338", "205718:341-205718:361", "205718:363-205718:524", "205718:527-205718:531", 
        "205718:534-205718:589", "205718:591-205718:694", "205774:1-205774:80", "205777:1-205777:8", "205781:1-205781:89", 
        "205781:91-205781:197", "205781:200-205781:502", "205826:80-205826:232", "205826:235-205826:303", "205826:306-205826:468", 
        "205833:84-205833:86", "205833:89-205833:121", "205833:123-205833:155", "205833:157-205833:165", "205833:167-205833:173", 
        "205833:176-205833:219", "205833:221-205833:267", "205833:270-205833:312", "205833:315-205833:346", "205833:350-205833:355", 
        "205833:360-205833:366", "205834:1-205834:12", "205834:14-205834:195", "205908:68-205908:200", "205908:202-205908:209", 
        "205921:22-205921:73", "205921:76-205921:268", "205921:271-205921:394", "205921:397-205921:401", "205921:410-205921:428", 
        "205921:431-205921:498", "205921:500-205921:571", "205921:574-205921:779", "205921:782-205921:853", "206066:89-206066:146", 
        "206088:86-206088:159", "206088:161-206088:178", "206088:181-206088:199", "206088:202-206088:286", "206102:83-206102:116", 
        "206102:120-206102:130", "206102:133-206102:208", "206102:211-206102:235", "206102:238-206102:246", "206102:249-206102:278", 
        "206102:281-206102:349", "206187:107-206187:169", "206187:172-206187:242", "206187:245-206187:288", "206187:290-206187:340", 
        "206187:343-206187:427", "206187:429-206187:435", "206187:437-206187:486", "206187:489-206187:569", "206187:571-206187:647", 
        "206187:649-206187:662", "206187:664-206187:708", "206188:1-206188:40", "206188:42-206188:55", "206199:1-206199:75", 
        "206199:77-206199:82", "206199:85-206199:114", "206207:82-206207:130", "206207:132-206207:176", "206207:179-206207:194", 
        "206207:196-206207:388", "206207:390-206207:419", "206207:422-206207:447", "206207:450-206207:569", "206207:572-206207:690", 
        "206208:1-206208:470", "206208:472-206208:518", "206210:11-206210:25", "206210:28-206210:275", "206210:277-206210:298", 
        "206210:300-206210:383", "206210:386-206210:466", "206243:62-206243:169", "206243:172-206243:196", "206243:199-206243:354", 
        "206243:357-206243:433", "206243:435-206243:448", "206243:451-206243:533", "206243:536-206243:554", "206243:557-206243:723", 
        "206243:726-206243:905", "206245:1-206245:62", "206246:1-206246:14", "206246:16-206246:237", "206246:240-206246:285", 
        "206246:288-206246:407", "206246:412-206246:676", "206246:678-206246:704", "206246:706-206246:785", "206246:787-206246:962", 
        "206246:965-206246:997", "206246:1000-206246:1198", "206246:1201-206246:1290", "206257:1-206257:29", "206258:1-206258:36", 
        "206258:39-206258:223", "206258:226-206258:249", "206302:1-206302:8", "206302:11-206302:33", "206302:36-206302:44", 
        "206302:47-206302:82", "206302:84-206302:108", "206302:110-206302:149", "206302:151-206302:186", "206302:189-206302:229", 
        "206302:231-206302:232", "206302:234-206302:241", "206302:243-206302:276", "206303:1-206303:19", "206303:23-206303:286", 
        "206304:1-206304:4", "206304:6-206304:62", "206331:91-206331:222", "206331:225-206331:312", "206389:88-206389:185", 
        "206389:187-206389:249", "206389:252-206389:272", "206389:275-206389:392", "206391:1-206391:55", "206391:57-206391:91", 
        "206401:69-206401:90", "206401:92-206401:194", "206401:197-206401:210", "206401:212-206401:249", "206401:251-206401:265", 
        "206401:267-206401:409", "206446:92-206446:141", "206446:143-206446:159", "206446:162-206446:205", "206446:208-206446:301", 
        "206446:304-206446:442", "206446:445", "206446:448-206446:474", "206446:476-206446:616", "206446:619-206446:872", 
        "206446:874-206446:910", "206446:912-206446:948", "206446:950-206446:989", "206446:992-206446:1030", "206446:1033-206446:1075", 
        "206446:1109-206446:1149", "206448:1-206448:143", "206448:145-206448:559", "206448:561-206448:1170", "206448:1173-206448:1231", 
        "206448:1235-206448:1237", "206466:24-206466:137", "206466:140-206466:277", "206466:280-206466:296", "206466:299-206466:303", 
        "206466:306-206466:405", "206466:407-206466:419", "206466:422-206466:477", "206466:480-206466:511", "206466:514-206466:676", 
        "206476:73-206476:129", "206476:133-206476:137", "206476:140-206476:141", "206476:143-206476:219", "206477:1-206477:14", 
        "206477:16-206477:31", "206477:33-206477:41", "206477:44-206477:51", "206477:53-206477:70", "206477:73-206477:75", 
        "206477:77-206477:89", "206477:91-206477:94", "206477:97-206477:115", "206477:118-206477:184", "206478:1-206478:27", 
        "206478:29-206478:136", "206478:139-206478:144", "206484:73-206484:95", "206484:98-206484:133", "206484:136-206484:163", 
        "206484:166-206484:186", "206484:189-206484:384", "206484:387-206484:463", "206484:465-206484:551", "206484:554", 
        "206484:556-206484:669", "206512:91-206512:123", "206512:125-206512:133", "206512:136-206512:161", "206512:163-206512:190", 
        "206512:193-206512:201", "206512:203-206512:212", "206512:214-206512:332", "206512:334-206512:584", "206512:587-206512:604", 
        "206512:607-206512:1005", "206512:1008-206512:1123", "206512:1126-206512:1163", "206512:1165-206512:1211", "206513:3-206513:39", 
        "206513:42-206513:188", "206513:191-206513:234", "206513:237-206513:238", "206513:241-206513:323", "206542:1-206542:115", 
        "206542:117-206542:165", "206542:168-206542:511", "206542:514-206542:547", "206542:550-206542:603", "206542:606-206542:668", 
        "206542:671-206542:727", "206542:730-206542:739", "206542:741-206542:833", "206550:77-206550:132", "206550:135-206550:144", 
        "206572:37-206572:47", "206573:2-206573:14", "206574:1-206574:87", "206575:1-206575:7", "206575:10", 
        "206575:12-206575:69", "206594:72-206594:107", "206594:110-206594:246", "206594:249-206594:281", "206595:1-206595:34", 
        "206595:37-206595:42", "206595:45-206595:193", "206596:1-206596:13", "206596:15-206596:220", "206596:222-206596:228", 
        "206596:231-206596:236", "206596:239-206596:292", "206596:295-206596:695", "206596:697-206596:728", "206596:730-206596:810", 
        "206598:1-206598:81", "206598:83-206598:103", "206598:105-206598:588", "206598:591-206598:657", "206598:659-206598:719", 
        "206605:1-206605:36", "206605:39-206605:78", "206744:49-206744:157", "206744:160-206744:192", "206744:195-206744:395", 
        "206744:398-206744:452", "206745:1-206745:81", "206745:84-206745:199", "206745:202-206745:224", "206745:227-206745:237", 
        "206745:240-206745:304", "206745:306-206745:318", "206745:321-206745:720", "206745:723-206745:796", "206745:799-206745:894", 
        "206745:897-206745:944", "206745:946-206745:1106", "206745:1108-206745:1524", "206745:1527-206745:1862", "206745:1988-206745:1996", 
        "206859:79-206859:210", "206859:212-206859:258", "206859:260-206859:323", "206859:325-206859:356", "206859:359-206859:609", 
        "206859:612-206859:681", "206859:684-206859:732", "206859:734-206859:768", "206859:771-206859:808", "206859:811-206859:827", 
        "206859:830-206859:848", "206866:1-206866:30", "206866:33-206866:113", "206866:115-206866:274", "206868:1-206868:3", 
        "206868:10-206868:16", "206869:1-206869:251", "206869:253-206869:271", "206869:274-206869:502", "206869:507-206869:520", 
        "206869:522-206869:566", "206869:568-206869:752", "206897:1-206897:34", "206897:38-206897:61", "206897:63-206897:102", 
        "206897:109", "206897:111-206897:112", "206897:114-206897:131", "206897:133-206897:137", "206901:1-206901:98", 
        "206906:1-206906:31", "206906:38-206906:94", "206906:96-206906:136", "206906:138-206906:139", "206906:142-206906:149", 
        "206906:151-206906:175", "206906:177-206906:206", "206940:1-206940:151", "206940:153", "206940:155-206940:298", 
        "206940:301-206940:382", "206940:384-206940:712", "206940:715-206940:803", "206940:805-206940:960", "206940:963-206940:1027", 
        "207099:83-207099:134", "207099:137-207099:172", "207099:175-207099:213", "207099:216-207099:314", "207099:316-207099:320", 
        "207099:323-207099:330", "207099:333-207099:367", "207099:370-207099:481", "207099:484-207099:602", "207099:605-207099:755", 
        "207099:757-207099:1046", "207099:1048-207099:1171", "207100:1-207100:91", "207100:94", "207214:57-207214:112", 
        "207214:114-207214:177", "207214:179-207214:181", "207214:184-207214:196", "207214:199-207214:220", "207214:223-207214:262", 
        "207214:265-207214:405", "207214:408-207214:482", "207214:485-207214:640", "207214:643-207214:708", "207214:718-207214:757", 
        "207214:759-207214:808", "207214:811-207214:829", "207217:1-207217:32", "207219:1-207219:112", "207220:1-207220:160", 
        "207221:1-207221:102", "207222:1-207222:17", "207222:20-207222:289", "207231:70-207231:84", "207231:86-207231:121", 
        "207231:123-207231:184", "207231:187-207231:189", "207231:192-207231:303", "207231:306-207231:354", "207231:357-207231:481", 
        "207231:484-207231:504", "207231:508-207231:549", "207231:552-207231:626", "207231:628-207231:690", "207231:693-207231:875", 
        "207231:878-207231:1000", "207231:1003-207231:1170", "207231:1173-207231:1187", "207231:1189-207231:1227", "207231:1229-207231:1415", 
        "207231:1418-207231:1445", "207231:1447-207231:1505", "207233:1-207233:119", "207233:121-207233:148", "207269:80-207269:394", 
        "207269:397-207269:436", "207269:439-207269:463", "207269:466-207269:551", "207269:568-207269:577", "207273:3-207273:877", 
        "207279:68-207279:138", "207279:141-207279:149", "207279:151-207279:237", "207279:240-207279:266", "207279:269-207279:307", 
        "207279:309-207279:416", "207279:498-207279:551", "207279:554-207279:640", "207279:643-207279:961", "207279:963-207279:1095", 
        "207279:1098-207279:1160", "207320:1-207320:110", "207320:112-207320:350", "207371:72-207371:117", "207371:120-207371:124", 
        "207372:1-207372:27", "207372:30-207372:113", "207372:116-207372:154", "207372:156-207372:174", "207372:176-207372:478", 
        "207372:480-207372:496", "207397:32-207397:77", "207397:80-207397:140", "207397:143-207397:179", "207398:1-207398:14", 
        "207398:16-207398:33", "207454:79-207454:95", "207454:98-207454:123", "207454:126-207454:259", "207454:261-207454:363", 
        "207454:365-207454:458", "207454:461-207454:498", "207454:501-207454:609", "207454:612-207454:632", "207454:635-207454:781", 
        "207454:784-207454:866", "207454:869-207454:974", "207454:977-207454:1064", "207454:1067-207454:1079", "207454:1081-207454:1321", 
        "207454:1323-207454:1464", "207454:1467-207454:1569", "207454:1571-207454:1604", "207454:1607-207454:1712", "207454:1714-207454:1988", 
        "207469:1-207469:31", "207469:34-207469:45", "207477:76-207477:104", "207477:107-207477:111", "207477:114-207477:147", 
        "207477:150-207477:295", "207477:298-207477:483", "207477:486-207477:494", "207477:497-207477:527", "207477:530-207477:563", 
        "207477:565-207477:570", "207487:50-207487:98", "207487:101-207487:311", "207487:313-207487:359", "207487:363-207487:468", 
        "207487:471-207487:472", "207488:1-207488:63", "207488:66-207488:92", "207488:95-207488:113", "207488:116-207488:198", 
        "207488:200-207488:250", "207488:252-207488:288", "207488:291-207488:365", "207488:368-207488:377", "207488:379-207488:440", 
        "207490:1-207490:48", "207490:51-207490:111", "207491:1-207491:176", "207491:179-207491:458", "207492:1-207492:20", 
        "207492:23-207492:298", "207515:79-207515:109", "207515:112-207515:132", "207515:134-207515:208", "207515:211-207515:225", 
        "207515:228-207515:320", "207515:322-207515:381", "207515:383-207515:498", "207515:500-207515:730", "207515:733-207515:849", 
        "207515:851-207515:954", "207515:957-207515:994", "207515:997-207515:1052", "207515:1055-207515:1143", "207515:1145-207515:1211", 
        "207517:1-207517:12", "207517:15-207517:57", "207518:1-207518:59", "207518:61-207518:83", "207882:22-207882:45", 
        "207883:1", "207883:3-207883:4", "207883:7-207883:75", "207884:1-207884:106", "207884:108-207884:183", 
        "207885:1-207885:90", "207886:1-207886:30", "207886:32-207886:90", "207886:92-207886:156", "207886:158-207886:166", 
        "207886:168-207886:171", "207889:1-207889:43", "207889:47-207889:57", "207889:60-207889:303", "207889:306-207889:442", 
        "207889:445", "207889:447-207889:551", "207889:553-207889:731", "207889:733-207889:907", "207889:910-207889:945", 
        "207898:1-207898:33", "207898:36-207898:57", "207898:60-207898:235", "207898:239-207898:257", "207898:260-207898:277", 
        "207905:75-207905:196", "207905:198-207905:281", "207905:284-207905:329", "207905:331-207905:402", "207905:404-207905:565", 
        "207905:568-207905:672", "207905:675-207905:805", "207905:807-207905:850", "207905:852-207905:861", "207905:864-207905:884", 
        "207905:886-207905:1180", "207905:1183-207905:1283", "207905:1285-207905:1331", "207905:1333-207905:1515", "207905:1518-207905:1734", 
        "207905:1737-207905:1796", "207920:84-207920:146", "207920:149-207920:241", "207920:243-207920:261", "207920:264-207920:291", 
        "207920:294-207920:486", "207920:489-207920:518", "207920:520-207920:598", "207920:600-207920:708", "207920:710-207920:826", 
        "207921:1-207921:37", "207921:40-207921:58", "207922:1-207922:69", "207922:71-207922:100", "207922:103-207922:126", 
        "207922:129-207922:242", "207922:274-207922:291", "207924:1-207924:52", "207924:54-207924:171", "207924:173-207924:178", 
        "207924:181-207924:339", "208307:2-208307:42", "208307:45", "208307:47-208307:70", "208307:72-208307:147", 
        "208307:150-208307:252", "208307:256-208307:259", "208307:262-208307:275", "208307:278-208307:342", "208307:345-208307:450", 
        "208307:453-208307:527", "208307:530-208307:583", "208307:586-208307:605", "208307:608-208307:616", "208307:618-208307:667", 
        "208307:670-208307:761", "208307:763-208307:798", "208307:800-208307:889", "208307:891-208307:893", "208307:896-208307:1055", 
        "208307:1057-208307:1205", "208307:1208-208307:1294", "208307:1297-208307:1328", "208339:77-208339:89", "208339:91-208339:122", 
        "208339:125-208339:208", "208339:211-208339:346", "208339:349-208339:363", "208341:1-208341:84", "208341:87-208341:117", 
        "208341:120-208341:513", "208341:515-208341:685", "208341:688-208341:693", "208341:695-208341:775", "208341:777-208341:824", 
        "208351:83-208351:97", "208351:100-208351:356", "208351:359-208351:367", "208351:369", "208352:1-208352:15", 
        "208352:17", "208352:19", "208353:1-208353:76", "208353:78-208353:269", "208353:271-208353:348", 
        "208357:1-208357:70", "208357:73-208357:507", "208390:72-208390:128", "208390:130-208390:169", "208391:52-208391:82", 
        "208391:84-208391:162", "208391:164-208391:216", "208391:219-208391:493", "208391:495-208391:498", "208391:500-208391:523", 
        "208391:526-208391:533", "208391:535-208391:588", "208391:591-208391:660", "208391:663-208391:869", "208427:49-208427:89", 
        "208427:92-208427:161", "208427:164", "208427:166-208427:173", "208427:175-208427:268", "208427:271-208427:312", 
        "208427:315", "208427:317-208427:335", "208427:337-208427:361", "208427:364-208427:402", "208427:404-208427:422", 
        "208427:425-208427:577", "208427:580-208427:647", "208428:1-208428:58", "208428:61-208428:68", "208428:70-208428:156", 
        "208428:159-208428:227", "208429:1-208429:56", "208429:59-208429:139", "208429:141-208429:159", "208429:162-208429:237", 
        "208429:240-208429:440", "208429:442-208429:452", "208429:455-208429:589", "208429:592-208429:712", "208429:715-208429:922", 
        "208487:2-208487:26", "208487:29-208487:159", "208487:161-208487:307", "208487:309-208487:459", "208487:462-208487:476", 
        "208487:479-208487:621", "208509:71-208509:232", "208538:2-208538:43", "208540:1-208540:26", "208540:29-208540:98", 
        "208541:1-208541:57", "208541:59-208541:173", "208541:175-208541:376", "208541:378-208541:413", "208551:119-208551:193", 
        "208551:195-208551:212", "208551:215-208551:300", "208551:303-208551:354", "208551:356-208551:554", "208551:557-208551:580", 
        "208686:73-208686:79", "208686:82-208686:181", "208686:183-208686:224", "208686:227-208686:243", "208686:246-208686:311", 
        "208686:313-208686:459" ) )
)
process.cmgDiTauCorSVFitPreSel = cms.EDProducer("TauTauWithSVFitProducer",
    diTauSrc = cms.InputTag("recoilCorMETDiTau"),
    SVFitVersion = cms.int32(2),
    verbose = cms.untracked.bool(False)
)


process.cmgTauEleCorSVFitPreSel = cms.EDProducer("TauEleWithSVFitProducer",
    diTauSrc = cms.InputTag("recoilCorMETTauEle"),
    SVFitVersion = cms.int32(2),
    verbose = cms.untracked.bool(False)
)


process.cmgTauMuCorSVFitPreSel = cms.EDProducer("TauMuWithSVFitProducer",
    diTauSrc = cms.InputTag("recoilCorMETTauMu"),
    SVFitVersion = cms.int32(2),
    verbose = cms.untracked.bool(False)
)


process.diTauSVFit = cms.EDProducer("TauTauWithSVFitProducer",
    diTauSrc = cms.InputTag("cmgDiTauCorPreSel"),
    SVFitVersion = cms.int32(2),
    verbose = cms.untracked.bool(False)
)


process.embeddingKineReweightGENembedding = cms.EDProducer("EmbeddingKineReweightProducer",
    verbosity = cms.int32(0),
    maxWeight = cms.double(10.0),
    lutNames = cms.PSet(
        genDiTauMassVsGenDiTauPt = cms.string('embeddingKineReweight_diMuonMass_vs_diMuonPt'),
        genTau2EtaVsGenTau1Eta = cms.string('embeddingKineReweight_muon2Eta_vs_muon1Eta'),
        genTau2PtVsGenTau1Pt = cms.string('embeddingKineReweight_muon2Pt_vs_muon1Pt')
    ),
    inputFileName = cms.FileInPath('TauAnalysis/MCEmbeddingTools/data/embeddingKineReweight_genEmbedding_mutau.root'),
    srcGenDiTaus = cms.InputTag("genZdecayToTausForEmbeddingKineReweight"),
    minWeight = cms.double(0.0)
)


process.embeddingKineReweightRECembedding = cms.EDProducer("EmbeddingKineReweightProducer",
    verbosity = cms.int32(0),
    maxWeight = cms.double(10.0),
    lutNames = cms.PSet(
        genDiTauMassVsGenDiTauPt = cms.string('embeddingKineReweight_diMuonMass_vs_diMuonPt'),
        genTau2EtaVsGenTau1Eta = cms.string('embeddingKineReweight_muon2Eta_vs_muon1Eta'),
        genTau2PtVsGenTau1Pt = cms.string('embeddingKineReweight_muon2Pt_vs_muon1Pt')
    ),
    inputFileName = cms.FileInPath('TauAnalysis/MCEmbeddingTools/data/embeddingKineReweight_tautau_recEmbedded.root'),
    srcGenDiTaus = cms.InputTag("genZdecayToTausForEmbeddingKineReweight"),
    minWeight = cms.double(0.0)
)


process.genTausFromZsForEmbeddingKineReweight = cms.EDProducer("GenParticlesFromZsSelectorForMCEmbedding",
    src = cms.InputTag("genParticles"),
    minDaughters = cms.int32(2),
    pdgIdsDaughters = cms.vint32(15),
    before_or_afterFSR = cms.string('afterFSR'),
    pdgIdsMothers = cms.vint32(23, 22),
    maxDaughters = cms.int32(2)
)


process.genWorZ = cms.EDProducer("GenParticlePruner",
    src = cms.InputTag("genParticlesPruned"),
    select = cms.vstring('keep status()==3 & pdgId = {W+}', 
        'keep status()==3 & pdgId = {W-}', 
        'keep status()==3 & pdgId = {Z0}', 
        'keep status()==3 & pdgId = {gamma}', 
        'keep status()==3 & pdgId = {h0}', 
        'keep status()==3 & pdgId = 35', 
        'keep status()==3 & pdgId = 36')
)


process.genZdecayToTausForEmbeddingKineReweight = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(True),
    cut = cms.string('charge = 0'),
    decay = cms.string('genTausFromZsForEmbeddingKineReweight@+ genTausFromZsForEmbeddingKineReweight@-')
)


process.mvaMETDiTau = cms.EDProducer("MVAMETProducerDiTau",
    pucmetSrc = cms.InputTag("pcMet"),
    enable = cms.bool(True),
    tkmetSrc = cms.InputTag("tkMet"),
    verbose = cms.untracked.bool(False),
    nopumetSrc = cms.InputTag("nopuMet"),
    rhoSrc = cms.InputTag("kt6PFJets","rho"),
    pfmetSrc = cms.InputTag("pfMetForRegression"),
    weights_gbrmetphi = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmetphi_53_Dec2012.root'),
    pumetSrc = cms.InputTag("puMet"),
    weights_gbrmetu1cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru1cov_53_Dec2012.root'),
    weights_gbrmetu2cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru2cov_53_Dec2012.root'),
    vertexSrc = cms.InputTag("goodPVFilter"),
    jetSrc = cms.InputTag("cmgPFJetSel"),
    leadJetSrc = cms.InputTag("cmgPFBaseJetLead"),
    recBosonSrc = cms.InputTag("cmgDiTauPreSel"),
    nJetsPtGt1Src = cms.InputTag("nJetsPtGt1"),
    weights_gbrmet = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmet_53_Dec2012.root'),
    puJetIdLabel = cms.string('met53x')
)


process.mvaMETTauEle = cms.EDProducer("MVAMETProducerTauEle",
    pucmetSrc = cms.InputTag("pcMet"),
    enable = cms.bool(True),
    tkmetSrc = cms.InputTag("tkMet"),
    verbose = cms.untracked.bool(False),
    nopumetSrc = cms.InputTag("nopuMet"),
    rhoSrc = cms.InputTag("kt6PFJets","rho"),
    pfmetSrc = cms.InputTag("pfMetForRegression"),
    weights_gbrmetphi = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmetphi_53_Dec2012.root'),
    pumetSrc = cms.InputTag("puMet"),
    weights_gbrmetu1cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru1cov_53_Dec2012.root'),
    weights_gbrmetu2cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru2cov_53_Dec2012.root'),
    vertexSrc = cms.InputTag("goodPVFilter"),
    jetSrc = cms.InputTag("cmgPFJetSel"),
    leadJetSrc = cms.InputTag("cmgPFBaseJetLead"),
    recBosonSrc = cms.InputTag("cmgTauElePreSel"),
    nJetsPtGt1Src = cms.InputTag("nJetsPtGt1"),
    weights_gbrmet = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmet_53_Dec2012.root'),
    puJetIdLabel = cms.string('met53x')
)


process.mvaMETTauMu = cms.EDProducer("MVAMETProducerTauMu",
    pucmetSrc = cms.InputTag("pcMet"),
    enable = cms.bool(True),
    tkmetSrc = cms.InputTag("tkMet"),
    verbose = cms.untracked.bool(False),
    nopumetSrc = cms.InputTag("nopuMet"),
    rhoSrc = cms.InputTag("kt6PFJets","rho"),
    pfmetSrc = cms.InputTag("pfMetForRegression"),
    weights_gbrmetphi = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmetphi_53_Dec2012.root'),
    pumetSrc = cms.InputTag("puMet"),
    weights_gbrmetu1cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru1cov_53_Dec2012.root'),
    weights_gbrmetu2cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru2cov_53_Dec2012.root'),
    vertexSrc = cms.InputTag("goodPVFilter"),
    jetSrc = cms.InputTag("cmgPFJetSel"),
    leadJetSrc = cms.InputTag("cmgPFBaseJetLead"),
    recBosonSrc = cms.InputTag("cmgTauMuPreSel"),
    nJetsPtGt1Src = cms.InputTag("nJetsPtGt1"),
    weights_gbrmet = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmet_53_Dec2012.root'),
    puJetIdLabel = cms.string('met53x')
)


process.recoilCorMETDiTau = cms.EDProducer("RecoilCorrectedMETProducerDiTau",
    enable = cms.bool(False),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_ztt53X_20pv_njet.root'),
    leptonLeg = cms.int32(0),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgDiTauPtSel")
)


process.recoilCorMETTauEle = cms.EDProducer("RecoilCorrectedMETProducerTauEle",
    enable = cms.bool(False),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    leptonLeg = cms.int32(2),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauEleTauPtSel")
)


process.recoilCorMETTauMu = cms.EDProducer("RecoilCorrectedMETProducerTauMu",
    enable = cms.bool(False),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    leptonLeg = cms.int32(2),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauMuTauPtSel")
)


process.recoilCorrectedMETDiTau = cms.EDProducer("RecoilCorrectedMETProducerDiTau",
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_ztt53X_20pv_njet.root'),
    leptonLeg = cms.int32(0),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgDiTauSel")
)


process.recoilCorrectedMETMuEle = cms.EDProducer("RecoilCorrectedMETProducerMuEle",
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    leptonLeg = cms.int32(2),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgMuEleSel"),
    metSrc = cms.InputTag("cmgPFMET")
)


process.recoilCorrectedMETTauEle = cms.EDProducer("RecoilCorrectedMETProducerTauEle",
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    leptonLeg = cms.int32(2),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauEleSel")
)


process.recoilCorrectedMETTauMu = cms.EDProducer("RecoilCorrectedMETProducerTauMu",
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    leptonLeg = cms.int32(2),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauMuSel")
)


process.tauEleSVFit = cms.EDProducer("TauEleWithSVFitProducer",
    diTauSrc = cms.InputTag("cmgTauEleCorPreSel"),
    SVFitVersion = cms.int32(2),
    verbose = cms.untracked.bool(False)
)


process.tauMuSVFit = cms.EDProducer("TauMuWithSVFitProducer",
    diTauSrc = cms.InputTag("cmgTauMuCorPreSel"),
    SVFitVersion = cms.int32(2),
    verbose = cms.untracked.bool(False)
)


process.vertexWeight05AugReReco = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v2.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeight2011AB = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_160404-180252_4.6invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeight2011B = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2011B.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeight2invfb = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_160404-173692_2.1invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeight3D05AugReReco = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v2.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeight3D2011AB = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_160404-180252_4.6invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeight3D2011B = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_2011B.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeight3D2invfb = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_160404-173692_2.1invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeight3DFall1105AugReReco = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v2.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DFall112011AB = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_160404-180252_4.6invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DFall112011B = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_2011B.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DFall112invfb = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_160404-173692_2.1invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DFall11May10ReReco = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DFall11PromptRecov4 = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_165088-167913_7TeV_PromptReco_JSON.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DFall11PromptRecov6 = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_172620-173692_PromptReco_JSON.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Fall11MC.root')
)


process.vertexWeight3DMay10ReReco = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeight3DPromptRecov4 = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_165088-167913_7TeV_PromptReco_JSON.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeight3DPromptRecov6 = cms.EDProducer("PileUpWeight3DProducer",
    verbose = cms.untracked.bool(False),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_172620-173692_PromptReco_JSON.pileupTruth_v2_finebin.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup3D_Summer11MC.root')
)


process.vertexWeightEPSJul8 = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Pileup_2011_EPS_8_jul.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeightFall1105AugReReco = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v2.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall112011AB = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_160404-180252_4.6invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall112011B = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2011B.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall112invfb = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_160404-173692_2.1invfb.pileup.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall11EPSJul8 = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Pileup_2011_EPS_8_jul.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall11LeptonPhoton = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Pileup_2011_to_172802_LP_LumiScale.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall11May10ReReco = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall11PromptRecov4 = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_165088-167913_7TeV_PromptReco_JSON.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightFall11PromptRecov6 = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_172620-173692_PromptReco_JSON.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Fall11MC.root')
)


process.vertexWeightLeptonPhoton = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Pileup_2011_to_172802_LP_LumiScale.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeightMay10ReReco = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeightPromptRecov4 = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_165088-167913_7TeV_PromptReco_JSON.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeightPromptRecov6 = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(1),
    inputHistData = cms.string('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/Cert_172620-173692_PromptReco_JSON.pileup_v2.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer11MC.root')
)


process.vertexWeightSummer12MC53X2012ABCDData = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(2),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2012ABCD.true.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer12MC53X.true.root')
)


process.vertexWeightSummer12MC53X2012BCDData = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(2),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2012BCD.true.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer12MC53X.true.root')
)


process.vertexWeightSummer12MC53X2012D6fbData = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(2),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2012D6fb_203894_207898.true.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer12MC53X.true.root')
)


process.vertexWeightSummer12MC53XHCPData = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(2),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2012HCP_190456_203002.true.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer12MC53X.true.root')
)


process.vertexWeightSummer12MC53XICHEPData = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(2),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2012ICHEP_start_196509.true.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer12MC53X.true.root')
)


process.vertexWeightSummer12MCICHEPData = cms.EDProducer("PileUpWeightProducer",
    src = cms.InputTag("addPileupInfo"),
    verbose = cms.untracked.bool(False),
    type = cms.int32(2),
    inputHistData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_2012ICHEP_start_196509.true.root'),
    inputHistMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/RootTools/data/vertexWeight/Pileup_Summer12MC52X.true.root')
)


process.cmgBaseMETFromPFMET = cms.EDFilter("PFMETPOProducer",
    cfg = cms.PSet(
        ptThreshold = cms.double(-1.0),
        inputCollection = cms.InputTag("pfMet")
    ),
    cuts = cms.PSet(

    )
)


process.cmgDiTau = cms.EDFilter("DiTauPOProducer",
    cfg = cms.PSet(
        leg2Collection = cms.InputTag("cmgTauSel"),
        leg1Collection = cms.InputTag("cmgTauSel"),
        metsigCollection = cms.InputTag(""),
        metCollection = cms.InputTag("cmgPFMET")
    ),
    cuts = cms.PSet(
        baseline = cms.PSet(
            tau1Leg = cms.PSet(
                iso = cms.string('leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
                kinematics = cms.PSet(
                    eta = cms.string('abs(leg1().eta())<2.1'),
                    pt = cms.string('leg1().pt()>35.')
                ),
                id = cms.PSet(
                    decay = cms.string('leg1().tauID("decayModeFinding")')
                )
            ),
            mass = cms.string('mass()>10'),
            tau2Leg = cms.PSet(
                iso = cms.string('leg2().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
                kinematics = cms.PSet(
                    eta = cms.string('abs(leg2().eta())<2.1'),
                    pt = cms.string('leg2().pt()>35.')
                ),
                id = cms.PSet(
                    decay = cms.string('leg2().tauID("decayModeFinding")')
                )
            )
        )
    )
)


process.cmgDiTauCor = cms.EDFilter("DiTauUpdatePOProducer",
    cfg = cms.PSet(
        shift1Prong1Pi0 = cms.double(0.012),
        diObjectCollection = cms.InputTag("mvaMETDiTau"),
        leg1Collection = cms.InputTag(""),
        shiftMet = cms.bool(True),
        shiftTaus = cms.bool(True),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.012),
        nSigma = cms.double(1),
        leg2Collection = cms.InputTag(""),
        ptDependence1Pi0 = cms.double(0.0),
        ptDependence3Prong = cms.double(0.0)
    ),
    cuts = cms.PSet(

    )
)


process.cmgDiTauCorSVFitFullSel = cms.EDFilter("CmgDiTauSelector",
    src = cms.InputTag("cmgDiTauCorSVFitPreSel"),
    cut = cms.string('')
)


process.cmgDiTauCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgDiTauSel"),
    minNumber = cms.uint32(1)
)


process.cmgDiTauPreSel = cms.EDFilter("CmgDiTauSelector",
    src = cms.InputTag("cmgDiTau"),
    cut = cms.string('leg1().pt()>38. && leg2().pt()>38. && leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10. &&  leg2().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.')
)


process.cmgDiTauPtSel = cms.EDFilter("CmgDiTauSelector",
    src = cms.InputTag("cmgDiTauCor"),
    cut = cms.string('leg1().pt()>45. && leg2().pt()>45.')
)


process.cmgDiTauSel = cms.EDFilter("CmgDiTauSelector",
    src = cms.InputTag("cmgDiTau"),
    cut = cms.string(' pt()>0 ')
)


process.cmgMuEle = cms.EDFilter("MuElePOProducer",
    cfg = cms.PSet(
        leg2Collection = cms.InputTag("cmgElectronSel"),
        leg1Collection = cms.InputTag("cmgMuonSel"),
        metCollection = cms.InputTag("")
    ),
    cuts = cms.PSet(

    )
)


process.cmgMuEleCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgMuEleSel"),
    minNumber = cms.uint32(1)
)


process.cmgMuEleSel = cms.EDFilter("CmgMuEleSelector",
    src = cms.InputTag("cmgMuEle"),
    cut = cms.string('pt()>0')
)


process.cmgPFJetForRecoil = cms.EDFilter("CMGJetPUIDSelector",
    src = cms.InputTag("cmgPFJetForRecoilPresel"),
    cut = cms.string(''),
    puJetIDParams = cms.VPSet(cms.PSet(
        minDiscs = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        maxPt = cms.double(20.0),
        minPt = cms.double(0.0),
        maxEtas = cms.vdouble(2.5, 2.75, 3.0, 5.0)
    ), 
        cms.PSet(
            minDiscs = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
            maxPt = cms.double(99999.0),
            minPt = cms.double(20.0),
            maxEtas = cms.vdouble(2.5, 2.75, 3.0, 5.0)
        )),
    puIDName = cms.string('full53x')
)


process.cmgPFJetForRecoilPresel = cms.EDFilter("CmgPFJetSelector",
    src = cms.InputTag("cmgPFJetSel"),
    cut = cms.string('pt()>30 && abs(eta)<4.7 && getSelection("cuts_looseJetId")')
)


process.cmgPFJetPUIDSel = cms.EDFilter("CMGJetPUIDSelector",
    src = cms.InputTag("cmgPFJetSel"),
    cut = cms.string(''),
    puJetIDParams = cms.VPSet(cms.PSet(
        minDiscs = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        maxPt = cms.double(20.0),
        minPt = cms.double(0.0),
        maxEtas = cms.vdouble(2.5, 2.75, 3.0, 5.0)
    ), 
        cms.PSet(
            minDiscs = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
            maxPt = cms.double(99999.0),
            minPt = cms.double(20.0),
            maxEtas = cms.vdouble(2.5, 2.75, 3.0, 5.0)
        )),
    puIDName = cms.string('full53x')
)


process.cmgPFJetSel = cms.EDFilter("CmgPFJetSelector",
    src = cms.InputTag("cmgPFJet"),
    cut = cms.string('pt()>0')
)


process.cmgTauEle = cms.EDFilter("TauElePOProducer",
    cfg = cms.PSet(
        leg2Collection = cms.InputTag("cmgElectronSel"),
        leg1Collection = cms.InputTag("cmgTauSel"),
        metCollection = cms.InputTag("cmgPFMET"),
        metsigCollection = cms.InputTag("")
    ),
    cuts = cms.PSet(
        baseline = cms.PSet(
            tauLeg = cms.PSet(
                iso = cms.string('leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
                kinematics = cms.PSet(
                    eta = cms.string('abs(leg1().eta())<2.3'),
                    pt = cms.string('leg1().pt()>15.0')
                ),
                id = cms.PSet(
                    decay = cms.string('leg1().tauID("decayModeFinding")')
                )
            ),
            eleLeg = cms.PSet(
                kinematics = cms.PSet(
                    eta = cms.string('abs(leg2().eta())<2.1'),
                    pt = cms.string('leg2().pt()>20.0')
                ),
                ID = cms.PSet(
                    hitsnum = cms.string('leg2().numberOfHits==0'),
                    mvaID = cms.string('(abs(leg2().sourcePtr().superCluster().eta())<0.8 && leg2().mvaNonTrigV0() > 0.925) || (abs(leg2().sourcePtr().superCluster().eta())>0.8 && abs(leg2().sourcePtr().superCluster().eta())<1.479 && leg2().mvaNonTrigV0() > 0.975) || (abs(leg2().sourcePtr().superCluster().eta())>1.479 && leg2().mvaNonTrigV0() > 0.985)'),
                    convVeto = cms.string('leg2().passConversionVeto()!=0')
                )
            )
        )
    )
)


process.cmgTauEleCor = cms.EDFilter("TauEleUpdatePOProducer",
    cfg = cms.PSet(
        shift1Prong1Pi0 = cms.double(0.0),
        diObjectCollection = cms.InputTag("mvaMETTauEle"),
        leg1Collection = cms.InputTag(""),
        metCollection = cms.InputTag("recoilCorrectedMET"),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.0),
        nSigma = cms.double(0),
        leg2Collection = cms.InputTag(""),
        ptDependence1Pi0 = cms.double(0.0),
        ptDependence3Prong = cms.double(0.0)
    ),
    cuts = cms.PSet(

    )
)


process.cmgTauEleCorSVFitFullSel = cms.EDFilter("CmgTauEleSelector",
    src = cms.InputTag("cmgTauEleCorSVFitPreSel"),
    cut = cms.string('')
)


process.cmgTauEleCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgTauEleSel"),
    minNumber = cms.uint32(1)
)


process.cmgTauEleMVAPreSel = cms.EDFilter("TauEleUpdatePOProducer",
    cfg = cms.PSet(
        shift1Prong1Pi0 = cms.double(0.0),
        diObjectCollection = cms.InputTag("cmgTauElePreSel"),
        leg1Collection = cms.InputTag(""),
        metCollection = cms.InputTag("recoilCorrectedMET"),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.0),
        nSigma = cms.double(0),
        leg2Collection = cms.InputTag(""),
        ptDependence1Pi0 = cms.double(0.0),
        ptDependence3Prong = cms.double(0.0)
    ),
    cuts = cms.PSet(

    )
)


process.cmgTauElePreSel = cms.EDFilter("CmgTauEleSelector",
    src = cms.InputTag("cmgTauEle"),
    cut = cms.string('getSelection("cuts_baseline")')
)


process.cmgTauEleSel = cms.EDFilter("CmgTauEleSelector",
    src = cms.InputTag("cmgTauEle"),
    cut = cms.string('pt()>0')
)


process.cmgTauEleTauPtSel = cms.EDFilter("CmgTauEleSelector",
    src = cms.InputTag("cmgTauEleCor"),
    cut = cms.string('leg1().pt()>18.')
)


process.cmgTauMu = cms.EDFilter("TauMuPOProducer",
    cfg = cms.PSet(
        leg2Collection = cms.InputTag("cmgMuonSel"),
        leg1Collection = cms.InputTag("cmgTauSel"),
        metCollection = cms.InputTag("cmgPFMET"),
        metsigCollection = cms.InputTag("")
    ),
    cuts = cms.PSet(
        caloMuVeto = cms.string('leg1().eOverP()>0.2'),
        baseline = cms.PSet(
            tauLeg = cms.PSet(
                iso = cms.string('leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
                kinematics = cms.PSet(
                    eta = cms.string('abs(leg1().eta())<2.3'),
                    pt = cms.string('leg1().pt()>15.0')
                ),
                id = cms.PSet(
                    muRejection = cms.string('leg1().tauID("againstMuonTight") > 0.5'),
                    decay = cms.string('leg1().tauID("decayModeFinding")')
                )
            ),
            muLeg = cms.PSet(
                kinematics = cms.PSet(
                    eta = cms.string('abs(leg2().eta())<2.1'),
                    pt = cms.string('leg2().pt()>17.0')
                )
            ),
            mass = cms.string('mass()>10')
        )
    )
)


process.cmgTauMuCor = cms.EDFilter("TauMuUpdatePOProducer",
    cfg = cms.PSet(
        shift1Prong1Pi0 = cms.double(0.0),
        diObjectCollection = cms.InputTag("mvaMETTauMu"),
        leg1Collection = cms.InputTag(""),
        metCollection = cms.InputTag("recoilCorrectedMET"),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.0),
        nSigma = cms.double(0),
        leg2Collection = cms.InputTag(""),
        ptDependence1Pi0 = cms.double(0.0),
        ptDependence3Prong = cms.double(0.0)
    ),
    cuts = cms.PSet(

    )
)


process.cmgTauMuCorSVFitFullSel = cms.EDFilter("CmgTauMuSelector",
    src = cms.InputTag("cmgTauMuCorSVFitPreSel"),
    cut = cms.string('')
)


process.cmgTauMuCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgTauMuSel"),
    minNumber = cms.uint32(1)
)


process.cmgTauMuMVAPreSel = cms.EDFilter("TauMuUpdatePOProducer",
    cfg = cms.PSet(
        shift1Prong1Pi0 = cms.double(0.0),
        diObjectCollection = cms.InputTag("cmgTauMuPreSel"),
        leg1Collection = cms.InputTag(""),
        metCollection = cms.InputTag("recoilCorrectedMET"),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.0),
        nSigma = cms.double(0),
        leg2Collection = cms.InputTag(""),
        ptDependence1Pi0 = cms.double(0.0),
        ptDependence3Prong = cms.double(0.0)
    ),
    cuts = cms.PSet(

    )
)


process.cmgTauMuPreSel = cms.EDFilter("CmgTauMuSelector",
    src = cms.InputTag("cmgTauMu"),
    cut = cms.string('getSelection("cuts_baseline")')
)


process.cmgTauMuSel = cms.EDFilter("CmgTauMuSelector",
    src = cms.InputTag("cmgTauMu"),
    cut = cms.string('pt()>0')
)


process.cmgTauMuTauPtSel = cms.EDFilter("CmgTauMuSelector",
    src = cms.InputTag("cmgTauMuCor"),
    cut = cms.string('leg1().pt()>18.')
)


process.diTauFullSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgDiTauCorSVFitFullSel"),
    minNumber = cms.uint32(1)
)


process.diTauPreSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgDiTauCorSVFitPreSel"),
    minNumber = cms.uint32(1)
)


process.goodPVFilter = cms.EDFilter("VertexSelector",
    filter = cms.bool(True),
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string('!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2')
)


process.muEleFullSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgMuEleCorSVFitFullSel"),
    minNumber = cms.uint32(1)
)


process.muElePreSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgMuEleCorSVFitPreSel"),
    minNumber = cms.uint32(1)
)


process.tauEleFullSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgTauEleCorSVFitFullSel"),
    minNumber = cms.uint32(1)
)


process.tauElePreSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgTauEleCorSVFitPreSel"),
    minNumber = cms.uint32(1)
)


process.tauMuFullSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgTauMuCorSVFitFullSel"),
    minNumber = cms.uint32(1)
)


process.tauMuPreSelCount = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("cmgTauMuCorSVFitPreSel"),
    minNumber = cms.uint32(1)
)


process.diTau_fullsel_tree_CMG = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *', 
        'drop *', 
        'keep *_source_*_*', 
        'keep *_generator_*_*', 
        'keep *_TriggerResults__*', 
        'keep *_addPileupInfo__HLT', 
        'keep *_genJetSel__PAT', 
        'keep *_tauGenJetsSelectorAllHadrons__PAT', 
        'keep *_genParticlesPruned__PAT', 
        'keep *_vertexWeight*__*', 
        'keep *_ak5CaloJets_rho_RECO', 
        'keep *_ak5PFJets_rho_RECO', 
        'keep *_ak5TrackJets_rho_RECO', 
        'keep *_ak7BasicJets_rho_RECO', 
        'keep *_ak7CaloJets_rho_RECO', 
        'keep *_ak7PFJets_rho_RECO', 
        'keep *_kt4CaloJets_rho_RECO', 
        'keep *_kt4PFJets_rho_RECO', 
        'keep *_kt6CaloJets_rho_RECO', 
        'keep *_kt6CaloJetsCentral_rho_RECO', 
        'keep *_kt6PFJets_rho_RECO', 
        'keep *_kt6PFJetsCentralChargedPileUp_rho_RECO', 
        'keep *_kt6PFJetsCentralNeutral_rho_RECO', 
        'keep *_kt6PFJetsCentralNeutralTight_rho_RECO', 
        'keep *_TriggerResults__RECO', 
        'keep *_offlinePrimaryVertices__RECO', 
        'keep *_pfMetSignificance__PAT', 
        'keep *_ak5PFJetsCHS_rho_PAT', 
        'keep *_ak5PFJetsCHSpruned_rho_PAT', 
        'keep *_kt6PFJetsCHSForIso_rho_PAT', 
        'keep *_kt6PFJetsForIso_rho_PAT', 
        'keep *_kt6PFJetsForRhoComputationVoronoi_rho_PAT', 
        'keep *_TriggerResults__PAT', 
        'keep *_nJetsPtGt1__PAT', 
        'keep *_cmgPFBaseJetLead__PAT', 
        'keep *_cmgPFBaseJetLeadCHS__PAT', 
        'keep *_cmgPFMET__PAT', 
        'keep *_cmgPFMETRaw__PAT', 
        'keep *_cmgDiElectronSel__PAT', 
        'keep *_cmgDiMuonSel__PAT', 
        'keep *_cmgElectronSel__PAT', 
        'keep *_cmgMuonSel__PAT', 
        'keep *_cmgPFJetLooseJetIdFailed__PAT', 
        'keep *_cmgPFJetMediumJetIdFailed__PAT', 
        'keep *_cmgPFJetSel__PAT', 
        'keep *_cmgPFJetSelCHS__PAT', 
        'keep *_cmgPFJetTightJetIdFailed__PAT', 
        'keep *_cmgPFJetVeryLooseJetId95Failed__PAT', 
        'keep *_cmgPFJetVeryLooseJetId95gammaFailed__PAT', 
        'keep *_cmgPFJetVeryLooseJetId95h0Failed__PAT', 
        'keep *_cmgPFJetVeryLooseJetId99Failed__PAT', 
        'keep *_cmgPhotonSel__PAT', 
        'keep *_cmgStructuredPFJetSel__PAT', 
        'keep *_cmgTriggerObjectListSel__PAT', 
        'keep *_cmgTriggerObjectSel__PAT', 
        'keep *_patElectronsWithTrigger__PAT', 
        'keep *_patMuonsWithTrigger__PAT', 
        'keep *_nopuMet__PAT', 
        'keep *_pcMet__PAT', 
        'keep *_pfMetForRegression__PAT', 
        'keep *_puMet__PAT', 
        'keep *_tkMet__PAT', 
        'keep *_TriggerResults__H2TAUTAU', 
        'keep *_cmgDiTauCorSVFitFullSel__H2TAUTAU', 
        'keep *_mvaMETdiTau__H2TAUTAU', 
        'keep *_goodPVFilter__H2TAUTAU', 
        'keep *_genParticles_*_*', 
        'keep *_embeddingKineReweightRECembedding_*_*', 
        'keep *_TauSpinnerReco_*_*', 
        'keep *_ZmumuEvtSelEffCorrWeightProducer_*_*', 
        'keep *_muonRadiationCorrWeightProducer_*_*', 
        'keep *_generator_*_*', 
        'keep *_genTausFromZsForEmbeddingKineReweight_*_*'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('diTauPath')
    ),
    fileName = cms.untracked.string('diTau_fullsel_tree_CMG.root')
)


process.vertexWeightSequence = cms.Sequence(process.vertexWeightEPSJul8+process.vertexWeightLeptonPhoton+process.vertexWeightMay10ReReco+process.vertexWeightPromptRecov4+process.vertexWeight05AugReReco+process.vertexWeightPromptRecov6+process.vertexWeight2invfb+process.vertexWeight2011B+process.vertexWeight2011AB+process.vertexWeightFall11EPSJul8+process.vertexWeightFall11LeptonPhoton+process.vertexWeightFall11May10ReReco+process.vertexWeightFall11PromptRecov4+process.vertexWeightFall1105AugReReco+process.vertexWeightFall11PromptRecov6+process.vertexWeightFall112invfb+process.vertexWeightFall112011B+process.vertexWeightFall112011AB+process.vertexWeight3DMay10ReReco+process.vertexWeight3DPromptRecov4+process.vertexWeight3D05AugReReco+process.vertexWeight3DPromptRecov6+process.vertexWeight3D2invfb+process.vertexWeight3D2011B+process.vertexWeight3D2011AB+process.vertexWeight3DFall11May10ReReco+process.vertexWeight3DFall11PromptRecov4+process.vertexWeight3DFall1105AugReReco+process.vertexWeight3DFall11PromptRecov6+process.vertexWeight3DFall112invfb+process.vertexWeight3DFall112011B+process.vertexWeight3DFall112011AB+process.vertexWeightSummer12MCICHEPData+process.vertexWeightSummer12MC53XICHEPData+process.vertexWeightSummer12MC53XHCPData+process.vertexWeightSummer12MC53X2012D6fbData+process.vertexWeightSummer12MC53X2012ABCDData+process.vertexWeightSummer12MC53X2012BCDData)


process.diTauPreSelSkimSequence = cms.Sequence(process.diTauPreSelCount)


process.muEleFullSelSkimSequence = cms.Sequence(process.muEleFullSelCount)


process.embeddingKineReweightSequenceGENembedding = cms.Sequence(process.genTausFromZsForEmbeddingKineReweight+process.genZdecayToTausForEmbeddingKineReweight+process.embeddingKineReweightGENembedding)


process.tauMuMvaMETrecoilSequence = cms.Sequence(process.goodPVFilter+process.mvaMETTauMu+process.cmgTauMuCor+process.cmgTauMuTauPtSel+process.recoilCorMETTauMu)


process.tauEleMvaMETRecoilSequence = cms.Sequence(process.goodPVFilter+process.mvaMETTauEle+process.cmgTauEleCor+process.cmgTauEleTauPtSel+process.recoilCorMETTauEle)


process.tauMuCorSVFitSequence = cms.Sequence(process.tauMuMvaMETrecoilSequence+process.cmgTauMuCorSVFitPreSel+process.cmgTauMuCorSVFitFullSel)


process.tauEleFullSelSkimSequence = cms.Sequence(process.tauEleFullSelCount)


process.tauMuStdSequence = cms.Sequence(process.cmgTauMu+process.cmgTauMuPreSel)


process.tauEleStdSequence = cms.Sequence(process.cmgTauEle+process.cmgTauElePreSel)


process.embeddingKineReweightSequenceRECembedding = cms.Sequence(process.genTausFromZsForEmbeddingKineReweight+process.genZdecayToTausForEmbeddingKineReweight+process.embeddingKineReweightRECembedding)


process.diTauFullSelSkimSequence = cms.Sequence(process.diTauFullSelCount)


process.metRecoilCorrectionInputSequence = cms.Sequence(process.cmgPFJetForRecoilPresel+process.cmgPFJetForRecoil+process.genWorZ)


process.metRecoilCorrectionSequence = cms.Sequence(process.metRecoilCorrectionInputSequence+process.recoilCorrectedMETTauMu+process.recoilCorrectedMETTauEle+process.recoilCorrectedMETMuEle)


process.tauElePreSelSkimSequence = cms.Sequence(process.tauElePreSelCount)


process.muElePreSelSkimSequence = cms.Sequence(process.muElePreSelCount)


process.tauEleCorSVFitSequence = cms.Sequence(process.tauEleMvaMETRecoilSequence+process.cmgTauEleCorSVFitPreSel+process.cmgTauEleCorSVFitFullSel)


process.tauMuSequence = cms.Sequence(process.tauMuStdSequence+process.tauMuCorSVFitSequence)


process.mvaMETSequence = cms.Sequence(process.goodPVFilter+process.mvaMETDiTau+process.cmgDiTauCor+process.cmgDiTauPtSel+process.recoilCorMETDiTau)


process.diTauStdSequence = cms.Sequence(process.cmgDiTau+process.cmgDiTauPreSel)


process.tauMuPreSelSkimSequence = cms.Sequence(process.tauMuPreSelCount)


process.tauMuFullSelSkimSequence = cms.Sequence(process.tauMuFullSelCount)


process.embeddingKineReweightSequence = cms.Sequence(process.embeddingKineReweightSequenceGENembedding+process.embeddingKineReweightSequenceRECembedding)


process.genSequence = cms.Sequence(process.metRecoilCorrectionInputSequence+process.vertexWeightSequence)


process.tauEleSequence = cms.Sequence(process.tauEleStdSequence+process.tauEleCorSVFitSequence)


process.diTauCorSVFitSequence = cms.Sequence(process.mvaMETSequence+process.cmgDiTauCorSVFitPreSel+process.cmgDiTauCorSVFitFullSel)


process.diTauSequence = cms.Sequence(process.diTauStdSequence+process.diTauCorSVFitSequence)


process.diTauPath = cms.Path(process.diTauSequence+process.embeddingKineReweightSequenceRECembedding+process.diTauFullSelSkimSequence)


process.tauElePath = cms.Path(process.tauEleSequence+process.tauEleFullSelSkimSequence)


process.tauMuPath = cms.Path(process.tauMuSequence+process.tauMuFullSelSkimSequence)


process.outpath = cms.EndPath(process.diTau_fullsel_tree_CMG)


process.MessageLogger = cms.Service("MessageLogger",
    suppressInfo = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    suppressDebug = cms.untracked.vstring(),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr_stats = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        output = cms.untracked.string('cerr'),
        optionalPSet = cms.untracked.bool(True)
    ),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noTimeStamps = cms.untracked.bool(False),
        FwkReport = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(5000),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        threshold = cms.untracked.string('INFO'),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        FwkSummary = cms.untracked.PSet(
            reportEvery = cms.untracked.int32(1),
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    FrameworkJobReport = cms.untracked.PSet(
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring(),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
    infos = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport')
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.diObjectFactory = cms.PSet(
    leg2Collection = cms.InputTag("dummy"),
    leg1Collection = cms.InputTag("dummy"),
    metCollection = cms.InputTag("")
)

process.diTauCuts = cms.PSet(
    baseline = cms.PSet(
        tau1Leg = cms.PSet(
            iso = cms.string('leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
            kinematics = cms.PSet(
                eta = cms.string('abs(leg1().eta())<2.3'),
                pt = cms.string('leg1().pt()>15.0')
            ),
            id = cms.PSet(
                decay = cms.string('leg1().tauID("decayModeFinding")')
            )
        ),
        mass = cms.string('mass()>10'),
        tau2Leg = cms.PSet(
            iso = cms.string('leg2().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
            kinematics = cms.PSet(
                eta = cms.string('abs(leg2().eta())<2.3'),
                pt = cms.string('leg2().pt()>15.0')
            ),
            id = cms.PSet(
                decay = cms.string('leg2().tauID("decayModeFinding")')
            )
        )
    )
)

process.ditauFactory = cms.PSet(
    leg2Collection = cms.InputTag("cmgTauSel"),
    leg1Collection = cms.InputTag("cmgTauSel"),
    metsigCollection = cms.InputTag(""),
    metCollection = cms.InputTag("cmgPFMET")
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.muEleFactory = cms.PSet(
    leg2Collection = cms.InputTag("cmgElectronSel"),
    leg1Collection = cms.InputTag("cmgMuonSel"),
    metCollection = cms.InputTag("")
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

process.puJetIdAlgo = cms.PSet(
    tmvaVariables = cms.vstring('nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    tmvaMethod = cms.string('JetIDMVAMET'),
    cutBased = cms.bool(False),
    tmvaWeights = cms.string('CMGTools/External/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml'),
    tmvaSpectators = cms.vstring(),
    label = cms.string('met53x'),
    version = cms.int32(-1),
    JetIdParams = cms.PSet(
        Pt2030_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
        Pt2030_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt010_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_MET = cms.vdouble(-0.2, -0.2, 0.0, 0.2),
        Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
        Pt1020_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt010_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_MET = cms.vdouble(-0.2, -0.2, -0.2, 0.1),
        Pt010_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Tight = cms.vdouble(-2, -2, -2, -2, -2)
    ),
    impactParTkThreshold = cms.double(1.0)
)

process.tauEFactory = cms.PSet(
    leg2Collection = cms.InputTag("cmgElectronSel"),
    leg1Collection = cms.InputTag("cmgTauSel"),
    metCollection = cms.InputTag("cmgPFMET")
)

process.tauEleCuts = cms.PSet(
    baseline = cms.PSet(
        tauLeg = cms.PSet(
            iso = cms.string('leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
            kinematics = cms.PSet(
                eta = cms.string('abs(leg1().eta())<2.3'),
                pt = cms.string('leg1().pt()>15.0')
            ),
            id = cms.PSet(
                decay = cms.string('leg1().tauID("decayModeFinding")')
            )
        ),
        eleLeg = cms.PSet(
            kinematics = cms.PSet(
                eta = cms.string('abs(leg2().eta())<2.1'),
                pt = cms.string('leg2().pt()>20.0')
            ),
            ID = cms.PSet(
                hitsnum = cms.string('leg2().numberOfHits==0'),
                mvaID = cms.string('(abs(leg2().sourcePtr().superCluster().eta())<0.8 && leg2().mvaNonTrigV0() > 0.925) || (abs(leg2().sourcePtr().superCluster().eta())>0.8 && abs(leg2().sourcePtr().superCluster().eta())<1.479 && leg2().mvaNonTrigV0() > 0.975) || (abs(leg2().sourcePtr().superCluster().eta())>1.479 && leg2().mvaNonTrigV0() > 0.985)'),
                convVeto = cms.string('leg2().passConversionVeto()!=0')
            )
        )
    )
)

process.tauMuCuts = cms.PSet(
    caloMuVeto = cms.string('leg1().eOverP()>0.2'),
    baseline = cms.PSet(
        tauLeg = cms.PSet(
            iso = cms.string('leg1().tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < 10.0'),
            kinematics = cms.PSet(
                eta = cms.string('abs(leg1().eta())<2.3'),
                pt = cms.string('leg1().pt()>15.0')
            ),
            id = cms.PSet(
                muRejection = cms.string('leg1().tauID("againstMuonTight") > 0.5'),
                decay = cms.string('leg1().tauID("decayModeFinding")')
            )
        ),
        muLeg = cms.PSet(
            kinematics = cms.PSet(
                eta = cms.string('abs(leg2().eta())<2.1'),
                pt = cms.string('leg2().pt()>17.0')
            )
        ),
        mass = cms.string('mass()>10')
    )
)

process.tauMuFactory = cms.PSet(
    leg2Collection = cms.InputTag("cmgMuonSel"),
    leg1Collection = cms.InputTag("cmgTauSel"),
    metCollection = cms.InputTag("cmgPFMET")
)

process.schedule = cms.Schedule(*[ process.diTauPath, process.outpath ])
