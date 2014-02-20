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
7860122,
2289978,
22449616,
849728958,
182296969,
63881669,
122056547,
770286229,
707389896,
723531344,
725208638,
732182332,
743547286,
72011301,
272576016,
390411212,
408628970,
417337975,
437069349,
472671299,
472988104,
502511575,
503943130,
516794165,
113805131,
15351880,
9455403,
184224556,
64341671,
690308987,
500095584,
509897105,
535216294,
442865573,
211045776,
108725862,
141325586,
160882680,
178219985,
178916858,
184460360,
188847488,
59552159,
68065763,
84332631,
95440468,
96467703,
20345398,
20707714,
29994343,
37516368,
39334294,
233018666,
455585743,
11359550,
21332097,
27039165,
356666690,
56247049,
72311656,
325256228,
598648221,
189796021,
409340903,
339703537,
344409172,
353073055,
35351683,
362985617,
368488426,
372625976,
400578563,
411135390,
423303161,
446058111,
447597705,
450240879,
459918005,
463164020,
48841299,
12518571,
22726719,
48017802,
57176862,
233975889,
473777975,
491046491,
508103845,
7624441,
368625561,
370800094,
160691502,
476534862,
135030286,
158961688,
190513582,
192803646,
195445692,
203897346,
31952391,
63916487,
89538597,
125772839,
135752920,
143305195,
147521614,
156040004,
199574583,
207098601,
267556820,
290054537,
293318425,
321509518,
324089132,
350743393,
384351595,
45611315,
459269246,
472119747,
47360436,
511144141,
518833704,
535790422,
582119049,
594752990,
92420104,
327926716,
515946995,
715003415,
152704709,
17399496,
178244008,
191202731,
192732384,
234492697,
243337202,
250690355,
254753536,
26745136,
270927660,
40717785,
62853746,
78763106,
89081993,
3126154,
34679166,
78822188,
443506451,
573707492,
575891028,
576961595,
583636529,
590290943,
616705031,
676088359,
679647220,
686216227,
691089861,
700451482,
713065467,
713726097,
722209962,
727251901,
731303171,
752685748,
752762737,
152026168,
264013693,
793110394,
21683910,
23107202,
68946935,
84157006,
85468107,
90886320,
63436042,
74993108,
83051017,
90165568,
91735519,
29516582,
491902206,
311762008,
267137234,
624943687,
321770295,
154875562,
16417987,
467498185,
59249076,
86774263,
23819818,
105293521,
160065918,
17802640,
2470120,
29915913,
492142130,
9752107,
146984714,
478764783,
12803053,
100439259,
111791553,
71250566,
77503756,
1622193,
14678786,
25773277,
982938,
20980503,
26433640,
6615225,
10361507,
107936932,
108105250,
110833224,
117999408,
136745046,
151797901,
152873458,
16812143,
172602421,
175725385,
199567570,
214173090,
220288725,
25484406,
276125615,
288988533,
321460694,
34085225,
342372321,
349741108,
350038922,
359369602,
359467620,
383793812,
386113535,
403214993,
409355179,
415606309,
418653525,
435925301,
45267039,
467362923,
498532222,
518140502,
523419203,
540014709,
543858970,
61079758,
82385089,
85578001,
86056517,
11108281,
20821330,
2456714,
150100310,
15499508,
164359001,
174303920,
180161312,
2986932,
40781816,
6215097,
72334434,
25465529,
7196047,
8188426,
472235716,
596136449,
104325184,
145039587,
180698479,
287244874,
63892677,
58223193,
7212866,
7500492,
103306178,
106365825,
146959137,
157027699,
161437149,
209422578,
209703673,
216883365,
43233308,
55012977,
6403009,
64897599,
67739965,
81478861,
82231334,
98705806,
99783826,
8871934,
808354056,
102488502,
107774795,
107775649,
109377567,
109463344,
117209683,
125437375,
138693930,
141582165,
145288078,
148580105,
148908785,
150896339,
156061525,
176359153,
181120476,
181325313,
181328745,
183533049,
203754258,
208091079,
219809917,
229690497,
240880672,
243975219,
248233883,
260558602,
267548910,
272026774,
275583686,
278975572,
283651585,
283794186,
296857176,
305622117,
307707841,
311391009,
315575466,
318400103,
320826108,
321130041,
321494869,
54169106,
74213138,
74283794,
79144605,
81313899,
91442460,
95299253,
17398977,
106983336,
108245368,
117565115,
127066695,
135031503,
13537854,
135869825,
148998972,
33688577,
35521724,
35648367,
39187003,
41046191,
54541862,
65232800,
66329657,
70530464,
89084846,
89821712,
91797477,
166276992,
167339945,
183931057,
186169880,
764823626,
821475237,
995677370,
582108010,
582968023,
138359222,
18590302,
30887446,
10350284,
7666292,
8959442
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
selectedComponents = [embed_Run2012B_22Jan2013_v1]
# selectedComponents = [embed_Run2012A_22Jan2013_v1,embed_Run2012B_22Jan2013_v1,embed_Run2012C_22Jan2013_v1,embed_Run2012D_22Jan2013_v1]
# selectedComponents = [HiggsGGH125, embed_Run2012B_22Jan2013_v1]
for c in selectedComponents : c.splitFactor *= 10
# print [(c.name,'split:',c.splitFactor) for c in selectedComponents]

sequence = cfg.Sequence( [
    eventSelector,
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
    treeProducer,
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
test = 1    # test = 0 run on batch, test = 1 run locally
if test == 1:
    cache = True
    #HiggsGGH120.files = getFiles('/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_13Jun_manzoni_Nom', 'manzoni', 'diTau_fullsel.*root', cache)
    #HiggsGGH120.files = getFiles('/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_23Jun_manzoni_Nom_newrecoil_newTauES', 'manzoni', 'diTau_fullsel.*root', cache)
    #HiggsGGH120.files = getFiles('/GluGluToHToTauTau_M-120_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_23Jun_manzoni_Nom_oldrecoil_oldTauES', 'manzoni', 'diTau_fullsel.*root', cache)
    #comp = embed_Run2012B_22Jan2013_v1
    comp = embed_Run2012B_22Jan2013_v1	
    #data_Run2012C_22Jan2013_v1.files = getFiles('/TauParked/Run2012C-22Jan2013-v1/AOD/PAT_CMG_V5_16_0/HTT_13Jun_manzoni_Nom', 'manzoni', 'diTau_fullsel.*root', cache)
    #comp = data_Run2012C_22Jan2013_v1
    selectedComponents = [comp]
    comp.splitFactor = 1
    #comp.splitFactor *= 50
    #comp.files = comp.files[:5]
elif test == 2:
    selectedComponents = []
    for comp in MC_list:
        selectedComponents.append(comp)
        comp.splitFactor = 1
        comp.files = comp.files[:1]

print [s.name for s in selectedComponents]
    
config = cfg.Config( components = selectedComponents,
                     sequence   = sequence )
