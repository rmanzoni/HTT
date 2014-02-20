import copy
import os 
import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.H2TauTau.triggerMap import pathsAndFilters

use_diTau           = False  ## be careful only one at at time can be True
use_diTauJet        = False  ## be careful only one at at time can be True
use_Both            = True   ## be careful only one at at time can be True
use_embTrig         = True   ## require trigger for embedded samples
use_recHit          = False  ## RecHit embedded samples
MC_trigger_matching = True   ## don't change to False unless you want to test something tricky

puFileMC   = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/07-01-13/MC_Summer12_PU_S10-600bins.root'
puFileData = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/12-06-13/Data_Pileup_2012_ReReco-600bins.root' ## new for rereco

mc_tauEffWeight_mc = 'effTau2012MC'
mc_muEffWeight_mc  = 'effMu2012MC'
mc_tauEffWeight    = 'effTau2012AB'
mc_muEffWeight     = 'effMu2012AB'
    
eventSelector = cfg.Analyzer(
    'EventSelector',
    toSelect = [
    985506,
    ]
    )

triggerAna = cfg.Analyzer(
    'TriggerAnalyzer'           ,
    keepFailingEvents     = True,
    keepAllTriggerObjects = True, ## DEFAULT False !!
    verbose               = False
    )

vertexAna = cfg.Analyzer(
    'VertexAnalyzer',
    goodVertices = 'offlinePrimaryVertices', 
    fixedWeight  = 1,
    verbose      = False
    )

embedWeighter = cfg.Analyzer(
    'EmbedWeighter',
    isRecHit = use_recHit, ## if False it means that it is PFemb
    verbose  = False
    )

pileUpAna = cfg.Analyzer(
    'PileUpAnalyzer',
    true = True
    )

TauMuAna = cfg.Analyzer(
    'TauMuAnalyzer',
    pt1        = 20    ,
    eta1       = 2.3   ,
    iso1       = 999   ,
    pt2        = 18    , 
    eta2       = 2.1   ,
    iso2       = 0.1   ,
    m_min      = 10    ,
    m_max      = 99999 ,
#     triggerMap = pathsAndFilters
    )

tauWeighter = cfg.Analyzer(
    'LeptonWeighter_tau',
    effWeight     = mc_tauEffWeight,
    effWeightMC   = mc_tauEffWeight_mc,
    lepton        = 'leg1',
    verbose       = False,
    #disable       = False,
    #recEffVersion = None
    )

muonWeighter = cfg.Analyzer(
    'LeptonWeighter_mu',
    effWeight     = mc_muEffWeight,
    effWeightMC   = mc_muEffWeight_mc,
    lepton        = 'leg2',
    verbose       = False,
    #disable       = True,
    #recEffVersion = None
    )


# defined for vbfAna and eventSorter
vbfKwargs = dict( Mjj = 400, deltaEta = 4.0 )

vbfAna = cfg.Analyzer(
    'VBFAnalyzer',
    vbfMvaWeights = os.environ['CMSSW_BASE'] + '/src/CMGTools/H2TauTau/data/VBFMVA_BDTG_HCP_52X.weights.xml',
    jetCol     = 'cmgPFJetSel',
    jetPt      = 30,
    looseJetPt = 20,
    jetEta     = 4.7,
    cjvPtCut   = 30.,
    btagSFseed = 123456,
    relaxJetId = False,
    **vbfKwargs
    )


treeProducer = cfg.Analyzer(
    'H2TauTauTreeProducerTauMu'
    )

#########################################################################################

from CMGTools.H2TauTau.proto.samples.run2012.tauMu_JanAug06 import * 

#########################################################################################

mc_jet_scale = 1.
mc_jet_smear = 0.
for mc in MC_list:
    # could handle the weights in the same way
    mc.jetScale   = mc_jet_scale
    mc.jetSmear   = mc_jet_smear
    mc.puFileData = puFileData
    mc.puFileMC   = puFileMC

selectedComponents  = allsamples

###################################################
###             SET COMPONENTS BY HAND          ###
###################################################
selectedComponents  = [HiggsSUSYBB300,HiggsSUSYGluGlu300]
for c in selectedComponents : c.splitFactor *= 50

###################################################
###                    SEQUENCE                 ###
###################################################

sequence = cfg.Sequence( [
    eventSelector,
    triggerAna   ,
    vertexAna    ,
    TauMuAna     ,
    vbfAna       ,
    pileUpAna    ,
    embedWeighter, 
    tauWeighter  , 
    muonWeighter , 
    treeProducer
   ] )

###################################################
###    SET THE TRIGGERS TO BE USED WITH DATA    ###
###################################################
# for data in data_parked_2012:
#   if use_diTau :
#     data.triggers = data_parked_triggers_2012
#   elif use_diTauJet :
#     data.triggers = data_triggers_2012
#   elif use_Both:
#     data.triggers  = data_parked_triggers_2012  ## ORDER MATTERS!
#     data.triggers += data_triggers_2012         ## ORDER MATTERS!

###################################################
###     SET THE TRIGGERS TO BE USED WITH MC     ###
###################################################
for mc in MC_list:
  mc.triggers = mc_triggers
  if MC_trigger_matching:
    if   use_diTau     : mc.triggers = ['HLT_IsoMu24_eta2p1_v13']
    elif use_diTauJet  : mc.triggers = ['HLT_IsoMu24_eta2p1_v13']
    elif use_Both      : mc.triggers = ['HLT_IsoMu24_eta2p1_v13','HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk1_eta2p1_v4'] ## ORDER MATTERS !!!
  else:
    mc.triggers = []

###################################################
###   SET THE TRIGGERS TO BE USED WITH RH EMB   ###
###################################################
# for emb in embed_list:
#   if use_embTrig :
#     emb.triggers = emb_rechit_triggers

###################################################
###     SPLIT DY AND W IN REAL AND FAKES        ###
###################################################

DYJets.fakes = True
WJets.fakes  = True

###################################################
###            SET BATCH OR LOCAL               ###
###################################################
test = 1   # test = 0 run on batch, test = 1 run locally
if test == 1:
    cache = True
    HiggsSUSYGluGlu300.files = getFiles('/SUSYGluGluToHToTauTau_M-300_8TeV-pythia6-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_13Sep_manzoni_MuTau_Nom', 'manzoni', 'tauMu_fullsel.*root', cache)
    comp = HiggsSUSYGluGlu300
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
