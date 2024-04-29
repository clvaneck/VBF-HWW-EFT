// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/DressedLeptons.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "Rivet/Projections/PromptFinalState.hh"
#include "Rivet/Projections/IdentifiedFinalState.hh"
#include "Rivet/Projections/ParticleFinder.hh"
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
      FastJets fastjets(fs, FastJets::ANTIKT, 0.6);
      declare(fastjets, "jets");

      PromptFinalState leps(Cuts::abspid == PID::MUON || Cuts::abspid == PID::ELECTRON);
      declare(leps, "leptons");

      IdentifiedFinalState nu_id;
      nu_id.acceptNeutrinos();
      PromptFinalState neutrinos_parton(nu_id);
      neutrinos_parton.acceptTauDecays(false);
      declare(neutrinos_parton, "neutrinos_parton");

      declare(MissingMomentum(fs), "MET");

      book(_h_M_T, "M_T", 40, 50.,800.);
      book(_h_Ptll, "Ptll", 40, 50.,1000);
      book(_h_m_ll, "m_ll",40, 50, 800);

      book(_h_V_x, "V_x", 40, 50., 1000.);
      book(_h_DEta_ll, "DEta", 20, 0., 6.);
      book(_h_DPhi_ll, "DPhi", 20, 0., 3.5);
      book(_h_DR_ll, "DR", 20, 0., 10.);
      book(_h_m_WW,"m_WW", 40, 0, 1000.);

      // Adding jet histograms
      book(_h_first_jet_pt, "First_Jet_Pt", 40, 0, 500);  // PT of the first jet
      book(_h_second_jet_pt, "Second_Jet_Pt", 40, 0, 500);  // PT of the second jet
      book(_h_HT, "HT", 40, 0, 2000);  // Scalar sum of jet PTs

    }

    /// Perform the per-event analysis
    void analyze(const Event& event) {
      const Particles& leptons = apply<PromptFinalState>(event, "leptons").particlesByPt();
      const Particles& neutrinos_parton = apply<PromptFinalState>(event, "neutrinos_parton").particlesByPt();
      const MissingMomentum& met = apply<MissingMomentum>(event, "MET");
      const Jets& jets = apply<FastJets>(event, "jets").jetsByPt(20.0);

      if (leptons.size() != 2 ) vetoEvent;

      double HT = 0;
      if (!jets.empty()) {
        _h_first_jet_pt->fill(jets[0].pt()/GeV);
        HT += jets[0].pt()/GeV;
        if (jets.size() > 1) {
          _h_second_jet_pt->fill(jets[1].pt()/GeV);
          HT += jets[1].pt()/GeV;
        }
      }
      for (size_t i = 2; i < jets.size(); ++i) {
        HT += jets[i].pt()/GeV;
      }
      _h_HT->fill(HT);

      const FourMomentum dileptons = leptons[0].mom() + leptons[1].mom();
      _h_M_T->fill((met.met() + dileptons.mass())/GeV);
      _h_Ptll->fill(dileptons.pt()/GeV);
      _h_m_ll->fill(dileptons.mass()/GeV);
      _h_V_x->fill(0.3*(met.met() + dileptons.mass())/GeV + dileptons.mass()/GeV);
      _h_DEta_ll->fill(fabs(leptons[0].eta() - leptons[1].eta()));
      _h_DPhi_ll->fill(deltaPhi(leptons[0], leptons[1]));
      _h_DR_ll->fill(deltaR(leptons[0], leptons[1]));
      _h_m_WW->fill((leptons[0].mom() + leptons[1].mom() + 
                     neutrinos_parton[0].mom() + neutrinos_parton[1].mom()).mass()/GeV);
    }

    /// Normalise histograms etc., after the run
    void finalize() {
      const double luminosity= 138965.16; //picobarn^-1
      const double scaling = crossSection() * luminosity / sumOfWeights(); //scaling factor
      scale(_h_M_T, scaling);
      scale(_h_Ptll, scaling);
      scale(_h_m_ll, scaling);
      scale(_h_V_x, scaling);
      scale(_h_DEta_ll, scaling);
      scale(_h_DPhi_ll, scaling);
      scale(_h_DR_ll, scaling);
      scale(_h_m_WW, scaling);
      scale(_h_first_jet_pt, scaling);
      scale(_h_second_jet_pt, scaling);
      scale(_h_HT, scaling);
    }

    private:
      Histo1DPtr _h_Ptll, _h_M_T, _h_m_WW, _h_m_ll, _h_V_x, _h_DEta_ll, _h_DPhi_ll, _h_DR_ll;
      Histo1DPtr _h_first_jet_pt, _h_second_jet_pt, _h_HT;
  };

  DECLARE_RIVET_PLUGIN(MY_ANALYSIS);
}
