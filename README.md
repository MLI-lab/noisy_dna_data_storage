# Noisy DNA data storage


This repository provides code for reproducing the results in the paper:

**``Low Cost DNA data storage using Photolithographic Synthesis and Advanced Information Reconstruction and Error Correction''**, by
Philipp L. Antkowiak, Jory Lietard, Mohammad Darestani, Mark Somoza, Wendelin J. Stark, Reinhard Heckel, Robert N. Grass

Code by: Mohammad Zalbagi Darestani and Reinhard Heckel (rh43@rice.edu)

The aim of the code is to recover the data stored on DNA sequences from millions of noisy reads. The overall procedure comprises of i) clustering the noisy reads, ii) performing multiple sequence alignment, and iii) majority voting. By performing weighted majority voting on each cluster, we generate a number of candidates and by putting them into a decoder, we receover the original file. Details about "setup and installation," "main flags in the code," and "the data" is provided below.

### List of contents
[Setup and Installation](#Setup-and-Installation) <br>
[Data dependencies](#Data-dependencies) <br>
[Running the code and reproducing the results](#Running-the-code-and-reproducing-the-results) <br>
[License](#License)

# Setup and Installation

### OS requirements
The code has been tested on the following operating system:

	Linux: Ubuntu 16.04.5

### Python dependencies
To reproduce the results, run the jupyter notebook LSH_clustering.ipynb. To run this notebook, the following softwares are required. Assuming the experiment is being performed in a docker container or a linux machine, the following libraries and packages need to be installed.

        apt-get update
        apt-get install gcc
        apt-get install make
        apt-get install git
        apt-get install libboost-all-dev
        apt-get install python3.6       # --> or any other system-specific command for installing python3 on your system.
		pip install jupyter
		pip install numpy
		pip install biopython
		pip install sklearn
		pip install scikit-bio
		
If pip does not come with version of python you installed, install pip manually from [here](https://ehmatthes.github.io/pcc/chapter_12/installing_pip.html).

### Encoder-decoder installation
The encoding/decoding we use is with our Reed-Solomon encoder/decoder, that can be downloaded from the repository [dna_rs_coding](https://github.com/reinhardh/dna_rs_coding). Clone the repository [dna_rs_coding](https://github.com/reinhardh/dna_rs_coding) and move the LSH_clustering.ipynb jupyter notebook (and other contents of this repository (noisy dna data storage)) into the main directory dna_rs_coding folder (remember to simply merge the 2 "include" folders).

Compile the encoder/decoder by running the following commands:

	cd simulate
 	make texttodna

### Multiple-sequence-alignment software installation
For multiple sequence alignment, we used MUSCLE command line. Please download the proper version of the software from http://www.drive5.com/muscle/downloads.htm and put it in the "include" folder of the main directory (the 64-bit Linux version is already included in the "include" folder of this repository). LSH_clustering.ipynb is written for linux, so if you are using another operating system, after downloading the proper version of MUSCLE software and putting it in the main directory, you need to change "muscle_exe" in the "multiple_alignment_muscle" function to the name of the file you dowloaded. 

# Data dependencies

The "data" folder contains two files and a link to a third file containing the sequencing data:

File_1.zip: if you choose to run the code for a simulated dataset, this file will be loaded.

File1_ODNA.txt and the link to the noisy reads: if you choose to run the code for the synthesized data, these 2 files will be loaded.

Note that you need to download all 3 files and put them in the "data" folder in your main directory.
Based on the runtimes measured on a 6-core server, you may decide which options you are willing to pick.

| clustering method (&#8594;) <br /> data (&#8595;)   | Trivial       	      | LSH<sup>1</sup>	   |
| :--------------------------------------------------:|:---------------------:|:------------------:|
| Simulated      		      		      | 6 <sup>mins</sup>     | 18 <sup>mins</sup> |
| Synthesized      		      		      | 45 <sup>hrs</sup>     | 120 <sup>hrs</sup> |

<sup>1</sup> LSH recovers more original sequences compared to Trivial, but since both are able to recover enough (with respect to the redundancy in the Reed-Solomon codes) original sequences, both perfectly recover the original file stored on DNA. Hence, Trivial clustering might be a better choice in terms of the performance efficiency.


# Running the code and reproducing the results

To reproduce the result, run the jupyter notebook LSH_clustering.ipynb, for example by running the following code in the command line:

`jupyter notebook LSH_clustering.ipynb`

All dependencies like the encoder/decoder are called from this notebook. The notebook has two options/flags:

SIMULATE (**Demo**): if you set this flag to "True," the code runs for a simulated dataset, otherwise it runs for a real synthesized dataset.

TRIVIAL: if you set this flag to "True," clustering will be done based on the first "nbeg" characters of the noisy reads, otherwise, Locality-Sesitive-Hashing (LSH) techinque will be employed for clustering.

# License

This project is covered by **Apache 2.0 License**.

