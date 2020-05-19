# Summary of current directory

This folder contains data pertaining to the Enterics AMR Primer Panel positive controls design and testing.  
It contains all intermediate files pertaining to the design of positive controls for Twist Bioscience

## Location of Data

Current Path: `/scicomp/home/ick4/data/collabs/pos_ctrls/twist`  (referred to herein as `$PROJECT`)


## Description of Contents
`$PROJECT/S_coelicolor`
This directory contains all the data for the design of the positive controls for amplicons with high GC content 


`$PROJECT/Wolbachia`
This directory contains all the data for the design of the positive controls for amplicons with low GC content

`$PROJECT/NC_001422.1_phiX174.fasta`
Coliphage phi-X174, complete genome, https://www.ncbi.nlm.nih.gov/nuccore/9626372, downloaded May 18, 2019.

`$PROJECT/enterics.amr.fixed.genotypes_twistAll.txt`
Copy of all 749 primer pairs; this is fed to the first run of pos control design against the PhiX genome

`$PROJECT/enterics.amr.fixed.genotypes_twistHi.txt`
These are the primer pairs with GC content too high to match up pos contols against PhiX (n=147); they are run against S. coelicolor genome

`$PROJECT/enterics.amr.fixed.genotypes_twistLow.txt`
These are the primer pairs with GC content too low to match up pos contols against PhiX (n=10); they are run against Wolbachia genome

`$PROJECT/positive_controls.fasta`
The final file of positive controls designed against Phi-X174 genome passed to Twist Bioscience for production

`$PROJECT/positive_controls.txt`
A text file of the positive controls in the fasta above (n=592); lists primer name, forward primer, revers primer, and synthetic target 

`$PROJECT/positive_controls_outliers.fasta`
The final file of the positive controls designed against S. coelicolor or Wolbachia (the "outlier" targets with high/low GC content) passed to Twist Bioscience

`$PROJECT/positive_controls_outliers.txt`
A text file of the positive controls in the fasta above (n=157); lists primer name, forward primer, revers primer, and synthetic target

`$PROJECT/controls_found.txt`
List of primer names and GC content for targets where a pos control from Phi-X174 was found

`$PROJECT/controls_found.png`
Histogram of GC content for matched targets

`$PROJECT/controls_not_found.txt`
List of primer names and GC content for targets where a pos control from Phi-X174 was not found

`$PROJECT/controls_not_found.png`
Histogram of GC content for non-matched targets

`$PROJECT/distribution_length_N157.PNG`
Histogram of amplicon target for non-matched targets

`$PROJECT/GCF_000203835.1_ASM20383v1_genomic.fna`
Streptomyces coelicolor A3(2) (high GC Gram+)genome, https://www.ncbi.nlm.nih.gov/assembly/GCF_000203835.1/, downloaded May 18, 2019

`$PROJECT/GCF_001752665.1_ASM175266v1_genomic.fna`
Wolbachia pipientis genome, https://www.ncbi.nlm.nih.gov/assembly/GCF_001752665.1/, downloaded May 18, 2019

	
These files were generated using the following python script:
`pos_controls.py`
Located in: /scicomp/home/ick4/data/collabs/pos_ctrls
Also located inside the `pycharm` directory, as I used PyCharm for this project
Symlinked to: /scicomp/home/ick4/scripts
Created by: Jessica Rowell
Last modified: 08/06/2019


## END
		
