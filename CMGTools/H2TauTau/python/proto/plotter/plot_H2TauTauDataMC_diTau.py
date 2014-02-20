import numpy
import math
import inspect
import os
import imp
from ROOT import gROOT, gStyle, TText, TLatex
from numpy import array
from os import path
from copy import deepcopy
from CMGTools.RootTools.Style import formatPad,Style
from CMGTools.H2TauTau.proto.HistogramSet import histogramSet
from CMGTools.H2TauTau.proto.plotter.cuts_diTau                import *
from CMGTools.H2TauTau.proto.plotter.titles_diTau              import xtitles
from CMGTools.H2TauTau.proto.plotter.H2TauTauDataMC_diTau      import *
from CMGTools.H2TauTau.proto.plotter.QCDEstimation_diTau       import *
from CMGTools.H2TauTau.proto.plotter.DYEstimate_diTau          import *
from CMGTools.H2TauTau.proto.plotter.SaveHistograms_diTau      import *
from CMGTools.H2TauTau.proto.plotter.PrepareDictionaries_diTau import *

def blind(var, varToblind, plot, min, max ) :
  if var==varToblind :
   for bin in range(plot.Hist("Data").weighted.GetNbinsX()):
     if ( plot.Hist("Data").weighted.GetBinCenter(bin+1)>min and plot.Hist("Data").weighted.GetBinCenter(bin+1)<max ):
        plot.Hist("Data").weighted.SetBinContent(bin+1,-1)

def printYields(region, plots, mass=-1, fileout=None, qcd=False, susy=False, radion=False) :
  if fileout != None : print >> fileout, 'Yields in '+region
  else               : print             'Yields in '+region
  contributions = ["Data" ,"DYJets" ,"DYJets_ZL" ,"DYJets_ZJ", "WJets",'Tbar_tW','T_tW','TTJetsFullLept','TTJetsSemiLept','TTJetsHadronic','WWJetsTo2L2Nu','WZJetsTo2L2Q','WZJetsTo3LNu','ZZJetsTo4L','ZZJetsTo2L2Nu','ZZJetsTo2L2Q'] ## , "WJets_Fakes","TTJets" , "WW", 'ZZ', 'WZ'
  if qcd != False : contributions.extend(['QCDdata'])
  if mass!= -1 and not susy and not radion: 
    #contributions.extend(['HiggsGGH' +str(mass),'HiggsVBF'+str(mass),'HiggsVH' +str(mass)])
    contributions.extend(['HiggsGGH' +str(mass),'HiggsVBF'+str(mass),'HiggsWH' +str(mass),'HiggsZH' +str(mass),'HiggsttH' +str(mass)])
  if mass!= -1 and susy and not radion: 
    #contributions.extend(['HiggsGGH125','HiggsVBF125','HiggsVH125','TTJets_emb'])
    contributions.extend(['HiggsGGH125','HiggsVBF125','HiggsWH125','HiggsZH125','HiggsttH125','TTJets_emb'])
  if mass!= -1 and susy and not radion: 
    contributions.extend(['HiggsSUSYBB' +str(mass),'HiggsSUSYGluGlu'+str(mass)])
  if mass!= -1 and not susy and radion: 
    contributions.extend(['Radion' +str(mass)])
  for c in contributions :
    if fileout != None : print >> fileout, c+':'+' '*(15-len(c)),"{0:.2f}".format(round(integralAndError(plots.Hist(c).weighted)[0],2)) ,' '*(9-len("{0:.2f}".format(round(plots.Hist(c).Integral(),2))))+"+-","{0:.2f}".format(round(integralAndError(plots.Hist(c).weighted)[1],2))
    else               : print             c+':'+' '*(15-len(c)),"{0:.2f}".format(round(integralAndError(plots.Hist(c).weighted)[0],2)) ,' '*(9-len("{0:.2f}".format(round(plots.Hist(c).Integral(),2))))+"+-","{0:.2f}".format(round(integralAndError(plots.Hist(c).weighted)[1],2))

def removekey(dictionary, key):
  r = dict(dictionary)
  del r[key]
  return r

def shrinkEmbed(selComps, weights, abcd='') :
  '''
  pass the name of the sample to be dropped (useful for ABC vs D comparison)
  A ==> remove embed_Run2012A_13Jul2012_v1 and embed_Run2012A_recover_06Aug2012_v1
  B ==> remove embed_Run2012B_13Jul2012_v4
  C ==> remove embed_Run2012C_24Aug2012_v1 and embed_Run2012C_PromptReco_v2
  D ==> remove embed_2012D_PromptReco_v1
  '''
  
  dic = { 'A':['embed_Run2012A_22Jan2013_v1'],
          'B':['embed_Run2012B_22Jan2013_v1'],
          'C':['embed_Run2012C_22Jan2013_v1'],
          'D':['embed_Run2012D_22Jan2013_v1'] }

  if abcd == '' : 
    return selComps, weights
  else :
    for i in dic.keys() :
      if i in abcd :
        for l in dic[i] :
          selComps = removekey(selComps, l)
          weights  = removekey(weights , l)
    return selComps, weights

def shrinkData(selComps, weights, abcd='') :
  '''
  pass the name of the sample to be dropped
  A ==> remove data_Run2012A_22Jan2013_v1
  B ==> remove data_Run2012B_22Jan2013_v1
  C ==> remove data_Run2012C_22Jan2013_v1
  D ==> remove data_Run2012D_22Jan2013_v1
  '''

  dic = { 'A':['data_Run2012A_22Jan2013_v1'],
          'B':['data_Run2012B_22Jan2013_v1'],
          'C':['data_Run2012C_22Jan2013_v1'],
          'D':['data_Run2012D_22Jan2013_v1'] }

  if abcd == '' : 
    return selComps, weights
  else :
    for i in dic.keys() :
      if i in abcd :
        for l in dic[i] :
          selComps = removekey(selComps, l)
          weights  = removekey(weights , l)
    return selComps, weights

def lineno():
  '''Returns the current line number in our program.'''
  return inspect.currentframe().f_back.f_lineno

def integralAndError(hist):
  error    = numpy.array([0.])
  integral = hist.IntegralAndError(1, hist.GetNbinsX(),error)
  return integral, error[0]

def prepareComponents(dir, config):
  # list of components from configuration file
  selComps = dict( [ (comp.name, comp)            for comp in config.components ])
  weights  = dict( [ (comp.name,comp.getWeight()) for comp in selComps.values() ] )
  return selComps, weights

###### load weights, if needed, can be commented out
#if path.exists( os.environ.get('CMSSW_BASE')+'/src/CMGTools/H2TauTau/python/proto/rootlogonMoriond.C'):
#    gROOT.Macro(os.environ.get('CMSSW_BASE')+'/src/CMGTools/H2TauTau/python/proto/rootlogonMoriond.C')  # Run ROOT logon script
#print 'path exists?: ', path.exists(os.environ.get('CMSSW_BASE')+'/src/CMGTools/H2TauTau/python/proto/rootlogonMoriond.C')  # Run ROOT logon script

