import ROOT
ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

ifile = ROOT.TFile('IdealSpectrumHists.root')
bb0n_hist = ifile.Get("hist_bb0n")
bb2n_hist = ifile.Get("hist_bb2n")

c = ROOT.TCanvas("c", "c", 600, 400)
c.SetFillColor(ROOT.kWhite)
c.SetRightMargin(.02)
c.SetTopMargin(.02)
c.SetBottomMargin(.11)

dummy_hist = ROOT.TH2D("dummy_hist", "", 100, 0., 2700, 100, 0, 1)
dummy_hist.GetXaxis().SetTitle("Summed Electron Energy (keV)")
dummy_hist.GetYaxis().SetTitle("Rate (arbitrary units)")
dummy_hist.GetXaxis().SetLabelSize(.05)
dummy_hist.GetYaxis().SetLabelSize(.05)
dummy_hist.GetXaxis().SetTitleSize(.05)
dummy_hist.GetYaxis().SetTitleSize(.05)
dummy_hist.Draw()

bb0n_hist.Scale(200./bb0n_hist.GetSumOfWeights())
bb2n_hist.Scale(200./bb2n_hist.GetSumOfWeights())

bb0n_hist.Scale(1./(1.1e4/2.165)) # Scale realistically
bb0n_hist.Scale(10) # Adjust for visibility

#bb0n_hist.Scale(0.13)
#bb0n_hist.Scale(1./35000)
#bb2n_hist.Scale(1./35000)
bb2n_hist.Draw("same")
#bb0n_hist.SetLineColor(ROOT.TColor.GetColorDark(ROOT.kRed))
bb0n_hist.Draw("same")

bb2n_text1 = ROOT.TLatex(850, .56, "#beta#beta2#nu")
bb2n_text2 = ROOT.TLatex(850, .5, "T_{1/2} = 2.165 #times 10^{21} yrs")
bb2n_text1.SetTextAlign(21)
bb2n_text1.Draw()
bb2n_text2.SetTextAlign(21)
bb2n_text2.Draw()

bb0n_text = ROOT.TLatex(2680, .64, "#beta#beta0#nu?")
bb0n_text.SetTextAlign(31)
bb0n_text.Draw()
bb0n_text_question = ROOT.TLatex(2680, .62, "Shows T_{1/2} = 1.1 #times 10^{24} yrs")
bb0n_text_question2 = ROOT.TLatex(2680, .54, "(Actual limit 10x stronger)")
bb0n_text_question.SetTextAlign(33)
bb0n_text_question.Draw()
bb0n_text_question2.SetTextAlign(33)
bb0n_text_question2.Draw()


c.SaveAs("IdealSpectrum.pdf")
