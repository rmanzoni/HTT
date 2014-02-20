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
1257567,
2370610,
3710277,
4721953,
4059747,
1503996,
2642785,
3517658,
2318066,
1900598,
4257652,
1991869,
4814717,
803821,
121236,
3815740,
1169301,
2015873,
1072241,
4830110,
2481049,
1884537,
1933485,
2937258,
1827136,
3511371,
1352830,
2115675,
525169,
900109,
2808026,
3539917,
2635253,
3073410,
4598410,
3991303,
528718,
1870656,
1571225,
3901013,
2406523,
1604278,
4924682,
694568,
1904163,
3181997,
3434337,
797559,
662947,
180048,
3347509,
432422,
2314145,
559554,
1260624,
3520583,
1462787,
4000299,
1018016,
37959,
3469681,
2639909,
3571787,
2437642,
3654834,
4921189,
1569355,
4636810,
2131502,
2047340,
2745643,
846245,
3172357,
158089,
3039947,
3891641,
2128534,
1070928,
184828,
1261222,
3240794,
4663585,
350909,
4467498,
2470714,
725063,
3688187,
4302269,
3834698,
1017019,
509686,
1056948,
2257618,
3577483,
3209387,
3605122,
3682672,
2806278,
2855053,
2457978,
4849989,
2887053,
459644,
684533,
2083287,
3526351,
3966147,
2635668,
949962,
3865288,
1910127,
2530036,
2285481,
2887897,
3201688,
2657555,
2994291,
508563,
4701763,
2638993,
4471488,
3597640,
1308058,
3647821,
3651673,
4537697,
1357740,
3289677,
1874224,
785439,
3305510,
84042,
4303143,
161346,
2158375,
4251341,
2560572,
1954971,
1467078,
4959936,
4070872,
2350021,
3882639,
2221092,
1137822,
166172,
2188099,
632438,
3593464,
3018136,
19137,
2906602,
2435744,
4928696,
4494225,
67765,
10236,
987006,
2359335,
2943668,
4242743,
3702373,
4463148,
1190731,
970338,
3836736,
410764,
4344087,
3807934,
350225,
3259916,
4253085,
1424635,
3994951,
3440448,
3292770,
270749,
3016717,
2797920,
3661225,
3303221,
2882450,
4294290,
3805965,
1634456,
3443403,
4826478,
104104,
848785,
3268467,
110836,
2106025,
1145732,
2741797,
4800253,
3779977,
1591657,
2075237,
2153565,
3133090,
534383,
561959,
969562,
2313950,
3352461,
4277867,
1414457,
249176,
874535,
3953114,
335967,
2507585,
2061524,
3424286,
2757798,
2463303,
2931382,
1807304,
913376,
4151361,
345926,
2969614,
2751029,
3334680,
322590,
3378656,
2524332,
2100039,
2478869,
1869767,
2110764,
4385531,
3345202,
1691835,
3927994,
1278064,
2073538,
1598149,
1558667,
164029,
3871530,
3947335,
1598381,
3377650,
1662968,
1236356,
1599648,
2959565,
891391,
2065313,
1611964,
2514397,
3936834,
3251166,
4812633,
588901,
425737,
1973436,
2302062,
4688241,
1601335,
2316152,
524729,
654354,
4673397,
356086,
1431983,
340296,
3936882,
370804,
3259608,
4001142,
3753182,
2256366,
1397617,
2530705,
693060,
2922521,
442720,
897139,
1489298,
4627404,
4249720,
404550,
2895515,
747674,
938417,
2964479,
890205,
1715396,
2350287,
48219,
1195988,
4909635,
975520,
4628655,
4971662,
2822564,
1669851,
870224,
347502,
4663703,
1268734,
1340086,
1709242,
533816,
3934545,
1027365,
3549904,
3277570,
894828,
3348270,
1648945,
578697,
2528790,
2938603,
2837403,
1551784,
3117014,
816866,
2841753,
1100062,
947253,
2905324,
1511785,
3491662,
3082035,
1622128,
1682915,
4536987,
2712988,
2763216,
771146,
2085357,
2682629,
3689195,
3721724,
3941413,
2232130,
4015112,
3664933,
1139224,
2452604,
2843317,
2404384,
4838344,
245946,
816534,
2721213,
2202782,
4690490,
2866735,
4185936,
116174,
2598768,
2450000,
2739250,
2561987,
812447,
658790,
4377779,
4108500,
4271255,
802477,
317909,
3292487,
1360508,
1224800,
1593390,
2248890,
4192583,
4774707,
3271009,
2716773,
3298009,
2453809,
3073180,
337458,
4559747,
2913881,
4212602,
4494511,
775608,
1635309,
1483518,
1011423,
905380,
3134774,
2816755,
444550,
3824116,
3016361,
3106168,
2680205,
1128039,
4324954,
3327460,
2826532,
4147813,
4947474,
1021134,
4630843,
3030938,
1629690,
4551406,
3124844,
4325627,
3043955,
2622341,
2076296,
81429,
4191412,
3540547,
1112386,
3399929,
2786522,
4023457,
3523221,
4878785,
4250381,
2807263,
4887361,
4728379,
4033102,
713205,
3736450,
3810797,
618399,
504224,
4046455,
4447573,
1898511,
4993461,
3208035,
1384480,
1563964,
987052,
59143,
1577329,
1033694,
1113076,
1991883,
4607774,
1214988,
2849390,
2143529,
1957850,
231322,
1241818,
4736864,
797742,
206451,
2245432,
384568,
3278929,
404665,
2507280,
3091624,
3148253,
3617816,
1254089,
4703437,
3298678,
388968,
2518486,
1241656,
4696382,
893612,
928779,
1196855,
3722402,
3465424,
2041826,
3479333,
610949,
2868586,
4017642,
3699605,
4749947,
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

selectedComponents = [HiggsGGH120]
print [(c.name,'split:',c.splitFactor) for c in selectedComponents]
for c in selectedComponents :
  c.splitFactor *= 4 

sequence = cfg.Sequence( [
    #eventSelector,
    triggerAna,
    vertexAna,
    TauTauAna,
    #WNJetsAna,
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
    comp = HiggsGGH120
    cache = False
    selectedComponents = [comp]
    comp.splitFactor = 1
    #comp.files = comp.files[:2]
elif test == 2:
    selectedComponents = []
    for comp in MC_list:
        selectedComponents.append(comp)
        comp.splitFactor = 1
        comp.files = comp.files[:1]

print [s.name for s in selectedComponents]
    
config = cfg.Config( components = selectedComponents,
                     sequence = sequence )