### some switches
run2012       = True
blinding      = False
just125       = False
embZtt        = True
scale_1pb     = True ## leave this always true, is turns of when running susy
final         = True
remove_signal = False
post_fit      = False
datacards     = ['svfitMass','visMass','bbMass','radionMass']
logVars       = ['pThiggs']#["nJets","nbJets"]#,"jet1Pt","jet2Pt","l1Pt","l2Pt","pThiggs","met"]#"svfitMass","visMass"

if __name__ == '__main__':

  ##################################################
  ##                    OPTIONS                   ##
  ##################################################
  from optparse import OptionParser
  from CMGTools.RootTools.RootInit import *

  parser = OptionParser()
  parser.usage = '''
  %prog <anaDir> <cfgFile>

  cfgFile: analysis configuration file, see CMGTools.H2TauTau.macros.MultiLoop
  anaDir: analysis directory containing all components, see CMGTools.H2TauTau.macros.MultiLoop.

  hist: histogram you want to plot
  '''
  parser.add_option("-S", "--shift"    , dest = "shift"     ,  help = "TES nom,up,down. Default is nom" , default = 'nom'      )
  parser.add_option("-P", "--prong"    , dest = "prong"     ,  help = "diTau 1 prong. Default False"    , default = False      )
  parser.add_option("-B", "--box"      , dest = "box"       ,  help = "box. Default is Inclusive"       , default = 'Inclusive')
  parser.add_option("-M", "--mtregion" , dest = "mtregion"  ,  help = "mT region. Default is LowMT"     , default = 'LowMT'    )
  parser.add_option("-H", "--histlist" , dest = "histlist"  ,  help = "histogram list"                  , default = None       )
  parser.add_option("-C", "--cut"      , dest = "cut"       ,  help = "cut to apply in TTree::Draw"     , default = '1'        )
  parser.add_option("-G", "--histgroup", dest = "histgroup" ,  help = "histogram group"                 , default = None       )
  parser.add_option("-R", "--rebin"    , dest = "rebin"     ,  help = "rebinning factor"                , default = None       )
  parser.add_option("-T", "--susy"     , dest = "susy"      ,  help = "run on susy"                     , default = False      )
  parser.add_option("-Z", "--radion"   , dest = "radion"    ,  help = "run and save radion signal"      , default = False      )
  parser.add_option("-E", "--embed"    , dest = "embed"     ,  help = "Use embedd samples."             , default = False      , action="store_true")
      
  (options,args) = parser.parse_args()
  if len(args) != 2:
      parser.print_help() 
      sys.exit(1)

  dataName = 'Data'
  ##################################################
  ##       APPLY TRIGGER ON MC NOT ON DATA        ##
  ##################################################
  ## if diTau is matched, apply diTau data/MC correction factor 
  weight  = '   ( ((l1TrigMatched_diTau>0.5) && (l2TrigMatched_diTau>0.5))*triggerWeight_diTau +\
                  ((l1TrigMatched_diTau<0.5) || (l2TrigMatched_diTau<0.5))                     ) '
  ## if diTauJet is matched, apply diTau data/MC correction factor 
  weight += ' * ( ((l1TrigMatched_diTauJet>0.5) && (l2TrigMatched_diTauJet>0.5) && (jetTrigMatched_diTauJet)>0.5)*triggerWeight_diTauJet +\
                  ((l1TrigMatched_diTauJet<0.5) || (l2TrigMatched_diTauJet<0.5) || (jetTrigMatched_diTauJet)<0.5)                        ) '
  ## apply the diTau data turn on on embed sample
  weight += ' * ( (embedWeight == 1) + (embedWeight != 1)*triggerEffData_diTau )'
  ## stitching weight
  weight += ' * ( weight * (1/(triggerWeight_diTau*triggerWeight_diTauJet)) )'
  ## scale down real taus with decay mode 1 prong no pi zero by 0.88
  weight += ' * ( ((isRealTau==1) * ((l1DecayMode==0)*0.88 + (l1DecayMode!=0))) + (isRealTau==0) ) ' 
  weight += ' * ( ((isRealTau==1) * ((l2DecayMode==0)*0.88 + (l2DecayMode!=0))) + (isRealTau==0) ) ' 
 
  anaDir      = args[0]
  hists       = histogramSet( options )
  cfgFileName = args[1]
  file        = open( cfgFileName, 'r' )
  cfg         = imp.load_source( 'cfg', cfgFileName, file)
    
  selComps, weights = prepareComponents(anaDir, cfg.config)
  
  ##################################################
  ##                 SWITCH RADION                ##
  ##################################################
  radion = options.radion 
  if radion : scale_1pb = True
  ##################################################
  ##                  SWITCH SUSY                 ##
  ##################################################
  susy = options.susy 
  if susy : scale_1pb = False
  if susy :
    ##################################################
    ##         PASS THE PERIOD(S) TO DROP           ##
    ##################################################
    selComps, weights = shrinkData( selComps, weights, abcd='A') ## remove 2012A as no suitable trigger was there
    selComps, weights = shrinkEmbed(selComps, weights, abcd='A') ## remove 2012A as no suitable trigger was there
  ##################################################
  ##                SWITCH EMBEDDED               ##
  ##################################################
  options.embed = embZtt
  crossCheckZee = False #embZtt
  
  
  ##################################################
  ##  READS THE TREES AND CREATES THE COMPONENTS  ##
  ##################################################
  selCompsDataMass, weightsDataMass = componentsWithData( selComps, weights, susy, radion )
  selCompsNoSignal, weightsNoSignal = componentsWithOutSignal( selComps, weights, susy, radion )      

  ##################################################
  ##        COMPUTE EMBEDDED NORMALIZATION        ##
  ##################################################
  
  if options.embed:
    embedSF = True
    embeddedScaleFactor(anaDir, selCompsNoSignal, weightsNoSignal, selCompsDataMass, weightsDataMass, weight, options.prong, susy=susy)
  else : 
    embedSF = False
  if crossCheckZee:
    zeeScaleFactor(anaDir, selCompsNoSignal, weightsNoSignal, selCompsDataMass, weightsDataMass, weight, embed=False, susy=False)
    
  if options.prong :
    #baseline   += ' && abs(jet1Eta)<4.7 && jet1Pt>30. '  ### only for 1p
    baseline   += ' && l1DecayMode<3 && l2DecayMode<3 '  ### only for 1p
  else :  
    pass
    #baseline   += ' && abs(jet1Eta)<4.7 && jet1Pt>30. '
    #baseline   += ' && nbJets == 0'
    #baseline   += ' && abs(jet1Eta)<3.0 && jet1Pt>50. '
  
  #baselineSS = baseline.replace('diTauCharge==0','diTauCharge!=0')
  baselineSS = baseline.replace('l1Charge*l2Charge<0','l1Charge*l2Charge>0')
  
  cuts=[    

#       ("CMS_2012_ptHiggs100_looseIso_sm_BOOSTED"      , baseline, ['45','45'], '              & pThiggs>100', isolationLL , 5 ),
#       ("CMS_2012_ptHiggs100_looseIso_1bjet_sm_BOOSTED", baseline, ['45','45'], ' & nbJets > 0 & pThiggs>100', isolationLL , 5 ),
#       ("CMS_2012_ptHiggs100_looseIso_2bjet_sm_BOOSTED", baseline, ['45','45'], ' & nbJets > 1 & pThiggs>100', isolationLL , 5 ),

#       ("CMS_2012_incl_mssm_BOOSTED", baseline , ['45','45'], ''                         , isolationMM , 5 ),
#       ("CMS_2012_nobtag_BOOSTED"   , baseline , ['45','45'], '&& nbJets == 0'           , isolationMM , 5 ),
#       ("CMS_2012_btag_BOOSTED"     , baseline , ['45','45'], '&& nbJets  > 0 & nJets<2' , isolationMM , 5 ),

#       ("CMS_2012_fb_incl_mssm_BOOSTED", baseline , ['45','45'], ''                         , isolationMM , 5 ),
#       ("CMS_2012_fb_nobtag_BOOSTED"   , baseline , ['45','45'], '&& nbJets == 0'           , isolationMM , 5 ),
#       ("CMS_2012_fb_btag_BOOSTED"     , baseline , ['45','45'], '&& nbJets  > 0 & nJets<2' , isolationMM , 5 ),


### check the name otherwise normalization gets screwed
      ("CMS_2012_pth100_170_low_BOOSTED" , baseline + NOVBFstandard, ['45','45'], ' & jet1Pt>30. & abs(jet1Eta)<4.7 & nbJets == 0 & pThiggs>100 & pThiggs<170', isolationMM , 5 ),
      ("CMS_2012_pth170_high_BOOSTED"    , baseline + NOVBFstandard, ['45','45'], ' & jet1Pt>30. & abs(jet1Eta)<4.7 & nbJets == 0 & pThiggs>170'              , isolationMM , 5 ),
      ("CMS_2012_VBF"                    , baseline +   VBFstandard, ['45','45'], ' & jet1Pt>30. & abs(jet1Eta)<4.7 & nbJets == 0 & pThiggs>100'              , isolationMM , 5 ),
#       ("CMS_2012_incl_sm_BOOSTED"        , baseline                , ['45','45'], ''                                                                          , isolationMM , 5 ),
#       ("CMS_2012_dataTurnOn_pth170_high_BOOSTED"    , baseline + NOVBFstandard, ['45','45'], ' & pThiggs>170'              , isolationMM , 5 ),
#       ("CMS_2012_dataTurnOn_pth100_170_low_BOOSTED" , baseline + NOVBFstandard, ['45','45'], ' & pThiggs>100 & pThiggs<170', isolationMM , 5 ),
#       ("CMS_2012_dataTurnOn_VBF"                    , baseline +   VBFstandard, ['45','45'], ' & pThiggs>100'              , isolationMM , 5 ),






#       ("CMS_2012_pth100_e1bjet_BOOSTED"  , baseline , ['45','45'], ' & nbJets == 1 & pThiggs>100 ', isolationMM , 5 ),
#       ("CMS_2012_pth100_eg1bjet_BOOSTED" , baseline , ['45','45'], ' & nbJets >= 1 & pThiggs>100 ', isolationMM , 5 ),
#       ("CMS_2012_pth100_e2bjet_BOOSTED"  , baseline , ['45','45'], ' & nbJets == 2 & pThiggs>100 & bjet1PtCharge*bjet2PtCharge<0.', isolationMM , 5 ),
#       ("CMS_2012_pth100_eg2bjet_BOOSTED" , baseline , ['45','45'], ' & nbJets >= 2 & pThiggs>100 & bjet1PtCharge*bjet2PtCharge<0.', isolationMM , 5 ),
#       ("CMS_2012_pth100_e2bjet_BOOSTED"  , baseline , ['45','45'], ' & nbJets == 2 & pThiggs>100 ', isolationMM , 5 ),
#       ("CMS_2012_pth100_eg2bjet_BOOSTED" , baseline , ['45','45'], ' & nbJets >= 2 & pThiggs>100 ', isolationMM , 5 ),
#       ("CMS_2012_e1bjet_BOOSTED"  , baseline , ['45','45'], ' & nbJets == 1', isolationMM , 5 ),
#       ("CMS_2012_eg1bjet_BOOSTED" , baseline , ['45','45'], ' & nbJets >= 1', isolationMM , 5 ),
#       ("CMS_2012_e2bjet_BOOSTED"  , baseline , ['45','45'], ' & nbJets == 2 & bjet1PtCharge*bjet2PtCharge<0.', isolationMM , 5 ),
#       ("CMS_2012_eg2bjet_BOOSTED" , baseline , ['45','45'], ' & nbJets >= 2 & bjet1PtCharge*bjet2PtCharge<0.', isolationMM , 5 ),
#       ("CMS_2012_e2bjet_BOOSTED"  , baseline , ['45','45'], ' & nbJets == 2 ', isolationMM , 5 ),
#       ("CMS_2012_eg2bjet_BOOSTED" , baseline , ['45','45'], ' & nbJets >= 2 ', isolationMM , 5 ),


      ]
  
  ##################################################
  ##      LOOP OVER THE DIFFERENT SELECTIONS      ##
  ##################################################
  for prefix,cut,ptcut,antiqcdcut,isocut,qcdEstimate in cuts:
            
    prefix      += '_'+options.shift
    ptCutString  = ' && l1Pt>'+ptcut[0] +' && l2Pt>'+ptcut[1]
    cut         += ptCutString
 
    if 'VBF' in prefix or '_btag' in prefix :
      rebin  = 2
      mjjMin = 100
      mjjMax = 1000
      mjjBin = 30
    else :
      rebin  = 1
      mjjMin = 0
      mjjMax = 800
      mjjBin = 20
    
