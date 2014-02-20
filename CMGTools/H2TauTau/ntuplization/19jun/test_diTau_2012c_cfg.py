import copy
import os 
import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.H2TauTau.triggerMap import pathsAndFilters

use_diTau           = False  ## be careful only one at at time can be True
use_diTauJet        = False  ## be careful only one at at time can be True
use_Both            = True   ## be careful only one at at time can be True
MC_trigger_matching = True   ## don't change to False unless you want to test something tricky

puFileMC   = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/07-01-13/MC_Summer12_PU_S10-600bins.root'
puFileData = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/12-06-13/Data_Pileup_2012_ReReco-600bins.root' ## new for rereco
#puFileData = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/07-01-13/Data_Pileup_2012_Moriond-600bins.root' ## old for promt reco

## diTau trigger weights
diTau_tauEffWeight_mc = 'eff2012IsoParkedTau19fbMC_Simone'
diTau_tauEffWeight    = 'eff2012IsoParkedTau19fb_Simone'

## diTauJet trigger weights
diTauJet_tauEffWeight_mc = 'eff2012IsoTau19fbMC_Simone'
diTauJet_tauEffWeight    = 'eff2012IsoTau19fb_Simone'
diTauJet_jetEffWeight_mc = 'eff2012Jet19fb'  ## DUMMY: that means scale factor 1. for the MC trigger jet leg
diTauJet_jetEffWeight    = 'eff2012Jet19fb'

eventSelector = cfg.Analyzer(
    'EventSelector',
    toSelect = [
3171224,
3117144,
3171140,
159368,
5196,
131833,
3117014,
4489329,
4489947,
148811,
3086626,
6880,
4490352,
4271255,
149063,
149016,
180505,
3085452,
2922526,
2994401,
165756,
3171219,
1033694,
2922521,
1137822,
2202782,
3117258,
3170209,
159393,
3171543,
3097322,
6699,
3097361,
158333,
4491111,
4489459,
3089023,
2203,
171670,
2219630,
224629,
4489351,
3085462,
3111333,
2219734,
180324,
3169218,
3171386,
148932,
3111390,
4235854,
2962562,
4491295,
4490115,
167370,
2940668,
    ]
    )

triggerAna = cfg.Analyzer(
    'TriggerAnalyzer',
    verbose = False
    )
    
TauTauAna = cfg.Analyzer(
    'TauTauAnalyzer',
    pt                = 45,  ### same tau pt cut for both
    eta               = 2.1, ### same |eta| for both taus
    iso_test          = 999, ### at least one leg with this isolation ## NOT IN YET
    iso_lowest        = 999, ### most relaxed isolation ## NOT IN YET
    m_min             = 0,
    m_max             = 99999,
    diLeptonCutString = '',
    triggerMap        = pathsAndFilters,
    isolation         = 'db3h', ### options available in TauTauAnalyzer: db3h, mva, mva2
    #jetPt             = 50.,    ### change this when not using diTauJet 
    jetPt             = 0.,    ### change this when not using diTauJet 
    jetEta            = 30.0,
    relaxJetId        = False,
    )

diTau_tau1Weighter = cfg.Analyzer(
    'LeptonWeighter_diTau_tau1',
    effWeight   = diTau_tauEffWeight,
    effWeightMC = diTau_tauEffWeight_mc,
    lepton      = 'leg1',
    verbose     = False
    )

diTau_tau2Weighter = cfg.Analyzer(
    'LeptonWeighter_diTau_tau2',
    effWeight   = diTau_tauEffWeight,
    effWeightMC = diTau_tauEffWeight_mc,
    lepton      = 'leg2',
    verbose     = False
    )

diTauJet_tau1Weighter = cfg.Analyzer(
    'LeptonWeighter_diTauJet_tau1',
    effWeight   = diTauJet_tauEffWeight,
    effWeightMC = diTauJet_tauEffWeight_mc,
    lepton      = 'leg1',
    verbose     = False
    )

diTauJet_tau2Weighter = cfg.Analyzer(
    'LeptonWeighter_diTauJet_tau2',
    effWeight   = diTauJet_tauEffWeight,
    effWeightMC = diTauJet_tauEffWeight_mc,
    lepton      = 'leg2',
    verbose     = False
    )

diTauJet_jetWeighter = cfg.Analyzer(
    'JetWeighter_diTauJet_jet1',
    effWeight   = diTauJet_jetEffWeight,
    effWeightMC = diTauJet_jetEffWeight_mc,
    verbose     = False
    )

vertexAna = cfg.Analyzer(
    'VertexAnalyzer',
    goodVertices = 'offlinePrimaryVertices', 
    fixedWeight  = 1,
    verbose      = False
    )

embedWeighter = cfg.Analyzer(
    'EmbedWeighter',
    verbose = False
    )

pileUpAna = cfg.Analyzer(
    'PileUpAnalyzer',
    true = True
    )

# defined for vbfAna and eventSorter
vbfKwargs = dict( Mjj = 400,
                  deltaEta = 4.0    
                  )

vbfAna = cfg.Analyzer(
    'VBFAnalyzer',
    vbfMvaWeights = os.environ['CMSSW_BASE'] + '/src/CMGTools/H2TauTau/data/VBFMVA_BDTG_HCP_52X.weights.xml',
    jetCol     = 'cmgPFJetSel',
    jetPt      = 30,
    jetEta     = 4.7,
    cjvPtCut   = 30.,
    btagSFseed = 123456,
    relaxJetId = False,
    **vbfKwargs
    )

