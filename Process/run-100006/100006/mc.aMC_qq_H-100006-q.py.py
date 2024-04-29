##100006 ctp

from MadGraphControl.MadGraphUtils import *
from MadGraphControl.MadGraph_NNPDF30NLO_Base_Fragment import *


#----------------------------------------------------------------------------
# Random Seed
#----------------------------------------------------------------------------
randomSeed = 0
if hasattr(runArgs,'randomSeed'): randomSeed = runArgs.randomSeed

#----------------------------------------------------------------------------
# Beam energy
#----------------------------------------------------------------------------
if hasattr(runArgs,'ecmEnergy'):
    beamEnergy = int(runArgs.ecmEnergy) / 2.
else:
    raise RunTimeError("No center of mass energy found.")

#---------------------------------------------------------------------------
# Number of Events
#---------------------------------------------------------------------------
safefactor=1.2
if hasattr(runArgs,'maxEvents') and runArgs.maxEvents > 0:  nevents = int(runArgs.maxEvents)*safefactor
else: nevents = nevents*safefactor
process="""
set complex_mass_scheme True
set max_npoint_for_channel 4
define p = g u c d s b u~ c~ d~ s~ b~
define j = g u c d s b u~ c~ d~ s~ b~
import model /project/atlas/users/smugnier/MG5_aMC_v3_5_1/models/SMEFTatNLO-NLO
generate g g > h > l+ l- vl vl~ /z a  NP^2==4 QCD=2 QED=4 [QCD]
output -f"""

process_dir = new_process(process,keepJpegs=True, usePMGSettings=False)

#Fetch default LO run_card.dat and set parameters
settings = {'lhe_version' : '3.0',
           'cut_decays'   : 'F',
            'maxjetflavor': 5,     #mlm
            'pta':0.0,
            'ptj':0.0,
            'ptb':0.0,
            'ptl':5,
            'draa':0.0,
            'drll':0.0,
            'drjl':0.0,
            'drjj':0.0,
            'etaj':5,
            'etal':3,
            'dynamical_scale_choice' : '3', #default value
            'beamEnergy':beamEnergy,
           'nevents'      : int(nevents)}
modify_run_card(process_dir=process_dir,runArgs=runArgs,settings=settings)

#---------------------------------------------------------------------------
# MG5 parameter Card
#---------------------------------------------------------------------------

params={}

## Block dim6
# 2 # cpDC = 0
# 3 # cpWB = 0
# 4 # cdp = 0
# 5 # cp = 0
# 6 # cWWW = 0
# 9 # cpW = 0
# 10 # cpBB = 0

c_dim6={'2': '0', '3' : '0', '4' : '0', '5' : '0', '6' : '0','9' : '0', '10' : '0'} 

## Block dim62f
# 1 # cpl1 = 0
# 2 # cpl2 = 0
# 3 # cpl3 = 0
# 4 # c3pl1 = 0
# 5 # c3pl2 = 0
# 6 # c3pl3 = 0
# 7 # cpe = 0
# 8 # cpmu = 0
# 9 # cpta = 0
# 10 # cpqMi = 0
# 11 # cpq3i = 0
# 12 # cpQ3 = 0
# 13 # cpQM = 0
# 14 # cpu = 0
# 15 # cpt = 0
# 16 # cpd = 0
# 19 # ctp = 1
# 22 # ctZ = 0
# 23 # ctW = 0
# 24 # ctG = 0
c_dim62f={'1' : '0', '2' : '0', '3' : '0', '4' : '0', '5' : '0', '6' : '0', '7' : '0', '8' : '0', '9' : '0', '10' : '0', '11' : '0', '12' : '0', '13' : '0', '14' : '0', '15' : '0', '16' : '0', '19' : '1', '22' : '0', '23' : '0', '24' : '0'} 

## Block dim64f
# 1 # cQq83 = 0
# 2 # cQq81 = 0
# 3 # cQu8 = 0
# 4 # ctq8 = 0
# 6 # cQd8 = 0
# 7 # ctu8 = 0
# 8 # ctd8 = 0
# 10 # cQq13 = 0
# 11 # cQq11 = 0
# 12 # cQu1 = 0
# 13 # ctq1 = 0
# 14 # cQd1 = 0
# 16 # ctu1 = 0
# 17 # ctd1 = 0
# 19 # cQQ8 = 0
# 20 # cQQ1 = 0
# 21 # cQt1 = 0
# 23 # ctt1 = 0
# 25 # cQt8 = 0
c_dim64f={'1' : '0', '2' : '0', '3' : '0', '4' : '0', '6' : '0', '7' : '0', '8' : '0', '10' : '0', '11' : '0', '12' : '0', '13' : '0', '14' : '0', '16' : '0', '17' : '0', '19' : '0', '20' : '0', '21' : '0', '23' : '0', '25' : '0'} 

##Block dim64f2l 
# 1 # cQlM1 = 0
# 2 # cQlM2 = 0
# 3 # cQl31 = 0
# 4 # cQl32 = 0
# 5 # cQe1 = 0
# 6 # cQe2 = 0
# 7 # ctl1 = 0
# 8 # ctl2 = 0
# 9 # cte1 = 0
# 10 # cte2 = 0
# 13 # cQlM3 = 0
# 14 # cQl33 = 0
# 15 # cQe3 = 0
# 16 # ctl3 = 0
# 17 # cte3 = 0
c_dim64f2l={'1' : '0', '2' : '0', '3' : '0', '4' : '0', '5' : '0', '6' : '0', '7' : '0', '8' : '0', '9' : '0', '10' : '0', '13' : '0', '14' : '0', '15' : '0', '16' : '0', '17' : '0'}

##Block dim64f4l 
# 1 # cll1111 = 0
# 2 # cll2222 = 0
# 3 # cll3333 = 0
# 4 # cll1122 = 0
# 5 # cll1133 = 0
# 6 # cll2233 = 0
# 7 # cll1221 = 0
# 8 # cll1331 = 0
# 9 # cll2332 = 0
c_dim64f4l={'1' : '0', '2' : '0', '3' : '0', '4' : '0', '5' : '0', '6' : '0', '7' : '0', '8' : '0', '9' : '0'} 

params['dim6'] =c_dim6
params['dim62f']=c_dim62f
params['dim64f'] =c_dim64f
params['dim64f2l']=c_dim64f2l
params['dim64f4l']=c_dim64f4l

modify_param_card(process_dir=process_dir,params=params)

print_cards()

#---------------------------------------------------------------------------
# MG5 + Pythia8 setup
#---------------------------------------------------------------------------



generate(process_dir=process_dir,runArgs=runArgs)
arrange_output(process_dir=process_dir,runArgs=runArgs,lhe_version=3,saveProcDir=True)  

# Helper for resetting process number
check_reset_proc_number(opts)

#### Shower 
evgenConfig.description = 'aMcAtNlo_H_WW'
evgenConfig.keywords+=['Higgs','2lepton', 'WW']

include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
include("Pythia8_i/Pythia8_MadGraph.py")