#     #####################################################
#     ##   IF INCLUSIVE REMOVE BJET VETO AND EXTRA JET   ##
#     #####################################################
#     #import pdb ; pdb.set_trace()
#     if 'incl' in prefix :
#       cut.replace(' && nbJets == 0','')
#       cut.replace(' && jet1Pt>30. && abs(jet1Eta)<4.7 ','')

    #####################################################
    ##histos you want to produce, defined in cuts_diTau##
    #####################################################
    variables = hists_pref( rebin, mjjMin, mjjMax, mjjBin, susy )
    if susy and final:
      #variables.append(('svfitMass' ,300 , 0 , 1500))
      #variables.append(('svfitMass' ,400 , 0 , 2000))
      variables.append(('svfitMass' ,140 , 0 , 700))
        
    #####################################################
    ###               SAVE LIST OF CUTS               ###
    #####################################################
    Cutlist = open(os.getcwd()+"/list_of_Cuts.txt","a")
    print >> Cutlist, prefix
    print >> Cutlist, cut+antiqcdcut+isocut, 'Taus pT', ptCutString,  'QCD estimate', qcdEstimate
    print >> Cutlist, '\n\n' 

    for varLoop in variables:
      
      if len(varLoop) == 4 :
        var  = varLoop[0]
        nx   = varLoop[1] 
        xmin = varLoop[2]
        xmax = varLoop[3]
      else :
        var  = varLoop[0]
        nx   = varLoop[2]
        xmin = None
        xmax = None
      
      print 'I\'m using this cut string\n',cut+isocut+antiqcdcut    
      
      prefix1 = os.getcwd()+"/"+prefix+"/diTau_2012_"
      dirList = os.listdir(os.getcwd())
      exists = False
      for fname in dirList:
        if fname == prefix :
          exists = True
      if not(exists) :
        os.mkdir(os.getcwd()+"/"+prefix)
          
