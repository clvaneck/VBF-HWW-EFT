
OUTPUTDIR=/project/atlas/users/cvaneck/SampleGeneration/Process/plots #Here you have to pick the output directory of your plot


# Before running the following line, make sur that you did
# setupATLAS
# asetup 21.6.77,AthGeneration # or later (please avoid 21.6.19-21.6.32)
# source setupRivet.sh
# to have access to the rivet commands

rivet-cmphistos /project/atlas/users/cvaneck/SampleGeneration/Process/HWW_ATLAS.yoda.gz:"Title=$ qq \rightarrow H \rightarrow WW, S$:DefaultWeight=Default:Variations=none" \
           --config /project/atlas/users/cvaneck/SampleGeneration/MY_ANALYSIS/MY_ANALYSIS.plot \
           --outdir ${OUTPUTDIR} \
           --errs

cd ${OUTPUTDIR}

# You can plot as many histograms you want on the same graph, just be careful to give them the same name in the rivet.RunName command in the Rivet job option.
make-plots *dat # Make plots out of the data file create with the rivet-cmphistos command
pdfjoin -o combined_plots_name.pdf *.pdf # Combines all the plots in one pdf file
