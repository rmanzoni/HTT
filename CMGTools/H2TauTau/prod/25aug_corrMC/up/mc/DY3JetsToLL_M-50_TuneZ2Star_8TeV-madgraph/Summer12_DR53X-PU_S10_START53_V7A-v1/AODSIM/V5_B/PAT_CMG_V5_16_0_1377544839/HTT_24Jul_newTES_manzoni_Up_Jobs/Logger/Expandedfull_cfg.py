import FWCore.ParameterSet.Config as cms

process = cms.Process("H2TAUTAU")

process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring( ('/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_10.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_100.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1000.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1001.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1002.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1003.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1004.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1005.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1006.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1007.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1008.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1009.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_101.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1010.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1011.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1012.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1013.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1014.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1015.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1016.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1017.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1018.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1019.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_102.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1020.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1021.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1022.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1023.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1024.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1025.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1026.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1027.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1028.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1029.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_103.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1030.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1031.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1032.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1033.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1034.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1035.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1036.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1037.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1038.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1039.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_104.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1040.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1041.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1042.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_1043.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_105.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_106.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_107.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_108.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_109.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_11.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_110.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_111.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_112.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_113.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_114.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_115.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_116.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_117.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_118.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_119.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_12.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_120.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_121.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_122.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_123.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_124.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_125.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_126.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_127.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_128.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_129.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_13.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_130.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_131.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_132.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_133.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_134.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_135.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_136.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_137.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_138.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_139.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_14.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_140.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_141.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_142.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_143.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_144.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_145.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_146.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_147.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_148.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_149.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_15.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_150.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_151.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_152.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_153.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_154.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_155.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_156.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_157.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_158.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_159.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_16.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_160.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_161.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_162.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_163.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_164.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_165.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_166.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_167.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_168.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_169.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_17.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_170.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_171.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_172.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_173.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_174.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_175.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_176.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_177.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_178.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_179.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_18.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_180.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_181.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_182.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_183.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_184.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_185.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_186.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_187.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_188.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_189.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_19.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_190.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_191.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_192.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_193.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_194.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_195.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_196.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_197.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_198.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_199.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_2.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_20.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_200.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_201.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_202.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_203.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_204.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_205.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_206.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_207.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_208.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_209.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_21.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_210.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_211.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_212.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_213.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_214.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_215.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_216.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_217.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_218.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_219.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_22.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_220.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_221.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_222.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_223.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_224.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_225.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_226.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_227.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_228.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_229.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_23.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_230.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_231.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_232.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_233.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_234.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_235.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_236.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_237.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_238.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_239.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_24.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_240.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_241.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_242.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_243.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_244.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_245.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_246.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_247.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_248.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_249.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_25.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_250.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_251.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_252.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_253.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_254.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_255.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_256.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_257.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_258.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_259.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_26.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_260.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_261.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_262.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_263.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_264.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_265.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_266.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_267.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_268.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_269.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_27.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_270.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_271.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_272.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_273.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_274.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_275.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_276.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_277.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_278.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_279.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_28.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_280.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_281.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_282.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_283.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_284.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_285.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_286.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_287.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_288.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_289.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_29.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_290.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_291.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_292.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_293.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_294.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_295.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_296.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_297.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_298.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_299.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_3.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_30.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_300.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_301.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_302.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_303.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_304.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_305.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_306.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_307.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_308.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_309.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_31.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_310.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_311.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_312.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_313.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_314.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_315.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_316.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_317.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_318.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_319.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_32.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_320.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_321.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_322.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_323.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_324.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_325.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_326.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_327.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_328.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_329.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_33.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_330.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_331.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_332.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_333.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_334.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_335.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_336.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_337.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_338.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_339.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_34.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_340.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_341.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_342.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_343.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_344.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_345.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_346.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_347.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_348.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_349.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_35.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_350.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_351.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_352.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_353.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_354.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_355.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_356.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_357.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_358.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_359.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_36.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_360.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_361.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_362.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_363.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_364.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_365.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_366.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_367.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_368.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_369.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_37.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_370.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_371.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_372.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_373.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_374.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_375.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_376.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_377.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_378.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_379.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_38.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_380.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_381.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_382.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_383.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_384.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_385.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_386.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_387.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_388.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_389.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_39.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_390.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_391.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_392.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_393.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_394.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_395.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_396.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_397.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_398.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_399.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_4.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_40.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_400.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_401.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_402.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_403.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_404.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_405.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_406.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_407.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_408.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_409.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_41.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_410.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_411.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_412.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_413.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_414.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_415.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_416.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_417.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_418.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_419.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_42.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_420.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_421.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_422.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_423.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_424.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_425.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_426.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_427.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_428.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_429.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_43.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_430.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_431.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_432.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_433.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_434.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_435.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_436.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_437.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_438.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_439.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_44.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_440.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_441.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_442.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_443.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_444.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_445.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_446.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_447.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_448.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_449.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_45.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_450.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_451.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_452.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_453.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_454.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_455.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_456.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_457.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_458.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_459.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_46.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_460.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_461.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_462.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_463.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_464.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_465.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_466.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_467.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_468.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_469.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_47.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_470.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_471.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_472.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_473.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_474.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_475.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_476.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_477.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_478.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_479.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_48.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_480.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_481.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_482.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_483.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_484.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_485.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_486.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_487.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_488.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_489.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_49.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_490.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_491.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_492.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_493.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_494.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_495.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_496.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_497.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_498.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_499.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_5.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_50.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_500.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_501.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_502.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_503.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_504.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_505.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_506.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_507.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_508.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_509.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_51.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_510.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_511.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_512.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_513.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_514.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_515.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_516.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_517.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_518.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_519.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_52.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_520.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_521.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_522.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_523.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_524.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_525.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_526.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_527.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_528.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_529.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_53.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_530.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_531.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_532.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_533.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_534.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_535.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_536.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_537.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_538.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_539.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_54.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_540.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_541.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_542.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_543.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_544.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_545.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_546.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_547.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_548.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_549.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_55.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_550.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_551.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_552.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_553.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_554.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_555.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_556.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_557.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_558.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_559.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_56.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_560.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_561.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_562.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_563.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_564.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_565.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_566.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_567.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_568.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_569.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_57.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_570.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_571.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_572.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_573.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_574.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_575.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_576.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_577.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_578.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_579.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_58.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_580.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_581.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_582.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_583.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_584.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_585.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_586.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_587.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_588.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_589.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_59.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_590.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_591.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_592.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_593.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_594.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_595.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_596.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_597.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_598.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_599.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_6.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_60.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_600.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_601.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_602.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_603.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_604.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_605.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_606.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_607.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_608.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_609.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_61.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_610.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_611.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_612.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_613.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_614.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_615.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_616.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_617.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_618.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_619.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_62.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_620.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_621.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_622.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_623.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_624.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_625.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_626.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_627.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_628.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_629.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_63.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_630.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_631.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_632.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_633.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_634.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_635.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_636.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_637.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_638.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_639.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_64.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_640.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_641.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_642.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_643.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_644.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_645.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_646.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_647.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_648.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_649.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_65.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_650.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_651.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_652.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_653.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_654.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_655.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_656.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_657.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_658.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_659.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_66.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_660.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_661.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_662.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_663.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_664.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_665.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_666.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_667.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_668.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_669.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_67.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_670.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_671.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_672.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_673.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_674.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_675.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_676.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_677.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_678.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_679.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_68.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_680.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_681.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_682.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_683.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_684.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_685.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_686.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_687.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_688.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_689.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_69.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_690.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_691.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_692.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_693.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_694.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_695.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_696.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_697.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_698.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_699.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_7.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_70.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_700.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_701.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_702.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_703.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_704.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_705.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_706.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_707.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_708.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_709.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_71.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_710.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_711.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_712.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_713.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_714.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_715.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_716.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_717.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_718.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_719.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_72.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_720.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_721.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_722.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_723.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_724.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_725.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_726.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_727.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_728.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_729.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_73.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_730.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_731.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_732.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_733.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_734.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_735.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_736.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_737.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_738.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_739.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_74.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_740.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_741.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_742.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_743.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_744.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_745.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_746.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_747.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_748.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_749.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_75.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_750.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_751.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_752.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_753.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_754.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_755.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_756.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_757.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_758.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_759.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_76.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_760.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_761.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_762.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_763.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_764.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_765.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_766.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_767.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_768.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_769.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_77.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_770.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_771.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_772.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_773.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_774.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_775.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_776.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_777.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_778.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_779.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_78.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_780.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_781.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_782.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_783.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_784.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_785.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_786.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_787.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_788.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_789.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_79.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_790.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_791.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_792.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_793.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_794.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_795.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_796.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_797.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_798.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_799.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_8.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_80.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_800.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_801.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_802.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_803.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_804.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_805.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_806.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_807.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_808.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_809.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_81.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_810.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_811.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_812.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_813.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_814.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_815.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_816.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_817.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_818.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_819.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_82.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_820.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_821.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_822.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_823.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_824.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_825.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_826.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_827.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_828.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_829.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_83.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_830.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_831.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_832.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_833.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_834.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_835.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_836.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_837.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_838.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_839.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_84.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_840.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_841.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_842.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_843.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_844.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_845.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_846.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_847.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_848.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_849.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_85.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_850.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_851.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_852.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_853.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_854.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_855.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_856.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_857.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_858.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_859.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_86.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_860.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_861.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_862.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_863.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_864.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_865.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_866.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_867.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_868.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_869.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_87.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_870.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_871.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_872.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_873.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_874.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_875.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_876.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_877.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_878.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_879.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_88.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_880.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_881.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_882.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_883.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_884.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_885.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_886.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_887.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_888.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_889.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_89.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_890.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_891.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_892.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_893.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_894.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_895.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_896.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_897.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_898.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_899.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_9.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_90.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_900.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_901.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_902.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_903.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_904.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_905.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_906.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_907.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_908.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_909.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_91.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_910.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_911.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_912.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_913.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_914.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_915.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_916.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_917.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_918.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_919.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_92.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_920.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_921.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_922.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_923.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_924.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_925.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_926.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_927.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_928.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_929.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_93.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_930.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_931.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_932.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_933.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_934.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_935.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_936.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_937.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_938.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_939.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_94.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_940.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_941.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_942.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_943.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_944.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_945.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_946.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_947.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_948.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_949.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_95.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_950.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_951.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_952.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_953.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_954.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_955.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_956.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_957.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_958.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_959.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_96.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_960.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_961.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_962.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_963.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_964.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_965.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_966.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_967.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_968.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_969.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_97.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_970.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_971.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_972.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_973.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_974.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_975.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_976.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_977.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_978.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_979.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_98.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_980.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_981.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_982.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_983.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_984.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_985.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_986.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_987.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_988.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_989.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_99.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_990.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_991.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_992.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_993.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_994.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_995.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_996.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_997.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_998.root', 
        '/store/cmst3/user/cmgtools/CMG/DY3JetsToLL_M-50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/V5_B/PAT_CMG_V5_16_0/cmgTuple_999.root' ) ),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT')
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
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_ztt53X_20pv_njet.root'),
    leptonLeg = cms.int32(0),
    correctionType = cms.int32(1),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgDiTauPtSel")
)


