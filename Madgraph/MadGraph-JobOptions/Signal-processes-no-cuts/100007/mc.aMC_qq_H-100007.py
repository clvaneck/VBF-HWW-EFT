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
set zerowidth_tchannel False
import model SMEFTatNLO-NLO
define p = g u c d s b u~ c~ d~ s~ b~
define j = g u c d s b u~ c~ d~ s~ b~
define top = t t~
generate p p > h > j j e- ve~ mu+ vm $$ z NP=2 QCD=0 QED==6 / top
add process p p > h > j j e+ ve mu- vm~ $$ z NP=2 QCD=0 QED==6 / top
add process p p > h > j j e+ ve e- ve~ $$ z NP=2 QCD=0 QED==6 / top
add process p p > h > j j mu+ vm mu- vm~ $$ z NP=2 QCD=0 QED==6 / top
output -f"""


process_dir = new_process(process,keepJpegs=True, usePMGSettings=False)

#Fetch default LO run_card.dat and set parameters
settings = {'lhe_version' : '3.0',
            'cut_decays'   : 'F',
            'maxjetflavor': 5,     #mlm
            'asrwgtflavor':5.0,     
            'ptj':10,
            'ptb':10,
            'pta':10,
            'ptl':10,
            'etaj':5,
            'etab':5,
            'etal':3.0,
            'drjj':0.1,
            'drll':0.1,
            'draa':0.1,
            'draj':0.1,
            'drjl':0.1,
            'dral':0.1,
            'mmjj':10,
            'mmbb':10,
            'dynamical_scale_choice' : '3', #default value
            'beamEnergy':beamEnergy,
            'nevents'      : int(nevents)}
modify_run_card(process_dir=process_dir,runArgs=runArgs,settings=settings)

#---------------------------------------------------------------------------
# MG5 parameter Card
#---------------------------------------------------------------------------

params={}

## Block dim6
# 2 # cpDC = 1e-8
# 3 # cpWB = 1e-8
# 4 # cdp = 1e-8
# 5 # cp = 1e-8
# 6 # cWWW = 1e-8
# 9 # cpW = 1
# 10 # cpBB = 1e-8

c_dim6={'2': '1e-8', '3' : '1e-8', '4' : '1e-8', '5' : '1e-8', '6' : '1e-8','9' : '1', '10' : '1e-8'} 

## Block dim62f
# 1 # cpl1 = 1e-8
# 2 # cpl2 = 1e-8
# 3 # cpl3 = 1e-8
# 4 # c3pl1 = 1e-8
# 5 # c3pl2 = 1e-8
# 6 # c3pl3 = 1e-8
# 7 # cpe = 1e-8
# 8 # cpmu = 1e-8
# 9 # cpta = 1e-8
# 10 # cpqMi = 1e-8
# 11 # cpq3i = 1e-8
# 12 # cpQ3 = 1e-8
# 13 # cpQM = 1e-8
# 14 # cpu = 1e-8
# 15 # cpt = 1e-8
# 16 # cpd = 1e-8
# 19 # ctp = 1e-8
# 22 # ctZ = 1e-8
# 23 # ctW = 1e-8
# 24 # ctG = 1e-8
c_dim62f={'1' : '1e-8', '2' : '1e-8', '3' : '1e-8', '4' : '1e-8', '5' : '1e-8', '6' : '1e-8', '7' : '1e-8', '8' : '1e-8', '9' : '1e-8', '10' : '1e-8', '11' : '1e-8', '12' : '1e-8', '13' : '1e-8', '14' : '1e-8', '15' : '1e-8', '16' : '1e-8', '19' : '1e-8', '22' : '1e-8', '23' : '1e-8', '24' : '1e-8'} 

## Block dim64f
# 1 # cQq83 = 1e-8
# 2 # cQq81 = 1e-8
# 3 # cQu8 = 1e-8
# 4 # ctq8 = 1e-8
# 6 # cQd8 = 1e-8
# 7 # ctu8 = 1e-8
# 8 # ctd8 = 1e-8
# 10 # cQq13 = 1e-8
# 11 # cQq11 = 1e-8
# 12 # cQu1 = 1e-8
# 13 # ctq1 = 1e-8
# 14 # cQd1 = 1e-8
# 16 # ctu1 = 1e-8
# 17 # ctd1 = 1e-8
# 19 # cQQ8 = 1e-8
# 20 # cQQ1 = 1e-8
# 21 # cQt1 = 1e-8
# 23 # ctt1 = 1e-8
# 25 # cQt8 = 1e-8
c_dim64f={'1' : '1e-8', '2' : '1e-8', '3' : '1e-8', '4' : '1e-8', '6' : '1e-8', '7' : '1e-8', '8' : '1e-8', '10' : '1e-8', '11' : '1e-8', '12' : '1e-8', '13' : '1e-8', '14' : '1e-8', '16' : '1e-8', '17' : '1e-8', '19' : '1e-8', '20' : '1e-8', '21' : '1e-8', '23' : '1e-8', '25' : '1e-8'} 

##Block dim64f2l 
# 1 # cQlM1 = 1e-8
# 2 # cQlM2 = 1e-8
# 3 # cQl31 = 1e-8
# 4 # cQl32 = 1e-8
# 5 # cQe1 = 1e-8
# 6 # cQe2 = 1e-8
# 7 # ctl1 = 1e-8
# 8 # ctl2 = 1e-8
# 9 # cte1 = 1e-8
# 10 # cte2 = 1e-8
# 13 # cQlM3 = 1e-8
# 14 # cQl33 = 1e-8
# 15 # cQe3 = 1e-8
# 16 # ctl3 = 1e-8
# 17 # cte3 = 1e-8
c_dim64f2l={'1' : '1e-8', '2' : '1e-8', '3' : '1e-8', '4' : '1e-8', '5' : '1e-8', '6' : '1e-8', '7' : '1e-8', '8' : '1e-8', '9' : '1e-8', '10' : '1e-8', '13' : '1e-8', '14' : '1e-8', '15' : '1e-8', '16' : '1e-8', '17' : '1e-8'}

##Block dim64f4l 
# 1 # cll1111 = 1e-8
# 2 # cll2222 = 1e-8
# 3 # cll3333 = 1e-8
# 4 # cll1122 = 1e-8
# 5 # cll1133 = 1e-8
# 6 # cll2233 = 1e-8
# 7 # cll1221 = 1e-8
# 8 # cll1331 = 1e-8
# 9 # cll2332 = 1e-8
c_dim64f4l={'1' : '1e-8', '2' : '1e-8', '3' : '1e-8', '4' : '1e-8', '5' : '1e-8', '6' : '1e-8', '7' : '1e-8', '8' : '1e-8', '9' : '1e-5'} 

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

