# Summary of current directory

This folder contains data pertaining to the Enterics AMR Primer Panel positive controls design and testing.  
The primary objective is to design positive controls for the 749  primer pairs on the original panel.  

## Location of Data

Current Path: `/scicomp/home/ick4/data/collabs/pos_ctrls`  (referred to herein as `$PROJECT`)


## Description of Contents
`$PROJECT/twist`
The main folder, contains all the data for the design of the positive controls 

`$PROJECT/primers.csv`
Lists the 1498 primers on the original panel, including forward/reverse indicator. 
Each line is one primer, not one primer pair (hence 1498 lines of data instead of 749).

	
These files were generated using the following python script:
`pos_controls.py`
Located in: /scicomp/home/ick4/data/collabs/pos_ctrls
Also located inside the `pycharm` directory, as I used PyCharm for this project
Symlinked to: /scicomp/home/ick4/scripts
Created by: Jessica Rowell
Last modified: 08/06/2019


## END
		
