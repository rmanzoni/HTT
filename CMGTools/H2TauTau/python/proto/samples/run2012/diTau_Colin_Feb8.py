import itertools
import copy
from CMGTools.RootTools.fwlite.Config     import printComps
from CMGTools.RootTools.utils.connect     import connect
from CMGTools.RootTools.utils.splitFactor import splitFactor

from CMGTools.H2TauTau.proto.samples.run2012.data_diTau import * 
from CMGTools.H2TauTau.proto.samples.run2012.embed      import *
from CMGTools.H2TauTau.proto.samples.run2012.ewk        import *
from CMGTools.H2TauTau.proto.samples.run2012.diboson    import *
from CMGTools.H2TauTau.proto.samples.run2012.higgs      import *
from CMGTools.H2TauTau.proto.samples.run2012.higgs_susy import *
from CMGTools.H2TauTau.proto.samples.run2012.radion     import *

from CMGTools.H2TauTau.proto.samples.run2012.triggers_diTau import *

aliases = {
#     '/AbelianZprime_hh_TauTauBB.*'                :'Radion',
#     '/SUSYBB.*START53.*'                        :'HiggsSUSYBB',
#     '/SUSYGluGluTo.*START53.*'                  :'HiggsSUSYGluGlu',
#     '/VBF.*ToTauTau.*START53.*'                 :'HiggsVBF',
#     '/GluGluTo.*ToTauTau.*START53.*'            :'HiggsGGH',
    '/WH_ZH_TTH_.*ToTauTau.*START53.*'          :'HiggsVH',
#     '/VBF.*ToWW.*START53.*'                     :'HiggsVBFtoWW',
#     '/GluGluTo.*ToWW.*START53.*'                :'HiggsGGHtoWW',
#     '/WH_ZH_TTH_.*ToWW.*START53.*'              :'HiggsVHtoWW',
#     '/DYJets.*START53.*'                        :'DYJets',
#     '/DY1Jets.*START53.*'                       :'DY1Jets',
#     '/DY2Jets.*START53.*'                       :'DY2Jets',
#     '/DY3Jets.*START53.*'                       :'DY3Jets',
#     '/DY4Jets.*START53.*'                       :'DY4Jets',
#     '/T_tW-channel.*START53.*'                  :'T_tW',
#     '/Tbar_tW-channel.*START53.*'               :'Tbar_tW',
#     '/WJetsToLNu.*START53.*'                    :'WJets',
#     '/WJetsToLNu.*START53.*v1.*'                :'WJets' ,
#     '/WJetsToLNu.*START53.*v2.*'                :'WJets_v2' ,
#     '/W1Jets.*START53.*V7A.*'                   :'W1Jets',
#     '/W2Jets.*START53.*V7A.*'                   :'W2Jets',
#     '/W3Jets.*START53.*V7A.*'                   :'W3Jets',
#     '/W4Jets.*START53.*V7A.*'                   :'W4Jets',
#     '/W1Jets.*START53.*V19.*'                   :'W1Jets_new',
#     '/W2Jets.*START53.*V19.*'                   :'W2Jets_new',
#     '/W3Jets.*START53.*V19.*'                   :'W3Jets_new',
#       'TTJets_FullLeptMGDecays_8TeV-madgraph/StoreResults-Summer12_DR53X_PU_S10_START53_V7A_v1_ReplaceRecMuons_RHembedded_trans1_tau132_pthad1_30had2_30_v1-f456bdbb960236e5c696adfe9b04eaae.*':'TTJets_emb',
#     '/TTJets.*START53.*'                        :'TTJets',
#     '/TTJets_FullLeptMGDecays.*START53.*'       :'TTJetsFullLept',
#     '/TTJets_SemiLeptMGDecays.*START53.*'       :'TTJetsSemiLept',
#     '/TTJets_HadronicMGDecays.*START53.*'       :'TTJetsHadronic',
#     '/DoubleMu.*Run2012A_22Jan2013_v1.*embedded':'embed_Run2012A_22Jan2013_v1',
#     '/DoubleMu.*Run2012B_22Jan2013_v1.*embedded':'embed_Run2012B_22Jan2013_v1',
#     '/DoubleMu.*Run2012C_22Jan2013_v1.*embedded':'embed_Run2012C_22Jan2013_v1',
#     '/DoubleMu.*Run2012D_22Jan2013_v1.*embedded':'embed_Run2012D_22Jan2013_v1',
#     '/Tau/Run2012A-22Jan2013-v1.*'              :'data_Run2012A_22Jan2013_v1',
#     '/TauParked/Run2012B-22Jan2013-v1.*'        :'data_Run2012B_22Jan2013_v1',
#     '/TauParked/Run2012C-22Jan2013-v1.*'        :'data_Run2012C_22Jan2013_v1',
#     '/TauParked/Run2012D-22Jan2013-v1.*'        :'data_Run2012D_22Jan2013_v1',
#     '/WW_TuneZ2.*START53.*'                     :'WW',
#     '/WZ_TuneZ2.*START53.*'                     :'WZ',
#     '/ZZ_TuneZ2.*START53.*'                     :'ZZ',
#     '/WWJetsTo2L2Nu_TuneZ2.*START53.*'          :'WWJetsTo2L2Nu',     
#     '/WZJetsTo2L2Q_TuneZ2.*START53.*'           :'WZJetsTo2L2Q',
#     '/WZJetsTo3LNu_TuneZ2.*START53.*'           :'WZJetsTo3LNu',
#     '/ZZJetsTo4L_TuneZ2.*START53.*'             :'ZZJetsTo4L',
#     '/ZZJetsTo2L2Nu_TuneZ2.*START53.*'          :'ZZJetsTo2L2Nu',
#     '/ZZJetsTo2L2Q_TuneZ2.*START53.*'           :'ZZJetsTo2L2Q',
    }

