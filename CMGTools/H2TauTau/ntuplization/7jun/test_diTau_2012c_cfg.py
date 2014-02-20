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
263375,
289703,
295756,
297501,
303384,
302745,
319381,
366009,
  8849,
120525,
312017,
314108,
374837,
374974,
462981,
572148,
574195,
 58943,
 90376,
221905,
243206,
879294,
774487,
817966,
819730,
867054,
249679,
363959,
366439,
377094,
815280,
932883,
933440,
949346,
971756,
972358,
981503,
981616,
 75137,
127569,
213943,
306190,
275736,
 78280,
 78479,
114090,
133769,
208503,
881952,
715239,
902215,
938741,
939306,
937843,
957240,
308167,
237330,
237579,
238933,
239421,
255818,
299734,
331965,
414367,
602195,
927294,
927670,
927784,
970217,
970341,
982312,
838024,
846840,
911334,
937349,
608275,
627910,
628089,
636066,
637799,
650451,
736824,
835322,
296347,
296702,
325187,
344655,
365298,
367032,
376575,
388614,
389788,
209226,
212774,
234859,
450937,
465395,
512945,
528815,
546842,
549576,
577213,
578222,
563596,
586880,
593175,
655223,
656680,
656684,
657230,
658829,
658835,
 14159,
176544,
521433,
526593,
202008,
456082,
535664,
553718,
553918,
569802,
671710,
681023,
866233,
866248,
866301,
103814,
103954,
116516,
116542,
123783,
139613,
141628,
208864,
673083,
693973,
694058,
695572,
721577,
758582,
696988,
802361,
835674,
851396,
857715,
871590,
481569,
481656,
591441,
628172,
751740,
853148,
960200,
988585,
605870,
608643,
646472,
704844,
735208,
794880,
864644,
864836,
865034,
506109,
526798,
533487,
853548,
941586,
590523,
651864,
926101,
926147,
945990,
731978,
839610,
899723,
909719,
909942,
944199,
958796,
 73255,
 84810,
113524,
113624,
150652,
152416,
471358,
877565,
289142,
989218,
993181,
917253,
976770,
978480,
980040,
734187,
756265,
775250,
798111,
827602,
861541,
869686,
889240,
903942,
912053,
912165,
930549,
930614,
 10867,
264428,
282537,
358968,
365009,
144338,
193861,
200149,
205765,
252052,
272095,
 11526,
346838,
475546,
310866,
873258,
961539,
 47965,
892701,
910502,
986414,
639355,
640283,
687000,
843147,
813165,
848235,
918379,
933827,
934156,
 53202,
 92725,
152309,
162372,
202329,
112580,
112640,
136578,
438113,
 61160,
 61199,
 67477,
104250,
138391,
138450,
139814,
184408,
204575,
568239,
671078,
672160,
876223,
877026,
 91152,
112076,
115703,
100242,
101424,
140548,
147084,
171541,
183681,
215272,
219684,
  3893,
420272,
823138,
923606,
923719,
 19466,
 49329,
 56326,
 65965,
 67177,
132401,
606871,
606968,
672612,
718170,
444939,
754491,
429285,
478014,
505917,
504235,
504432,
514941,
531809,
532750,
532836,
535856,
171726,
426419,
477712,
512388,
569206,
451739,
452125,
566350,
566540,
 17847,
 28701,
 45634,
 46077,
 93739,
887253,
987025,
991547,
178820,
180134,
180184,
226866,
227277,
312425,
339936,
356513,
357051,
357074,
357216,
357268,
396588,
396924,
500387,
582711,
595038,
651068,
766457,
103188,
136369,
134118,
233777,
619915,
690962,
730724,
732528,
818859,
891038,
 91933,
187939,
187993,
190304,
203754,
264280,
303948,
850917,
851221,
895357,
906637,
916122,
948838,
401450,
445335,
467864,
467997,
468600,
468893,
379087,
379134,
498805,
659633,
872277,
872845,
921193,
963612,
185331,
212158,
230689,
231911,
288633,
278885,
278936,
298106,
335737,
333995,
334031,
 12636,
 21689,
322961,
322987,
382962,
409646,
428309,
  5772,
400965,
472855,
545385,
565253,
597082,
603912,
800875,
780600,
289826,
310269,
317491,
891218,
890715,
910944,
 27328,
 27353,
217206,
218827,
221632,
260159,
260373,
320785,
324134,
446741,
446810,
131425,
231158,
264640,
264808,
226170,
258035,
261255,
269644,
325839,
540463,
607136,
622002,
223792,
245980,
266095,
347860,
240637,
327544,
342987,
434750,
437246,
437428,
438727,
153093,
217946,
255342,
256210,
268918,
320514,
337322,
361737,
424520,
487391,
488633,
509017,
513925,
574471,
576813,
393750,
407593,
407695,
432521,
481879,
873655,
990954,
992281,
393392,
417165,
403326,
416049,
412044,
501053,
524725,
536248,
545812,
546372,
884518,
169880,
660519,
661454,
667500,
789623,
808191,
808212,
 34707,
 47120,
 43439,
 43579,
129645,
148244,
351148,
624229,
884801,
175778,
311642,
420473,
423123,
526034,
583899,
946417,
997298,
999462,
692735,
699553,
720577,
769743,
770699,
482708,
488730,
733147,
746942,
782309,
792225,
792458,
 45055,
 62706,
 65200,
 82053,
 85495,
104783,
104945,
122016,
564169,
612137,
652462,
673472,
938456,
943428,
286505,
287376,
313239,
394825,
403067,
421136,
421613,
428673,
431059,
630031,
639744,
705764,
671515,
676321,
682587,
683992,
 27028,
 31202,
 60652,
 87556,
100933,
126544,
126564,
666509,
695952,
712782,
718708,
 19775,
 33665,
 88101,
120035,
888452,
858988,
685815,
735111,
735162,
735680,
740512,
744606,
749404,
748210,
755252,
530345,
530479,
546530,
546778,
560978,
561035,
567167,
575245,
842759,
855171,
856810,
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
for c in selectedComponents :
  c.splitFactor *= 3

sequence = cfg.Sequence( [
    eventSelector,
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
    treeProducer,
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

test = 1    # test = 0 run on batch, test = 1 run locally
if test == 1:
    #comp = WJets
    comp = HiggsVBF125
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
