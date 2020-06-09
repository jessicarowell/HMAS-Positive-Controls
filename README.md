# Summary of current directory

This folder contains data pertaining to the Enterics AMR Primer Panel positive controls design and testing.    
The primary objective is to design positive controls for the 749  primer pairs on the original panel.  

The basic premise of the design is as follows:
 1. For each amplicon ("target"), identify the length and GC content
 2. Search along the positive control genome via sliding windows (where window = target length) for a chunk with GC content equal to target's GC content
 3. Save this chunk as the positive control for that target

Note: if desired, the windows could be randomly sorted before searching for a chunk with matching GC content, but it was decided that this was not necessary for this project.  Thus, most of the positive controls are from the first part of the genome and are similar to one another.

The positive controls were designed in 3 phases:
 1. Get as many matches as possible with Coliphage phi-X174 as the target genome
 2. Run the script again, against Streptomyces coelicolor, to get matches for the targets with high GC content
 3. Run it against Wolbachia pipientis to get matches for the targets with low GC content


## Location of Data

Current Path: `/scicomp/home/ick4/data/collabs/pos_ctrls`  (referred to herein as `$PROJECT`)


## Description of Contents
`$PROJECT/twist`
The main folder, contains all the data for the design of the positive controls 

`$PROJECT/primers.csv`
Lists the 1498 primers on the original panel, including forward/reverse indicator. 
Each line is one primer, not one primer pair (hence 1498 lines of data instead of 749).

`$PROJECT/PositiveControls.pdf`
A pdf copy of the PowerPoint presentation given at CIMS meeting June 2020

	
These files were generated using the following python script:  
`pos_controls.py`  
Located in: `/scicomp/home/ick4/data/collabs/pos_ctrls`  
Also located inside the `pycharm` directory, as I used PyCharm for this project  
Symlinked to: `/scicomp/home/ick4/scripts`  
Created by: Jessica Rowell  
Last modified: 08/06/2019  


## END
		
