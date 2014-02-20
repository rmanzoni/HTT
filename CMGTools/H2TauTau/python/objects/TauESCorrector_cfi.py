import FWCore.ParameterSet.Config as cms

cmgTauEsCorrectorFactory = cms.PSet(
		   src    = cms.InputTag("cmgTauSel"),
		   nSigma             = cms.double(0),
		   uncertainty        = cms.double(0.03),
		   shift1ProngNoPi0   = cms.double(0.),
		   shift1Prong1Pi0    = cms.double(0.027),
		   ptDependence1Pi0   = cms.double(0.001),
		   shift3Prong        = cms.double(0.012),
		   ptDependence3Prong = cms.double(0.001),
                   )

cmgTauEsCorrector = cms.EDProducer(
		   "TauESCorrector",
		   cfg  = cmgTauEsCorrectorFactory.clone(),
		   cuts = cms.PSet()
                   )
