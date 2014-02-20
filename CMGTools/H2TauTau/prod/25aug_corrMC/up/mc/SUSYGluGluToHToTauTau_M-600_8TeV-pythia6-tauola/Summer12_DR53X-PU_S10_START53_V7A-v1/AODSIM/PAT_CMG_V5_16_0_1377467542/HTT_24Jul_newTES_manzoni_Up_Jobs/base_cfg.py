import FWCore.ParameterSet.Config as cms

process = cms.Process("H2TAUTAU")

process.source = cms.Source("PoolSource",
    noEventSort = cms.untracked.bool(True),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop cmgStructuredPFJets_cmgStructuredPFJetSel__PAT'),
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/cmst3/group/cmgtools/CMG/SUSYGluGluToHToTauTau_M-600_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_99_1_NpL.root', 
        '/store/cmst3/group/cmgtools/CMG/SUSYGluGluToHToTauTau_M-600_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/cmgTuple_9_1_0wd.root')
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
    nJetsPtGt1Src = cms.InputTag("nJetsPtGt1"),
    pumetSrc = cms.InputTag("puMet"),
    weights_gbrmetu1cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru1cov_53_Dec2012.root'),
    weights_gbrmetu2cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru2cov_53_Dec2012.root'),
    vertexSrc = cms.InputTag("goodPVFilter"),
    jetSrc = cms.InputTag("cmgPFJetSel"),
    leadJetSrc = cms.InputTag("cmgPFBaseJetLead"),
    recBosonSrc = cms.InputTag("cmgDiTauPreSel"),
    weights_gbrmetphi = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmetphi_53_Dec2012.root'),
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
    nJetsPtGt1Src = cms.InputTag("nJetsPtGt1"),
    pumetSrc = cms.InputTag("puMet"),
    weights_gbrmetu1cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru1cov_53_Dec2012.root'),
    weights_gbrmetu2cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru2cov_53_Dec2012.root'),
    vertexSrc = cms.InputTag("goodPVFilter"),
    jetSrc = cms.InputTag("cmgPFJetSel"),
    leadJetSrc = cms.InputTag("cmgPFBaseJetLead"),
    recBosonSrc = cms.InputTag("cmgTauElePreSel"),
    weights_gbrmetphi = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmetphi_53_Dec2012.root'),
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
    nJetsPtGt1Src = cms.InputTag("nJetsPtGt1"),
    pumetSrc = cms.InputTag("puMet"),
    weights_gbrmetu1cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru1cov_53_Dec2012.root'),
    weights_gbrmetu2cov = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbru2cov_53_Dec2012.root'),
    vertexSrc = cms.InputTag("goodPVFilter"),
    jetSrc = cms.InputTag("cmgPFJetSel"),
    leadJetSrc = cms.InputTag("cmgPFBaseJetLead"),
    recBosonSrc = cms.InputTag("cmgTauMuPreSel"),
    weights_gbrmetphi = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmetphi_53_Dec2012.root'),
    weights_gbrmet = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/mvaMET/gbrmet_53_Dec2012.root'),
    puJetIdLabel = cms.string('met53x')
)


process.recoilCorMETDiTau = cms.EDProducer("RecoilCorrectedMETProducerDiTau",
    leptonLeg = cms.int32(0),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_htt53X_20pv_njet.root'),
    enable = cms.bool(True),
    correctionType = cms.int32(1),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgDiTauPtSel")
)


process.recoilCorMETTauEle = cms.EDProducer("RecoilCorrectedMETProducerTauEle",
    leptonLeg = cms.int32(0),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_htt53X_20pv_njet.root'),
    enable = cms.bool(True),
    correctionType = cms.int32(1),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauEleTauPtSel")
)


process.recoilCorMETTauMu = cms.EDProducer("RecoilCorrectedMETProducerTauMu",
    leptonLeg = cms.int32(0),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection//recoilfit_htt53X_20pv_njet.root'),
    enable = cms.bool(True),
    correctionType = cms.int32(1),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauMuTauPtSel")
)


