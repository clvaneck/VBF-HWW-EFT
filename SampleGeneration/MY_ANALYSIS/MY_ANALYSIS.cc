// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Event.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh" // Include FastJets for jet clustering
#include "Rivet/Projections/DressedLeptons.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "Rivet/Projections/PromptFinalState.hh"
#include "Rivet/Projections/VetoedFinalState.hh"
#include "Rivet/Projections/DISFinalState.hh"
#include "Rivet/Projections/WFinder.hh"
#include "Rivet/Particle.hh"

namespace Rivet {

  /// @brief Add a short analysis description here
  class MY_ANALYSIS : public Analysis {
  public:

    /// Constructor
    DEFAULT_RIVET_ANALYSIS_CTOR(MY_ANALYSIS);

    /// @name Analysis methods
    ///@{

    /// Book histograms and initialise projections before the run
    void init() {
      // Initialise and register projections
      const FinalState fs(Cuts::abseta < 4.9);

      // Declare FastJets projection
      FastJets fastjets(fs, FastJets::ANTIKT, 0.4);
      declare(fastjets, "Jets");

      PromptFinalState leps(Cuts::abspid == PID::MUON || Cuts::abspid == PID::ELECTRON);
      declare(leps, "leptons");

      IdentifiedFinalState nu_id;
      nu_id.acceptNeutrinos();
      PromptFinalState neutrinos_parton(nu_id);
      neutrinos_parton.acceptTauDecays(false);
      declare(neutrinos_parton, "neutrinos_parton");

      declare(MissingMomentum(fs), "MET");

      // Book histograms
      book(_h_M_T, "M_T", 40, 50., 800.);
      book(_h_Ptll, "Ptll", 40, 50., 1000);
      book(_h_m_ll, "m_ll", 40, 50, 800);
      book(_h_V_x, "V_x", 40, 50., 1000.);
      book(_h_DEta_ll, "DEta", 20, 0., 6.);
      book(_h_DPhi_ll, "DPhi", 20, 0., 3.5);
      book(_h_DR_ll, "DR", 20, 0., 10.);
      book(_h_m_WW, "m_WW", 40, 0, 1000.);
      book(_h_jet_pT, "jet_pT", 40, 0., 1000.);  // New histogram for leading jet pT

    }

    /// Perform the per-event analysis
    void analyze(const Event& event) {
      const Particles& leptons = apply<PromptFinalState>(event, "leptons").particlesByPt();
      const Particles& neutrinos_parton = apply<ParticleFinder>(event, "neutrinos_parton").particlesByPt();
      const MissingMomentum& met = apply<MissingMomentum>(event, "MET");

      if (leptons.size() != 2) vetoEvent;
      const FourMomentum dileptons = leptons[0].mom() + leptons[1].mom();

      // Get jets and sort by pT
      Jets jets = apply<FastJets>(event, "Jets").jetsByPt(Cuts::pT > 20*GeV && Cuts::absrap < 4.5);
      if (!jets.empty()) {
        const double jet_pT = jets[0].pt() / GeV; // Leading jet pT
        _h_jet_pT->fill(jet_pT);  // Fill histogram for leading jet pT
      }

      // Existing analysis code...
      const double mll = dileptons.mass() / GeV;
      _h_m_ll->fill(mll);
      // More histogram fills...

    }

    /// Normalise histograms etc., after the run
    void finalize() {
      const double luminosity = 138965.16; // picobarn^-1
      const double scaling = crossSection() * luminosity / sumOfWeights();
      scale(_h_M_T, scaling);
      scale(_h_m_ll, scaling);
      scale(_h_Ptll, scaling);
      scale(_h_m_WW, scaling);
      scale(_h_V_x, scaling);
      scale(_h_DEta_ll, scaling);
      scale(_h_DPhi_ll, scaling);
      scale(_h_DR_ll, scaling);
      scale(_h_jet_pT, scaling);  // Scale the new histogram
    }

    ///@}
    /// @name Histograms
    ///@{
    private :
      Histo1DPtr _h_Ptll, _h_M_T, _h_m_WW, _h_m_ll, _h_V_x, _h_DEta_ll, _h_DPhi_ll, _h_DR_ll, _h_jet_pT;  // Added _h_jet_pT
    ///@}
  };

  DECLARE_RIVET_PLUGIN(MY_ANALYSIS);
}
