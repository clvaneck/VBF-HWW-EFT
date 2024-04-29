This file gives a description of all the DSIDs (number that is a reference to a particular process) of the processes I've generated.

Syntax precision in the job option:
- NP=2: generateSM and both linear and quadratic EFT
- NP=1: generate SM with linear EFT terms
- NP^2==2: generation of only linear EFT terms
- NP^2==4: generation of only quadratic EFT terms
- [QCD]: loop diagrams generation (needed for ggF)

NB: in every job option, the model loaded is pointing toward my Nikhef repository, however all the necessary model files are in this repository Madgraph/models.
When you import a model you can import a modified model by creating a copy of the parameter card of your choice (restrict_NLO.dat or restrict_LO.dat) and rename it restrict_arg.dat. 
Then you can call it by typing `import model Madgraph/models/SMEFTatNLO-arg`.


## SIGNAL processes (ggF: gg -> h -> lvlv)

The DSIDs starts at 100004, I used 100000 to 100003 to make some tests in the beginning and I haven't reinitialise the numbers.
The -i/q after the DSID stand for "interference EFT", which are linear EFT terms, and "quadratic EFT"

    100004 : Standard Model only, all EFT operators are set to zero

    100005 : Used only for initial testing

    100006-i/q : EFT operator ctp=1 with only linear/quadratic terms generated

    100007-i/q : EFT operator cpW=1 with only linear/quadratic terms generated

    100008-i/q : EFT operator ctG=1 with only linear/quadratic terms generated

    100009-i/q : EFT operator cpDc=1 with only linear/quadratic terms generated

    100010-i/q : EFT operator cdp=1 with only linear/quadratic terms generated

    100011-i/q : EFT operator c3pl1=1 with only linear/quadratic terms generated

    100012-i/q : EFT operator c3pl2=1 with only linear/quadratic terms generated

    100013-i/q : EFT operator cll1221=1 with only linear/quadratic terms generated
    
    100014-i/q : EFT operator cpG=1 with only linear/quadratic terms generated


## BACKGROUND processes (gg -> e+ mu- ve vm~ without Higgs)

The DSIDs starts at 100100.
The -i/q after the DSID stand for "interference EFT", which are linear EFT terms, and "quadratic EFT"

    100100 : Standard Model only, all EFT operators are set to zero

    100101-i/q : EFT operator cll1221=1 with only linear/quadratic terms generated

    100102-i/q : EFT operator cQl31=1 with only linear/quadratic terms generated

    100103-i/q : EFT operator cQl32=1 with only linear/quadratic terms generated

    100104-i/q : EFT operator ctG=1 with only linear/quadratic terms generated

    100105-i/q : EFT operator ctW=1 with only linear/quadratic terms generated

    100106-i/q : EFT operator c3pl1=1 with only linear/quadratic terms generated
    
    100107-i/q : EFT operator c3pl2=1 with only linear/quadratic terms generated


##SBI process (gg -> lvlv)

The DSIDs start at 100200
The -i/q after the DSID stand for "interference EFT", which are linear EFT terms, and "quadratic EFT"

    100200 : Standard Model only, all EFT operators are set to zero

    100201-i/q : EFT operator cpDc=1 with only linear/quadratic terms generated

    100202-i/q : EFT operator cpG=1 with only linear/quadratic terms generated

    100203-i/q : EFT operator cdp=1 with only linear/quadratic terms generated

    100204-i/q : EFT operator cpW=1 with only linear/quadratic terms generated

    100205-i/q : EFT operator c3pl1=1 with only linear/quadratic terms generated

    100206-i/q : EFT operator c3pl2=1 with only linear/quadratic terms generated

    100207-i/q : EFT operator ctp=1 with only linear/quadratic terms generated

    100208-i/q : EFT operator ctW=1 with only linear/quadratic terms generated

    100209-i/q : EFT operator ctG=1 with only linear/quadratic terms generated

    100210-i/q : EFT operator cQl31=1 with only linear/quadratic terms generated

    100211-i/q : EFT operator cQl32=1 with only linear/quadratic terms generated

    100212-i/q : EFT operator cll1221=1 with only linear/quadratic terms generated
