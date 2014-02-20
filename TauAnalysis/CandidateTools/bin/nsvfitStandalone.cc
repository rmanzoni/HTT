#include "TTree.h"
#include "TFile.h"
#include "TLorentzVector.h"
#include <time.h>

#include "TauAnalysis/CandidateTools/interface/NSVfitStandaloneAlgorithm.h"

/**
   \class nsvfitStandalone nsvfitStandalone.cc "TauAnalysis/CandidateTools/bin/nsvfitStandalone.cc"
   \brief Basic example of the use of the standalone version of NSVfit

   This is an example executable to show the use of the standalone version of NSVfit form a flat 
   n-tuple or single event.
*/

void singleEvent()
{
//   ************************************************************************************************************************************************************************************************************
//   *    Row   *       evt *      pt_1 *      pt_2 *     eta_1 *     eta_2 *     phi_1 *     phi_2 *       m_1 *       m_2 *    mvamet * mvametphi *  mvacov00 *  mvacov01 *  mvacov11 *      m_sv *      mvis *
//   ************************************************************************************************************************************************************************************************************
//   *       13 * 165907073 * 75.739288 * 48.324012 * -1.550589 * 0.2400562 * -1.087979 * 2.3772344 * 0.8414608 * 0.8543023 * 4.4676966 * -0.404438 * 166.29016 * 14.817026 * 283.93032 * 195.61764 * 171.72894 *
//   ************************************************************************************************************************************************************************************************************
// ************************************************************************************************************************************************
// *    Row   *     event *      l1Px *      l1Py *      l1Pz *       l1E *      l2Px *      l2Py *      l2Pz *       l2E *       met *    metPhi *
// ************************************************************************************************************************************************
// *     1715 * 165907073 * 35.163917 * -67.08158 * -170.4938 * 186.56179 * -34.88156 * 33.443786 * 11.712217 * 49.730434 * 4.4676966 * -0.404438 *
// ************************************************************************************************************************************************
// ************************************************************************************************************************************************************************
// *    Row   *     event *      l1Px *      l1Py *      l1Pz *       l1E *      l2Px *      l2Py *      l2Pz *       l2E *       met *    metPhi *       mex *       mey *
// ************************************************************************************************************************************************************************
// *        6 *   5955101 * -27.54659 * 47.296833 * 15.885040 * 56.993610 * 4.5915265 * -45.02828 * -76.17942 * 88.614402 * 7.7737574 * -1.827878 * -1.976556 * -7.518279 *





/*
Tau1 px()    	-80.8393
Tau1 py()    	-8.54607
Tau1 pz()    	57.1108
Tau1 mass()  	0.0258703
Tau1 energy()	99.3462
Tau1 eta()   	0.654761
Tau1 phi()   	-3.03627
Tau2 px()    	-40.0303
Tau2 py()    	34.8123
Tau2 pz()    	-25.784
Tau2 mass()  	0.00879871
Tau2 energy()	58.9842
Tau2 eta()   	-0.468683
Tau2 phi()   	2.4258
MET          	7.91566
MET Phi      	1.96094
MEx          	-3.01049
MEy          	7.32083
mvacov00     	416.892
mvacov01     	72.502
mvacov10     	72.502
mvacov11     	169.138
	m_vis = 93.7432, m_svfit = 106.369
found mass    = 109.028

*/



























  /* 
     This is a single event for testing in the integration mode.
  */
  // define MET
  // event 75225226
  //Vector MET(-15.6809989128504164, 6.12556021895826319, 0.); 
  //Vector MET(-19.73485, -5.720700, 0.); 
  Vector MET(TMath::Cos(-0.242009)*13.177546, TMath::Sin(-0.242009)*13.177546, 0.); 
  // define MET covariance
  TMatrixD covMET(2, 2);
  /*
  covMET[0][0] = 0.;
  covMET[1][0] = 0.;
  covMET[0][1] = 0.;
  covMET[1][1] = 0.;
  */
  // event 75225226
  //covMET[0][0] = 117.81176;
  //covMET[1][0] = 43.810665;
  //covMET[0][1] = 43.810665;
  //covMET[1][1] = 127.24190;
  covMET[0][0] = 535.00811;
  covMET[1][0] = -202.4530;
  covMET[0][1] = -202.4530;
  covMET[1][1] = 422.10998;
  // define lepton four vectors
                                //       px    ,  py      , pz        , E 
  // event 873552766
  NSVfitStandalone::LorentzVector l1( TMath::Cos(0.5807800)*145.91406, TMath::Sin(0.5807800)*145.91406, 3.01203229139404201e+01 ,1.48996438446225199e+02); // tau
  NSVfitStandalone::LorentzVector l2( TMath::Cos(0.8599243)*96.976562, TMath::Sin(0.8599243)*96.976562, 9.12369262040504907e+01 ,1.33148975816092161e+02); // tau
  //NSVfitStandalone::LorentzVector l1( -44.22908, 50.860073, 78.779418, 103.68624); // tau
  //NSVfitStandalone::LorentzVector l2( -40.81599, -24.83730, -126.8154, 135.52206); // tau
  std::vector<NSVfitStandalone::MeasuredTauLepton> measuredTauLeptons;
  measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay, l1));
  measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay, l2));