process.recoilCorrectedMETDiTau = cms.EDProducer("RecoilCorrectedMETProducerDiTau",
    leptonLeg = cms.int32(0),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53XRR_2012_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53XRR_2012_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_ztt53X_20pv_njet.root'),
    enable = cms.bool(True),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgDiTauSel")
)


process.recoilCorrectedMETMuEle = cms.EDProducer("RecoilCorrectedMETProducerMuEle",
    leptonLeg = cms.int32(2),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    metSrc = cms.InputTag("cmgPFMET"),
    enable = cms.bool(True),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgMuEleSel"),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root')
)


process.recoilCorrectedMETTauEle = cms.EDProducer("RecoilCorrectedMETProducerTauEle",
    leptonLeg = cms.int32(2),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    enable = cms.bool(True),
    correctionType = cms.int32(2),
    jetSrc = cms.InputTag("cmgPFJetForRecoil"),
    recBosonSrc = cms.InputTag("cmgTauEleSel")
)


process.recoilCorrectedMETTauMu = cms.EDProducer("RecoilCorrectedMETProducerTauMu",
    leptonLeg = cms.int32(2),
    force = cms.bool(False),
    verbose = cms.untracked.bool(False),
    genBosonSrc = cms.InputTag("genWorZ"),
    fileZmmMC = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_zmm53X_20pv_njet.root'),
    fileZmmData = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_datamm53X_20pv_njet.root'),
    fileCorrectTo = cms.string('/afs/cern.ch/user/m/manzoni/summer13/CMGTools/CMSSW_5_3_9/src/CMGTools/Utilities/data/metRecoilCorrection/recoilfit_wjets53X_20pv_njet.root'),
    enable = cms.bool(True),
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
        nSigma = cms.double(1),
        shift3Prong = cms.double(0.012),
        shift1ProngNoPi0 = cms.double(0.0),
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
        metsigCollection = cms.InputTag(""),
        metCollection = cms.InputTag("cmgPFMET")
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
        nSigma = cms.double(0),
        shift3Prong = cms.double(0.0),
        shift1ProngNoPi0 = cms.double(0.0),
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
        nSigma = cms.double(0),
        shift3Prong = cms.double(0.0),
        shift1ProngNoPi0 = cms.double(0.0),
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
        metsigCollection = cms.InputTag(""),
        metCollection = cms.InputTag("cmgPFMET")
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
        nSigma = cms.double(0),
        shift3Prong = cms.double(0.0),
        shift1ProngNoPi0 = cms.double(0.0),
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
        nSigma = cms.double(0),
        shift3Prong = cms.double(0.0),
        shift1ProngNoPi0 = cms.double(0.0),
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


process.diTauPreSelSkimSequence = cms.Sequence(process.diTauPreSelCount)


process.muEleFullSelSkimSequence = cms.Sequence(process.muEleFullSelCount)


process.tauEleMvaMETRecoilSequence = cms.Sequence(process.goodPVFilter+process.mvaMETTauEle+process.cmgTauEleCor+process.cmgTauEleTauPtSel+process.recoilCorMETTauEle)


process.tauEleFullSelSkimSequence = cms.Sequence(process.tauEleFullSelCount)


process.mvaMETSequence = cms.Sequence(process.goodPVFilter+process.mvaMETDiTau+process.cmgDiTauCor+process.cmgDiTauPtSel+process.recoilCorMETDiTau)


process.tauMuStdSequence = cms.Sequence(process.cmgTauMu+process.cmgTauMuPreSel)


process.tauEleStdSequence = cms.Sequence(process.cmgTauEle+process.cmgTauElePreSel)


process.tauMuMvaMETrecoilSequence = cms.Sequence(process.goodPVFilter+process.mvaMETTauMu+process.cmgTauMuCor+process.cmgTauMuTauPtSel+process.recoilCorMETTauMu)


process.diTauFullSelSkimSequence = cms.Sequence(process.diTauFullSelCount)


process.metRecoilCorrectionInputSequence = cms.Sequence(process.cmgPFJetForRecoilPresel+process.cmgPFJetForRecoil+process.genWorZ)


process.metRecoilCorrectionSequence = cms.Sequence(process.metRecoilCorrectionInputSequence+process.recoilCorrectedMETTauMu+process.recoilCorrectedMETTauEle+process.recoilCorrectedMETMuEle)


process.diTauCorSVFitSequence = cms.Sequence(process.mvaMETSequence+process.cmgDiTauCorSVFitPreSel+process.cmgDiTauCorSVFitFullSel)


process.tauElePreSelSkimSequence = cms.Sequence(process.tauElePreSelCount)


process.muElePreSelSkimSequence = cms.Sequence(process.muElePreSelCount)


process.tauEleCorSVFitSequence = cms.Sequence(process.tauEleMvaMETRecoilSequence+process.cmgTauEleCorSVFitPreSel+process.cmgTauEleCorSVFitFullSel)


process.vertexWeightSequence = cms.Sequence(process.vertexWeightEPSJul8+process.vertexWeightLeptonPhoton+process.vertexWeightMay10ReReco+process.vertexWeightPromptRecov4+process.vertexWeight05AugReReco+process.vertexWeightPromptRecov6+process.vertexWeight2invfb+process.vertexWeight2011B+process.vertexWeight2011AB+process.vertexWeightFall11EPSJul8+process.vertexWeightFall11LeptonPhoton+process.vertexWeightFall11May10ReReco+process.vertexWeightFall11PromptRecov4+process.vertexWeightFall1105AugReReco+process.vertexWeightFall11PromptRecov6+process.vertexWeightFall112invfb+process.vertexWeightFall112011B+process.vertexWeightFall112011AB+process.vertexWeight3DMay10ReReco+process.vertexWeight3DPromptRecov4+process.vertexWeight3D05AugReReco+process.vertexWeight3DPromptRecov6+process.vertexWeight3D2invfb+process.vertexWeight3D2011B+process.vertexWeight3D2011AB+process.vertexWeight3DFall11May10ReReco+process.vertexWeight3DFall11PromptRecov4+process.vertexWeight3DFall1105AugReReco+process.vertexWeight3DFall11PromptRecov6+process.vertexWeight3DFall112invfb+process.vertexWeight3DFall112011B+process.vertexWeight3DFall112011AB+process.vertexWeightSummer12MCICHEPData+process.vertexWeightSummer12MC53XICHEPData+process.vertexWeightSummer12MC53XHCPData+process.vertexWeightSummer12MC53X2012D6fbData+process.vertexWeightSummer12MC53X2012ABCDData+process.vertexWeightSummer12MC53X2012BCDData)


process.diTauStdSequence = cms.Sequence(process.cmgDiTau+process.cmgDiTauPreSel)


process.tauMuPreSelSkimSequence = cms.Sequence(process.tauMuPreSelCount)


process.tauMuFullSelSkimSequence = cms.Sequence(process.tauMuFullSelCount)


process.genSequence = cms.Sequence(process.metRecoilCorrectionInputSequence+process.vertexWeightSequence)


process.tauEleSequence = cms.Sequence(process.tauEleStdSequence+process.tauEleCorSVFitSequence)


process.tauMuCorSVFitSequence = cms.Sequence(process.tauMuMvaMETrecoilSequence+process.cmgTauMuCorSVFitPreSel+process.cmgTauMuCorSVFitFullSel)


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
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    cerr = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noTimeStamps = cms.untracked.bool(False),
        FwkReport = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(5000),
            limit = cms.untracked.int32(10000000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        FwkSummary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1),
            limit = cms.untracked.int32(10000000)
        ),
        threshold = cms.untracked.string('INFO')
    ),
    FrameworkJobReport = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        FwkJob = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(10000000)
        )
    ),
    suppressWarning = cms.untracked.vstring(),
    statistics = cms.untracked.vstring('cerr_stats'),
    infos = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        Root_NoDictionary = cms.untracked.PSet(
            optionalPSet = cms.untracked.bool(True),
            limit = cms.untracked.int32(0)
        ),
        placeholder = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    debugModules = cms.untracked.vstring(),
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

