# This file allow to ubmit the event generation to the cluster, so that you don't have to run it on your own computer.
# Before running the following line, make sur that you are in the repository SampleGeneration/Process/run-DSID/DSID. Otherwise the
# commane disd="$(basename $PWD)" will not work.
# You can change the DATADIR to the place where all your running files are going to end up.
# The lines in the end that are creating the directories are not necessary, but were used to centralise all the EVNT files in one place.

setupATLAS
asetup 21.6.77,AthGeneration # or later (please avoid 21.6.19-21.6.32)
source setupRivet.sh

dsid="$(basename $PWD)"
cd ..
JOname="aMC_gg_to_H_to_WW_2l2v_EFT"
DATADIR=/project/atlas/users/cvaneck/SampleGeneration/Process/run-${dsid}

for jobid in {1..10}
do
mkdir -p ${DATADIR}/${dsid}/${dsid}.${jobid}
cd ${DATADIR}/${dsid}/${dsid}.${jobid}
SCRIPT=${PWD}/generate_${jobid}.sh
cat <<EOF > ${SCRIPT}
#!/bin/bash
Gen_tf.py --ecmEnergy=13000.0 \
    --randomSeed=$RANDOM \
    --jobConfig=${DATADIR}/${dsid} \
    --runNumber=${dsid} \
    --outputEVNTFile=${dsid}.EVNT.${jobid}.ROOT \
    --maxEvents=10000

mkdir -p /project/atlas/users/cvaneck/SampleGeneration/Process/HWWOffshellEFT-ggF/${dsid}-i-or-q
mkdir -p /project/atlas/users/cvaneck/SampleGeneration/Process/HWWOffshellEFT-ggF/${dsid}-i-or-q/EVNT
mv ${dsid}.EVNT.${jobid}.ROOT /project/atlas/users/cvaneck/SampleGeneration/Process/HWWOffshellEFT-ggF/${dsid}-i-or-q/EVNT/${dsid}.EVNT.${jobid}.ROOT
EOF

bsub -J ${dsid}.${jobid} ${DATADIR}/${dsid}/${dsid}.${jobid}/generate_${jobid}.sh

cd ${DATADIR}

done