MC_list = copy.copy( mc_ewk )
MC_list.extend( mc_higgs )
MC_list.extend( mc_diboson )
MC_list.extend( mc_higgs_susy )
MC_list.extend( mc_radion )

allsamples = copy.copy( data_parked_2012 )
allsamples.extend( MC_list )
allsamples.extend( embed_list )

# import pdb ; pdb.set_trace()
# pat = '%HTT_30May_noRecoil_manzoni_Nom'
# pat = '%HTT_3May_manzoni_Down'
# pat = '%HTT_6Jun_sync_recoil_manzoni_Nom'
# pat = '%HTT_6Jun_sync_recoil_fix2_manzoni_Nom'
# pat = '%HTT_13Jun_manzoni_Nom'
# pat = '%HTT_27Jun_manzoni_test'


# scale = 'Nom'
# pat1 = '%HTT_23Jun_manzoni_'
# pat2 = '%16_0_B/HTT_23Jun_manzoni_'
# pat1 += scale
# pat2 += scale


# pat = '%HTT_3Jul_noTauEScorr_manzoni_Nom'
# pat = '%HTT_23Jun_manzoni_Nom'
# pat = '%HTT_8Jul_manzoni_Up'
# pat = '%HTT_5Aug_manzoni_Nom'
# pat = '%HTT_8Jul_manzoni_Nom_vegaIntegration'
# pat = '%HTT_5Sep_L1study_manzoni_Nom'
####################################################
# pat = '%HTT_22Jul_manzoni_Nom' ## for most of bkg
pat = '%HTT_24Jul_newTES_manzoni_Down' ## for DY & signal
connect( allsamples, pat, 'diTau.*root', aliases, cache=True, verbose=False)

# cache = False
# T_tW.files = getFiles('/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/'+pat.replace('%',''), 'manzoni', 'diTau_fullsel.*root', cache)

# cache = False
# TTJetsFullLept.files = getFiles('/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/V5_B/PAT_CMG_V5_16_0/'+pat.replace('%',''), 'manzoni', 'diTau_fullsel.*root', cache)

allsamples.extend( embed_list )


# dy_nevents = [ DYJets.nGenEvents ,
#                DY1Jets.nGenEvents,
#                DY2Jets.nGenEvents,
#                DY3Jets.nGenEvents,
#                DY4Jets.nGenEvents
#                ]
#                
# for dy in ztt_mc_ewk:
#     dy.nevents = dy_nevents
# 
# 
# w_nevents = [ WJets.nGenEvents ,
#               W1Jets.nGenEvents,
#               W2Jets.nGenEvents,
#               W3Jets.nGenEvents,
#               W4Jets.nGenEvents
#               ]
#                
# for w in w_mc_ewk:
#     w.nevents = w_nevents

for c in allsamples:
    c.splitFactor = int(1*splitFactor(c)/1)

# when stitching
WJets.nGenEvents += WJets_v2.nGenEvents
































'''
aliases.update({
    '/Tau/Run2012A-13Jul2012-v1.*'         :'data_Run2012A_13Jul2012_v1',       
    '/Tau/Run2012A-recover-06Aug2012-v1.*' :'data_Run2012A_recover_06Aug2012_v1',
    '/Tau/Run2012B-13Jul2012-v1.*'         :'data_Run2012B_13Jul2012_v1',       
    '/Tau/Run2012C-24Aug2012-v1.*'         :'data_Run2012C_24Aug2012_v1',       
    '/Tau/Run2012C-PromptReco-v2.*'        :'data_Run2012C_PromptReco_v2',      
    '/Tau/Run2012D-PromptReco-v1.*'        :'data_Run2012D_PromptReco_v1',       
    '/DoubleMu/StoreResults-DoubleMu_Run2012A-recover_06Aug2012_v1.*':'embed_Run2012A_recover_06Aug2012_v1',  ## missing in summer13
    '/DoubleMu/StoreResults-DoubleMu_Run2012A_13Jul2012_v1.*' :'embed_Run2012A_13Jul2012_v1',
    '/DoubleMu/StoreResults-DoubleMu_Run2012B_13Jul2012_v4.*' :'embed_Run2012B_13Jul2012_v4',
    '/DoubleMu/StoreResults-DoubleMu_Run2012C_24Aug2012_v1.*' :'embed_Run2012C_24Aug2012_v1',
    '/DoubleMu/StoreResults-Run2012C_PromptReco_v2.*'         :'embed_Run2012C_PromptReco_v2', 
    '/DoubleMu/StoreResults-DoubleMu_2012D_PromptReco_v1.*'   :'embed_2012D_PromptReco_v1',
    '/DoubleMu/StoreResults-DoubleMu_Run2012C_PromptReco_v2.*'       :'embed_Run2012C_PromptReco_v2', ## till moriond
    '/WWJetsTo2L2Nu.*START53.*':'WWJetsTo2L2Nu',
    '/WZJetsTo2L2Q.*START53.*' :'WZJetsTo2L2Q',
    '/WZJetsTo3LNu.*START53.*' :'WZJetsTo3LNu',
    '/ZZJetsTo2L2Nu.*START53.*':'ZZJetsTo2L2Nu',
    '/ZZJetsTo2L2Q.*START53.*' :'ZZJetsTo2L2Q',
    '/ZZJetsTo4L.*START53.*'   :'ZZJetsTo4L',
    })
'''