process.recoilCorMETTauEle = cms.EDProducer("RecoilCorrectedMETProducerTauEle",
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_ztt53X_20pv_njet.root'),
    leptonLeg = cms.int32(0),
    correctionType = cms.int32(1),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauEleTauPtSel")
)


process.recoilCorMETTauMu = cms.EDProducer("RecoilCorrectedMETProducerTauMu",
    enable = cms.bool(True),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_ztt53X_20pv_njet.root'),
    leptonLeg = cms.int32(0),
    correctionType = cms.int32(1),
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
        shift1Prong1Pi0 = cms.double(0.012),
        diObjectCollection = cms.InputTag("mvaMETTauMu"),
        leg1Collection = cms.InputTag(""),
        shiftMet = cms.bool(True),
        shiftTaus = cms.bool(True),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.012),
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
        shift1Prong1Pi0 = cms.double(0.012),
        diObjectCollection = cms.InputTag("cmgTauMuPreSel"),
        leg1Collection = cms.InputTag(""),
        shiftMet = cms.bool(True),
        shiftTaus = cms.bool(True),
        uncertainty = cms.double(0.03),
        shift1ProngNoPi0 = cms.double(0.0),
        shift3Prong = cms.double(0.012),
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
        'keep *_genParticles_*_*'),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('diTauPath')
    ),
    fileName = cms.untracked.string('diTau_fullsel_tree_CMG.root')
)


