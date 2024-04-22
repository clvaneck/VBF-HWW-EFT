## This file is the skeleton of a Rivet job option. Rivet allows to run a set of analyses on a given set of events.
## for example, one can compute the transverse mass of the W boson, the invariant mass of the leptons, the pseudorapidity of the letpons, etc.

import glob


theApp.EvtMax = -1

import AthenaPoolCnvSvc.ReadAthenaPool

# POINT TO YOR FILES HERE, in my case I stored all my EVNT files in dcache because it's the fastest way to access them
input = glob.glob('/project/atlas/users/cvaneck/SampleGeneration/Process/HWWOffshellEFT-ggF/100004-i-or-q/EVNT/100004.EVNT.ROOT')
svcMgr.EventSelector.InputCollections = input
svcMgr += CfgMgr.AthenaEventLoopMgr(EventPrintoutInterval=100)
svcMgr.MessageSvc.OutputLevel = INFO
svcMgr.MessageSvc.defaultLimit = 500

from AthenaCommon.AlgSequence import AlgSequence
job = AlgSequence()

from Rivet_i.Rivet_iConf import Rivet_i
rivet = Rivet_i()
import os
# Here you should give the path to your analysis, which is the compile C++ code that will compute histograms out of the events that you gave it.
rivet.AnalysisPath = '/project/atlas/users/cvaneck/SampleGeneration/MY_ANALYSIS'
# Here you give the name of the analysis you will use
rivet.Analyses += ['MY_ANALYSIS']
rivet.RunName = 'HWWOffshell'
rivet.HistoFile = 'HWW_ATLAS.yoda.gz'
# Really important here, you should give the cross section of your process in nano-barns, you can find it in the log.generate file after typing MetaData: cross-section
rivet.CrossSection =  37.26 # unit = nb
job += rivet 
