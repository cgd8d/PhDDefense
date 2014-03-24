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

dummy_hist = ROOT.TH2D("dummy_hist", "", 100, 0., 2700, 100, 0, 1)
dummy_hist.GetXaxis().SetTitle("Summed Electron Energy (keV)")
dummy_hist.GetYaxis().SetTitle("Rate (arbitrary units)")
dummy_hist.Draw()

bb0n_hist.Scale(0.13)
bb0n_hist.Scale(1./35000)
bb2n_hist.Scale(1./35000)
bb2n_hist.Draw("same")
#bb0n_hist.SetLineColor(ROOT.TColor.GetColorDark(ROOT.kRed))
bb0n_hist.Draw("same")

bb2n_text = ROOT.TLatex(850, .8, "#beta#beta2#nu")
bb2n_text.SetTextAlign(21)
bb2n_text.Draw()

bb0n_text = ROOT.TLatex(2457, .8, "#beta#beta0#nu")
bb0n_text.SetTextAlign(21)
bb0n_text.Draw()
bb0n_text_question = ROOT.TLatex(2457, .78, "?")
bb0n_text_question.SetTextAlign(23)
bb0n_text_question.Draw()

c.SaveAs("IdealSpectrum.pdf")