##### 2012 WJets weights using ewk.py
#  0j : (36257.2 - 6440.4 - 2087.2 - 619.0 - 255.2) / 36257.2 = 0.74069150403230244
#  1j : 6440.4 / 36257.2                                      = 0.17763092571958122
#  2j : 2087.2 / 36257.2                                      = 0.057566497137120351
#  3j : 619.0  / 36257.2                                      = 0.017072471122976954
#  4j : 255.2  / 36257.2                                      = 0.0070386019880189317

WNJetsAna = cfg.Analyzer(
    'WNJetsAnalyzer',
    verbose = False,
    fractions = [ 0.74069150403230244,
                  0.17763092571958122,
                  0.057566497137120351,
                  0.017072471122976954,
                  0.0070386019880189317,
                  ],
    )

treeProducer = cfg.Analyzer(
    'H2TauTauTreeProducerTauTau',
    )


treeProducerXcheck = cfg.Analyzer(
    'H2TauTauSyncTreeTauTau',
    pt20 = False
    )


#########################################################################################

from CMGTools.H2TauTau.proto.samples.run2012.diTau_Colin_Feb8 import *

#########################################################################################

WNJetsAna.nevents = [ WJets.nGenEvents,
                      W1Jets.nGenEvents,
                      W2Jets.nGenEvents,
                      W3Jets.nGenEvents,
                      W4Jets.nGenEvents
                      ]

WJetsSoup = copy.copy(WJets)
WJetsSoup.name = 'WJetsSoup'
MC_list.append(WJetsSoup)

mc_jet_scale = 1.
mc_jet_smear = 0.
for mc in MC_list:
    # could handle the weights in the same way
    mc.jetScale   = mc_jet_scale
    mc.jetSmear   = mc_jet_smear
    mc.puFileData = puFileData
    mc.puFileMC   = puFileMC


selectedComponents = allsamples
selectedComponents.append(WJetsSoup)


#### FOR TESTING
selectedComponents = [HiggsVBF125]
#print [(c.name,'split:',c.splitFactor) for c in selectedComponents]
#
for c in selectedComponents :
  c.splitFactor *= 30

sequence = cfg.Sequence( [
    #eventSelector,
    triggerAna,
    vertexAna,
    TauTauAna,
    WNJetsAna,
    vbfAna,
    pileUpAna,
    embedWeighter, 
    diTau_tau1Weighter,
    diTau_tau2Weighter,
    diTauJet_tau1Weighter,
    diTauJet_tau2Weighter,
    diTauJet_jetWeighter,
    #treeProducer,
    treeProducerXcheck,
    ] )
    
###################################################
### REMOVE UNNEEDED TRIGGER WEIGHTER IF (!BOTH) ###
###################################################
if use_diTau:
  sequence.remove(diTauJet_tau1Weighter)
  sequence.remove(diTauJet_tau2Weighter)
  sequence.remove(diTauJet_jetWeighter)
if use_diTauJet:
  sequence.remove(diTau_tau1Weighter)
  sequence.remove(diTau_tau2Weighter)

###################################################
###    SET THE TRIGGERS TO BE USED WITH DATA    ###
###################################################
for data in data_parked_2012:
  if use_diTau :
    data.triggers = data_parked_triggers_2012
  elif use_diTauJet :
    data.triggers = data_triggers_2012
  elif use_Both:
    data.triggers  = data_parked_triggers_2012  ## ORDER MATTERS!
    data.triggers += data_triggers_2012         ## ORDER MATTERS!
  

###################################################
###     SET THE TRIGGERS TO BE USED WITH MC     ###
###################################################
for mc in MC_list:
  mc.triggers = mc_triggers
  if MC_trigger_matching:
    if   use_diTau     : mc.triggers = ['HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6']
    elif use_diTauJet  : mc.triggers = ['HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2']
    elif use_Both      : mc.triggers = ['HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6','HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2'] ## ORDER MATTERS !!!
  else:
    mc.triggers = []

###################################################
###     SPLIT DY AND W IN REAL AND FAKES        ###
###################################################

DYJets.fakes = True
WJets.fakes  = True

###################################################
###            SET BATCH OR LOCAL               ###
###################################################
test = 0    # test = 0 run on batch, test = 1 run locally
if test == 1:
    cache = False
    #HiggsGGH120.files = getFiles('/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_13Jun_manzoni_Nom', 'manzoni', 'diTau_fullsel.*root', cache)
    #comp = HiggsGGH120
    data_Run2012C_22Jan2013_v1.files = getFiles('/TauParked/Run2012C-22Jan2013-v1/AOD/PAT_CMG_V5_16_0/HTT_13Jun_manzoni_Nom', 'manzoni', 'diTau_fullsel.*root', cache)
    comp = data_Run2012C_22Jan2013_v1
    selectedComponents = [comp]
    comp.splitFactor = 1
    #comp.splitFactor *= 50
    comp.files = comp.files[:1]
elif test == 2:
    selectedComponents = []
    for comp in MC_list:
        selectedComponents.append(comp)
        comp.splitFactor = 1
        comp.files = comp.files[:1]

print [s.name for s in selectedComponents]
    
config = cfg.Config( components = selectedComponents,
                     sequence   = sequence )
