setupATLAS
asetup 21.6.77,AthGeneration
source setupRivet.sh

dsid="$(basename $PWD)"
cd ..
JOname="aMC_gg_to_H_to_WW_2l2v_EFT"
DATADIR=/data/atlas/users/smugnier/SampleGeneration/Processes/run-${dsid}-grid-i-or-q/

SCRIPT=${PWD}/generate_gridpack.sh
cat <<EOF > ${SCRIPT}
#!/bin/bash
Gen_tf.py --ecmEnergy=13000.0 \
    --randomSeed=$RANDOM \
    --jobConfig=${DATADIR}/${dsid} \
    --runNumber=${dsid} \
    --outputEVNTFile=${dsid}.EVNT.ROOT \
    --maxEvents=10000 ## This is the number of events you want to generate but has no impact in the gridpack generation as it is only the matrix elements calculation.

EOF

bsub -J running-name -l nodes=1:ppn=16 source generate_gridpack.sh # Here you are allowing the usage of 16 cores.
