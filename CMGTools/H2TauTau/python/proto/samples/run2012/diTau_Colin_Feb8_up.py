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
    '/AbelianZprime_hh_TauTauBB.*'                :'Radion',
    '/SUSYBB.*START53.*'                         :'HiggsSUSYBB',
    '/SUSYGluGluTo.*START53.*'                   :'HiggsSUSYGluGlu',
    '/VBF.*ToTauTau.*START53.*'                  :'HiggsVBF',
    '/GluGluTo.*ToTauTau.*START53.*'             :'HiggsGGH',
    '/WH_ZH_TTH_.*ToTauTau.*START53.*'           :'HiggsVH',
    '/VBF.*ToWW.*START53.*'                      :'HiggsVBFtoWW',
    '/GluGluTo.*ToWW.*START53.*'                 :'HiggsGGHtoWW',
    '/WH_ZH_TTH_.*ToWW.*START53.*'               :'HiggsVHtoWW',
    '/DYJets.*START53.*'                         :'DYJets',
    '/DY1Jets.*START53.*'                        :'DY1Jets',
    '/DY2Jets.*START53.*'                        :'DY2Jets',
    '/DY3Jets.*START53.*'                        :'DY3Jets',
    '/DY4Jets.*START53.*'                        :'DY4Jets',
    '/T_tW-channel.*START53.*'                   :'T_tW',
    '/Tbar_tW-channel.*START53.*'                :'Tbar_tW',
    '/WJetsToLNu.*START53.*v1.*'                 :'WJets' ,
    '/WJetsToLNu.*START53.*v2.*'                 :'WJets_v2' ,
    '/W1Jets.*START53.*V7A.*'                    :'W1Jets',
    '/W2Jets.*START53.*V7A.*'                    :'W2Jets',
    '/W3Jets.*START53.*V7A.*'                    :'W3Jets',
    '/W4Jets.*START53.*V7A.*'                    :'W4Jets',
    '/W1Jets.*START53.*V19.*'                    :'W1Jets_new',
    '/W2Jets.*START53.*V19.*'                    :'W2Jets_new',
    '/W3Jets.*START53.*V19.*'                    :'W3Jets_new',
    #'/TTJets.*START53.*'                         :'TTJets',
    '/TTJets_FullLeptMGDecays.*tauola.*START53.*':'TTJetsFullLept',
    '/TTJets_SemiLeptMGDecays.*tauola.*START53.*':'TTJetsSemiLept',
    '/TTJets_HadronicMGDecays.*START53.*'        :'TTJetsHadronic',
    '/DoubleMu.*Run2012A_22Jan2013_v1.*embedded' :'embed_Run2012A_22Jan2013_v1',
    '/DoubleMu.*Run2012B_22Jan2013_v1.*embedded' :'embed_Run2012B_22Jan2013_v1',
    '/DoubleMu.*Run2012C_22Jan2013_v1.*embedded' :'embed_Run2012C_22Jan2013_v1',
    '/DoubleMu.*Run2012D_22Jan2013_v1.*embedded' :'embed_Run2012D_22Jan2013_v1',
    '/Tau/Run2012A-22Jan2013-v1.*'               :'data_Run2012A_22Jan2013_v1',
    '/TauParked/Run2012B-22Jan2013-v1.*'         :'data_Run2012B_22Jan2013_v1',
    '/TauParked/Run2012C-22Jan2013-v1.*'         :'data_Run2012C_22Jan2013_v1',
    '/TauParked/Run2012D-22Jan2013-v1.*'         :'data_Run2012D_22Jan2013_v1',
    '/WW_TuneZ2.*START53.*'                      :'WW',
    '/WZ_TuneZ2.*START53.*'                      :'WZ',
    '/ZZ_TuneZ2.*START53.*'                      :'ZZ',
    '/WWJetsTo2L2Nu_TuneZ2.*START53.*'           :'WWJetsTo2L2Nu',     
    '/WZJetsTo2L2Q_TuneZ2.*START53.*'            :'WZJetsTo2L2Q',
    '/WZJetsTo3LNu_TuneZ2.*START53.*'            :'WZJetsTo3LNu',
    '/ZZJetsTo4L_TuneZ2.*START53.*'              :'ZZJetsTo4L',
    '/ZZJetsTo2L2Nu_TuneZ2.*START53.*'           :'ZZJetsTo2L2Nu',
    '/ZZJetsTo2L2Q_TuneZ2.*START53.*'            :'ZZJetsTo2L2Q',
    }

MC_list = copy.copy( mc_ewk )
MC_list.extend( mc_higgs )
MC_list.extend( mc_diboson )
MC_list.extend( mc_higgs_susy )
MC_list.extend( mc_radion )

allsamples0 = copy.copy( mc_radion )
pat0 = '%HTT_22Jul_manzoni_Up'

allsamples1 = copy.copy( data_parked_2012 )
allsamples1.extend( w_mc_ewk )
allsamples1.extend( t_mc_ewk )
allsamples1.extend( mc_diboson )
pat1 = '%HTT_22Jul_manzoni_Nom'

allsamples2 = copy.copy( mc_higgs )
allsamples2.extend( mc_higgs_susy )
allsamples2.extend( ztt_mc_ewk )
pat2 = '%HTT_24Jul_newTES_manzoni_Up' # with 26Aug
# pat2 = '%HTT_22Jul_manzoni_Up' # with 29Jul

allsamples3 = copy.copy( embed_list )
# pat3 = '%HTT_22Jul_manzoni_Up'
pat3 = '%HTT_24Jul_newTES_manzoni_Up'

connect( allsamples0, pat0, 'diTau.*root', aliases, cache=True, verbose=False)
connect( allsamples1, pat1, 'diTau.*root', aliases, cache=True, verbose=False)
connect( allsamples2, pat2, 'diTau.*root', aliases, cache=True, verbose=False)
connect( allsamples3, pat3, 'diTau.*root', aliases, cache=True, verbose=False)

cache = True
T_tW.files = getFiles('/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/PAT_CMG_V5_16_0/HTT_22Jul_manzoni_Nom', 'manzoni', 'diTau_fullsel.*root', cache)
T_tW.nGenEvents = 497658.

TTJetsHadronic.nGenEvents = 31223821.
TTJetsHadronic.xSection = 249.5*0.676*0.676*0.96

TTJets_emb.files = getFiles('/TTJets_FullLeptMGDecays_8TeV-madgraph/StoreResults-Summer12_DR53X_PU_S10_START53_V7A_v1_ReplaceRecMuons_RHembedded_trans1_tau132_pthad1_30had2_30_v1-f456bdbb960236e5c696adfe9b04eaae/USER/V5_B/PAT_CMG_V5_16_0/HTT_22Jul_manzoni_Nom', 'manzoni', 'diTau_fullsel.*root', cache)
TTJets_emb.nGenEvents = 4243699.
TTJets_emb.xSection = 249.5 * (1-0.676)*(1-0.676)*0.96

allsamples = copy.copy( allsamples1 )
allsamples.extend( allsamples2 )
allsamples.extend( allsamples3 )

for c in allsamples:
    c.splitFactor = int(100*splitFactor(c)/1)

# when stitching
WJets.nGenEvents += WJets_v2.nGenEvents


