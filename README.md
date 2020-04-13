# Intro
<p align= "justify"> The aim of this project is to recover the data stored on DNA sequences from millions of noisy reads. The overall procedure comprises of clustering the noisy reads and by performing Multiple Sequence Alignment. Finally, by doing Majority Voting on each cluster, we generate a number of candidates and by putting them into a decoder, we receover the original file. Details about "setup and installation," "main flags in the code," and "the data" is provided below. </p>

==============

# Setup and Installation
Assuming the experiment is being performed in a docker container, the following libraries and packages need to be installed.

        apt-get update
        apt-get install gcc
        apt-get install make
        apt-get install git
        apt-get install libboost-all-dev
		apt-get install python3.6
		apt-get install python-numpy
		apt-get install python-biopython
		apt-get install python-sklearn

 
The encoder/decoder I used is a Reed-Solomon encoder/decoder written by [Reinhard Heckel](https://github.com/reinhardh). Download [dna_rs_coding](https://github.com/reinhardh/dna_rs_coding) as a zip file and extract it, then put the LSH_clustering.ipynb jupyter notebook in the main directory where you extracted that zip file.

compile the encoder/decoder by running the following commands:

	cd simulate
 	make texttodna

 <p align= "justify">For multiple sequence alignment, I used MUSCLE command line. Please download the proper version of the software from http://www.drive5.com/muscle/downloads.htm and put it in the main directory. LSH_clustering.ipynb is written for linux, so if you are using another operating system, after downloading the proper version of MUSCLE software and putting it in the main directory, you need to change "muscle_exe" in the "multiple_alignment_muscle" function (cell #12 in LSH_clustering.ipynb) to the name of the file you dowloaded. </p>

==============

# Main flags in the code
There are two main flags in the code: 

SIMULATE: if you set this flag to "True," the code runs for a simulated dataset, otherwise it runs for a real synthesized dataset.

TRIVIAL: if you set this flag to "True," clustering will be done based on the first "nbeg" characters of the noisy reads, otherwise, Locality-Sesitive-Hashing (LSH) techinque will be employed for clustering.

==============

# Data 
In the "data" folder there are 2 files plus a link to another file:

File_1.zip: if you choose to run the code for a simulated dataset, this file will be loaded.

File1_ODNA.txt and the link to the noisy reads: if you choose to run the code for the synthesized data, these 2 files will be loaded.

Note that you need to download all 3 files and put them in the "data" folder in your main directory.
Based on the runtimes measured on a 6-core server, you may decide which options you would pick.

| Tables <br /> hey| Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


==============

# Run and reproduce the results
Now, all you need to do is to open and LSH_clustering.ipynb or simply run the following code in the command line.

`jupyter notebook LSH_clustering.ipynb`
