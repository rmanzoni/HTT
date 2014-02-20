import ROOT
from ROOT import TFile, TTree, TH1F, gDirectory, gROOT, gStyle, TCanvas, TLegend, gPad

### style parameters
gROOT.SetStyle("Plain")
gROOT.SetBatch(True)
gStyle.SetLegendFillColor(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetStatBorderSize(0)
gStyle.SetTitleBorderSize(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetTitleX(0.125)
gStyle.SetTitleY(0.96)
gStyle.SetTitleW(0.8)
gStyle.SetTextFont(42)
gStyle.SetLegendFont(42)
gStyle.SetOptStat(False)

f1 = TFile.Open('ggh125_ggh125_12_5_percent_smear1.root','r')
# f1 = TFile.Open('ggh125_tau1_tau2.root','r')
# f1 = TFile.Open('ggh125_tau2_tau1_2p5.root','r')
tree1 = gDirectory.FindObjectAny('SimpleTree')
tree1.SetLineColor(ROOT.kRed)
tree1.SetLineWidth(2)

f2 = TFile.Open('ggh125_ggh125_12_5_percent_smear2.root','r')
# f2 = TFile.Open('ggh125_tau1_tau2_2p5.root','r')
# f2 = TFile.Open('ggh125_tau2_tau1.root','r')
tree2 = gDirectory.FindObjectAny('SimpleTree')
tree2.SetLineColor(ROOT.kBlue)
tree2.SetLineWidth(2)

f3 = TFile.Open('ggh125_ggh125_12_5_percent_smear3.root','r')
# f3 = TFile.Open('ggh125_tau1_tau2.root','r')
tree3 = gDirectory.FindObjectAny('SimpleTree')
tree3.SetLineColor(ROOT.kBlack)
tree3.SetLineWidth(2)
# tree3.SetLineStyle(3)



h1 = TH1F('ggH125','ggH125',35,0,350)
h1.GetXaxis().SetTitle('m_{#tau#tau}')
# h1 = TH1F('ggH125','ggH125',40,0,200)
# h1.GetXaxis().SetTitle('ME_{T}')
h1.GetYaxis().SetTitle('events')
h1.GetYaxis().SetTitleOffset(1.6)


l1 = TLegend(0.5,0.7,0.88,0.88)
# l1.AddEntry(tree1,"#tau_{1}#tau_{2}, 0.1% step")
# l1.AddEntry(tree2,"#tau_{2}#tau_{1}, 0.1% step")
# l1.AddEntry(tree1,"#tau_{2}#tau_{1}, 2.5% step")
# l1.AddEntry(tree2,"#tau_{1}#tau_{2}, 2.5% step")
# l1.AddEntry(tree3,"#tau_{1}#tau_{2}, 0.1% step")
l1.AddEntry(tree1,"#tau_{1}#tau_{2}, 2.5% step, smear 1")
l1.AddEntry(tree2,"#tau_{1}#tau_{2}, 2.5% step, smear 2")
l1.AddEntry(tree3,"#tau_{1}#tau_{2}, 2.5% step, smear 3")
l1.SetFillColor(0)


c1 = TCanvas('','',700,700)
gPad.SetLeftMargin(0.15)

# tree1.Draw("met>>ggH125")
# tree1.Draw("met","","SAME")
# tree2.Draw("met","","SAME")
# tree3.Draw("met","","SAME")

tree1.Draw("m_sv>>ggH125")
tree1.Draw("m_sv","","SAME")
tree2.Draw("m_sv","","SAME")
tree3.Draw("m_sv","","SAME")
l1.Draw('sameAEPZ')
c1.SaveAs('bla.pdf')