process.vertexWeightSequence = cms.Sequence(process.vertexWeightEPSJul8+process.vertexWeightLeptonPhoton+process.vertexWeightMay10ReReco+process.vertexWeightPromptRecov4+process.vertexWeight05AugReReco+process.vertexWeightPromptRecov6+process.vertexWeight2invfb+process.vertexWeight2011B+process.vertexWeight2011AB+process.vertexWeightFall11EPSJul8+process.vertexWeightFall11LeptonPhoton+process.vertexWeightFall11May10ReReco+process.vertexWeightFall11PromptRecov4+process.vertexWeightFall1105AugReReco+process.vertexWeightFall11PromptRecov6+process.vertexWeightFall112invfb+process.vertexWeightFall112011B+process.vertexWeightFall112011AB+process.vertexWeight3DMay10ReReco+process.vertexWeight3DPromptRecov4+process.vertexWeight3D05AugReReco+process.vertexWeight3DPromptRecov6+process.vertexWeight3D2invfb+process.vertexWeight3D2011B+process.vertexWeight3D2011AB+process.vertexWeight3DFall11May10ReReco+process.vertexWeight3DFall11PromptRecov4+process.vertexWeight3DFall1105AugReReco+process.vertexWeight3DFall11PromptRecov6+process.vertexWeight3DFall112invfb+process.vertexWeight3DFall112011B+process.vertexWeight3DFall112011AB+process.vertexWeightSummer12MCICHEPData+process.vertexWeightSummer12MC53XICHEPData+process.vertexWeightSummer12MC53XHCPData+process.vertexWeightSummer12MC53X2012D6fbData+process.vertexWeightSummer12MC53X2012ABCDData+process.vertexWeightSummer12MC53X2012BCDData)


