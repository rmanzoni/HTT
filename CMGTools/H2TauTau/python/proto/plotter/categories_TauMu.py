import copy

from CMGTools.H2TauTau.proto.plotter.categories_common import *
from CMGTools.H2TauTau.proto.plotter.cut import * 

from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X

pt1 = 20
pt2 = 17 # 2011
if cmsswIs52X():
    pt2 = 20 # 2012, check that

#inc_sig_tau = Cut('l1_looseMvaIso>0.5 && (l1_EOverp>0.2 || l1_decayMode!=0) && l1_againstMuonTight>0.5 && l1_againstElectronLoose>0.5 && l1_dxy<0.045 && l1_dz<0.2 && l1_pt>{pt1}'.format(pt1=pt1))
inc_sig_tau = Cut('l1_looseMvaIso>0.5 && l1_againstMuonTight>0.5 && l1_againstElectronLoose>0.5 && l1_dxy<0.045 && l1_dz<0.2 && l1_pt>{pt1}'.format(pt1=pt1))
inc_sig_mu = Cut('l2_relIso05<0.1 && l2_tightId>0.5 && l2_dxy<0.045 && l2_dz<0.2 && l2_pt>{pt2}'.format(pt2=pt2))
inc_sig = inc_sig_mu & inc_sig_tau


def cutstr_signal():
    return inc_sig

def cutstr_rlxmuiso(cutstr, muIsoCut):
    '''WARNING: assumes mu iso cut is 0.1'''
    return cutstr.replace( 'l2_relIso05<0.1',
                           'l2_relIso05<{cut}'.format(cut=muIsoCut) )

def cutstr_rlxtauiso(cutstr, tauIsoCut):
    '''WARNING: assumes mu iso cut is 0.1'''
    return cutstr.replace('l1_looseMvaIso>0.5',
                          'l1_rawMvaIso>{cut}'.format(cut=tauIsoCut) )

def cutstr_rlxtaumuiso(cutstr, tauIsoCut, muIsoCut):
    '''WARNING: assumes mu iso cut is 0.1'''
    cutstr = cutstr_rlxmuiso(cutstr, muIsoCut)
    return cutstr_rlxtauiso(cutstr, tauIsoCut)


cat_Inc_RlxMuIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05<1.0')
cat_Inc_RlxTauIso = str(inc_sig).replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>0.')
cat_Inc_RlxMuTauIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05<0.5').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>-0.5')
cat_Inc_AntiMuTauIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.1').replace('l1_looseMvaIso>0.5', 'l1_looseMvaIso<0.5')
cat_Inc_AntiMuTauIso_B = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>-0.75')

cat_Inc_AntiMuTauIsoJosh = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2 && l2_relIso05<0.5').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>0.7')
cat_Inc_AntiMuIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.1')
cat_Inc_AntiTauIso = str(inc_sig).replace('l1_looseMvaIso>0.5', 'l1_looseMvaIso<0.5')
cat_Inc_RlxMuTauIso_b = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05<0.5').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>0.5')
cat_Inc = str(inc_sig)

categories = {
    'Xcat_Inc_AntiMuTauIsoJoshX':cat_Inc_AntiMuTauIsoJosh,
    'Xcat_Inc_RlxMuIsoX':cat_Inc_RlxMuIso,
    'Xcat_Inc_RlxTauIsoX':cat_Inc_RlxTauIso,
    'Xcat_IncX':cat_Inc,
    }

categories.update( categories_common )
