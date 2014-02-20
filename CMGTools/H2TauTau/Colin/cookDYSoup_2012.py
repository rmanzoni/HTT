# python cookDYSoup_2012.py /afs/cern.ch/work/m/manzoni/public/diTau22Jun/nom/DYJets /afs/cern.ch/work/m/manzoni/public/diTau22Jun/nom/DY1Jets /afs/cern.ch/work/m/manzoni/public/diTau22Jun/nom/DY2Jets /afs/cern.ch/work/m/manzoni/public/diTau22Jun/nom/DY3Jets /afs/cern.ch/work/m/manzoni/public/diTau22Jun/nom/DY4Jets
# python cookDYSoup_2012.py /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom/DYJets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom/DY1Jets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom/DY2Jets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom/DY3Jets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom/DY4Jets
# python cookDYSoup_2012.py /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom_dy_new/DYJets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom_dy_new/DY1Jets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom_dy_new/DY2Jets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom_dy_new/DY3Jets /afs/cern.ch/work/m/manzoni/public/diTau_22Jul/nom_dy_new/DY4Jets
# python cookDYSoup_2012.py /afs/cern.ch/work/m/manzoni/public/diTau_26Jul/nom/DYJets /afs/cern.ch/work/m/manzoni/public/diTau_26Jul/nom/DY1Jets /afs/cern.ch/work/m/manzoni/public/diTau_26Jul/nom/DY2Jets /afs/cern.ch/work/m/manzoni/public/diTau_26Jul/nom/DY3Jets /afs/cern.ch/work/m/manzoni/public/diTau_26Jul/nom/DY4Jets

# python cookDYSoup_2012.py /afs/cern.ch/work/m/manzoni/public/diTau_29Jul/nom_dy/DrellYann/DYJets /afs/cern.ch/work/m/manzoni/public/diTau_29Jul/nom_dy/DrellYann/DY1Jets /afs/cern.ch/work/m/manzoni/public/diTau_29Jul/nom_dy/DrellYann/DY2Jets /afs/cern.ch/work/m/manzoni/public/diTau_29Jul/nom_dy/DrellYann/DY3Jets /afs/cern.ch/work/m/manzoni/public/diTau_29Jul/nom_dy/DrellYann/DY4Jets

import copy
from CMGTools.RootTools.PyRoot import *
from CMGTools.RootTools.statistics.TreeNumpy import *

files = []

class Component(object):
    def __init__(self, name, numberForNaming = 99):
        self.name = name.rstrip('/')
        self.tree = None
        self.numberForNaming = numberForNaming
        self.attachTree()

    def attachTree(self):
        fileName = '{name}/H2TauTauTreeProducerTauTau/H2TauTauTreeProducerTauTau_tree.root'.format(name=self.name)
        #fileName = '{name}/H2TauTauTreeProducerTauTau/forStitching.root'.format(name=self.name)
        treeName = 'H2TauTauTreeProducerTauTau'
        self.file = TFile(fileName)
        self.tree = self.file.Get(treeName)
        self.tree.SetName('H2TauTauTreeProducerTauTau_{0:d}'.format(self.numberForNaming))


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    
class H2TauTauSoup(TreeNumpy):

    def __init__(self, name, title):
        super(H2TauTauSoup, self).__init__(name,title)
        self.var('DYJetWeight')
        # fraction of events with a given parton jet multiplicity, 
        # from the LO cross sections in prep:

        #  0j : (3503.71 - 561.0 - 181. - 51.1 - 23.04) / 3503.71 = 0.76706405495888652
        #  1j : 561.0 / 3503.71 = 0.16011599133489929
        #  2j : 181.0 / 3503.71 = 0.051659526616072676
        #  3j : 51.1  / 3503.71 = 0.014584540387189579
        #  4j : 23.04 / 3503.71 = 0.0065758867029520138


#         self.fractions = [ 
#             (3503.71 - 561.0 - 181. - 51.1 - 23.04) / 3503.71,
#             561.0 / 3503.71,
#             181.0 / 3503.71,
#             51.1  / 3503.71,
#             23.04 / 3503.71
#             ]

        self.fractions = [ 
            (2950. - 561.0 - 181. - 51.1 - 23.04) / 2950.,
            561.0 / 2950.,
            181.0 / 2950.,
            51.1  / 2950.,
            23.04 / 2950.
            ]

        # number of events in the inclusive sample, corrected for prod efficiency
        self.ninc = 30459503*0.997196
        # approximate number of events in each exclusive component of the inclusive sample
        self.Ninc = [frac * self.ninc for frac in self.fractions]

        # number of events in the excusive samples, corrected for prod efficiency
        self.Nexc = [
            0              , ## 30459503 inclusive
            24045248. * 0.999005 , #w/o weights
            21852156. * 1. , #w/o weights
            11015445. * 1. , #w/o weights
            6402827.  * 1.   #w/o weights
            ]

        self.DYJetWeights = []
        for nJets in range (5):
            self.DYJetWeights.append (self.Ninc[nJets] / ( self.Ninc[nJets] + self.Nexc[nJets]))
            print nJets, self.DYJetWeights[nJets]
        #import pdb ; pdb.set_trace()
# .... .... .... .... .... .... .... .... .... .... .... .... ....

    def importEntries(self, comp, nEntries=-1):
        print 'importing', comp.name
        tree = comp.tree
        for index, ie in enumerate(tree):
            if index%1000==0: print 'entry:', index
            # get the additional weight
            nJets = None
            for varName in self.vars:
                if not hasattr(ie, varName):
                    continue
                if varName == 'NUP':
                    val = getattr(ie, varName)
                    nJets = int(val-5)
            # fill all the variables
            for varName in self.vars:
                if not hasattr(ie, varName):
                    continue
                val = getattr(ie, varName)
                if varName == 'weight':
                    #print 'nJets:', nJets
                    #import pdb ; pdb.set_trace()
                    val = val * self.DYJetWeights[nJets]
                self.fill(varName, val)
            self.tree.Fill()
            if nEntries>0 and index+1>=nEntries:
                return 


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    
if __name__ == '__main__':

    # import sys
    import imp

    args = sys.argv[1:]

##     anaDir = args[0]
##     cfgFileName = args[1]
##     file = open( cfgFileName, 'r' )
##     cfg = imp.load_source( 'cfg', cfgFileName, file)

# call the function from the folder that contains the components
# arguments are: the inclusive component, the exclusive components in order

    components = []
    
    numberForNaming = 0
    incComp = Component( args[0], numberForNaming )
    numberForNaming = numberForNaming + 1  
    components.append( incComp )
    print 'Inclusive DYJets sample: ', incComp.name

    excNames = args[1:]
    for arg in excNames:
        print 'Exclusive DYJets sample: ', arg
        components.append( Component(arg, numberForNaming) )
        numberForNaming = numberForNaming + 1  
    
    soupFile = TFile('soupDYdb3h_parked.root','recreate')
    soup = H2TauTauSoup('H2TauTauTreeProducerTauTau', 'H2TauTauTreeProducerTauTau')
    soup.copyStructure( incComp.tree )

    for c in components:
        soup.importEntries (c)
#        soup.importEntries (c, nEntries = 20)

    soupFile.Write()
    soupFile.Close()
