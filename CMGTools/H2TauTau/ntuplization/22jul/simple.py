import ROOT
from DataFormats.FWLite import Events, Handle
import math
#import array
#from tdrstyle import setTDRStyle

def deltaPhi(phi1, phi2):
     PHI = abs(phi1-phi2)
     if (PHI<=3.14159265):
         return PHI
     else:
         return 2*3.14159265-PHI

def deltaR(eta1, phi1, eta2, phi2) :
    deta = eta1-eta2
    dphi = deltaPhi(phi1,phi2)
    return math.sqrt(deta*deta + dphi*dphi)

def histograms():
    filename = 'root://eoscms//eos/cms/store/cmst3/user/manzoni/CMG/TTJets_FullLeptMGDecays_8TeV-madgraph/StoreResults-Summer12_DR53X_PU_S10_START53_V7A_v1_ReplaceRecMuons_RHembedded_trans1_tau132_pthad1_30had2_30_v1-f456bdbb960236e5c696adfe9b04eaae/USER/V5_B/PAT_CMG_V5_16_0/HTT_22Jul_manzoni_Nom/diTau_fullsel_tree_CMG_7.root'
    events = Events(filename)

    genfilterHandle = Handle('GenFilterInfo')
    genfilterLabel  = ('generator', 'minVisPtFilter', 'EmbeddedRECO')

    hltHandle = Handle('edm::TriggerResults')
    hltLabel  = ('TriggerResults','','HLT')

    
    import pdb ; pdb.set_trace()

    for event in events:
        event.getByLabel(genfilterLabel, genfilterHandle)
        genfilter = genfilterHandle.product()
        print genfilter.filterEfficiency()


        event.getByLabel(hltLabel, hltHandle)
        hlt = hltHandle.product()
        print hlt
        import pdb ; pdb.set_trace()

histograms()