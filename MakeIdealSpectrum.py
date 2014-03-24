import ROOT
ROOT.gROOT.SetBatch()
ROOT.gSystem.Load("libEXOCalibUtilities")

bb0nchain = ROOT.TChain('tree')
bb0nchain.Add('/nfs/slac/g/exo_data2/exo_data/data/MC/P3_nersc8274/bb0n/*.root')
bb2nchain = ROOT.TChain('tree')
bb2nchain.Add('/nfs/slac/g/exo_data2/exo_data/data/MC/P3_nersc8274/bb2n/*.root')


ofile = ROOT.TFile("IdealSpectrumHists.root", "recreate")
spectrum_bb0n_hist = ROOT.TH1D("hist_bb0n", "", 520, 0., 2600.)
spectrum_bb2n_hist = ROOT.TH1D("hist_bb2n", "", 520, 0., 2600.)
bb0nchain.Draw("fMonteCarloData.fTotalEnergyInLiquidXe*(1 + .0153*EXOMiscUtil::GetGaussVar())>>hist_bb0n",
              "fMonteCarloData.fTotalEnergyInLiquidXe > 0")
bb2nchain.Draw("fMonteCarloData.fTotalEnergyInLiquidXe*(1 + .0153*EXOMiscUtil::GetGaussVar())>>hist_bb2n",
              "fMonteCarloData.fTotalEnergyInLiquidXe > 0")
spectrum_bb0n_hist.Write()
spectrum_bb2n_hist.Write()
ofile.Close()
