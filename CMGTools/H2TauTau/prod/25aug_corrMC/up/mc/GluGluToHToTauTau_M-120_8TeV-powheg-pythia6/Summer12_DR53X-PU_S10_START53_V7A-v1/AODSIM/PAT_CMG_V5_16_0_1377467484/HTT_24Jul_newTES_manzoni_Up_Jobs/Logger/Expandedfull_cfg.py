import FWCore.ParameterSet.Config as cms

process = cms.Process("H2TAUTAU")

process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring( ('/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_100_1_Zhq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_101_1_tgN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_102_1_PXM.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_103_1_3X9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_104_1_74x.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_105_1_ynh.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_106_1_yxX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_107_1_AHn.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_108_1_K8A.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_109_1_ctV.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_10_1_hiu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_110_1_0kW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_111_1_7Kg.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_112_1_1iT.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_113_1_K4M.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_114_1_Pch.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_115_1_QFs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_116_1_MZg.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_117_1_ABq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_118_1_eQe.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_119_1_80b.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_11_1_QvO.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_120_1_uTu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_121_1_r3R.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_122_1_1wo.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_123_1_VhY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_124_1_Xx9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_125_1_ASD.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_126_1_fpD.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_127_1_DKY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_128_1_C6m.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_129_1_Chi.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_12_1_Y7T.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_130_1_ayG.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_131_1_XG6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_132_1_7YE.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_133_1_njz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_134_1_wGV.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_135_1_IN9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_136_1_jOK.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_137_1_dhy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_138_1_gxs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_139_1_mme.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_13_1_qZX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_140_1_Zw3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_141_1_WkZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_142_1_BGe.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_143_1_jOt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_144_1_gps.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_145_1_cFf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_146_1_Pty.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_147_1_hXz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_148_1_K1C.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_149_1_df0.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_14_1_laT.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_150_1_hlw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_151_1_BV0.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_152_1_jmI.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_153_1_K4J.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_154_1_Xte.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_155_1_Rlm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_156_1_xNv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_157_1_dXX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_158_1_mw7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_159_1_HCp.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_15_1_DWX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_160_1_Bw1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_161_1_cRL.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_162_1_sqj.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_163_1_TtS.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_164_1_kvZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_165_1_IJt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_166_1_Qpt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_167_1_b8g.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_168_1_jyM.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_169_1_3Kv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_16_1_s0w.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_170_1_HeQ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_171_1_JP9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_172_1_wpk.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_173_1_yPy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_174_1_m8K.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_175_1_0JN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_176_1_duZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_177_1_3D7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_178_1_SId.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_179_1_vIX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_17_1_sg3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_180_1_YWZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_181_1_UXU.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_182_1_s66.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_183_1_2IM.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_184_1_3JG.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_185_1_A34.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_186_1_ZHG.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_187_1_1HQ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_188_1_OSC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_189_1_05q.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_18_1_0Dk.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_190_1_qJF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_191_1_797.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_192_1_U9X.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_193_1_mJy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_194_1_ekX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_195_1_rK8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_196_1_U1V.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_197_1_wwt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_198_1_mu4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_199_1_7Cf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_19_1_PVo.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_1_1_ISl.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_200_1_D6z.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_201_1_k5r.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_202_1_V9z.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_203_1_yQ3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_204_1_ry8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_205_1_5iH.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_206_1_vwc.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_207_1_uwz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_208_1_cj8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_209_1_am9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_20_1_Lfy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_210_1_eRG.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_211_1_7WP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_212_1_lzA.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_213_1_1yC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_214_1_Go5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_215_1_CKD.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_216_1_HWy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_217_1_BuN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_218_1_FQh.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_219_1_fS8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_21_1_sx2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_220_1_OVq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_221_1_HL4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_222_1_bQf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_223_1_5wZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_224_1_lTu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_225_1_Gwy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_226_1_0uw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_227_1_TGm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_228_1_FRz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_229_1_2c4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_22_1_cm3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_230_1_MbF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_231_1_U7t.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_232_1_ibg.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_233_1_okl.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_234_1_Keo.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_235_1_sEH.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_236_1_Nkf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_237_1_6Rj.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_238_1_E82.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_239_1_BXs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_23_1_xNA.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_240_1_g5N.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_241_1_41E.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_242_1_YEr.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_243_1_aiC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_244_1_TQY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_245_1_94v.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_246_1_DRh.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_247_1_RwX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_248_1_lTl.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_249_1_e72.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_24_1_Phj.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_250_1_Vyl.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_251_1_5JN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_252_1_Zn8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_253_1_yLV.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_254_1_D7e.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_255_1_JLb.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_256_1_eAr.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_257_1_cVi.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_258_1_M5f.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_259_1_4Q6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_25_1_Rhl.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_260_1_GDm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_261_1_Va1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_262_1_X7p.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_263_1_c77.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_264_1_vdw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_265_1_Ri1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_266_1_6mi.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_267_1_hcR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_268_1_L5D.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_269_1_M3m.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_26_1_P8G.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_270_1_vsS.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_271_1_eKs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_272_1_oSP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_273_1_8pl.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_274_1_Ovy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_275_1_khy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_276_1_uPT.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_277_1_Uwv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_278_1_ffs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_279_1_KeS.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_27_1_MdY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_280_1_mYB.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_281_1_BB8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_282_1_G4B.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_283_1_4lZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_284_1_DGo.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_285_1_0su.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_286_1_NWf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_287_1_Enj.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_288_1_4pR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_289_1_vnF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_28_1_Q5R.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_290_1_rk6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_291_1_gr2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_292_1_6kw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_293_1_92l.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_294_1_MEb.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_295_1_tdJ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_296_1_0Nx.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_297_1_KdF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_298_1_3s3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_299_1_ArW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_29_1_3vP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_2_1_aRW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_300_1_oT1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_301_1_K4w.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_302_1_xkH.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_303_1_31c.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_304_1_jg3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_305_1_BaN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_306_1_eLz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_307_1_4fz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_308_1_A2Z.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_309_1_dzG.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_30_1_UHJ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_310_1_6pC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_311_1_pRn.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_312_1_vJF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_313_1_QOx.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_314_1_vvh.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_315_1_OST.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_316_1_ZLQ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_317_1_7sh.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_318_1_Utk.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_319_1_e6E.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_31_1_qB8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_320_1_YOP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_322_1_RG2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_323_1_9Js.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_324_1_I21.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_325_1_Rzk.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_326_1_S8z.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_327_1_nOb.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_328_1_Vim.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_329_1_7xD.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_32_1_pK1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_330_1_y9C.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_331_1_RZ2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_332_1_uwR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_333_1_LHU.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_334_1_Jz9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_335_1_AAa.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_336_1_0rr.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_337_1_Ty7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_338_1_ZMq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_339_1_MZt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_33_1_GC4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_340_1_IRf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_341_1_lLC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_342_1_u0U.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_343_1_lJ5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_344_1_O3x.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_345_1_pHv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_346_1_YVZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_347_1_QjL.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_348_1_Lrv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_349_1_Ucd.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_34_1_HzS.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_350_1_nkV.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_351_1_Z7h.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_352_1_3Lx.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_353_1_f6t.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_354_1_Tmn.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_355_1_36U.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_356_1_viQ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_357_1_ld4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_358_1_Nuf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_359_1_GY1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_35_1_bLg.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_360_1_2sG.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_361_1_FWk.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_362_1_8fr.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_363_1_Q2N.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_364_1_zdE.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_365_1_Oni.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_366_1_luW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_367_1_5rt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_368_1_ac4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_369_1_2np.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_36_1_21L.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_370_1_3r6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_371_1_t9M.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_372_1_iAj.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_373_1_gl4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_374_1_P1o.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_375_1_WQu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_376_1_Crc.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_377_1_bcz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_378_1_KuB.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_379_1_SwD.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_37_1_13K.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_380_1_5hV.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_381_1_s6j.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_382_1_LYw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_383_1_sl2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_384_1_X56.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_385_1_HTQ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_386_1_PrW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_387_1_nS6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_388_1_ZOU.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_389_1_NY5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_38_1_otx.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_390_1_DW8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_391_1_7Fc.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_392_1_Gpw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_393_1_sHd.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_394_1_AoZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_395_1_zJv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_396_1_yX9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_397_1_82q.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_398_1_LeE.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_399_1_uHm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_39_1_wvz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_3_1_XPs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_400_1_sbq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_401_1_sD1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_402_1_JKd.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_403_1_6Ap.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_404_1_FBw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_405_1_2AP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_406_1_2p9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_407_1_L5c.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_408_1_XiS.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_409_1_HCY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_40_1_HCE.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_410_1_UC6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_411_1_iMo.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_412_1_VHF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_413_1_Lko.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_414_1_YMp.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_415_1_f1Q.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_416_1_RT5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_417_1_Yz1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_418_1_oEe.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_419_1_3We.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_41_1_AKp.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_420_1_SAP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_421_1_Crw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_422_1_K21.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_423_1_RK2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_424_1_F6O.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_425_1_DFB.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_426_1_l87.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_427_1_959.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_428_1_JVT.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_429_1_KgL.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_42_1_MDv.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_430_1_KC5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_431_1_zYI.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_432_1_rDO.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_433_1_UN9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_434_1_YVd.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_435_1_Iuk.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_436_1_566.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_437_1_7Uc.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_438_1_BVS.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_439_1_5PN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_43_1_A08.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_440_1_0x5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_441_1_V0c.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_442_1_WZN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_443_1_S5U.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_444_1_XmB.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_445_1_6qO.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_446_1_Zi8.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_447_1_99L.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_448_1_jNF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_449_1_ADU.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_44_1_NYP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_450_1_X5X.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_451_1_D4V.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_452_1_kAI.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_453_1_nxa.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_454_1_jbH.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_455_1_I6T.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_456_1_87h.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_457_1_Csg.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_458_1_NA9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_459_1_MQK.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_45_1_SQA.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_460_1_2KX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_461_1_Dxm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_462_1_rWd.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_463_1_9ps.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_464_1_Qtu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_465_1_PWu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_466_1_R4e.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_467_1_7E4.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_468_1_bwR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_469_1_nch.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_46_1_42I.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_470_1_hz6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_471_1_6nz.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_472_1_UVy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_473_1_Stw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_474_1_SL1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_475_1_nPB.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_476_1_AaR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_477_1_d81.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_478_1_0Sf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_479_1_uHJ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_47_1_6VC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_480_1_cWq.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_481_1_DbC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_482_1_LGP.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_483_1_vPW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_484_1_hwM.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_485_1_IlN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_486_1_mcW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_487_1_ViZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_488_1_KMm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_489_1_Ov0.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_48_1_uWn.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_490_1_qM6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_491_1_9Aj.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_492_1_POp.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_493_1_TaN.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_494_1_UGb.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_495_1_q74.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_496_1_eU3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_497_1_Ozm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_498_1_sQO.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_499_1_nz7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_49_1_jj6.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_4_1_ZIs.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_500_1_HNC.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_50_1_AI2.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_51_1_Dq9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_52_1_tV7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_53_1_AMu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_54_1_hEO.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_55_1_PU7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_56_1_7PF.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_57_1_9NM.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_58_1_RC7.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_59_1_akO.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_5_1_hwL.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_60_1_W0i.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_61_1_dy5.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_62_1_APX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_63_1_jWt.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_64_1_79P.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_65_1_mPi.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_66_1_bW1.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_67_1_F5U.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_68_1_n1p.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_69_1_1rm.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_6_1_KOf.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_70_1_gkY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_71_1_WyR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_72_1_TPK.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_73_1_uF3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_74_1_hbo.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_75_1_kry.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_76_1_LFZ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_77_1_ABY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_78_1_hHu.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_79_1_4Ky.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_7_1_cD3.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_80_1_ZIM.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_81_1_8TY.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_82_1_Wat.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_83_1_G89.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_84_1_CJX.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_85_1_yuI.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_86_1_64g.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_87_1_Ub9.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_88_1_gGw.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_89_1_bhR.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_8_1_LjL.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_90_1_R4u.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_91_1_eJQ.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_92_1_19k.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_93_1_5mD.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_94_1_EkW.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_95_1_meb.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_96_1_dYT.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_97_1_XZy.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_98_1_o5D.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_99_1_vYe.root', 
        '/store/cmst3/group/cmgtools/CMG/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_9_1_5ey.root' ) ),
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
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_htt53X_20pv_njet.root'),
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
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_htt53X_20pv_njet.root'),
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
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_htt53X_20pv_njet.root'),
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
