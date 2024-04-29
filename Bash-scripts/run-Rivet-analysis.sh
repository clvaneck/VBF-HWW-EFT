# This run file is used to run the Rivet analysis on your computer. You can also submit this code to the cluster by
# typing bsub -J [name of your submission] running-analyis.sh. To run this, you need to be in the repository where you
# want to create your histogram file, with extension .yoda.gz. The best is to name it run-dsid


setupATLAS
asetup 21.6.77,AthGeneration # or later (please avoid 21.6.19-21.6.32)
source setupRivet.sh

athena /project/atlas/users/smugnier/RivetRoutine/HWWOffshell_test_ana/JO/HWW_ATLAS_JO_x.py

# here you should put the path to your Rivet job option, I advise you to nicely organise your folders in order to avoid any confusion.
# The Rivet job option is the file that contains the Rivet analysis you want to run.
