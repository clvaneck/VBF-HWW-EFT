## This file will explain how to run a sample generation, using a MadGraph job option in the Athena framework

First of all, you need to create a folder where you are going to run your generation.
In this folder, you need to create another folder that HAS to be named with the DSID of the process you want to generate
In this DSID-named folder, you are going to put the MadGraph job option. And then you can run your bash scripts containing the
running parameters (cf. submission-scripts folder in the repo)
e.g.

I want to generate the process with a DSID=10000X, then the folder will look like that:
run-10000X
    10000X
        MadGraph-JO.py
        run-submission.sh <<- this run file is the submission (to the cluster) file that you can find in the Bash-scripts folder


### For the background process and the SBI process, the job option will be slightly different as they will include a so-called gridpack calculation

For the B and the SBI, the gridpack is necessary as the processes are way more complicated (way more diagrams to generate as one have to account for every different quark).
The gridpack mode of the job option allows the calculation of the matrix element to be done in parallel, splitted in different GPUs. The running file for the gridpack is in Bash-scripts/run-gridpack
This will create a file with extension .GRID.tar.gz that you will have to put in the folder where you want to run the events generation.

Once the gridpack generation is done. Create another running folder, with again a folder that has the same name as the DSID
and put in this folder the MadGraph job option (python file) as well as the .GRID.tar.gz file. Then submit the calculation to the cluster (Bash-scripts/run-submission.sh).