#       if var in logVars and susy:
      if var in logVars :
        log = True
      else:
        log = False
  
      #########################################################
      ##         DEFINITION OF LOOSE ISO CUT FOR QCD         ##
      #########################################################
      if susy or 'incl' in prefix and '_btag' not in prefix :
        isolationLL4 =  ' && l1RawDB3HIso < 2. && l2RawDB3HIso < 2. '
      if susy and '_btag' in prefix :
        isolationLL4 =  ' && l1RawDB3HIso < 4. && l2RawDB3HIso < 4. '
      else :
        isolationLL4 =  ' && l1RawDB3HIso < 10.&& l2RawDB3HIso < 10.'
      

      looseisocut     = isolationLL4 + " && !(1 "+isocut+")"
                
      #cutSS = cut.replace("diTauCharge==0","diTauCharge!=0") ## correct spell is important
      cutSS = cut.replace('l1Charge*l2Charge<0','l1Charge*l2Charge>0')
                                  
      #########################################################
      ##            RELAXING VBF SELECTION FOR QCD           ##
      #########################################################
      
      relaxedVBF = ' && jet2Pt>30. && abs(jet2Eta)<4.7 && abs(jet1Eta - jet2Eta)>2.0 && mjj>200 && nCentralJets==0 '
      
      if 'VBF' in prefix : 
         cutLooseIsoOS_VBF     = cut                           + antiqcdcut + looseisocut               
         cutLooseIsoSS_VBF     = cutSS                         + antiqcdcut + looseisocut               
         cutLooseIsoOS_relVBF  = cut.replace(VBFstandard,'')   + antiqcdcut + looseisocut + relaxedVBF  
         cutLooseIsoSS_relVBF  = cutSS.replace(VBFstandard,'') + antiqcdcut + looseisocut + relaxedVBF  
         cutTightIsoOS_relVBF  = cut.replace(VBFstandard,'')   + antiqcdcut +      isocut + relaxedVBF  
         cutTightIsoSS_relVBF  = cutSS.replace(VBFstandard,'') + antiqcdcut +      isocut + relaxedVBF  

      else :
         cutLooseOS      = cut   + looseisocut + antiqcdcut
         cutLooseSS      = cutSS + looseisocut + antiqcdcut
         cutTightSS      = cutSS + isocut      + antiqcdcut 
              
      #########################################################
      ##         CREATE THE THREE QCD CONTROL REGIONS        ##
      #########################################################

      if 'VBF' in prefix :
        LooseIsoOS_VBF    = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                           cut    = cutLooseIsoOS_VBF    , 
                                           weight = weight               ,                   
                                           embed  = embedSF              ,
                                           susy   = susy                 )
        LooseIsoSS_VBF    = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                           cut    = cutLooseIsoSS_VBF    , 
                                           weight = weight               ,                   
                                           embed  = embedSF              ,
                                           susy   = susy                 )
        LooseIsoOS_relVBF = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                           cut    = cutLooseIsoOS_relVBF , 
                                           weight = weight               ,                   
                                           embed  = embedSF              ,
                                           susy   = susy                 )
        LooseIsoSS_relVBF = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                           cut    = cutLooseIsoSS_relVBF , 
                                           weight = weight               ,                   
                                           embed  = embedSF              ,
                                           susy   = susy                 )
        TightIsoOS_relVBF = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                           cut    = cutTightIsoOS_relVBF , 
                                           weight = weight               ,                   
                                           embed  = embedSF              ,
                                           susy   = susy                 )
        TightIsoSS_relVBF = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                           cut    = cutTightIsoSS_relVBF , 
                                           weight = weight               ,                   
                                           embed  = embedSF              ,
                                           susy   = susy                 )
        QCDShapeVBF, QCDScaleVBF, QCDlooseSSVBF, QCDtightSSVBF, tightLooseVBF, tightLooseErrVBF = QCDEstimate2( prefix, prefix1, var, xmin, xmax,
                                                                                                                LooseIsoSS_VBF, 
                                                                                                                LooseIsoOS_relVBF, 
                                                                                                                LooseIsoOS_relVBF, 
                                                                                                                LooseIsoSS_relVBF, 
                                                                                                                log )
      else : 
        TightIsoSS = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,  
                                    cut    = cutTightSS, 
                                    weight = weight    ,                 
                                    embed  = embedSF   ,
                                    susy   = susy      )
                   
        LooseIsoSS = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                              
                                    cut    = cutLooseSS,
                                    weight = weight    ,#+"*weightQCD_nVert(nVert)*weightQCD_HpT(pThiggs)",                     
                                    embed  = embedSF   , 
                                    susy   = susy      )
                        
        LooseIsoOS = H2TauTauDataMC(var, anaDir, selCompsNoSignal, weightsNoSignal, nx, xmin, xmax,                             
                                    cut    = cutLooseOS, 
                                    weight = weight    ,                   
                                    embed  = embedSF   ,
                                    susy   = susy      )
        QCDScaleVBF = 0.

      
      #######################################################
      ###               PLOTTING DATA/MC                  ###
      #######################################################
      yields = False
      if 'svfitMass' in var or 'visMass' in var or 'l1Pt' or 'bbMass' in var :
        if just125 : massesRange = [125]
        else       : massesRange = [90,95,100,105,110,115,120,125,130,135,140,145,150,155,160]
