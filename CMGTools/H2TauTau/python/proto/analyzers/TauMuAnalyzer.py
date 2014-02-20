import operator
from CMGTools.RootTools.analyzers.DiLeptonAnalyzer import DiLeptonAnalyzer
from CMGTools.RootTools.fwlite.AutoHandle import AutoHandle
from CMGTools.RootTools.physicsobjects.DiObject import TauMuon
from CMGTools.RootTools.physicsobjects.PhysicsObjects import Muon, GenParticle
from CMGTools.RootTools.physicsobjects.HTauTauElectron import HTauTauElectron as Electron
from CMGTools.RootTools.utils.TriggerMatching import selTriggerObjects
from CMGTools.RootTools.physicsobjects.PhysicsObjects import TriggerObject
from CMGTools.RootTools.utils.TriggerMatching import triggerMatched
from CMGTools.H2TauTau.triggerMap import pathsAndFilters

class TauMuAnalyzer( DiLeptonAnalyzer ):

    DiObjectClass = TauMuon
    LeptonClass = Muon
    OtherLeptonClass = Electron

    def declareHandles(self):
        super(TauMuAnalyzer, self).declareHandles()
        self.handles['diLeptons']               = AutoHandle( 'cmgTauMuCorSVFitFullSel'   , 'std::vector<cmg::DiTauObject<cmg::Tau,cmg::Muon>>')
        self.handles['otherLeptons']            = AutoHandle( 'cmgElectronSel'            , 'std::vector<cmg::Electron>'                       )
        self.handles['leptons']                 = AutoHandle( 'cmgMuonSel'                , 'std::vector<cmg::Muon>'                           )
        self.mchandles['genParticles']          = AutoHandle( 'genParticlesPruned'        , 'std::vector<reco::GenParticle>'                   )
        self.handles['triggerResults']          = AutoHandle( ('TriggerResults','','HLT') , 'edm::TriggerResults'                              )
        self.handles['cmgTriggerObjectListSel'] = AutoHandle( 'cmgTriggerObjectListSel'   , 'std::vector<cmg::TriggerObject>'                  )
        
        self.triggers=[
          'HLT_IsoMu24_eta2p1_v13',
          'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk5_eta2p1_v7',
          'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v2',
        ]

    def buildDiLeptons(self, cmgDiLeptons, event):
        '''Build di-leptons, associate best vertex to both legs,
        select di-leptons with a tight ID muon.
        The tight ID selection is done so that dxy and dz can be computed
        (the muon must not be standalone).
        '''
        diLeptons = []
        for index, dil in enumerate(cmgDiLeptons):
            pydil = self.__class__.DiObjectClass(dil)
            pydil.leg1().associatedVertex = event.goodVertices[0]
            pydil.leg2().associatedVertex = event.goodVertices[0]
            if not self.testLeg2( pydil.leg2(), 99999 ):
                continue
            #if hasattr(self.cfg_ana, 'mvametsigs'):
            #    pydil.mvaMetSig = mvaMetSig = self.handles['mvametsigs'].product()[index]
            pydil.mvaMetSig = mvaMetSig = dil.metSig()
            diLeptons.append( pydil )
        return diLeptons


    def buildLeptons(self, cmgLeptons, event):
        '''Build muons for veto, associate best vertex, select loose ID muons.
        The loose ID selection is done to ensure that the muon has an inner track.'''
        leptons = []
        for index, lep in enumerate(cmgLeptons):
            pyl = self.__class__.LeptonClass(lep)
            pyl.associatedVertex = event.goodVertices[0]
            leptons.append( pyl )
        return leptons


    def buildOtherLeptons(self, cmgOtherLeptons, event):
        '''Build electrons for third lepton veto, associate best vertex.
        '''
        otherLeptons = []
        for index, lep in enumerate(cmgOtherLeptons):
            pyl = self.__class__.OtherLeptonClass(lep)
            pyl.associatedVertex = event.goodVertices[0]
            otherLeptons.append( pyl )
        return otherLeptons


    def process(self, iEvent, event):

        #if event.eventId == 70370:
        #    print 'EVENT', event.eventId
        result = super(TauMuAnalyzer, self).process(iEvent, event)

        # import pdb; pdb.set_trace()

        if result is False:
            # trying to get a dilepton from the control region.
            # it must have well id'ed and trig matched legs,
            # di-lepton and tri-lepton veto must pass
            result = self.selectionSequence(event, fillCounter=False,
                                            leg1IsoCut = -9999,
                                            leg2IsoCut = 9999)
            if result is False:
                # really no way to find a suitable di-lepton,
                # even in the control region
                return False
            event.isSignal = False
        else:
            event.isSignal = True
       
        event.genMatched = None
        if self.cfg_comp.isMC:
            # print event.eventId
            genParticles = self.mchandles['genParticles'].product()
            event.genParticles = map( GenParticle, genParticles)
            leg1DeltaR, leg2DeltaR = event.diLepton.match( event.genParticles ) 
            if leg1DeltaR>-1 and leg1DeltaR < 0.1 and \
               leg2DeltaR>-1 and leg2DeltaR < 0.1:
                event.genMatched = True
            else:
                event.genMatched = False
       
        cross = False
        
	triggerResults = self.handles['triggerResults'].product()
        triggerNames = iEvent._event.triggerNames(triggerResults)
	for trig in self.triggers:
          index = triggerNames.triggerIndex(trig)
          if index >= triggerNames.size():
            trigres = -1
          else:
            trigres = triggerResults.accept(index)
            if trig == 'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk5_eta2p1_v7' and trigres:
              trigObjs = map( TriggerObject, self.handles['cmgTriggerObjectListSel'].product())
              event.monitorTriggerObjects = selTriggerObjects( trigObjs, trig )
              #for obj in self.handles['cmgTriggerObjectListSel'].product() : 
              #  print obj.pt()
              #  for name in obj.getSelectionNames() :
              #    print name
              ## leg1 Tau leg2 Mu 
              #import pdb ; pdb.set_trace()
              l1match, index1 = self.trigMatched2(event, event.diLepton.leg1() , 'leg1', trig, trigObj=event.monitorTriggerObjects)
              l2match, index2 = self.trigMatched2(event, event.diLepton.leg2() , 'leg2', trig, trigObj=event.monitorTriggerObjects)
              import pdb ; pdb.set_trace()

              if (not l1match or not l2match or event.monitorTriggerObjects[index1].pt()<35 ) :
                trigres = False

            if trig == 'HLT_IsoMu24_eta2p1_v13' and trigres:
              #import pdb ; pdb.set_trace()
              #l2match, dummy = self.trigMatched2(event, event.diLepton.leg2() , 'leg1', trig)
              #import pdb ; pdb.set_trace()
              #if (not l2match) :
              #  trigres = False
              pass
              
          setattr(event,trig,trigres)
        
        
        
                
        return True
        

    def testLeg1ID(self, tau):
        if tau.decayMode() == 0 and \
               tau.calcEOverP() < 0.2: #reject muons faking taus in 2011B
            return False
        #return tau.tauID("againstMuonTight2")>0.5 and \
        # JAN: revert back to old muon rejection (Jose HN)
        return tau.tauID("againstMuonLoose")>0.5 and \
               tau.tauID("againstElectronLoose")>0.5 and \
               self.testVertex( tau )
        

    def testLeg1Iso(self, tau, isocut):
        '''if isocut is None, returns true if three-hit iso cut is passed.
        Otherwise, returns true if iso MVA > isocut.'''
        if isocut is None:
            return tau.tauID('byCombinedIsolationDeltaBetaCorrRaw3Hits') < 1.5
        else:
            return tau.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < isocut


    def testVertex(self, lepton):
        '''Tests vertex constraints, for mu and tau'''
        return abs(lepton.dxy()) < 0.045 and \
               abs(lepton.dz()) < 0.2 


    def testLeg2ID(self, muon):
        '''Tight muon selection, no isolation requirement'''
        return muon.tightId() and \
               self.testVertex( muon )
               

    def testLeg2Iso(self, muon, isocut):
        '''Tight muon selection, with isolation requirement'''
        if isocut is None:
            isocut = self.cfg_ana.iso2
        return muon.relIsoAllChargedDB05()<isocut    


    def thirdLeptonVeto(self, leptons, otherLeptons, ptcut = 10, isocut = 0.3) :
        '''The tri-lepton veto. returns False if > 2 leptons (e or mu).'''
        vleptons = [lep for lep in leptons if
                    self.testLegKine(lep, ptcut=ptcut, etacut=2.4) and 
                    self.testLeg2ID(lep) and
                    self.testLeg2Iso(lep, isocut) ]
        # count electrons
        votherLeptons = [olep for olep in otherLeptons if 
                         self.testLegKine(olep, ptcut=ptcut, etacut=2.5) and \
                         olep.looseIdForTriLeptonVeto()           and \
                         self.testVertex( olep )           and \
                         olep.relIsoAllChargedDB05() < isocut
                        ]
        if len(vleptons) + len(votherLeptons)> 1:
            return False
        else:
            return True
        

    def leptonAccept(self, leptons):
        '''The di-lepton veto, returns false if > one lepton.
        e.g. > 1 mu in the mu tau channel'''
        looseLeptons = [muon for muon in leptons if
                        self.testLegKine(muon, ptcut=15, etacut=2.4) and
                        muon.isGlobalMuon() and
                        muon.isTrackerMuon() and
                        muon.sourcePtr().userFloat('isPFMuon') and
                        #COLIN Not sure this vertex cut is ok... check emu overlap
                        #self.testVertex(muon) and
                        # JAN: no dxy cut
                        abs(muon.dz()) < 0.2 and
                        self.testLeg2Iso(muon, 0.3)
                        ]
        isPlus = False
        isMinus = False
        # import pdb; pdb.set_trace()
        for lepton in looseLeptons:
            if lepton.charge()<0: isMinus=True
            elif lepton.charge()>0: isPlus=True
            else:
                raise ValueError('Impossible!')
        veto = isMinus and isPlus
        return not veto


    def bestDiLepton(self, diLeptons):
        '''Returns the best diLepton (1st precedence opposite-sign, 2nd precedence
        highest pt1 + pt2).'''
        # # FIXME - temporary TEST for bias
        # return max( diLeptons, key=operator.methodcaller( 'sumPt' ) )
        osDiLeptons = [dl for dl in diLeptons if dl.leg1().charge() != dl.leg2().charge()]
        if osDiLeptons:
            return max( osDiLeptons, key=operator.methodcaller( 'sumPt' ) )
        else:
            return max( diLeptons, key=operator.methodcaller( 'sumPt' ) )


    def trigMatched2(self, event, leg, legName, trigpath, trigObj=None):
        '''Returns true if the leg is matched to a trigger object as defined in the
        triggerMap parameter'''
        #import pdb ; pdb.set_trace
        path = trigpath
        if trigObj is None : triggerObjects = event.triggerObjects
        else               : triggerObjects = trigObj
        filters = pathsAndFilters[ path ]
        filter = None
        #import pdb ; pdb.set_trace
        if   legName == 'leg1':
            filter = filters[0]
            #import pdb ; pdb.set_trace
        elif legName == 'leg2':
            filter = filters[1]
            #import pdb ; pdb.set_trace
        else:
            raise ValueError( 'legName should be leg1 or leg2, not {leg}'.format(
                leg=legName )  )
        # the default dR2Max value is 0.3^2
        pdgIds = None
        if len(filter) == 2:
            filter, pdgIds = filter[0], filter[1]
            
        return triggerMatched(leg, triggerObjects, path, filter, dR2Max=0.5*0.5, dRMax=0.5, pdgIds=pdgIds, index=True )



