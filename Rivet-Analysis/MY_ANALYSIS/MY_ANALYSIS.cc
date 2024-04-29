// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Event.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
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

      // The basic final-state projection:
      // all final-state particles within
      // the given eta acceptance
      const FinalState fs(Cuts::abseta < 4.9);

      // FinalState of prompt muons and electrons in the event
     
      PromptFinalState leps(Cuts::abspid == PID::MUON || Cuts::abspid == PID::ELECTRON);
      declare(leps, "leptons");

    // Projection to find neutrinos to produce parton level W's 
      IdentifiedFinalState nu_id;
      nu_id.acceptNeutrinos();
      PromptFinalState neutrinos_parton(nu_id);
      neutrinos_parton.acceptTauDecays(false);
      declare(neutrinos_parton, "neutrinos_parton");


      // Missing momentum
      declare(MissingMomentum(fs), "MET");

      // dileptons histograms

      book(_h_M_T, "M_T", 40, 50.,800.);
      book(_h_Ptll, "Ptll", 40, 50.,1000);
      book(_h_m_ll, "m_ll",40, 50, 800);

      // Other observables histograms
      book(_h_V_x, "V_x", 40, 50., 1000.);
      book(_h_DEta_ll, "DEta", 20, 0., 6.);
      book(_h_DPhi_ll, "DPhi", 20, 0., 3.5);
      book(_h_DR_ll, "DR", 20, 0., 10.);

      //WW boson plots
      book(_h_m_WW,"m_WW", 40, 0, 1000.);

    }


    /// Perform the per-event analysis
    void analyze(const Event& event) {

      // Retrieve dressed leptons, Missing Momentum
      const Particles& leptons = apply<PromptFinalState>(event, "leptons").particlesByPt();
      const Particles& neutrinos_parton = apply<ParticleFinder>(event, "neutrinos_parton").particlesByPt();
      const MissingMomentum& met = apply<MissingMomentum>(event, "MET");

      if (leptons.size()!=2 ) vetoEvent;
      const FourMomentum dileptons = leptons[0].mom() + leptons[1].mom() ; //Dilepton 4-momentum
      const FourMomentum neutrino0_p = neutrinos_parton.size()>0 ? neutrinos_parton[0].momentum() : FourMomentum(0,0,0,0);
      const FourMomentum neutrino1_p = neutrinos_parton.size()>1 ? neutrinos_parton[1].momentum() : FourMomentum(0,0,0,0);
      const FourMomentum lep0_p = leptons.size()>0 ? leptons[0].momentum() : FourMomentum(0,0,0,0);
      const FourMomentum lep1_p = leptons.size()>1 ? leptons[1].momentum() : FourMomentum(0,0,0,0);

     
    // Calculation of Observables

      //Dilepton observables

      const double mll = dileptons.mass()/GeV ;
      const double DEta_ll = leptons.size()>1 ? fabs(deltaEta(leptons[0], leptons[1])) : -7 ; //-7 is a random negative number that I picked
      const double DPhi_ll = leptons.size()>1 ? fabs(deltaPhi(leptons[0], leptons[1])) : -7;
      const double DR_ll = leptons.size()>1 ? fabs(deltaR(leptons[0],leptons[1])): -7;

      // Calculation of the transverse quantities

      Vector3 dileptons_tvec(dileptons.px(), dileptons.py(),0); //Transverse projection of the dilepton momentum vector
      Vector3 met_tvec = met.vectorMissingPt(); //
      double E_ll_T = std::sqrt(dileptons_tvec.mod2()+dileptons.mass()*dileptons.mass());

      //Calculation of the transverse mass of lvlv
      const double mt_lvlv = std::sqrt(std::abs(std::pow(E_ll_T + met.met(),2)-(dileptons_tvec+ met_tvec).mod2()));

      // Calculation of Vx/1

      const double v_x = 0.3*mt_lvlv + mll ; 
      
      //Calculation of the Transverse momentum of the leptons
      const double ptll = dileptons.pT()/GeV ;

      // Calculation of WW mass
      
      const FourMomentum p_WW = lep0_p+lep1_p+neutrino0_p+neutrino1_p;
      const double m_WW = p_WW.mass();

    // Filling histograms
      
      _h_M_T->fill(mt_lvlv);
      _h_m_ll->fill(mll);
      _h_Ptll->fill(ptll);
      _h_m_WW->fill(m_WW);
      _h_V_x->fill(v_x);
      _h_DEta_ll->fill(DEta_ll);
      _h_DPhi_ll->fill(DPhi_ll);
      _h_DR_ll->fill(DR_ll);
    }


    /// Normalise histograms etc., after the run
    void finalize() {
    const double luminosity= 138965.16; //picobarn^-1
    const double scaling = crossSection() * luminosity /sumOfWeights() ; //scaling;
    scale(_h_M_T, scaling);
    scale(_h_m_ll, scaling);
    scale(_h_Ptll, scaling);
    scale(_h_m_WW, scaling);
    scale(_h_V_x, scaling);
    scale(_h_DEta_ll, scaling);
    scale(_h_DPhi_ll, scaling);
    scale(_h_DR_ll, scaling);


    }

    ///@}

    /// @name Histograms
    ///@{
    private :

   Histo1DPtr _h_Ptll;
   Histo1DPtr _h_M_T;
   Histo1DPtr _h_m_WW;
   Histo1DPtr _h_m_ll;
   Histo1DPtr _h_V_x;
   Histo1DPtr _h_DEta_ll;
   Histo1DPtr _h_DPhi_ll;
   Histo1DPtr _h_DR_ll;   
 

    ///@}
  };

  DECLARE_RIVET_PLUGIN(MY_ANALYSIS);}
