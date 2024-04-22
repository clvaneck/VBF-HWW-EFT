# This code allows to compile the C++ code into a usable .so file, which is the analysis itself.
setupATLAS
asetup 21.6.77,AthGeneration # or later (please avoid 21.6.19-21.6.32)
source setupRivet.sh #This line allow to download the Rivet package.

rivet-build RivetMY_ANALYSIS.so MY_ANALYSIS.cc