process.diTauPreSelSkimSequence = cms.Sequence(process.diTauPreSelCount)


process.muEleFullSelSkimSequence = cms.Sequence(process.muEleFullSelCount)


process.tauEleMvaMETRecoilSequence = cms.Sequence(process.goodPVFilter+process.mvaMETTauEle+process.cmgTauEleCor+process.cmgTauEleTauPtSel+process.recoilCorMETTauEle)


process.tauEleFullSelSkimSequence = cms.Sequence(process.tauEleFullSelCount)


process.tauMuStdSequence = cms.Sequence(process.cmgTauMu+process.cmgTauMuPreSel)


process.tauEleStdSequence = cms.Sequence(process.cmgTauEle+process.cmgTauElePreSel)


process.tauMuMvaMETrecoilSequence = cms.Sequence(process.goodPVFilter+process.mvaMETTauMu+process.cmgTauMuCor+process.cmgTauMuTauPtSel+process.recoilCorMETTauMu)


process.diTauFullSelSkimSequence = cms.Sequence(process.diTauFullSelCount)


process.metRecoilCorrectionInputSequence = cms.Sequence(process.cmgPFJetForRecoilPresel+process.cmgPFJetForRecoil+process.genWorZ)


process.metRecoilCorrectionSequence = cms.Sequence(process.metRecoilCorrectionInputSequence+process.recoilCorrectedMETTauMu+process.recoilCorrectedMETTauEle+process.recoilCorrectedMETMuEle)


process.tauElePreSelSkimSequence = cms.Sequence(process.tauElePreSelCount)


process.muElePreSelSkimSequence = cms.Sequence(process.muElePreSelCount)


process.tauEleCorSVFitSequence = cms.Sequence(process.tauEleMvaMETRecoilSequence+process.cmgTauEleCorSVFitPreSel+process.cmgTauEleCorSVFitFullSel)


process.mvaMETSequence = cms.Sequence(process.goodPVFilter+process.mvaMETDiTau+process.cmgDiTauCor+process.cmgDiTauPtSel+process.recoilCorMETDiTau)


process.diTauStdSequence = cms.Sequence(process.cmgDiTau+process.cmgDiTauPreSel)


process.tauMuPreSelSkimSequence = cms.Sequence(process.tauMuPreSelCount)


process.tauMuFullSelSkimSequence = cms.Sequence(process.tauMuFullSelCount)


process.genSequence = cms.Sequence(process.metRecoilCorrectionInputSequence+process.vertexWeightSequence)


process.tauEleSequence = cms.Sequence(process.tauEleStdSequence+process.tauEleCorSVFitSequence)


process.tauMuCorSVFitSequence = cms.Sequence(process.tauMuMvaMETrecoilSequence+process.cmgTauMuCorSVFitPreSel+process.cmgTauMuCorSVFitFullSel)


process.diTauCorSVFitSequence = cms.Sequence(process.mvaMETSequence+process.cmgDiTauCorSVFitPreSel+process.cmgDiTauCorSVFitFullSel)


process.tauMuSequence = cms.Sequence(process.tauMuStdSequence+process.tauMuCorSVFitSequence)


process.diTauSequence = cms.Sequence(process.diTauStdSequence+process.diTauCorSVFitSequence)


process.diTauPath = cms.Path(process.genSequence+process.diTauSequence+process.diTauFullSelSkimSequence)


process.tauElePath = cms.Path(process.genSequence+process.tauEleSequence+process.tauEleFullSelSkimSequence)


process.tauMuPath = cms.Path(process.genSequence+process.tauMuSequence+process.tauMuFullSelSkimSequence)


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
