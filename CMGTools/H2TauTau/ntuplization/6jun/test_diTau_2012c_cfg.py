import copy
import os 
import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.H2TauTau.triggerMap import pathsAndFilters

useParked           = True
MC_trigger_matching = False   ## don't change to False unless you want to test something tricky

puFileMC   = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/07-01-13/MC_Summer12_PU_S10-600bins.root'
puFileData = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/07-01-13/Data_Pileup_2012_Moriond-600bins.root'

mc_tauEffWeight_mc = 'eff2012IsoTau19fbMC_Simone'
mc_jetEffWeight_mc = 'eff2012Jet19fb'  ## DUMMY: that means scale factor 1. for the MC trigger jet leg
mc_tauEffWeight    = 'eff2012IsoTau19fb_Simone'
mc_jetEffWeight    = 'eff2012Jet19fb'

if useParked :
  mc_tauEffWeight    = 'eff2012IsoParkedTau19fb_Simone'   
  mc_tauEffWeight_mc = 'eff2012IsoParkedTau19fbMC_Simone' 

eventSelector = cfg.Analyzer(
    'EventSelector',
    toSelect = [
       576115,
    ]
    )

triggerAna = cfg.Analyzer(
    'TriggerAnalyzer',
    verbose = False
    )
    
TauTauAna = cfg.Analyzer(
    'TauTauAnalyzer',
    pt                = 35,  ### same tau pt cut for both
    eta               = 2.1, ### same |eta| for both taus
    iso_test          = 999, ### at least one leg with this isolation ## NOT IN YET
    iso_lowest        = 999, ### most relaxed isolation ## NOT IN YET
    m_min             = 0,
    m_max             = 99999,
    diLeptonCutString = '',
    triggerMap        = pathsAndFilters,
    isolation         = 'db3h', ### options available in TauTauAnalyzer: db3h, mva, mva2
    jetPt             = 50.,    ### change this when not using diTauJet 
    jetEta            = 3.0,
    relaxJetId        = False,
    )

tau1Weighter = cfg.Analyzer(
    'LeptonWeighter_tau1',
    effWeight   = mc_tauEffWeight,
    effWeightMC = mc_tauEffWeight_mc,
    lepton      = 'leg1',
    verbose     = False
    )

tau2Weighter = cfg.Analyzer(
    'LeptonWeighter_tau2',
    effWeight   = mc_tauEffWeight,
    effWeightMC = mc_tauEffWeight_mc,
    lepton      = 'leg2',
    verbose     = False
    )

jetWeighter = cfg.Analyzer(
    'JetWeighter_jet1',
    effWeight   = mc_jetEffWeight,
    effWeightMC = mc_jetEffWeight_mc,
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

selectedComponents = [HiggsVBF125]
#print [(c.name,'split:',c.splitFactor) for c in selectedComponents]
#
#for c in selectedComponents :
#  c.splitFactor *= 4

sequence = cfg.Sequence( [
    #eventSelector,
    triggerAna,
    vertexAna,
    TauTauAna,
    WNJetsAna,
    vbfAna,
    pileUpAna,
    embedWeighter, 
    tau1Weighter, 
    tau2Weighter,
    jetWeighter,
    #treeProducer,
    treeProducerXcheck,
    ] )
    
if useParked:
  sequence.remove(jetWeighter)

#import pdb ; pdb.set_trace()

if useParked :
  for data in data_parked_2012:
    data.triggers = data_parked_triggers_2012
else :
  for data in data_2012:
    data.triggers = data_triggers_2012

for mc in MC_list:
  mc.triggers = mc_triggers
  if MC_trigger_matching:
    if useParked : mc.triggers = ['HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6']
    else         : mc.triggers = ['HLT_DoubleMediumIsoPFTau30_Trk5_eta2p1_Jet30_v2']
  else:
    mc.triggers = []

DYJets.fakes = True
WJets.fakes  = True

#import pdb ; pdb.set_trace()

test = 0    # test = 0 run on batch, test = 1 run locally
if test == 1:
    #comp = WJets
    comp = HiggsVBF125
    cache = False
    selectedComponents = [comp]
    comp.splitFactor = 1
    comp.files = comp.files[:2]
elif test == 2:
    selectedComponents = []
    for comp in MC_list:
        selectedComponents.append(comp)
        comp.splitFactor = 1
        comp.files = comp.files[:1]

print [s.name for s in selectedComponents]
    
config = cfg.Config( components = selectedComponents,
                     sequence = sequence )