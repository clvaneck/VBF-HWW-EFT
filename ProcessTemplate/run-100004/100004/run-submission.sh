# This file allow to ubmit the event generation to the cluster, so that you don't have to run it on your own computer.
# Before running the following line, make sur that you are in the repository SampleGeneration/Process/run-DSID/DSID. Otherwise the
# commane disd="$(basename $PWD)" will not work.
# You can change the DATADIR to the place where all your running files are going to end up.
# The lines in the end that are creating the directories are not necessary, but were used to centralise all the EVNT files in one place.

# setupATLAS
# asetup 21.6.77,AthGeneration # or later (please avoid 21.6.19-21.6.32)
# source setupRivet.sh

dsid="100004"
JOname="aMC_qq_H"
DATADIR=/project/atlas/users/cvaneck/Process/run-${dsid}

#!/bin/bash
Gen_tf.py --ecmEnergy=13000.0 \
    --randomSeed=$RANDOM \
    --jobConfig=${DATADIR}/${dsid} \
    --runNumber=${dsid} \
    --outputEVNTFile=${dsid}.EVNT.ROOT \
    --maxEvents=10000

mkdir -p /project/atlas/users/cvaneck/Process/HWW/${dsid}-i-or-q
mkdir -p /project/atlas/users/cvaneck/Process/HWW/${dsid}-i-or-q/EVNT
mv ${dsid}.EVNT.ROOT /project/atlas/users/cvaneck/Process/HWW/${dsid}-i-or-q/EVNT/${dsid}.EVNT.ROOT

cd ${DATADIR}