//   measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay, l1));
  // define algorithm (set the debug level to 3 for testing)
  NSVfitStandaloneAlgorithm algo(measuredTauLeptons, MET, covMET, /*debug=*/3);
  algo.addLogM(false);
  /* 
     the following lines show how to use the different methods on a single event
  */
  // minuit fit method
  //algo.fit();
  // integration by VEGAS (same as function algo.integrate() that has been in use when markov chain integration had not yet been implemented)
  algo.integrateVEGAS();
  // integration by markov chain MC
  //algo.integrateMarkovChain();

  double mass = algo.getMass(); // mass uncertainty not implemented yet
  if(algo.isValidSolution()){
    std::cout << "found mass    = " << mass << std::endl;
  }
  else{
    std::cout << "sorry -- status of NLL is not valid [" << algo.isValidSolution() << "]" << std::endl;
  }
  return;
}

void eventsFromTree(int argc, char* argv[]) 
{
  // parse arguments
  if ( argc < 3 ) {
    std::cout << "Usage : " << argv[0] << " [inputfile.root] [tree_name] [Chunks] [nchunk] [outfile.root]" << std::endl;
    return;
  }
  
  
  // get intput directory up to one before mass points
  TFile* file = new TFile(argv[1]); 
  // access tree in file
  TTree* tree = (TTree*) file->Get(argv[2]);
  // chunks to split
  int chunks = atoi(argv[3]) ;
  // input variables
  float met, metPhi;
  float covMet11, covMet12; 
  float covMet21, covMet22;
  float l1E, l1M, l1Px, l1Py, l1Pz;
  float l2E, l2M, l2Px, l2Py, l2Pz;
  float l1Pt, l1Eta, l1Phi;
  float l2Pt, l2Eta, l2Phi;
//   double met, metPhi;
//   double covMet11, covMet12; 
//   double covMet21, covMet22;
//   double l1E, l1M, l1Px, l1Py, l1Pz;
//   double l2E, l2M, l2Px, l2Py, l2Pz;
//   double l1Pt, l1Eta, l1Phi;
//   double l2Pt, l2Eta, l2Phi;
  //float mTrue;
  int ievent ;

  // save the result into a TTree
  TFile hfile(argv[5],"RECREATE");
  Int_t evt;
  Double_t m_sv;

  TTree* pMyTree= new TTree("SimpleTree","An example of a tree");
  pMyTree->Branch("evt"      ,&evt      ,"evt/I"      );
  pMyTree->Branch("m_sv"     ,&m_sv     ,"m_sv/D"     );
  pMyTree->Branch("met"      ,&met      ,"met/F"      );
  pMyTree->Branch("metPhi"   ,&metPhi   ,"metPhi/F"   );
  pMyTree->Branch("covMet11" ,&covMet11 ,"covMet11/F" );
  pMyTree->Branch("covMet12" ,&covMet12 ,"covMet12/F" );
  pMyTree->Branch("covMet21" ,&covMet21 ,"covMet21/F" );
  pMyTree->Branch("covMet22" ,&covMet22 ,"covMet22/F" );
  pMyTree->Branch("l1E"      ,&l1E      ,"l1E/F"      );
  //pMyTree->Branch("l1M"      ,&l1M      ,"l1M/F"      );
  pMyTree->Branch("l1Px"     ,&l1Px     ,"l1Px/F"     );
  pMyTree->Branch("l1Py"     ,&l1Py     ,"l1Py/F"     );
  pMyTree->Branch("l1Pz"     ,&l1Pz     ,"l1Pz/F"     );
  pMyTree->Branch("l2E"      ,&l2E      ,"l2E/F"      );
  //pMyTree->Branch("l2M"      ,&l2M      ,"l2M/F"      );
  pMyTree->Branch("l2Px"     ,&l2Px     ,"l2Px/F"     );
  pMyTree->Branch("l2Py"     ,&l2Py     ,"l2Py/F"     );
  pMyTree->Branch("l2Pz"     ,&l2Pz     ,"l2Pz/F"     );
  
  // branch adresses
//   tree->SetBranchAddress("evt"          , &ievent     );
//   tree->SetBranchAddress("mvamet"       , &met        );
//   tree->SetBranchAddress("metphi"       , &metPhi     );
//   tree->SetBranchAddress("mvacov00"     , &covMet11   );
//   tree->SetBranchAddress("mvacov01"     , &covMet12   );
//   tree->SetBranchAddress("mvacov10"     , &covMet21   );
//   tree->SetBranchAddress("mvacov11"     , &covMet22   );
//   tree->SetBranchAddress("m_1"          , &l1M        );
//   tree->SetBranchAddress("pt_1"         , &l1Pt       );
//   tree->SetBranchAddress("eta_1"        , &l1Eta       );
//   tree->SetBranchAddress("phi_1"        , &l1Phi       );
//   tree->SetBranchAddress("m_2"          , &l2M        );
//   tree->SetBranchAddress("pt_2"         , &l2Pt       );
//   tree->SetBranchAddress("eta_2"        , &l2Eta       );
//   tree->SetBranchAddress("phi_2"        , &l2Phi       );
  //tree->SetBranchAddress("m_true"       , &mTrue      );
  // branch adresses
  tree->SetBranchAddress("event"        , &ievent     );
  tree->SetBranchAddress("met"          , &met        );
  tree->SetBranchAddress("metPhi"       , &metPhi     );
  tree->SetBranchAddress("mvacov00"     , &covMet11   );
  tree->SetBranchAddress("mvacov01"     , &covMet12   );
  tree->SetBranchAddress("mvacov10"     , &covMet21   );
  tree->SetBranchAddress("mvacov11"     , &covMet22   );
  tree->SetBranchAddress("l1E"          , &l1E        );
  tree->SetBranchAddress("l1M"          , &l1M        );
  tree->SetBranchAddress("l1Px"         , &l1Px       );
  tree->SetBranchAddress("l1Py"         , &l1Py       );
  tree->SetBranchAddress("l1Pz"         , &l1Pz       );
  tree->SetBranchAddress("l2E"          , &l2E        );
  tree->SetBranchAddress("l2M"          , &l2M        );
  tree->SetBranchAddress("l2Px"         , &l2Px       );
  tree->SetBranchAddress("l2Py"         , &l2Py       );
  tree->SetBranchAddress("l2Pz"         , &l2Pz       );
  //tree->SetBranchAddress("m_true"       , &mTrue      );
  int nevent = tree->GetEntries();
  //nevent = 10 ;
  int nchunk = atoi(argv[4]) ;
  int evt_per_chunk = ( (int) nevent / chunks )+ 1                   ;
  int start_evt     = evt_per_chunk * nchunk                         ;
  int end_evt       = TMath::Min(nevent, evt_per_chunk * (nchunk+1)) ;
  
  std::cout << "running on " << evt_per_chunk << " events " << std::endl ; 
  std::cout << "from  " << start_evt << " to " << end_evt << std::endl ; 
  std::cout << "total  " << nevent << " events "<< std::endl ; 
  
  for(int i=start_evt; i<end_evt; ++i){    
  //for(int i=0; i<nevent; ++i){    
    tree->GetEvent(i);
    std::cout << "event " << i+1  << std::endl;
    
    /* smear the variables to simulate small differences */
    /* initialize random seed: */
    srand (time(NULL));
    
    //std::cout << "random1 " << ((float)50*rand()/(RAND_MAX)) << std::endl;
    if (((float)rand()/(RAND_MAX)) > 0.5) {met      = met      * (1. + ((float)10*rand()/(RAND_MAX))/200.);}
    else                                  {met      = met      * (1. - ((float)10*rand()/(RAND_MAX))/200.);}
    srand (time(NULL));
    if (((float)rand()/(RAND_MAX)) > 0.5) {metPhi   = metPhi   * (1. + ((float)10*rand()/(RAND_MAX))/200.);}
    else                                  {metPhi   = metPhi   * (1. - ((float)10*rand()/(RAND_MAX))/200.);}
    srand (time(NULL));
    if (((float)rand()/(RAND_MAX)) > 0.5) {covMet11 = covMet11 * (1. + ((float)10*rand()/(RAND_MAX))/200.);}
    else                                  {covMet11 = covMet11 * (1. - ((float)10*rand()/(RAND_MAX))/200.);}
    srand (time(NULL));
    if (((float)rand()/(RAND_MAX)) > 0.5) {covMet12 = covMet12 * (1. + ((float)10*rand()/(RAND_MAX))/200.);}
    else                                  {covMet12 = covMet12 * (1. - ((float)10*rand()/(RAND_MAX))/200.);}
    srand (time(NULL));
    if (((float)rand()/(RAND_MAX)) > 0.5) {covMet21 = covMet21 * (1. + ((float)10*rand()/(RAND_MAX))/200.);}
    else                                  {covMet21 = covMet21 * (1. - ((float)10*rand()/(RAND_MAX))/200.);}
    srand (time(NULL));
    if (((float)rand()/(RAND_MAX)) > 0.5) {covMet22 = covMet22 * (1. + ((float)10*rand()/(RAND_MAX))/200.);}
    else                                  {covMet22 = covMet22 * (1. - ((float)10*rand()/(RAND_MAX))/200.);}    
    //std::cout << "random2 " << (float)50*rand() / (RAND_MAX) << std::endl;
     
    std::cout << "met "      << met      << std::endl;
    std::cout << "metPhi "   << metPhi   << std::endl;
    std::cout << "covMet11 " << covMet11 << std::endl;
    std::cout << "covMet12 " << covMet12 << std::endl;
    std::cout << "covMet21 " << covMet21 << std::endl;
    std::cout << "covMet22 " << covMet22 << std::endl;
    // setup MET input vector
    NSVfitStandalone::Vector measuredMET(met *TMath::Cos(metPhi), met *TMath::Sin(metPhi), 0); 
    // setup the MET significance
    TMatrixD covMET(2,2);
    covMET[0][0] = covMet11;
    covMET[0][1] = covMet12;
    covMET[1][0] = covMet21;
    covMET[1][1] = covMet22;
    // setup measure tau lepton vectors 
    //NSVfitStandalone::LorentzVector l1(l1Px, l1Py, l1Pz, TMath::Sqrt(l1M*l1M+l1Px*l1Px+l1Py*l1Py+l1Pz*l1Pz));
    //NSVfitStandalone::LorentzVector l2(l2Px, l2Py, l2Pz, TMath::Sqrt(l2M*l2M+l2Px*l2Px+l2Py*l2Py+l2Pz*l2Pz));
    NSVfitStandalone::LorentzVector l1(l1Px, l1Py, l1Pz, l1E);
    NSVfitStandalone::LorentzVector l2(l2Px, l2Py, l2Pz, l2E);
    //NSVfitStandalone::LorentzVector l1;
    //NSVfitStandalone::LorentzVector l2;
//     TLorentzVector ll1;
//     TLorentzVector ll2;
//     ll1.SetPtEtaPhiM(l1Pt, l1Eta, l1Phi, l1M) ;
//     ll2.SetPtEtaPhiM(l2Pt, l2Eta, l2Phi, l2M) ;
//     NSVfitStandalone::LorentzVector l1(ll1.Px(), ll1.Py(), ll1.Pz(), ll1.E());
//     NSVfitStandalone::LorentzVector l2(ll2.Px(), ll2.Py(), ll2.Pz(), ll2.E());
    std::vector<NSVfitStandalone::MeasuredTauLepton> measuredTauLeptons;
    //measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(std::string(argv[2])==std::string("EMu") ? NSVfitStandalone::kLepDecay : NSVfitStandalone::kLepDecay, l1));
    //measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(std::string(argv[2])==std::string("EMu") ? NSVfitStandalone::kLepDecay : NSVfitStandalone::kHadDecay, l2));
    //measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay, l1));
    //measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kLepDecay, l1));
    measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay, l1));
    measuredTauLeptons.push_back(NSVfitStandalone::MeasuredTauLepton(NSVfitStandalone::kHadDecay, l2));
    // construct the class object from the minimal necesarry information
    NSVfitStandaloneAlgorithm algo(measuredTauLeptons, measuredMET, covMET, 0);
    // apply customized configurations if wanted (examples are given below)
    algo.maxObjFunctionCalls(50000);
    algo.addLogM(false);
    //algo.metPower(0.5)
    // run the fit
    algo.integrateVEGAS();
    //algo.integrateMarkovChain();
    // retrieve the results upon success
    //std::cout << "... m truth : " << mTrue  << std::endl;
    if(algo.isValidSolution()){
      std::cout << "event: " << ievent << "... m svfit : " << algo.mass() << "+/-" << algo.massUncert() << std::endl;
      evt  = ievent ;
      m_sv = algo.mass() ;
      pMyTree->Fill();
    }
    else{
      std::cout << "event: " << ievent <<  "... m svfit : ---" << std::endl;
    }
  }
  
  pMyTree->Print();
  pMyTree->Write();
  hfile.Close();
  //delete hfile;

  return;
}

int main(int argc, char* argv[]) 
{
  //eventsFromTree(argc, argv);
  singleEvent();
  return 0;
}