#         if susy    : massesRange = [80,90,100,110,120,130,140,160,180,200,250,300,350,400,450,500,600,700,800,900,1000]
        if susy    : massesRange = [160]
        if radion  : massesRange = [300,500,700]
        print 'I\'m plotting mass distribution for masses in',massesRange,' GeV'
        if (var == "svfitMass" or var == "visMass") :
          yields = True
      else :
        massesRange = [125]
        if susy : 
          massesRange = [160]
        if radion : 
          massesRange = [700]
        print 'I\'m plotting distribution just for mass {M} GeV'.format(M=str(massesRange))

      #####################################################
      ###                 QCD ESTIMATION                ###
      #####################################################
      #import pdb ; pdb.set_trace()
      if 'VBF' in prefix :
        TightIsoSS = TightIsoSS_relVBF
        LooseIsoOS = LooseIsoOS_relVBF
        LooseIsoSS = LooseIsoSS_relVBF
      QCDShape, QCDScale, QCDlooseSS, QCDtightSS, tightLoose, tightLooseErr = QCDEstimate2( prefix, prefix1, var, xmin, xmax,
                                                                                            TightIsoSS, 
                                                                                            LooseIsoOS, 
                                                                                            LooseIsoOS, 
                                                                                            LooseIsoSS, 
                                                                                            log )      
      if 'VBF' in prefix and QCDScaleVBF>0. :
        QCDScale *= QCDScaleVBF
        print 'Scaling QCD down by',QCDScale, '=', QCDScale/QCDScaleVBF,'*', QCDScaleVBF
        
      print "QCD yield uncertainty:", tightLooseErr
      print "QCDShape yield"        , QCDShape.Integral()
       
      #####################################################
      ###       PRINT YIELDS in QCD CONTROL REGION      ###
      #####################################################
      if 'VBF' in prefix and yields : 
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_LooseIsoOS_VBF_"+var+".txt","w")
        printYields('LooseIsoOS_VBF', LooseIsoOS_VBF, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_LooseIsoSS_VBF_"+var+".txt","w")
        printYields('LooseIsoSS_VBF', LooseIsoSS_VBF, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_LooseIsoOS_relVBF_"+var+".txt","w")
        printYields('LooseIsoOS_relVBF', LooseIsoOS_relVBF, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_LooseIsoSS_relVBF_"+var+".txt","w")
        printYields('LooseIsoSS_relVBF', LooseIsoSS_relVBF, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_TightIsoOS_relVBF_"+var+".txt","w")
        printYields('TightIsoOS_relVBF', TightIsoOS_relVBF, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_TightIsoSS_relVBF_"+var+".txt","w")
        printYields('TightIsoSS_relVBF', TightIsoSS_relVBF, fileout=Yields_dump, susy=susy, radion=radion)       
      elif yields:
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_OSloose"+var+".txt","w")
        printYields('OS loose', LooseIsoOS, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_SStight"+var+".txt","w")
        printYields('SS tight', TightIsoSS, fileout=Yields_dump, susy=susy, radion=radion)       
        Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_SSloose"+var+".txt","w")
        printYields('SS loose', LooseIsoSS, fileout=Yields_dump, susy=susy, radion=radion)            


      #####################################################
      ###        LOOP OVER DIFFERENT HIGGS MASSES       ###
      #####################################################

      for mIndex in massesRange :    
        TightIsoOS = H2TauTauDataMC(var, anaDir, selCompsDataMass[mIndex], weightsDataMass[mIndex], nx, xmin, xmax,
                                    cut    = cut+isocut+antiqcdcut, 
                                    weight = weight ,
                                    embed  = embedSF,
                                    susy   = susy   )
        
        #####################################################
        ###              WJets ESTIMATION                 ###
        #####################################################
            
        if '_VBF'          in prefix : scaleFromMuTau = 1.03 # by Aram        #1.06  # for 2012D by Jose          
        if '_incl'         in prefix : scaleFromMuTau = 0.73 # by Aram        #0.65  # for 2012D by Jose
        if '_low_BOOSTED'  in prefix : scaleFromMuTau = 0.87 # by Aram        #0.65  # for 2012D by Jose
        if '_high_BOOSTED' in prefix : scaleFromMuTau = 0.76 # by Aram        #0.65  # for 2012D by Jose
        if '_nobtag'       in prefix : scaleFromMuTau = 0.73 # by Aram        #0.65  # for 2012D by Jose
        if '_btag'         in prefix : scaleFromMuTau = 1.50 # by Aram        #0.65  # for 2012D by Jose
    
        #if 'incl' in prefix or 'btag' in prefix :
        if susy :
          WJetsScale    = scaleFromMuTau  
          WJetsScaleSS  = scaleFromMuTau 
          TightIsoOS.Hist("WJets").Scale(WJetsScale)
          TightIsoSS.Hist('WJets').Scale(WJetsScaleSS)
        
        else : 
  
          if 'VBF' in prefix :
            WJetsShape        = deepcopy(LooseIsoOS_relVBF.Hist("WJets"))
            WJetsShapeSS      = deepcopy(LooseIsoSS_relVBF.Hist("WJets"))          
            try :                                             
              ##              scale factor   * vbf / !vbf                                                                    * iso / !iso
              WJetsScale    = scaleFromMuTau * LooseIsoOS_VBF.Hist('WJets').Integral() / LooseIsoOS_relVBF.Hist('WJets').Integral() * TightIsoOS_relVBF.Hist('WJets').Integral() / LooseIsoOS_relVBF.Hist('WJets').Integral() 
              WJetsScaleSS  = scaleFromMuTau * LooseIsoSS_VBF.Hist('WJets').Integral() / LooseIsoSS_relVBF.Hist('WJets').Integral() * TightIsoSS_relVBF.Hist('WJets').Integral() / LooseIsoSS_relVBF.Hist('WJets').Integral() 
            except : 
              WJetsScale    = 1.e-7
              WJetsScaleSS  = 1.e-7
          else :
            WJetsShape        = deepcopy(LooseIsoOS.Hist("WJets"))
            WJetsShapeSS      = deepcopy(LooseIsoSS.Hist("WJets"))          
            try :
              WJetsScale    = scaleFromMuTau * TightIsoOS.Hist('WJets').Integral() / LooseIsoOS.Hist('WJets').Integral()
              WJetsScaleSS  = scaleFromMuTau * TightIsoSS.Hist('WJets').Integral() / LooseIsoSS.Hist('WJets').Integral()
            except : 
              WJetsScale    = 1.e-7
              WJetsScaleSS  = 1.e-7
                        
          TightIsoOS.Hist("WJets").obj      = WJetsShape.obj
          TightIsoOS.Hist("WJets").weighted = WJetsShape.weighted
          TightIsoOS.Hist("WJets").Scale(WJetsScale)

          TightIsoSS.Hist('WJets').obj      = WJetsShapeSS.obj
          TightIsoSS.Hist('WJets').weighted = WJetsShapeSS.weighted
          TightIsoSS.Hist('WJets').Scale(WJetsScaleSS)

        #####################################################
        ###           ADD QCD TO OS TIGHT STACK           ###
        #####################################################
        qcdshape = deepcopy(QCDShape.weighted)
        qcdshape.Scale(QCDScale)
        
        if susy or 'incl' in prefix  :
          bin_min = 0
          bin_max = 0
          if var == 'svfitMass' :
            bin_min = 100
            bin_max = 150
          if var == 'visMass' :
            bin_min = 80
            bin_max = 130
          for bin in range(qcdshape.GetNbinsX()):
            if ( qcdshape.GetBinCenter(bin+1)>bin_min and qcdshape.GetBinCenter(bin+1)<bin_max ):
              if qcdshape.GetBinError(bin+1) < 0.1001*qcdshape.GetBinContent(bin+1) :
                qcdshape.SetBinError(bin+1,0.1001*qcdshape.GetBinContent(bin+1))

        TightIsoOS.AddHistogram("QCDdata",qcdshape)
        TightIsoOS.Hist('QCDdata').stack = True
        TightIsoOS.Hist('QCDdata').SetStyle( sHTT_QCD )
        TightIsoOS.Hist('QCDdata').layer = 0.99

        #####################################################
        ###           IF VBF TAKE DY FROM LOOSE OS        ###
        #####################################################
        
        if 'VBF' in prefix :
        
          ## take ZTT from relaxed VBF full iso
          for dy in ['DYJets'] :
            DYJetsShape = deepcopy(TightIsoOS_relVBF.Hist(dy))
            if TightIsoOS.Hist(dy).Integral() > 0 :
              DYJetsScale = TightIsoOS.Hist(dy).Integral() / TightIsoOS_relVBF.Hist(dy).Integral()
            else : 
              DYJetsScale = 1.e-7
            TightIsoOS.Hist(dy).obj      = DYJetsShape.obj
            TightIsoOS.Hist(dy).weighted = DYJetsShape.weighted
            TightIsoOS.Hist(dy).Scale(DYJetsScale)

          ## take ZL & ZJ from relaxed VBF loose iso
          for dy in ['DYJets_ZL','DYJets_ZJ'] :
            DYJetsShape = deepcopy(LooseIsoOS_relVBF.Hist(dy))
            if TightIsoOS.Hist(dy).Integral() > 0 :
              DYJetsScale = TightIsoOS.Hist(dy).Integral() / LooseIsoOS.Hist(dy).Integral()
            else : 
              DYJetsScale = 1.e-7 / LooseIsoOS.Hist(dy).Integral()
            TightIsoOS.Hist(dy).obj      = DYJetsShape.obj
            TightIsoOS.Hist(dy).weighted = DYJetsShape.weighted
            TightIsoOS.Hist(dy).Scale(DYJetsScale)

          ## take VV from relaxed VBF full iso
          for vv in ['Tbar_tW','T_tW','WWJetsTo2L2Nu','WZJetsTo2L2Q','WZJetsTo3LNu','ZZJetsTo4L','ZZJetsTo2L2Nu','ZZJetsTo2L2Q'] :
            VVJetsShape = deepcopy(TightIsoOS_relVBF.Hist(vv))
            if TightIsoOS.Hist(vv).Integral() > 0 :
              VVJetsScale = TightIsoOS.Hist(vv).Integral() / TightIsoOS_relVBF.Hist(vv).Integral()
            else : 
              VVJetsScale = 1.e-7
            TightIsoOS.Hist(vv).obj      = VVJetsShape.obj
            TightIsoOS.Hist(vv).weighted = VVJetsShape.weighted
            TightIsoOS.Hist(vv).Scale(VVJetsScale)

          ## take TT from relaxed VBF full iso
          for tt in ['TTJetsFullLept','TTJetsSemiLept','TTJetsHadronic'] :
            TTJetsShape = deepcopy(TightIsoOS_relVBF.Hist(tt))
            if TightIsoOS.Hist(tt).Integral() > 0 :
              TTJetsScale = TightIsoOS.Hist(tt).Integral() / TightIsoOS_relVBF.Hist(tt).Integral()
            else : 
              TTJetsScale = 1.e-7
            TightIsoOS.Hist(tt).obj      = TTJetsShape.obj
            TightIsoOS.Hist(tt).weighted = TTJetsShape.weighted
            TightIsoOS.Hist(tt).Scale(TTJetsScale)

        #####################################################
        ###         PRINT YIELDS in SIGNAL REGION         ###
        #####################################################
        
        if yields :                                        
          Yields_dump = open(os.getcwd()+"/"+prefix+"/Yields_"+var+"_mH"+str(mIndex)+".txt","w")
          printYields('OS tight', TightIsoOS, mass=mIndex, fileout=Yields_dump, qcd=True, susy=susy, radion=radion)            
        
        #####################################################
        ###     SAVE ROOT FILES FOR LIMIT COMPUTATION     ###
        #####################################################

        for dc in datacards :
          if dc in var and 'VBF'     in prefix :
            saveForLimit(deepcopy(TightIsoOS),prefix,mIndex,dc,not isinstance(nx, numpy.ndarray),"vbf"  ,susy, radion, scale_1pb, selCompsDataMass)
          if dc in var and 'BOOSTED' in prefix :
            saveForLimit(deepcopy(TightIsoOS),prefix,mIndex,dc,not isinstance(nx, numpy.ndarray),"boost",susy, radion, scale_1pb, selCompsDataMass)

        #####################################################
        ###        REMOVE PTH SHAPES FROM PLOTTING        ###
        #####################################################
        
        TightIsoOS.histos[:] = [ item for item in TightIsoOS.histos if '_pth' not in item.name ]        
        
        #####################################################
        ###   BOOSTING THE SIGNAL FOR PICTORIAL RESULTS   ###
        #####################################################
        ### for mA = 200 
        # xsec ggA  3.39277529716491699e+03
        # xsec bbA  3.10879477334919284e+04
        # BR tautau 1.19457997381687164e-01
        # nevents ggA 985855 * 1.0
        # nevents bbA 999408 * 1.0     
        if susy :
          TightIsoOS.Hist(str('HiggsSUSYBB'    +str(mIndex))).Scale(5)#10*18.4*3.10879477334919284e+04*1.19457997381687164e-01/999408)  
          TightIsoOS.Hist(str('HiggsSUSYGluGlu'+str(mIndex))).Scale(5)#10*18.4*3.39277529716491699e+03*1.19457997381687164e-01/985855)  
        elif radion :
          TightIsoOS.Hist(str('Radion'         +str(mIndex))).Scale(10.)#10*18.4*3.10879477334919284e+04*1.19457997381687164e-01/999408)  
        else :
          #pass
          TightIsoOS.Hist(str('HiggsGGH'+str(mIndex))).Scale(5)
          TightIsoOS.Hist(str('HiggsVBF'+str(mIndex))).Scale(5)
          #TightIsoOS.Hist(str('HiggsVH' +str(mIndex))).Scale(5)
          TightIsoOS.Hist(str('HiggsWH' +str(mIndex))).Scale(5)
          TightIsoOS.Hist(str('HiggsZH' +str(mIndex))).Scale(5)
          TightIsoOS.Hist(str('HiggsttH'+str(mIndex))).Scale(5)
        
        #####################################################
        ###             POST FIT SCALE FACTORS            ###
        #####################################################
        
        if post_fit :
          ### no btag by Felix https://www.dropbox.com/sh/j945812kfi5qwwh/unbn7pj261/scales_tt_8_8TeV.py
          scales = {
                    'WJets'         : [ 0.997             , 0.29100000000000004 ], 
                    'DYJets_ZJ'     : [ 1.0326196173991968, 0.20038121768269596 ], 
                    'TTJetsFullLept': [ 1.1151469634440145, 0.10752167223401993 ], 
                    'TTJetsSemiLept': [ 1.1151469634440145, 0.10752167223401993 ], 
                    'TTJetsHadronic': [ 1.1151469634440145, 0.10752167223401993 ], 
                    'T_tW'          : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'WWJetsTo2L2Nu' : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'WZJetsTo2L2Q'  : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'WZJetsTo3LNu'  : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'ZZJetsTo4L'    : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'ZZJetsTo2L2Nu' : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'ZZJetsTo2L2Q'  : [ 1.138218601221332 , 0.20147451451734524 ], 
                    'QCDdata'       : [ 1.0245            , 0.014000000000000004], 
                    'DYJets'        : [ 1.1968286655695997, 0.07150665982969698 ], 
                    #'ggH'           : [ 1.0689942568924617, 0.08733314147561626 ],
                    #'bbH'           : [ 1.1254465009797725, 0.08074025266247316 ], 
                   }
          ### btag by Felix https://www.dropbox.com/sh/j945812kfi5qwwh/BnFSfpANNB/scales_tt_9_8TeV.py
#           scales = {
#                     'WJets'         : [ 1.048             , 0.30600000000000005 ], 
#                     'DYJets_ZJ'     : [ 1.03741368        , 0.19880028269597602 ], 
#                     'TTJetsFullLept': [ 1.171663637022884 , 0.1288909616691567  ], 
#                     'TTJetsSemiLept': [ 1.171663637022884 , 0.1288909616691567  ], 
#                     'TTJetsHadronic': [ 1.171663637022884 , 0.1288909616691567  ], 
#                     'T_tW'          : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'WWJetsTo2L2Nu' : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'WZJetsTo2L2Q'  : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'WZJetsTo3LNu'  : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'ZZJetsTo4L'    : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'ZZJetsTo2L2Nu' : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'ZZJetsTo2L2Q'  : [ 1.1965028180280834, 0.2136444476226798  ], 
#                     'QCDdata'       : [ 0.9195            , 0.08050000000000003 ], 
#                     'DYJets'        : [ 1.1957540987309998, 0.07163052701188229 ], 
#                     #'ggH'           : [ 1.183076702943718, 0.10756838940878502],
#                     #'bbH'           : [ 1.180927824976716, 0.11055834839576799], 
#                    }
          
          print scales
           
          for h in scales.keys() :
            ## scale factor
            TightIsoOS.Hist(h).Scale(scales[h][0])
            
            ## add systematics       
            for bin in range(TightIsoOS.Hist(h).weighted.GetNbinsX()):
              binerr = TightIsoOS.Hist(h).weighted.GetBinError(bin+1)
              binc   = TightIsoOS.Hist(h).weighted.GetBinContent(bin+1)
              newbinerr = math.sqrt( binerr*binerr + scales[h][1]*scales[h][1]*binc*binc )
              #print 'h',h,'bin', bin+1, 'bin error', binerr, 'bin content',binc,'newbinerr', newbinerr,'scale',scales[h][1]
              TightIsoOS.Hist(h).weighted.SetBinError(bin+1,newbinerr)
        
        #####################################################
        ###                  REMOVE SIGNAL                ###
        #####################################################
        if remove_signal :
          TightIsoOS.histos[:] = [ item for item in TightIsoOS.histos if 'Higgs' not in item.name ]        

        #####################################################
        ###                 GROUPING BKGS                 ###
        #####################################################
                             
        TightIsoOS.Group('electroweak'          , ['WJets', 'DYJets_ZL', 'DYJets_ZJ','Tbar_tW','T_tW','WWJetsTo2L2Nu','WZJetsTo2L2Q','WZJetsTo3LNu','ZZJetsTo4L','ZZJetsTo2L2Nu','ZZJetsTo2L2Q']) #,'ZZ','WZ','WW'
        TightIsoOS.Group('t#bar{t}'             , ['TTJetsFullLept','TTJetsSemiLept','TTJetsHadronic'])
        TightIsoOS.Group('Fakes'                , ['QCDdata'])
        if susy :
          TightIsoOS.Group('Z#rightarrow#tau#tau' , ['DYJets','TTJets_emb'])
        else :
          TightIsoOS.Group('Z#rightarrow#tau#tau' , ['DYJets'])
        TightIsoOS.Group('Background uncertainty' , [])
        
        
        if susy and not remove_signal:
          TightIsoOS.Group('10x#phi('+str(mIndex)+' GeV)#rightarrow#tau#tau, tan#beta=20'  , ['HiggsSUSYBB'     + str(mIndex), 
                                                                                              'HiggsSUSYGluGlu' + str(mIndex)])         
          TightIsoOS.Group('electroweak'                                                   , ['WJets'        , 
                                                                                              'DYJets_ZL'    , 
                                                                                              'DYJets_ZJ'    ,
                                                                                              'Tbar_tW'      ,
                                                                                              'T_tW'         ,
                                                                                              'HiggsVBF125'  , 
                                                                                              'HiggsGGH125'  , 
                                                                                              #'HiggsVH125'   ,
                                                                                              'HiggsWH125'   ,
                                                                                              'HiggsZH125'   ,
                                                                                              'HiggsttH125'  ,
                                                                                              'WWJetsTo2L2Nu',
                                                                                              'WZJetsTo2L2Q' ,
                                                                                              'WZJetsTo3LNu' ,
                                                                                              'ZZJetsTo4L'   ,
                                                                                              'ZZJetsTo2L2Nu',
                                                                                              'ZZJetsTo2L2Q' ])
        elif not remove_signal :
          TightIsoOS.Group('5xH('   +str(mIndex)+' GeV)#rightarrow#tau#tau'  , ['HiggsVBF'+str(mIndex), 
                                                                                'HiggsGGH'+str(mIndex), 
                                                                                #'HiggsVH' +str(mIndex)]) 
                                                                                'HiggsWH' +str(mIndex), 
                                                                                'HiggsZH' +str(mIndex), 
                                                                                'HiggsttH'+str(mIndex)]) 
        else :
          pass
         
        for h in ['electroweak','t#bar{t}','Z#rightarrow#tau#tau','Data','Fakes'] :
          #TightIsoOS.Hist(h).weighted.SetTitle('CMS preliminary 2012, #sqrt{s} = 8TeV, L = 19.7 fb^{-1}        #tau_{h}#tau_{h}')
          TightIsoOS.Hist(h).weighted.SetTitle('CMS, 19.7 fb^{-1} at 8TeV')
          #TightIsoOS.Hist(h).weighted.GetXaxis().SetLabelSize(0.)
          if susy : TightIsoOS.Hist(h).weighted.SetTitle('CMS preliminary 2012, #sqrt{s} = 8TeV, L = 18.3 fb^{-1}        #tau_{h}#tau_{h}')
          #if susy : TightIsoOS.Hist(h).weighted.SetTitle('CMS, 18.3 fb^{-1} at 8TeV')
          TightIsoOS.Hist(h).GetXaxis().SetTitle(xtitles[var])
          TightIsoOS.Hist(h).GetXaxis().SetTitleSize(0.040)
          if TightIsoOS.Hist(h).Integral()<0.1 :
            TightIsoOS.Group('Fakes', ['QCDdata',h])
          if isinstance(nx, numpy.ndarray):
            TightIsoOS.Hist(h).GetYaxis().SetTitle('dN/dm_{#tau#tau} [1/GeV]')
          else :
            TightIsoOS.Hist(h).GetYaxis().SetTitle('Events')
          TightIsoOS.Hist(h).GetYaxis().SetTitleSize(0.040)
          if 'DecayMode' in var :
            #TightIsoOS.Hist(h).weighted.SetMaximum(1.3*TightIsoOS.Hist(h).GetMaximum())
            TightIsoOS.Hist(h).GetXaxis().SetBinLabel(1,'1 prong 0 #pi^{0}')
            TightIsoOS.Hist(h).GetXaxis().SetBinLabel(2,'1 prong 1 #pi^{0}')
            TightIsoOS.Hist(h).GetXaxis().SetBinLabel(3,'3 prongs')
          
        #####################################################
        ###           BLINDING DATA ABOVE Z PEAK          ###
        #####################################################
        
        if blinding and not susy:
          blind(var, 'svfitMass', TightIsoOS, 100., 150. )
          blind(var, 'visMass'  , TightIsoOS,  80., 120. )
          #blind(var, 'dRtt'     , TightIsoOS,   0.,   2. )
        if blinding and susy:
          blind(var, 'svfitMass', TightIsoOS, 110., 1500. )
          blind(var, 'visMass'  , TightIsoOS,  90., 1500. )

        #####################################################
        ###                    PLOTTING                   ###
        #####################################################         
        gPad.SetCanvasSize(700,700)
        gPad.SetLeftMargin(0.18)
        gPad.SetBottomMargin(0.18)
        gPad.SetFrameLineWidth(3)
        
        ## normalizing to bin width if variable binning 
        if isinstance(nx, numpy.ndarray) :
          TightIsoOS.NormalizeToBinWidth()
        
        #if not (susy and var == 'svfitMass' and not isinstance(nx, numpy.ndarray) ):
        #  TightIsoOS.DrawStack("HIST")
        
        #import pdb ; pdb.set_trace()
        ymax = None
        if 'Eta' in var or 'eta' in var or 'dRtt' in var or 'tau1Mass' in var or 'tau2Mass' in var or 'DecayMode' in var :
         ymax = TightIsoOS.Hist("Data").GetMaximum()*1.8
        if var in logVars:
          ymax = TightIsoOS.Hist("Data").GetMaximum()*20.
          TightIsoOS.DrawStack("HIST",xmin,xmax,0.1,ymax)
        else :
          TightIsoOS.DrawStack("HIST",xmin,xmax,0. ,ymax)

        xlabel = TLatex(.22,.845,"#tau_{h}#tau_{h}")
        xlabel.SetNDC()
        xlabel.SetTextColor(1)
        xlabel.SetTextSize(.05)
        xlabel.Draw()
                  
        gStyle.SetLabelSize(0.035,'xy')
        gStyle.SetTitleSize(0.035,'xy')

        gPad.SaveAs(prefix1+prefix+'_'+TightIsoOS.varName+"_mH"+str(mIndex)+"_data.pdf")
                  
        #####################################################
        ### SAVE ROOT FILE TO ACCESS THE TEMPLATES EASILY ###
        #####################################################
        
        #if not datacard in var or ((len(nx) == 1 and nx<100000) or isinstance(nx, numpy.ndarray)) :
        #  saveForPlotting(deepcopy(TightIsoOS),prefix,mIndex,susy)


#         #####################################################
#         ###                    PLOTTING                   ###
#         #####################################################         
#         can = TCanvas('can','',700,1000)
#         can.cd()
#         can.Draw()
#         pad = TPad('pad','',0.01,0.3,0.99, 0.99)
#         pad.SetBottomMargin(0.04)
#         padr = TPad('padr','',0.01, 0.01, 0.99, 0.31)
#         padr.SetTopMargin(0.04)
#         padr.SetBottomMargin(0.3)
# 
# 
# 
#         can.cd()
#         pad.Draw()
#         pad.cd()
#         gPad.SetCanvasSize(700,700)
#         gPad.SetLeftMargin(0.18)
#         #gPad.SetBottomMargin(0.18)
#         gPad.SetFrameLineWidth(3)
# 
#         if isinstance(nx, numpy.ndarray) :
#           TightIsoOS.NormalizeToBinWidth()
# 
#         ymax = None
#         if 'Eta' in var or 'eta' in var or 'dRtt' in var or 'tau1Mass' in var or 'tau2Mass' in var :
#          ymax = TightIsoOS.Hist("Data").GetMaximum()*1.8
#         if var in logVars:
#           ymax = TightIsoOS.Hist("Data").GetMaximum()*20.
#           TightIsoOS.DrawStack("HIST",xmin,xmax,0.1,ymax)
#         else :
#           TightIsoOS.DrawStack("HIST",xmin,xmax,0. ,ymax)
# 
#         can.cd()
#         padr.Draw()
#         padr.cd()
#         #gPad.SetCanvasSize(700,300)
#         gPad.SetLeftMargin(0.18)
#         #gPad.SetBottomMargin(0.18)
#         gPad.SetFrameLineWidth(3)
#                 
#         TightIsoOSRatio = deepcopy(TightIsoOS)
#         TightIsoOSRatio.legendOn = False
# 
#         ymax = None
# #         import pdb ; pdb.set_trace()
# #         for h in TightIsoOSRatio.histos :
# #           h.GetYaxis().SetNdivisions(4)
# #           h.GetYaxis().SetTitle('Exp./Obs.')
# #           h.GetYaxis().SetTitleSize(0.1)
# #           h.GetYaxis().SetTitleOffset(0.5)
# #           h.GetXaxis().SetTitle(xtitles[var])
# #           h.GetXaxis().SetTitleSize(0.13)
# #           h.GetXaxis().SetTitleOffset(0.9)
# #           rls = 0.075
# #           h.GetYaxis().SetLabelSize(rls)
# #           h.GetXaxis().SetLabelSize(rls)
# #           h.GetYaxis().SetRangeUser(0.5, 1.5)
# #         TightIsoOSRatio.stack.obj.SetMinimum(0.5)  
# #         TightIsoOSRatio.stack.obj.SetMaximum(1.5)  
# 
# 
# 
#         TightIsoOSRatio.DrawRatioStack("HIST", xmin=xmin, xmax=xmax, ymin=0.5, ymax=1.5)
#         hr = TightIsoOSRatio.stack.totalHist
#         TightIsoOSRatio.stack.totalHist = hr
#         # hr.weighted.Fit('pol1')
#         hr.obj.SetTitle('')
#         hr.GetYaxis().SetNdivisions(4)
#         hr.GetYaxis().SetTitle('Exp./Obs.')
#         hr.GetYaxis().SetTitleSize(0.1)
#         hr.GetYaxis().SetTitleOffset(0.5)
#         hr.GetXaxis().SetTitle(xtitles[var])
#         hr.GetXaxis().SetTitleSize(0.13)
#         hr.GetXaxis().SetTitleOffset(0.9)
#         rls = 0.09
#         hr.GetYaxis().SetLabelSize(rls)
#         hr.GetXaxis().SetLabelSize(rls)
#         hr.GetYaxis().SetRangeUser(0.5, 1.5)
#         padr.Update()    
#         #import pdb ; pdb.set_trace()
#         gStyle.SetOptTitle(0)
#         can.cd()
#         gPad.SaveAs(prefix1+prefix+'_'+TightIsoOS.varName+"_mH"+str(mIndex)+"_data.pdf")

















































