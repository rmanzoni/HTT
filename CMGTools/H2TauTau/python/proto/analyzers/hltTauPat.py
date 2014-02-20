import operator
import math
from CMGTools.RootTools.analyzers.DiLeptonAnalyzer     import DiLeptonAnalyzer
from CMGTools.RootTools.fwlite.AutoHandle              import AutoHandle
from CMGTools.RootTools.physicsobjects.DiObject        import TauMuon, DiObject
from CMGTools.RootTools.physicsobjects.PhysicsObjects  import Tau, Muon, GenParticle
from CMGTools.RootTools.physicsobjects.HTauTauElectron import HTauTauElectron as Electron
from ROOT import TH1F, TFile

class hltTauPat( DiLeptonAnalyzer ):

    DiObjectClass     = TauMuon
    LeptonClass       = Muon
    OtherLeptonClass  = Electron
    OtherLeptonClass2 = Tau

    histos = {}
    histos['m_pt' ]        = TH1F('m_pt'        ,'m_pt'        ,30, 0,150)     
    histos['m_eta']        = TH1F('m_eta'       ,'m_eta'       ,24,-3,3  )     
    histos['t_pt' ]        = TH1F('t_pt'        ,'t_pt'        ,30, 0,150)     
    histos['t_eta']        = TH1F('t_eta'       ,'t_eta'       ,24,-3,3  )     
    histos['t_muovtx_pt' ] = TH1F('t_muovtx_pt' ,'t_muovtx_pt' ,30, 0,150)     
    histos['t_muovtx_eta'] = TH1F('t_muovtx_eta','t_muovtx_eta',24,-3,3  )     
    histos['t_onlvtx_pt' ] = TH1F('t_onlvtx_pt' ,'t_onlvtx_pt' ,30, 0,150)     
    histos['t_onlvtx_eta'] = TH1F('t_onlvtx_eta','t_onlvtx_eta',24,-3,3  )     

    def declareHandles(self):

        super(hltTauPat, self).declareHandles()
        self.handles['isolatedTaus'            ] = AutoHandle( 'isolatedTaus'               , 'std::vector<pat::Tau>'           )
        self.handles['selectedHltPatTausNP'    ] = AutoHandle( 'selectedHltPatTausNP'       , 'std::vector<pat::Tau>'           )
        self.handles['selectedHltPatTausOnlNP' ] = AutoHandle( 'selectedHltPatTausOnlNP'    , 'std::vector<pat::Tau>'           )
        self.handles['offlinePrimaryVertices'  ] = AutoHandle( 'offlinePrimaryVertices'     , 'std::vector<reco::Vertex>'       )
        self.handles['hltIsoMuonVertex'        ] = AutoHandle( 'hltIsoMuonVertex'           , 'std::vector<reco::Vertex>'       )
        self.handles['hltOnlinePrimaryVertices'] = AutoHandle( 'hltOnlinePrimaryVertices'   , 'std::vector<reco::Vertex>'       )
        self.handles['hltPixelVertices'        ] = AutoHandle( 'hltPixelVertices'           , 'std::vector<reco::Vertex>'       )
        self.handles['isolatedMuons'           ] = AutoHandle( 'isolatedMuons'              , 'std::vector<pat::Muon>'          )
        self.handles['patMETsPF'               ] = AutoHandle( 'patMETsPF'                  , 'std::vector<pat::MET>'           )
        self.handles['selectedDiTaus'          ] = AutoHandle( 'selectedDiTaus'             , 'vector<reco::CompositeCandidate>')
        
        try    : del self.handles['cmgTriggerObjectSel']
        except : pass
        
    def buildLeptons(self, cmgLeptons, event):
        '''Build muons for veto, associate best vertex, select loose ID muons.
        The loose ID selection is done to ensure that the muon has an inner track.'''
        leptons = []
        for index, lep in enumerate(cmgLeptons):
            #return map( self.__class__.LeptonClass, cmgLeptons )
            pyl = self.__class__.LeptonClass(lep)
            #pyl.associatedVertex = event.goodVertices[0]
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

      self.readCollections( iEvent )

      event.ditau           = self.handles['selectedDiTaus'].product()
      event.met             = self.handles['patMETsPF'     ].product()

      event.offvtx          = self.handles['offlinePrimaryVertices'  ].product()
      event.muovtx          = self.handles['hltIsoMuonVertex'        ].product()
      event.onlvtx          = self.handles['hltOnlinePrimaryVertices'].product()
      event.pixvtx          = self.handles['hltPixelVertices'        ].product()

      event.taus            = self.handles['isolatedTaus'            ].product()
      event.hlt_taus_muovtx = self.handles['selectedHltPatTausNP'    ].product()
      event.hlt_taus_onlvtx = self.handles['selectedHltPatTausOnlNP' ].product()

      event.muons           = self.buildLeptons( self.handles['isolatedMuons'].product() , event )

      
      event.taus  = [ tau for tau in event.taus
                          if self.testLeg1ID (tau) and self.testLeg1Iso(tau) ]
                             
      event.muons = [ mu  for mu in event.muons
                          if self.testLeg2ID (mu)  and self.testLeg2Iso(mu)  ]
      
      if len(event.taus) != 1 or len(event.muons) != 1 : return False
      
      #print len(event.muons)
      #print len(event.taus )
      
      event.mu  = event.muons[0]
      event.tau = event.taus [0]
      
      if event.mu.pt()  < 20 : return False
      if event.tau.pt() < 25 : return False
      if abs(event.mu.pt()) > 2.1 : return False
      if abs(event.mu.pt()) > 2.1 : return False
      
      #import pdb ; pdb.set_trace()
            
      self.__class__.histos['m_pt' ].Fill(event.muons[0].pt())
      self.__class__.histos['m_eta'].Fill(event.muons[0].eta())
      self.__class__.histos['t_pt' ].Fill(event.taus[0].pt())
      self.__class__.histos['t_eta'].Fill(event.taus[0].eta())

      #if self.matchToOffline(event.hlt_taus_muovtx, event.tau) :
      #  event.tau.hlt_tau_muovtx = self.matchToOffline(event.hlt_taus_muovtx, event.tau)
      #else : return False
      #
      #if self.matchToOffline(event.hlt_taus_onlvtx, event.tau) :
      #  event.tau.hlt_tau_onlvtx = self.matchToOffline(event.hlt_taus_onlvtx, event.tau)
      #else : return False

      #self.__class__.histos['t_muovtx_pt' ].Fill(event.tau.hlt_tau_muovtx.pt())
      #self.__class__.histos['t_muovtx_eta'].Fill(event.tau.hlt_tau_muovtx.eta())
      #self.__class__.histos['t_onlvtx_pt' ].Fill(event.tau.hlt_tau_onlvtx.pt())
      #self.__class__.histos['t_onlvtx_eta'].Fill(event.tau.hlt_tau_onlvtx.eta())

      try :
        self.__class__.histos['t_muovtx_pt' ].Fill(event.hlt_taus_muovtx[0].pt())
        self.__class__.histos['t_muovtx_eta'].Fill(event.hlt_taus_muovtx[0].eta())
        self.__class__.histos['t_onlvtx_pt' ].Fill(event.hlt_taus_onlvtx[0].pt())
        self.__class__.histos['t_onlvtx_eta'].Fill(event.hlt_taus_onlvtx[0].eta())
      except :
        pass
      
      return True




    def write(self):        
      super(DiLeptonAnalyzer, self).write()
      #import pdb ; pdb.set_trace()
      fname = '/'.join([self.dirName,self.cfg_ana.filename])
      outfile = TFile.Open(fname,'recreate')   
      outfile.cd()
      for key, value in self.__class__.histos.items() :
      #for hist in self.__class__.histos :
        value.Write()

    def testLeg1ID(self, tau):
        # JAN: revert back to old muon rejection (Jose HN)
        return tau.tauID("againstMuonTight")     > 0.5 and \
               tau.tauID("againstElectronLoose") > 0.5 and \
               self.testVertex( tau )
        

    def testLeg1Iso(self, tau):
        '''if isocut is None, returns true if three-hit iso cut is passed.
        Otherwise, returns true if iso MVA > isocut.'''
        return tau.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") < self.cfg_ana.iso_cut_tau


    def testVertex(self, lepton):
        '''Tests vertex constraints, for mu and tau'''
        return True
        #return abs(lepton.dxy()) < 0.045 and \
        #       abs(lepton.dz()) < 0.2 


    def testLeg2ID(self, muon):
        '''Tight muon selection, no isolation requirement'''
        #return muon.tightId() and self.testVertex( muon )
        return muon.isTrackerMuon()             and \
               muon.isGlobalMuon()              and \
               muon.normChi2() < 10             and \
               muon.numberOfValidHits() > 0     and \
               muon.numberOfMatchedStations()>1 
               ## muon.trackerLayersWithMeasurement() > 5 ### tracks not saved by Michal!
               ## muon.sourcePtr().innerTrack().hitPattern().numberOfValidPixelHits()>0 and ### tracks not saved by Michal!
               

    def testLeg2Iso(self, muon):
        '''Tight muon selection, with isolation requirement'''
        ## RM: followed this https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId
        ## but DeltaBeta correction should be implemented...
        sumiso  = 0.
        sumiso += muon.pfIsolationR04().sumChargedHadronPt
        sumiso += muon.pfIsolationR04().sumNeutralHadronEt
        sumiso += muon.pfIsolationR04().sumPhotonEt
        
        return sumiso / muon.pt() < self.cfg_ana.iso_cut_muon
        #return muon.relIsoAllChargedDB05()<self.cfg_ana.iso_cut_muon


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


    def bestDiLepton(self, muons, taus):
        '''Returns the best diLepton (1st precedence opposite-sign, 2nd precedence
        highest pt1 + pt2).'''
        
        osDiLeptons = []
        for mu in muons :
          for tau in taus :
            if mu.charge() != tau.charge() :
              import pdb ; pdb.set_trace()
              dil = DiObject()
              dil.tau = tau
              dil.mu  = mu
              osDiLeptons.append(dil)
              
        #osDiLeptons = [dl for dl in diLeptons if dl.leg1().charge() != dl.leg2().charge()]

        

        if osDiLeptons:
            return max( osDiLeptons, key=operator.methodcaller( 'sumPt' ) )
        else:
            return osDiLeptons


    def matchToOffline(self, onlineParticles, offlineParticle, deltaRmax=0.5):
      matched = 0
      for part in onlineParticles :
        if self.deltaR(part,offlineParticle) < deltaRmax :
          deltaRmax = self.deltaR(part,offlineParticle)
          matched = part
      
      if matched : return matched
      else       : return False

      
    def deltaPhi(self, phi1, phi2):
      PHI = abs(phi1-phi2)
      if (PHI<=3.14159265):
        return PHI
      else:
        return 2*3.14159265-PHI

    
    def deltaR(self, particle1, particle2) :
      eta1 = particle1.eta()
      phi1 = particle1.phi()
      eta2 = particle2.eta()
      phi2 = particle2.phi()
 
      deta = eta1-eta2
      dphi = self.deltaPhi(phi1,phi2)
      return math.sqrt(deta*deta + dphi*dphi)
         
      
      
      
      
      
      