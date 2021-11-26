# BioinformaticsScript
## Table of contents
* [Description](#general-info)
* [Launch](#software_required/installation_instructions/execution_instructions)
* [Contributors](#contributors)
* [License](#license)

## Description
This repository contains a simple python script for addressing the following bioinformatics problem required for the Technical Interview:
>Problem: 
>Every week, virus samples are being sequenced and analyzed using a commonly found 
pipeline. This pipeline aligns all reads generated against a reference genome, and from this 
alignment it produces a consensus sequence. 
Besides the consensus fasta sequences, the pipeline also produces a file with quality metrics 
for all the samples analyzed. You have been provided such a file with quality metrics for 
each sample (samples.txt). It consists of 373 samples, and the head of the file looks like this: 
sample,pct_N_bases,pct_covered_bases,longest_no_N_run,num_aligned_reads,qc_pass DN-64554,3.91,96.07,7055,489499,TRUE 
DC-31756,4.14,95.93,7055,527966,TRUE
DD-28879,4.32,95.68,9033,444775,TRUE
DD-22466,3.63,96.37,7055,621979,TRUE
DC-95171,4.13,95.86,8855,510658,TRUE
DT-54370,3.80,96.18,12196,612425,TRUE
DT-97532,0.24,99.74,29786,644779,TRUE
DD-48974,0.12,99.86,29822,719234,TRUE
DC-90361,0.24,99.74,29786,519893,TRUE
As you can see this is a csv file with 6 columns. The columns show:
>1.	Name of the sample
>2.	Percentage of the bases in the consensus is denoted as ‘N’
>3.	Percentage of the bases of the reference genome has been covered
>4.	How long is the longest sequence in the consensus consisting of no ‘N’s
>5.	How many reads aligned to the reference genome
>6.	Does this consensus sequence pass the quality filter?

>One thing to know is that the second letter of the sample name denotes from where this sample came from. In this example dataset, there are 4 possible origins, 'C', 'T', 'D' and 'N'. However, in the future it is not impossible for there to be more origins. 
Your task as a bioinformatician, is to write a script that can be run automatically each time such a quality file is generated, and look at how many samples from each origin fail the set quality cut-off (< 95 % covered bases of the reference genome or ‘FALSE’ in column 6). 
As this script should run automatically once a week, the script should also serve as a warning system, sending warnings if there are certain origins producing more than 10% failed samples. Therefore, you need to implement a system that notifies its user in some way, telling them the latest results. 
Write such a script in python and submit it via a public GitHub repo. Emphasis should be put on making the script reliable, robust, and reproducible. 

Last update: 2021-11-26
## Launch

### Required Software:
* *_PROGRAMMING LANGUAGE/Version_*  (e.g.):
  *  You need a functional installation of **Python 2.7.16**  (and higher)
  
### Dependencies - Recommended Software:
* A functional installation of **git** and **Github**

### Installation and execution instructions
* Clone [BioinformaticsScript](https://github.com/DimitraLappa/BioinformaticsScript.git) repository
* Navigate to the  the directory of installation, preferably in a Terminal  
* Change mode to execution mode for the script:
	* ``` chmod +x BioinfoScript.py ```
* Execute the script:
	*  ```./BioinfoScript.py ```

## Contributors
- [Dimitra Lappa]( https://www.chalmers.se/en/staff/Pages/lappa.aspx), Chalmers University of Technology, Gothenburg Sweden

## License
The MIT License (MIT)

> Copyright (c) 2021, BioinformaticsScript, Dimitra Lappa
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
